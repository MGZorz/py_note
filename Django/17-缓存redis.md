# 一、缓存redis

## 1、概述

​	动态网站的基本权衡是，它们是动态的。每次用户请求页面时，Web服务器都会进行各种计算 - 从数据库查询到模板呈现再到业务逻辑 - 以创建站点访问者看到的页面。从处理开销的角度来看，这比标准的文件读取文件系统服务器要耗时多了。对于大多数Web应用程序来说，这种开销并不是什么大问题。因为大多数Web应用程序只是中小型网站，没有拥有一流的流量。但对于中到高流量的站点，尽可能减少开销是至关重要的，这就是缓存的用武之地。缓存某些内容是为了保存昂贵计算的结果，这样就不必在下次执行计算。

​	Django框架带有一个强大的缓存系统，可以保存动态页面，因此不必为每个请求计算它们。Django提供不同级别的缓存粒度：可以缓存特定视图的输出，也可以只缓存页面中难以生成的部分或者可以缓存整个站点。 

​	Redis，是一个内存数据库（现在已经支持内存数据持久化到硬盘当中，重新启动时，会自动从硬盘进行加载），由于其性能极高，因此经常作为中间件、缓存使用。

​	本文档介绍就是Django框架使用Redis数据库来应用缓存框架



## 2、Redis

​	redis默认不支持windows，由于一般开发环境在windows，因为需要使用第三方团队维护的windows版本，最好用的是微软团队 MicrosoftArchive 维护的版本，下载地址：

​	https://github.com/MicrosoftArchive/redis/releases

​	安装好之后，启动redis



## 3、应用redis缓存

​	django中应用redis，目前一般使用第三方库 django-redis

​	安装：pip install django-redis



### 1.settings配置

```python
CACHES = {
    # default 是缓存名，可以配置多个缓存
    "default": {
        # 应用 django-redis 库的 RedisCache 缓存类
        "BACKEND": "django_redis.cache.RedisCache",
        # 配置正确的 ip和port
        "LOCATION": "redis://127.0.0.1:6379",
        "OPTIONS": {
            # redis客户端类
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            # redis连接池的关键字参数
            "CONNECTION_POOL_KWARGS": {
                "max_connections": 100
            }
            # 如果 redis 设置了密码，那么这里需要设置对应的密码，如果redis没有设置密码，那么这里也不设置
            # "PASSWORD": "123456",
        }
    }
}
```

更多配置项：

- LOCATION：设置连接url，譬如："redis://127.0.0.1:6379/0"，如果要设置redis主从连接，设置列表：["redis://127.0.0.1:6379/1", "redis://127.0.0.1:6378/1"]，第一个连接是 master 服务器

- TIMEOUT：缓存的超时时间，单位秒，默认是 300秒，如果为None，表示缓存永不超时，如果为0，表示缓存立刻超时，相当于不使用缓存

- LOCATION：支持使用 本地url符号作为连接，

  支持三种 URL scheme :

  1. redis://: 普通的 TCP 套接字连接 - redis://[:password]@localhost:6379/0
  2. rediss://: SSL 包裹的 TCP 套接字连接 - rediss://[:password]@localhost:6379/0
  3. unix://: Unix 域套接字连接 - unix://[:password]@/path/to/socket.sock?db=0

  但是密码放在url中，不是很安全，所以建议使用示例中的方式

- OPTIONS：

  - SOCKET_CONNECT_TIMEOUT：建立连接超时时间，单位秒

  - SOCKET_TIMEOUT：连接建立后，读写超时时间，单位秒

  - COMPRESSOR：默认不使用压缩，指定压缩的类，譬如"django_redis.compressors.zlib.ZlibCompressor"

  - IGNORE_EXCEPTIONS：默认为False，当Redis仅用于缓存时，连接异常或关闭后，忽略异常，不触发异常，可以设置为True，也可以全局设置 DJANGO_REDIS_LOG_IGNORED_EXCEPTIONS=True

  - PICKLE_VERSION：序列化使用的是pickle，默认情况下使用最新的pickle版本，这里可以设置指定版本号（设置为 -1 也是指最新版本）

  - CONNECTION_POOL_CLASS：设置自定义的连接池类

  - PARSER_CLASS：redis.connection.HiredisParser，可以这样设置，使用C写的redis客户端，性能更好

  - CLIENT_CLASS：设置一些特殊客户端类，譬如：

    分片客户端：

    ```python
    CACHES = {
        "default": {
            "BACKEND": "django_redis.cache.RedisCache",
            "LOCATION": [
                "redis://127.0.0.1:6379/1",
                "redis://127.0.0.1:6379/2",
            ],
            "OPTIONS": {
                "CLIENT_CLASS": "django_redis.client.ShardClient",
            }
        }
    }
    ```

    集群客户端：

    ```python
    CACHES = {
        "default": {
            "BACKEND": "django_redis.cache.RedisCache",
            "LOCATION": [
                "redis://127.0.0.1:6379/1",
            ],
            "OPTIONS": {
                "CLIENT_CLASS": "django_redis.client.HerdClient",
            }
        }
    }
    ```

  - SERIALIZER：设置序列化，如 "django_redis.serializers.json.JSONSerializer"



全局配置，即设置在settings最外层的配置项：

```python
# 给所有缓存配置相同的忽略行为
DJANGO_REDIS_LOG_IGNORED_EXCEPTIONS  = True

# 设置指定的 logger 输出日志， 需要设置logger
DJANGO_REDIS_LOGGER = 'some.specified.logger'
```



### 2.手动操作redis

通过配置获取django_redis的get_redis_connection，进行操作，如下：

```python
from django_redis import get_redis_connection

conn = get_redis_connection("default")  # redis.client.StrictRedis
# 支持所有redis的接口
conn.hset('hash_test','k1','v1')

# 也可以手动将数据清除
get_redis_connection("default").flushall()

# 得知连接池的连接数
get_redis_connection("default").connection_pool
```



### 3.全站缓存

主要使用两个中间件实现：

- FetchFromCacheMiddleware ：从缓存中读取数据

  - 缓存状态为200的GET和HEAD请求的响应（除非响应头中设置不进行缓存）
  - 对具有不同查询参数的相同URL的请求的响应被认为是各自不同的页面，并且被分别单独缓存。
  - 该中间件会使用与对应的GET请求相同的响应头来回答HEAD请求，即可以为HEAD请求返回缓存的GET响应。

- UpdateCacheMiddleware ：将数据更新到缓存中

  - 该中间件会自动在每个响应中设置几个headers：
    - 设置Expires为当前日期/时间 加上 定义的CACHE_MIDDLEWARE_SECONDS值，GMT时间
    - 设置响应的Cache-Control的max-age，值是定义的CACHE_MIDDLEWARE_SECONDS值。

  - 如果视图设置了自己的缓存时间（即设置了Cache-Control 的max age），那么页面将被缓存直到到期时间，而不是CACHE_MIDDLEWARE_SECONDS。

    使用装饰器 django.views.decorators.cache可以设置视图的到期时间（使用cache_control()装饰器，代码：@cache_control(max_age=3600)）或禁用视图的缓存（使用never_cache()装饰器，代码：@never_cache）

  - 如果USE_I18N设置为True，则生成的缓存key将包含当前语言的名称，这样可以轻松缓存多语言网站，而无需自己创建缓存密钥。

  - 如果 USE_L10N设置为True 并且 USE_TZ被设置为True，缓存key也会包括当前语言



在settings的中间件中设置：

```python
MIDDLEWARE = [
    'django.middleware.cache.UpdateCacheMiddleware',
    
    # 其他中间件...
    
    'django.middleware.cache.FetchFromCacheMiddleware',
]
```

PS：UpdateCacheMiddleware必须是第一个中间件，FetchFromCacheMiddleware必须是最后一个中间件



然后，将以下必需设置添加到Django的settings文件中：

- CACHE_MIDDLEWARE_ALIAS - 用于存储的缓存别名。
- CACHE_MIDDLEWARE_SECONDS - 每个页面应缓存的秒数。
- CACHE_MIDDLEWARE_KEY_PREFIX - 用于生成缓存key的前缀，如果使用相同的Django安装在多个站点之间共享缓存，请将其设置为站点名称或此Django实例特有的其他字符串，以防止发生密钥冲突。如果你不在乎，请使用空字符串。



在视图中：

```python
def index(request):
    # 通过设置时间戳，进行多次访问，可以看到时间戳的变化，就可以得知是否是缓存页面了
    return HttpResponse('欢迎光临，当前时间戳：' + str(time.time()))
```



### 4.视图函数缓存

1. 通过装饰器cache_page

   ```python
   from django.views.decorators.cache import cache_page
    
    @cache_page(60 * 15)
    def index(request):
    ...
   ```

   说明：

   - cache_page除了默认的timeout参数外，还有两个可选的关键字参数

     - cache，示例代码：@cache_page(60 * 15, cache="special_cache")， 该cache指向settings中配置的缓存的名称，默认是"default"
     - key_prefix：缓存key的前缀，与CACHE_MIDDLEWARE_KEY_PREFIX功能相同

   - 如果多个url指向同一个视图函数，会为每个url建立一个单独的缓存，例如：

     ```python
     urlpatterns = [
         path('foo/<int:code>/', views.index),
     ]
     ```

     /foo/1/ 和/foo/23/ 请求会分别进行缓存

     

2. 通过urls中配置cache_page

   在URLconf中指定视图缓存，而不是在视图函数上硬编码装饰器，可以进一步解耦缓存和视图函数之间的关系，使用起来更灵活

   ```python
   from django.views.decorators.cache import cache_page
    
   urlpatterns = [
       path('index/', cache_page(60 * 15)(views.index)),
   ]
   ```



### 5.模板文件缓存

​	使用cache模板标记缓存模板片段

1. 引入TemplateTag

   ```django
   {% load cache %}
   ```

   

2. 使用缓存

   ```django
   {% cache 5000 cache_key %}
          缓存内容
   {% endcache %}
   ```

   说明：

   cache最少两个参数：

   - 5000： 缓存超时时间，单位秒，如果为None，那么就是永久缓存

   - cache_key：缓存的key，不能使用变量，只是一个字符串（不要引号），相当于CACHE_MIDDLEWARE_KEY_PREFIX 

     

   可以通过将一个或多个附加参数（可以是带或不带过滤器的变量，变量个数可以是多个，如：{% cache 500 sidebar var1 var2 var3 ... %}）传递给 cache 来唯一标识缓存片段来执行此操作，示例如下：

   ```python
   {% load cache %}
   {% cache 500 sidebar request.user.username %}
       指定登录用户的侧边栏
   {% endcache %}
   ```

   

   如果USE_I18N设置为True，每站点中间件缓存将根据语言进行区分，对于cache模板标记，可以使用模板中可用的特定于 转换的变量 来实现相同的结果，示例如下：

   ```python
   {% load i18n %}
   {% load cache %}
   
   {% get_current_language as LANGUAGE_CODE %}
   
   {% cache 600 welcome LANGUAGE_CODE %}
       {% trans "Welcome to example.com" %}
   {% endcache %}
   ```

   

   缓存超时可以是模板变量，使用变量可以避免多次使用同一个值，示例（假设my_timeout设置为 600）：

   ```python
   
   {% cache my_timeout sidebar %} ... {% endcache %}
   ```

   

   默认情况下，cache将尝试使用名为“template_fragments”的缓存。如果不存在此缓存，则使用默认的default缓存。可以通过using关键字参数指定使用的缓存，该关键字参数必须是标记的最后一个参数，示例：

   ```python
   {% cache 300 cache_key ... using="localcache" %}
   ```

   PS：指定不存在的 缓存名 会报错

   

### 6.低级缓存

有时不想缓存整个页面数据，而只是想缓存某些费时查询并且基本不会改变的数据，可以通过一个简单的低级缓存API实现，该API可以缓存任何可以安全pickle的Python对象：字符串，字典，模型对象列表等 

1. django.core.cache.caches

   ```python
   from django.core.cache import caches
   cache1 = caches['myalias']
   cache2 = caches['myalias']
   # 判断为True
   if cache1 is cache2: 
       ...
   ```

   说明：

   - 可以通过CACHES类似字典一样的方式访问settings中配置的缓存，在同一个线程中重复请求相同的别名将返回相同的对象

   - 如果指定的 myalias 不存在，将引发 InvalidCacheBackendError

   - 为了线程安全性，为会每个线程返回缓存的不同实例

   - 作为快捷方式， 默认缓存(default)可以使用 django.core.cache.cache ：

     ```python
     # 使用 default 缓存
     from django.core.cache import cache
     
     # 上面的cache等同于下面的写法
     from django.core.cache import caches
     cache = caches['default']
     ```

     

2. django.core.cache.cache

```python
from django.core.cache import cache

# 使用 redis 的一般用法
cache.set('manul_set', 'ok')
manul_set = cache.get('manul_set')

# 可以手动设置 timeout，如果不指定timeout，默认是 300秒
cache.set("key", "value", timeout=None)

# 可以获取key的超时设置（ttl：time to live）
# 返回值的3种情况：
# 0： key 不存在 (或已过期)
# None： key 存在但没有设置过期
# ttl： 任何有超时设置的 key 的超时值
cache.set("foo", "value", timeout=25)
cache.ttl("foo") # 得到 25 
cache.ttl("not-existent") # 得到 0

# 让一个值永久存在
cache.persist("foo")
cache.ttl("foo") # 得到 None

# 指定一个新的过期时间
cache.set("foo", "bar", timeout=22)
cache.ttl("foo") # 得到 22
cache.expire("foo", timeout=5)
cache.ttl("foo") # 得到 5

# 支持 redis 分布式锁， 使用 上下文管理器 分配锁
with cache.lock("somekey"):
    do_some_thing()
    
# 使用全局通配符的方式来检索或者删除键
cache.keys("foo_*")  # 返回所有匹配的值, 如 ["foo_1", "foo_2"]

# 使用 iter_keys 取代keys 得到 一个迭代器
cache.iter_keys("foo_*")  # 得到一个迭代器
next(cache.iter_keys("foo_*"))  # 得到 foo_1

# 删除 键
cache.delete_pattern("foo_*")  # 支持通配符
```



### 7.session缓存

```python
# 配置session的引擎为cache
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
# 此处别名依赖缓存的设置
SESSION_CACHE_ALIAS = 'default'  
```



