# 一、REST framework

##1、REST

### 1.什么是REST？

​	REST全称是Representational State Transfer，中文意思是表述（通常译为表征）性状态转移。 它首次出现在2000年Roy Fielding的博士论文中，Roy Fielding是HTTP规范的主要编写者之一。 他在论文中提到："我这篇文章的写作目的，就是想在符合架构原理的前提下，理解和评估以网络为基础的应用软件的架构设计，得到一个功能强、性能好、适宜通信的架构。REST指的是一组架构约束条件和原则。" 如果一个架构符合REST的约束条件和原则，我们就称它为RESTful架构。

​	REST本身并没有创造新的技术、组件或服务，而隐藏在RESTful背后的理念就是使用Web的现有特征和能力， 更好地使用现有Web标准中的一些准则和约束。虽然REST本身受Web技术的影响很深， 但是理论上REST架构风格并不是绑定在HTTP上，只不过目前HTTP是唯一与REST相关的实例。 



### 2.理解RESTful

​	要理解RESTful架构，需要理解Representational State Transfer这个词组到底是什么意思，它的每一个词都有些什么含义。

​	下面我们结合REST原则，围绕资源展开讨论，从资源的定义、获取、表述、关联、状态变迁等角度，列举一些关键概念并加以解释。

- 资源与URI
- 统一资源接口
- 资源的表述
- 资源的链接
- 状态的转移



#### 2. 1 资源与URI

REST全称是表述性状态转移，那究竟指的是什么的表述? 其实指的就是资源。任何事物，只要有被引用到的必要，它就是一个资源。资源可以是实体(例如手机号码)，也可以只是一个抽象概念(例如价值) 。下面是一些资源的例子：

- 某用户的手机号码
- 某用户的个人信息
- 最多用户订购的GPRS套餐
- 两个产品之间的依赖关系
- 某用户可以办理的优惠套餐
- 某手机号码的潜在价值

要让一个资源可以被识别，需要有个唯一标识，在Web中这个唯一标识就是URI(Uniform Resource Identifier)。

URI既可以看成是资源的地址，也可以看成是资源的名称。如果某些信息没有使用URI来表示，那它就不能算是一个资源， 只能算是资源的一些信息而已。URI的设计应该遵循可寻址性原则，具有自描述性，需要在形式上给人以直觉上的关联。这里以github网站为例，给出一些还算不错的URI：

- https://github.com/git
- https://github.com/git/git
- https://github.com/git/git/blob/master/block-sha1/sha1.h
- https://github.com/git/git/commit/e3af72cdafab5993d18fae056f87e1d675913d08
- https://github.com/git/git/pulls
- https://github.com/git/git/pulls?state=closed
- https://github.com/git/git/compare/master…next

下面让我们来看看URI设计上的一些技巧:

- 使用_或-来让URI可读性更好

曾经Web上的URI都是冰冷的数字或者无意义的字符串，但现在越来越多的网站使用_或-来分隔一些单词，让URI看上去更为人性化。 例如国内比较出名的开源中国社区，它上面的新闻地址就采用这种风格， 如http://www.oschina.net/news/38119/oschina-translate-reward-plan。

- 使用/来表示资源的层级关系

例如上述/git/git/commit/e3af72cdafab5993d18fae056f87e1d675913d08就表示了一个多级的资源， 指的是git用户的git项目的某次提交记录，又例如/orders/2012/10可以用来表示2012年10月的订单记录。

- 使用?用来过滤资源

很多人只是把?简单的当做是参数的传递，很容易造成URI过于复杂、难以理解。可以把?用于对资源的过滤， 例如/git/git/pulls用来表示git项目的所有推入请求，而/pulls?state=closed用来表示git项目中已经关闭的推入请求， 这种URL通常对应的是一些特定条件的查询结果或算法运算结果。

- ,或;可以用来表示同级资源的关系

有时候我们需要表示同级资源的关系时，可以使用,或;来进行分割。例如哪天github可以比较某个文件在随意两次提交记录之间的差异，或许可以使用/git/git /block-sha1/sha1.h/compare/e3af72cdafab5993d18fae056f87e1d675913d08;bd63e61bdf38e872d5215c07b264dcc16e4febca作为URI。 不过，现在github是使用…来做这个事情的，例如：/git/git/compare/master…next。



#### 2. 2 统一资源接口

RESTful架构应该遵循统一接口原则，统一接口包含了一组受限的预定义的操作，不论什么样的资源，都是通过使用相同的接口进行资源的访问。接口应该使用标准的HTTP方法如GET，PUT和POST，并遵循这些方法的语义。

如果按照HTTP方法的语义来暴露资源，那么接口将会拥有安全性和幂等性的特性，例如GET和HEAD请求都是安全的， 无论请求多少次，都不会改变服务器状态。而GET、HEAD、PUT和DELETE请求都是幂等的，无论对资源操作多少次， 结果总是一样的，后面的请求并不会产生比第一次更多的影响。

下面列出了GET，DELETE，PUT和POST的典型用法:

##### GET

- 安全且幂等
- 获取表示
- 变更时获取表示（缓存）

- 200（OK） - 表示已在响应中发出

- 204（无内容） - 资源有空表示
- 301（Moved Permanently） - 资源的URI已被更新
- 303（See Other） - 其他（如，负载均衡）
- 304（not modified）- 资源未更改（缓存）
- 400 （bad request）- 指代坏请求（如，参数错误）
- 404 （not found）- 资源不存在
- 406 （not acceptable）- 服务端不支持所需表示
- 500 （internal server error）- 通用错误响应
- 503 （Service Unavailable）- 服务端当前无法处理请求

##### POST

- 不安全且不幂等
- 使用服务端管理的（自动产生）的实例号创建资源
- 创建子资源
- 部分更新资源
- 如果没有被修改，则不过更新资源（乐观锁）

- 200（OK）- 如果现有资源已被更改

- 201（created）- 如果新资源被创建
- 202（accepted）- 已接受处理请求但尚未完成（异步处理）
- 301（Moved Permanently）- 资源的URI被更新
- 303（See Other）- 其他（如，负载均衡）
- 400（bad request）- 指代坏请求
- 404 （not found）- 资源不存在
- 406 （not acceptable）- 服务端不支持所需表示
- 409 （conflict）- 通用冲突
- 412 （Precondition Failed）- 前置条件失败（如执行条件更新时的冲突）
- 415 （unsupported media type）- 接受到的表示不受支持
- 500 （internal server error）- 通用错误响应
- 503 （Service Unavailable）- 服务当前无法处理请求

##### PUT

- 不安全但幂等
- 用客户端管理的实例号创建一个资源
- 通过替换的方式更新资源
- 如果未被修改，则更新资源（乐观锁）

- 200 （OK）- 如果已存在资源被更改

- 201 （created）- 如果新资源被创建
- 301（Moved Permanently）- 资源的URI已更改
- 303 （See Other）- 其他（如，负载均衡）
- 400 （bad request）- 指代坏请求
- 404 （not found）- 资源不存在
- 406 （not acceptable）- 服务端不支持所需表示
- 409 （conflict）- 通用冲突
- 412 （Precondition Failed）- 前置条件失败（如执行条件更新时的冲突）
- 415 （unsupported media type）- 接受到的表示不受支持
- 500 （internal server error）- 通用错误响应
- 503 （Service Unavailable）- 服务当前无法处理请求

##### DELETE

- 不安全但幂等
- 删除资源
- 200 （OK）- 资源已被删除
- 204 (没内容) - 操作成功，但是无返回内容
- 301 （Moved Permanently）- 资源的URI已更改
- 303 （See Other）- 其他，如负载均衡
- 400 （bad request）- 指代坏请求
- 404 （not found）- 资源不存在
- 409 （conflict）- 通用冲突
- 500 （internal server error）- 通用错误响应
- 503 （Service Unavailable）- 服务端当前无法处理请求

下面我们来看一些实践中常见的问题:

- POST和PUT用于创建资源时有什么区别?

POST和PUT在创建资源的区别在于，所创建的资源的名称(URI)是否由客户端决定。 例如为我的博文增加一个java的分类，生成的路径就是分类名/categories/java，那么就可以采用PUT方法。不过很多人直接把POST、GET、PUT、DELETE直接对应上CRUD，例如在一个典型的rails实现的RESTful应用中就是这么做的。这是因为rails默认使用服务端生成的ID作为URI的缘故，而不少人就是通过rails实践REST的，所以很容易造成这种误解。

- 客户端不一定都支持这些HTTP方法吧?

的确有这种情况，特别是一些比较古老的基于浏览器的客户端，只能支持GET和POST两种方法。

在实践上，客户端和服务端都可能需要做一些妥协。例如rails框架就支持通过隐藏参数method=DELETE来传递真实的请求方法， 而像Backbone这样的客户端MVC框架则允许传递method传输和设置X-HTTP-Method-Override头来规避这个问题。

- 统一接口是否意味着不能扩展带特殊语义的方法?

统一接口并不阻止你扩展方法，只要方法对资源的操作有着具体的、可识别的语义即可，并能够保持整个接口的统一性。

像WebDAV就对HTTP方法进行了扩展，增加了LOCK、UPLOCK等方法。而github的API则支持使用PATCH方法来进行issue的更新，例如:

```
PATCH /repos/:owner/:repo/issues/:number
```

不过，需要注意的是，像PATCH这种，服务端需要考虑客户端是否能够支持的问题。

- 统一资源接口对URI有什么指导意义?

统一资源接口要求使用标准的HTTP方法对资源进行操作，所以URI只应该来表示资源的名称，而不应该包括资源的操作。

通俗来说，URI不应该使用动作来描述。例如，下面是一些不符合统一接口要求的URI:

- GET /getUser/1
- POST /createUser
- PUT /updateUser/1
- DELETE /deleteUser/1

如果GET请求增加计数器，这是否违反安全性?

安全性不代表请求不产生副作用，例如像很多API开发平台，都对请求流量做限制。像github，就会限制没有认证的请求每小时只能请求60次。但客户端不是为了追求副作用而发出这些GET或HEAD请求的，产生副作用是服务端"自作主张"的。

另外，服务端在设计时，也不应该让副作用太大，因为客户端认为这些请求是不会产生副作用的。

- 直接忽视缓存可取吗?

即使你按各个动词的原本意图来使用它们，你仍可以轻易禁止缓存机制。 最简单的做法就是在你的HTTP响应里增加这样一个报头： Cache-control: no-cache。 但是，同时你也对失去了高效的缓存与再验证的支持(使用Etag等机制)。

对于客户端来说，在为一个REST式服务实现程序客户端时，也应该充分利用现有的缓存机制，以免每次都重新获取表示。

- 响应代码的处理有必要吗?

HTTP的响应代码可用于应付不同场合，正确使用这些状态代码意味着客户端与服务器可以在一个具备较丰富语义的层次上进行沟通。

例如，201（"Created"）响应代码表明已经创建了一个新的资源，其URI在Location响应报头里。

假如你不利用HTTP状态代码丰富的应用语义，那么你将错失提高重用性、增强互操作性和提升松耦合性的机会。

如果这些所谓的RESTful应用必须通过响应实体才能给出错误信息，那么SOAP就是这样的了，它就能够满足了。



#### 2. 3 资源的表述

上面提到，客户端通过HTTP方法可以获取资源，是吧? 不，确切的说，客户端获取的只是资源的表述而已。 资源在外界的具体呈现，可以有多种表述(或称为表现、表示)形式，在客户端和服务端之间传送的也是资源的表述，而不是资源本身。 例如文本资源可以采用html、xml、json等格式，图片可以使用PNG或JPG展现出来。

资源的表述包括数据和描述数据的元数据，例如，HTTP头"Content-Type" 就是这样一个元数据属性。

那么客户端如何知道服务端提供哪种表述形式呢?

答案是可以通过HTTP内容协商，客户端可以通过Accept头请求一种特定格式的表述，服务端则通过Content-Type告诉客户端资源的表述形式。

以github为例，请求某组织资源的json格式的表述形式:

![](.\imgs\rest_git_json.jpg)

　

　假如github也能够支持xml格式的表述格式，那么结果就是这样的:

![](.\imgs\rest_git_xml.jpg)

　

　下面我们来看一些实践上常见的设计:

##### 在URI里边带上版本号

有些API在URI里边带上版本号，例如:

- http://api.example.com/1.0/foo
- http://api.example.com/1.2/foo
- http://api.example.com/2.0/foo

如果我们把版本号理解成资源的不同表述形式的话，就应该只是用一个URL，并通过Accept头部来区分，还是以github为例，它的Accept的完整格式是:application/vnd.github[.version].param[+json]

对于v3版本的话，就是Accept: application/vnd.github.v3。对于上面的例子，同理可以使用使用下面的头部:

​	http://api.example.com/foo

- Accept: vnd.example-com.foo+json; version=1.0
- Accept: vnd.example-com.foo+json; version=1.2
- Accept: vnd.example-com.foo+json; version=2.0

##### 使用URI后缀来区分表述格式

像rails框架，就支持使用/users.xml或/users.json来区分不同的格式。 这样的方式对于客户端来说，无疑是更为直观，但混淆了资源的名称和资源的表述形式。 我个人认为，还是应该优先使用内容协商来区分表述格式。

##### 如何处理不支持的表述格式

当服务器不支持所请求的表述格式，那么应该怎么办？若服务器不支持，它应该返回一个HTTP 406响应，表示拒绝处理该请求。下面以github为例，展示了一个请求XML表述资源的结果：

![](.\imgs\rest_git_406.jpg)

　　

#### 2. 4 资源的链接

我们知道REST是使用标准的HTTP方法来操作资源的，但仅仅因此就理解成带CRUD的Web数据库架构就太过于简单了。

这种反模式忽略了一个核心概念："超媒体即应用状态引擎（hypermedia as the engine of application state）"。 

超媒体是什么?

当你浏览Web网页时，从一个连接跳到一个页面，再从另一个连接跳到另外一个页面，就是利用了超媒体的概念：把一个个把资源链接起来.

要达到这个目的，就要求在表述格式里边加入链接来引导客户端。在《RESTful Web Services》一书中，作者把这种具有链接的特性称为连通性。下面我们具体来看一些例子。

下面展示的是github获取某个组织下的项目列表的请求，可以看到在响应头里边增加Link头告诉客户端怎么访问下一页和最后一页的记录。 而在响应体里边，用url来链接项目所有者和项目地址。

![](.\imgs\rest_git_link.jpg)

　　又例如下面这个例子，创建订单后通过链接引导客户端如何去付款。

![](.\imgs\rest_git_location.jpg)

上面的例子展示了如何使用超媒体来增强资源的连通性。很多人在设计RESTful架构时，使用很多时间来寻找漂亮的URI，而忽略了超媒体。所以，应该多花一些时间来给资源的表述提供链接，而不是专注于"资源的CRUD"。



#### 2. 5 状态的转移

有了上面的铺垫，再讨论REST里边的状态转移就会很容易理解了。

不过，我们先来讨论一下REST原则中的无状态通信原则。初看一下，好像自相矛盾了，既然无状态，何来状态转移一说?

其实，这里说的无状态通信原则，并不是说客户端应用不能有状态，而是指服务端不应该保存客户端状态。



##### 2. 5.1 应用状态与资源状态

实际上，状态应该区分应用状态和资源状态，客户端负责维护应用状态，而服务端维护资源状态。

客户端与服务端的交互必须是无状态的，并在每一次请求中包含处理该请求所需的一切信息。

服务端不需要在请求间保留应用状态，只有在接受到实际请求的时候，服务端才会关注应用状态。

这种无状态通信原则，使得服务端和中介能够理解独立的请求和响应。

在多次请求中，同一客户端也不再需要依赖于同一服务器，方便实现高可扩展和高可用性的服务端。

但有时候我们会做出违反无状态通信原则的设计，例如利用Cookie跟踪某个服务端会话状态，常见的像J2EE里边的JSESSIONID。

这意味着，浏览器随各次请求发出去的Cookie是被用于构建会话状态的。

当然，如果Cookie保存的是一些服务器不依赖于会话状态即可验证的信息（比如认证令牌），这样的Cookie也是符合REST原则的。



##### 2. 5.2 应用状态的转移

状态转移到这里已经很好理解了， "会话"状态不是作为资源状态保存在服务端的，而是被客户端作为应用状态进行跟踪的。客户端应用状态在服务端提供的超媒体的指引下发生变迁。服务端通过超媒体告诉客户端当前状态有哪些后续状态可以进入。

这些类似"下一页"之类的链接起的就是这种推进状态的作用——指引你如何从当前状态进入下一个可能的状态。



## 2、REST framework

​	Django框架构建RESTful的api应用，推荐使用 REST framework 框架

​	官网：https://www.django-rest-framework.org/



### 1.安装

```
pip install djangorestframework==3.10.2
```

​	环境介绍：

- python3.6

- django2.2

- djangorestframework3.10.2

  

### 2.settings配置

​	首先新建一个django项目

​	然后如果要启用REST framework，那么需要将其添加到 INSTALLED_APPS 中

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
]
```



## 3、序列化

​	当前web api应用中，前端要用到从后台返回的数据来渲染页面的时候，一般都是使用的json类型的数据，因为json类型简单直观便于理解，那么就需要在django框架中，将模型类数据序列化为json



### 1.建立模型

```python
class Student(models.Model):

    SEX_CHOICES = ((1,'男')), (2, '女')

    name = models.CharField(max_length=20, verbose_name='姓名')
    age = models.IntegerField(null=True, blank=True, verbose_name='年龄')
    sex = models.IntegerField(choices=SEX_CHOICES, default=1, verbose_name='性别')
```



### 2.迁移模型

​	在迁移之前，需要正确配置settings当中的数据库信息

```
python manage.py makemigrations

python manage.py migrate
```



### 3.创建序列化类

在子应用的目录下，新建serializers.py 文件，在其中建立一个对应第一步建立的模型的序列化类：

```python
class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ['id', 'name', 'age', 'sex']
```

说明：

- 继承自serializers.ModelSerializer类

- 必须实现class Meta

- model 的值为对应的模型类

- fields 的值是要序列化的字段，设置为 fields = '\__all__' 则使用所有模型的字段，也可以使用 exclude 指明要排除的字段，例如：exclude = ['id'] , 通常使用 fields 

  

- 继承自ModelSerializer类，其实是一种快捷的方式，也可以直接继承serializers.Serializer，手动写 字段集以及 create、update方法。ModelSerializer有一个 repr 属性来查看 字段集 是如何编写的：

  ```
  # 在 django shell中
  from rest_app.serializers import StudentSerializer
  
  stu_serializer = StudentSerializer()
  print(repr(stu_serializer))
  ```



序列化：

- 序列化一个模型实例

```python
# 得到一个模型实例
stu = Student.objects.get(pk=1)
# 得到模型序列化类实例
stu_ser = StudentSerializer(stu)
# 得到 模型的字典数据 {"id": 1, ......}
data_dict = stu_ser.data

# 返回给用户之前，需要将 字典数据 转换为 json格式的 字节串  b'{"id": 1, ......}'
from rest_framework.renderers import JSONRenderer
data_json = JSONRenderer().render(data_dict)
```

- 序列化模型的查询集QuerySet

```python
# 必须指定 many=True
stu_ser = StudentSerializer(Student.objects.all(), many=True)
# 得到 字典数据列表 [OrderedDict([('id', 1),......)]
data_dict = stu_ser.data
```



反序列化：

```python
# 将 json格式的字节串 转换为字典
from rest_framework.parsers import JSONParser
stream = io.BytesIO(b'{"name":"rose", "age":19, sex:2}')
# 得到字典数据， {'id': 1,......}
data_dict = JSONParser().parse(stream)

# 将字典数据 反序列化
serializer = StudentSerializer(data=data_dict)
# 必须执行这一步验证， 返回True才可以获取后续的 validated_data数据和执行 save等方法
serializer.is_valid()
# 得到 OrderedDict([('name', 'terry'),......] , 会忽略掉 id 属性
serializer.validated_data
# 保存到数据库中
serializer.save()
```



### 4.views.py

在视图中实现函数 students API

```python
@csrf_exempt
def students(request):
    if request.method == 'GET':
        student_li = Student.objects.all()
        serializer = StudentSerializer(student_li, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    
@csrf_exempt
def student_detail(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = StudentSerializer(student, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        student.delete()
        return HttpResponse(status=204)
```



### 5.urls.py

```python
urlpatterns = [
    path('students/', views.students),
    path('students/<int:pk>/', views.student_detail),
]
```



### 6.测试

get请求可以使用浏览器发送，但是post等其他http method的请求，浏览器测试起来就不方便了，本文档中使用 curl 工具在cmd中执行）来测试api 命令



GET：

```
# 200 状态
curl -i http://127.0.0.1:8000/rest/students/
curl -i http://127.0.0.1:8000/rest/students/1/

# 404 状态
curl -i http://127.0.0.1:8000/rest/students/10000/
```

POST：

```
# 201 状态
curl -i http://127.0.0.1:8000/rest/students/ -X POST -d {\"id\":10,\"name\":\"shine\",\"age\":18,\"sex\":1}

# 400 状态
curl -i http://127.0.0.1:8000/rest/students/ -X POST -d {\"name\":\"\",\"age\":18,\"sex\":1}
```

PUT:

```
# 200 状态
curl -i http://127.0.0.1:8000/rest/students/1/ -X PUT -d {\"name\":\"terry_put\",\"age\":18,\"sex\":1}
```

DELETE:

```
# 204 状态
curl -i http://127.0.0.1:8000/rest/students/1/ -X DELETE
```



### 7.关系模型的序列化

models:

```python
class Classes(models.Model):
    name = models.CharField(max_length=20, verbose_name='班级')

class Student(models.Model):

    SEX_CHOICES = ((1,'男')), (2, '女')

    name = models.CharField(max_length=20, verbose_name='姓名')
    age = models.IntegerField(null=True, blank=True, verbose_name='年龄')
    sex = models.IntegerField(choices=SEX_CHOICES, default=1, verbose_name='性别')

    classes = models.ForeignKey(Classes, null=True, on_delete=models.SET_NULL, verbose_name='班级')

```



#### 关系为 一  的数据

serializers： 

```python
class ClassesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Classes
        fields = ['id', 'name']

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ['id', 'name', 'age', 'sex', 'classes']
```

说明：

- 只是在StudentSerializer类的meta中 fields 字段中添加了 classes 字段，那么序列化时，显示的只是 对应的班级的主键id，如：{"id": 3, "name": "terry", "age": 18, "sex": 1, "classes":1}

  如果想序列化对应的班级的信息，那么需要在 StudentSerializer 中，重新指定 classes 字段

  ```python
  class StudentSerializer(serializers.ModelSerializer):
  
      classes = ClassesSerializer()
  
      class Meta:
          model = Student
          fields = ['id', 'name', 'age', 'sex', 'classes']
  ```

  当前修改后的序列化内容为：{"id": 3, "name": "terry", "age": 18, "sex": 1, "classes": {"id": 1, "name": "\u4e00\u73ed"}}

  

#### 关系为 多 的数据

以上只是显示了一对多关系中，关系为一的数据的序列化，下面展示如何序列化多关系为多的一方

models：

```python
class Student(models.Model):

    SEX_CHOICES = ((1,'男')), (2, '女')

    name = models.CharField(max_length=20, verbose_name='姓名')
    age = models.IntegerField(null=True, blank=True, verbose_name='年龄')
    sex = models.IntegerField(choices=SEX_CHOICES, default=1, verbose_name='性别')
	
    # 必须增加属性 related_name='students'
    classes = models.ForeignKey(Classes, related_name='students', null=True, on_delete=models.SET_NULL, verbose_name='班级')
```

serializers：

```python
class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ['id', 'name', 'age', 'sex']

class ClassesSerializer(serializers.ModelSerializer):
	# students 命名是model中的 related_name
    # 多条记录，则指定 many=True , read_only=True
    students = StudentSerializer(many=True, read_only=True)

    class Meta:
        model = Classes
        fields = ['id', 'name', 'students']
```

​	注意：StudentSerializer 必须在 ClassesSerializer 上面

urls:

```
path('classes/<int:pk>/', views.classes_detail),
```

views：

```python
def classes_detail(request, pk):
    try:
        classes = Classes.objects.get(pk=pk)
    except Classes.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ClassesSerializer(classes)
        return JsonResponse(serializer.data)
    else:
        # 其他情况暂不处理
        return HttpResponse(status=503)
```

测试：

```
curl -i http://127.0.0.1:8000/rest/classes/1/

# 结果：
{"id": 1, "name": "\u4e00\u73ed", "students": [{"id": 3, "name": "terry", "age": 18, "sex": 1, "classes": 1}, {"id": 5, "name": "shine", "age": 18, "sex": 1, "classes": 1}]}
```



#### 手动处理关系字段

​	上述第二点中，由于类的引用关系的原因，左右只能自动序列化一个关系字段，如果业务需求，需要2个关系字段都序列化，那么就需要使用到 serializers.RelatedField 类，手动处理关系字段

serializers：

```python
class ClassesRelateField(serializers.RelatedField):

    def to_representation(self, value):
        # return f'classes：{value.name}'
        return {'id':value.id, 'name':value.name}

class StudentSerializer(serializers.ModelSerializer):

    classes = ClassesRelateField(read_only=True)

    class Meta:
        model = Student
        fields = ['id', 'name', 'age', 'sex', 'classes']

class ClassesSerializer(serializers.ModelSerializer):

    students = StudentSerializer(many=True, read_only=True)

    class Meta:
        model = Classes
        fields = ['id', 'name', 'students']
```

注意：上面3个类的先后顺序不能错



测试：

```
curl -i http://127.0.0.1:8000/rest/students/3/
# 结果：
{"id": 3, "name": "terry", "age": 18, "sex": 1, "classes": {"id": 1, "name": "\u4e00\u73ed"}}

curl -i http://127.0.0.1:8000/rest/classes/1/
# 结果：
{"id": 1, "name": "\u4e00\u73ed", "students": [{"id": 3, "name": "terry", "age": 18, "sex": 1, "classes": {"id": 1, "name": "\u4e00\u73ed"}}, {"id": 5, "name": "shine", "age": 18, "sex": 1, "classes": {"id": 1, "name": "\u4e00\u73ed"}}]}
```



## 4、请求和响应

​	REST framework引入了2个新的对象：Request和Response



### 1.Request

​	包结构：rest_framework.request.Request

​	该对象扩展了常规的HttpRequest ，增加了对REST框架灵活的请求解析和请求认证的支持

​	主要属性：

- data

  这个属性类似django的request的POST和FILES属性：

  - django的request.POST：只能获取POST请求的form表单数据
  - rest_framework的request.data：
    - 包括所有已解析的内容，包括文件和非文件输入
    - 支持'POST', 'PUT' 和'PATCH' 方法
    - 支持REST框架的灵活请求解析，而不仅仅支持表单数据。例如，可以传入JSON数据

- query_params

  就是标准的request.GET属性，不过从命名角度来说，更加合理，因为不是只有GET请求才有GET查询参数

- parsers

  一般不需要访问

  在视图中应用 APIView类或@api_view装饰（装饰视图函数）将确保这个属性被自动设置



​	注意：

​	如果客户端发送格式错误的内容，则访问request.data可能会引发错误ParseError。默认情况下，REST框架的APIView类或@api_view装饰器将捕获错误并返回400 Bad Request响应。

​	如果客户端发送的请求具有无法解析的内容类型，UnsupportedMediaType则会引发异常，默认情况下将捕获该异常并返回415 Unsupported Media Type响应



### 2.Response

​	包结构：rest_framework.response.Response

​	该类是Django的 SimpleTemplateResponse 的子类，使用python原始对象进行数据初始化，然后，REST框架使用标准HTTP内容协商来确定它应如何呈现最终的响应内容

​	初始化：Response(data, status=None, template_name=None, headers=None, content_type=None) 

- `data`：响应的序列化数据，如果是复杂对象，如模型实例，需要在传入之前序列化为原始数据类型（如dict等）
- `status`：响应的状态代码，默认为200
- `template_name`：`HTMLRenderer`选择时使用的模板名称
- `headers`：要在响应中使用的HTTP标头的字典
- `content_type`：响应的内容类型。通常，这将由内容协商确定的渲染器自动设置，但在某些情况下您可能需要明确指定内容类型



属性：

- data：响应的未呈现的序列化数据 

- status_code：响应状态码，建议使用HTTP_200_OK 这样的常量，而不是 200 这样的数字，常量给每个状态代码提供更明确的标识符 

  更详细的见：https://www.django-rest-framework.org/api-guide/status-codes/

- content：渲染后的响应内容，调用此属性前需要调用.render()方法渲染

- template_name：指定的模板名

- accepted_renderer：用于渲染响应内容的渲染器实例，在视图返回响应之前由`APIView`或`@api_view`自动设置 

- accepted_media_type：内容协商选择的媒体类型，在视图返回响应之前由`APIView`或`@api_view`自动设置 

- renderer_context：需要渲染的上下文字典对象，在视图返回响应之前由`APIView`或`@api_view`自动设置 



### 3.视图API包装器

框架使用了2个包装 API视图 的包装器：

- APIView：用于处理基于类的视图
- @api_view：用于处理基于函数的视图的装饰器 



### 4.项目应用

修改 views：

```python
# 使用 api_view 装饰器， 指定method，默认只有 GET
@api_view(['GET', 'POST'])
def students(request):
    if request.method == 'GET':
        student = Student.objects.all()
        serializer = StudentSerializer(student, many=True)
        # 使用Response替换 JsonResponse
        return Response(serializer.data)

    elif request.method == 'POST':
        # 直接使用 request.data 即可
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def student_detail(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
```

修改完毕后，在curl命令和浏览器分别测试查看效果



### 5.格式后缀

​	为了使我们的响应不再硬连接到单个内容类型这一事实，我们可以将API格式后缀添加到API之后。使用格式后缀为我们提供了明确引用给定格式的URL，譬如：http://example.com/api/items/4.json



views：在函数最后添加 formt=None 参数，示例：

```python
def students(request, format=None):

def student_detail(request, pk, format=None):
```



urls:

```python
from rest_framework.urlpatterns import format_suffix_patterns
# 可以使用 allowed=['json', 'html'] 参数指定允许的后缀
urlpatterns = format_suffix_patterns(urlpatterns)
```



测试：

通过后缀指定响应格式：

```
http://127.0.0.1:8000/rest/students.api

http://127.0.0.1:8000/rest/students/

http://127.0.0.1:8000/rest/students.json


```

使用请求头指定响应格式：

```
curl -i http://127.0.0.1:8000/rest/students/ -H Accept:application/json
```



## 5、基于类的视图（CBV）

​	我们上面的视图示例代码都是基于函数的（FBV），现在使用CBV的方式改写：

views：

```python
class StudentsView(APIView):

    def get(self, request, format=None):
        student = Student.objects.all()
        serializer = StudentSerializer(student, many=True)
        # 使用Response替换 JsonResponse
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

```

urls：

```python
path('students/', views.StudentsView.as_view()),
```

测试，和之前使用FBV是一样的结果



mixins：

使用CBV的优势是可以轻松的编写可重用的行为，在REST framework中使用mixins，可以实现通用的创建/检索/更新/删除等操作

views：

```
class StudentsView(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
```

说明：

- ListModelMixin：实现list列表功能
- CreateModelMixin：实现create新增功能
- GenericAPIView：实现通用功能



通用视图：

上面的写法中，get和post 方法的功能也是通用的，可以更进一步，使用通用视图，如下：

views：

```python
class StudentsView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
```



## 6、身份验证和权限

到目前为止，程序的API对任何人都可以编辑或删除，没有任何限制。我们希望有一些更高级的行为，进行身份验证和权限分配，以确保：

- 数据始终与创建者相关联
- 只有经过身份验证的用户才能创建数据
- 只有数据的创建者可以更新或删除
- 未经身份验证的请求只有只读访问权限



### 1.使用admin应用的User

- 配置好settings中的数据库配置
- 将admin应用的数据库进行迁移

```
python manage.py migrate admin
```

- 使用 createsuperuser 创建用户

```
python manage.py createsuperuser
```



### 2.给可浏览的API添加登录功能

在根urls中添加：

```
urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]
```

说明：

- api-auth： 可以设置为任意符合规则的路径
- 再次访问api页面，在页面的右上角会看到登录操作的按钮



### 3.视图中添加权限

​	实现未经身份验证的请求只有 只读 权限，需要使用CBV的方式，在视图类中添加权限，因此先将 student_detail 函数修改为 CBV的方式：

views：

```python
class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer
```

urls：

```python
path('students/<int:pk>/', views.StudentDetailView.as_view()),
```



设置权限，在对应的 view 类中增加属性：

```python
permission_classes = [permissions.IsAuthenticatedOrReadOnly]
```

说明：对比增加前后，会发现增加该属性后，未登录状态下，页面上没有删除等操作按钮

使用curl命令：

```
# 会返回 403， 禁止的操作
curl -i http://127.0.0.1:8000/rest/students/3/ -X DELETE

# 返回204，删除成功
curl -i http://127.0.0.1:8000/rest/students/3/ -X DELETE -u admin:qwer1234
```



### 4.数据和用户关联

实现 User 模型的序列化：

serializers：

```python
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username']
```

views：

```python
from django.contrib.auth.models import User


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
```

说明：注意，2个view类都只是实现了get功能

urls：

```python
path('users/', views.UserList.as_view()),
path('users/<int:pk>/', views.UserDetail.as_view()),
```

说明：修改完毕后，增加用户数据，并且进行查看



对应数据的模型中增加：

```
owner = models.ForeignKey('auth.User', related_name='students', null=True, on_delete=models.SET_NULL)
```

说明：修改完后执行数据库迁移

serializers：

```python
class StudentSerializer(serializers.ModelSerializer):

    classes = ClassesRelateField(read_only=True)
    owner = serializers.ReadOnlyField(source='owner.username')
    
    class Meta:
        model = Student
        fields = ['id', 'name', 'age', 'sex', 'classes', 'owner']
```

说明：

- 增加只读的owner = serializers.ReadOnlyField(source='owner.username')
- 在 Meta的 fields中增加 'owner'
- 修改完毕后，在页面中刷新，可以看到 owner 数据了



由于owner是只读的，所以需要在添加数据时，就根据用户验证情况，将 owner 数据保存起来，需要在对应的执行新增操作的view中，增加：

```python
class StudentsView(generics.ListCreateAPIView):

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
```

说明：perform_create方法，在对应的serializer执行新增操作的时候，传入指定的owner=self.request.user



当前数据的权限是未登录验证的请求只有可读权限，验证后的请求有删除/更新等所有操作权限。

现在将权限修改为只有所有者 owner 登录验证的请求才能执行删除/更新等操作

在子应用目录下，新增permissions.py：

```python
class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.owner == request.user
```

说明：

- 继承自permissions.BasePermission
- 实现方法has_object_permission，返回boolean
- if request.method in permissions.SAFE_METHODS 判断安全的操作，其实就是'GET', 'HEAD', 'OPTIONS'这3个操作，则返回True，只读
- 其他类型操作则 obj.owner == request.user 判断验证的用户是否为owner



修改对应视图类：

```python
class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    queryset = Student.objects.all()
    serializer_class = StudentSerializer
```

说明：

permission_classes 属性中增加了IsOwnerOrReadOnly，前面的IsAuthenticatedOrReadOnly可以不保留



### 5.JWT

#### 1.概述

基于django-rest-framework的登陆认证方式常用的大体可分为四种: 

1. BasicAuthentication：账号密码登陆验证 
2. SessionAuthentication：基于session机制会话验证 
3. TokenAuthentication： 基于令牌的验证 
4. JSONWebTokenAuthentication：基于Json-Web-Token的验证



我们前面演示的就是第1,2种认证方式，而实际项目中，最常用的就是JWT的方式

JWT具有以下优点： 

1. 签名的方式验证用户信息，安全性较之一般的认证高 
2. 加密后的字符串保存于客户端浏览器中，减少服务器存储压力 
3. 签名字符串中存储了用户部分的非私密信息，能够减少服务器数据库的开销
4. 能够不需要做任何额外工作，即可实现单点登录

缺点： 
1. 采用对称加密，一旦被恶意用户获取到加密方法，就可以不断破解入侵获取信息
2. 加大了服务器的计算开销



#### 2.JWT简介

​	JWT 是一个开放标准(RFC 7519)，它定义了一种用于简洁，自包含的用于通信双方之间以 JSON 对象的形式安全传递信息的方法。



#### 3.JWT 组成

![](.\imgs\jwt_header.png)

- header、Payload和Signature之间用 . 号连接
- Header 头部

头部包含了两部分，token 类型和采用的加密算法

```
{
  "alg": "HS256",
  "typ": "JWT"
}
```

- `typ`: （Type）类型，指明类型是`JWT`。
- `alg`: （Algorithm）算法，必须是JWS支持的算法，主要是HS256和RS256

它会使用 base64url编码组成 JWT 结构的第一部分



- **Payload 负载**

这部分就是我们存放信息的地方了，你可以把用户 ID 等信息放在这里，JWT 规范里面对这部分有进行了比较详细的介绍，JWT 规定了7个官方字段，供选用

```
iss (issuer)：签发人
exp (expiration time)：过期时间，时间戳
sub (subject)：主题
aud (audience)：受众
nbf (Not Before)：生效时间，时间戳
iat (Issued At)：签发时间，时间戳
jti (JWT ID)：编号
```

常用的有iss、iat、exp、aud和sub

同样的，它会使用 base64url 编码组成 JWT 结构的第二部分



- **Signature 签名**

 签名的作用是保证 JWT 没有被篡改过

前面两部分都是使用 base64url 进行编码的，前端可以解开知道里面的信息。Signature 需要使用编码后的 header 和 payload 以及我们提供的一个密钥，这个密钥只有服务器才知道，不能泄露给用户，然后使用 header 中指定的签名算法（HS256）进行签名。

```
HMACSHA256(
  base64UrlEncode(header) + "." +
  base64UrlEncode(payload),
  secret)
```

算出签名以后，把 Header、Payload、Signature 三个部分拼成一个字符串，每个部分之间用"点"（.）分隔，就可以返回给用户。

```
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNTY3MTU2MTA5LCJlbWFpbCI6ImFkbWluQGV4YW1wbGUuY29tIiwib3JpZ19pYXQiOjE1NjY1NTEzMDl9.VwVwdkQalKip4Cp1_8QjcqR0n_S9w3jgUJEf3oO4PoI
```

- 签名的目的

　　最后一步签名的过程，实际上是对头部以及负载内容进行签名，防止内容被篡改。如果有人对头部以及负载的内容解码之后进行修改，再进行编码，最后加上之前的签名组合形成新的JWT的话，那么服务器端会判断出新的头部和负载形成的签名和JWT附带上的签名是不一样的。如果要对新的头部和负载进行签名，在不知道服务器加密时用的密钥的话，得出来的签名也是不一样的。



#### 4.JWT 的使用方式

客户端收到服务器返回的 JWT，可以储存在 Cookie 里面，也可以储存在 localStorage。

 

此后，客户端每次与服务器通信，都要带上这个 JWT。你可以把它放在 Cookie 里面自动发送，但是这样不能跨域，所以更好的做法是放在 HTTP 请求的头信息`Authorization`字段里面。

![](.\imgs\jwt.png)

1. 首先，前端通过Web表单将自己的用户名和密码发送到后端的接口。这一过程一般是一个HTTP POST请求。建议的方式是通过SSL加密的传输（https协议），从而避免敏感信息被嗅探。

2. 后端核对用户名和密码成功后，将用户的id等其他信息作为JWT Payload（负载），将其与头部分别进行Base64编码拼接后签名，形成一个JWT。形成的JWT就是一个形同lll.zzz.xxx的字符串。

3. 后端将JWT字符串作为登录成功的返回结果返回给前端。前端可以将返回的结果保存在localStorage或sessionStorage上，退出登录时前端删除保存的JWT即可。

4. 前端在每次请求时将JWT放入HTTP Header中的Authorization位。(解决XSS和XSRF问题）

5. 后端检查是否存在，如存在验证JWT的有效性。例如，检查签名是否正确；检查Token是否过期；检查Token的接收方是否是自己（可选）。

   

#### 5.JWT 的几个特点

（1）JWT 默认是不加密，但也是可以加密的。生成原始 Token 以后，可以用密钥再加密一次。

（2）JWT 不加密的情况下，不能将秘密数据写入 JWT。

（3）JWT 不仅可以用于认证，也可以用于交换信息。有效使用 JWT，可以降低服务器查询数据库的次数。

（4）JWT 的最大缺点是，由于服务器不保存 session 状态，因此无法在使用过程中废止某个 token，或者更改 token 的权限。也就是说，一旦 JWT 签发了，在到期之前就会始终有效，除非服务器部署额外的逻辑。

（5）JWT 本身包含了认证信息，一旦泄露，任何人都可以获得该令牌的所有权限。为了减少盗用，JWT 的有效期应该设置得比较短。对于一些比较重要的权限，使用时应该再次对用户进行认证。

（6）为了减少盗用，JWT 不应该使用 HTTP 协议明码传输，要使用 HTTPS 协议传输。



#### 6.项目中应用JWT

1. 安装

一般使用 djangorestframework-jwt 库来实现JWT

```
pip install djangorestframework-jwt==1.11.0
```



2. settings：

```python
REST_FRAMEWORK = {
    # 默认的验证是按照验证列表 从上到下 的验证
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 配置JWT认证
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        # 配置session_id认证
        'rest_framework.authentication.SessionAuthentication',
        # 配置默认的认证方式 base:账号密码验证
        'rest_framework.authentication.BasicAuthentication',
    )
}

JWT_AUTH = {
    # 允许刷新token
    'JWT_ALLOW_REFRESH': True,
    # 每次刷新后，token的有效时间
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=1),
    # 生成 token 后，最大的有效时间：在有效期内通过刷新可以保持token有效；超过这个时间后，token失效，刷新也不起作用
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=30),
}
```



3. urls

   在根url或子应用项目下配置JWT登录的url路由，本文配置在根urls下：

```python
# post 登录JWT，获取token的url
path('api-token-auth/', obtain_jwt_token),
```



4. 登录JWT，获取token

```
# url 参数提交
curl http://127.0.0.1:8000/api-token-auth/ -i -X POST -d "username=admin&password=qwer1234"

# json 方式提交
curl http://127.0.0.1:8000/api-token-auth/ -i -X POST -H "Content-Type: application/json" -d {\"username\":\"admin\",\"password\":\"qwer1234\"} 
```



5. 应用JWT

   访问需要登录的请求时，通过 "Authorization: JWT <your_token>"携带 第4步 获取的token

```
curl -i http://127.0.0.1:8000/rest/students/ -X POST -H "Content-Type: application/json" -d {\"name\":\"jwt_stu\",\"age\":18,\"sex\":1} -H "Authorization:JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNTY3MzA0Mzc0LCJlbWFpbCI6ImFkbWluQGV4YW1wbGUuY29tIiwib3JpZ19pYXQiOjE1NjcyMTc5NzR9.JOLiavpHXxF70bZfTtB1bmgeQ780dSVcgX8i9pVoGhU"
```



6. 刷新token

   为了防止token失效，一般需要定期进行刷新

   urls中增加：

```python
# post 刷新JWT的token 的url
path('api-token-refresh/', refresh_jwt_token),
```

​	访问：

```
curl -i http://127.0.0.1:8000/api-token-refresh/ -X POST -H "Content-Type: application/json" -d {\"token\":\"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNTY3MTU4OTI5LCJlbWFpbCI6ImFkbWluQGV4YW1wbGUuY29tIiwib3JpZ19pYXQiOjE1NjY1NTQxMjl9.h8RNpuEXLhL9ZYlSCwrdXHUr5Nf-HGLZtlmMyQp3Frk\"} 
```



7. 认证token

   有些应用中，有专门的服务器进行token认证，其它服务器得到token后，提交给专门的认证服务器进行认证

   urls：

```python
path('api-token-verify/', verify_jwt_token),
```

​	访问：

```
curl -i http://127.0.0.1:8000/api-token-verify/ -X POST -H "Content-Type: application/json" -d {\"token\":\"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNTY3MTU4OTI5LCJlbWFpbCI6ImFkbWluQGV4YW1wbGUuY29tIiwib3JpZ19pYXQiOjE1NjY1NTQxMjl9.h8RNpuEXLhL9ZYlSCwrdXHUr5Nf-HGLZtlmMyQp3Frk\"} 
```

说明：

认证成功返回200状态码，内容是：{"token":"your_token"}

认证失败犯规400状态码，内容是：{"non_field_errors":["Error decoding signature."]}



8. 所有配置项在：rest_framework_jwt\settings.py 中可以查看到，不过一般不需要配置其它更多的配置项



## 7、xadmin

​	django自带的admin管理后台，样式一般，因此可以采用一个基于bootstrap的后台xadmin替代

​	文档：https://xadmin.readthedocs.io/en/docs-chinese/



### 1.安装

​	不建议使用 pip 安装，各种错误，而且django2之后的版本，需要使用特定版本的django2版本，因此建议从github网站上直接获取：https://github.com/sshwsfc/xadmin/tree/django2，下载zip文件，解压后，记住其中的 xadmin 文件夹，后续会使用到

​	在cmd中，切换解压目录，执行以下命令，安装依赖库：

```
pip install -r requirements.txt
```

​	注意：没有安装django-crispy-forms库，运行服务器会报 RuntimeError: populate() isn't reentrant  错误



### 2.项目中添加xadmin

根目录下添加 extra_apps 文件夹，并右键——Mark Directory as——Sources Root，设置为项目资源文件 

将 第一步 解压的 xadmin 文件夹拷贝到 extra_apps 文件夹中



### 3.settings

```python
# 将第二步的文件夹加载到系统路径中
sys.path.insert(0, os.path.join(BASE_DIR, 'extra_apps'))

# 添加应用
INSTALLED_APPS = [
    # ...
    'xadmin',
    'crispy_forms'
]
```



### 4.urls

在项目根urls中增加：

```python
path('xadmin/', xadmin.site.urls),
```



### 5.迁移数据库

```
python manage.py migrate xadmin
```



### 6.访问

在浏览器中，通过 http://127.0.0.1:8000/xadmin/ 即可访问新的xadmin管理后台



异常处理：

点击 添加小组件 时，会出现错误：

```
TypeError: render() got an unexpected keyword argument 'renderer'
```

解决方法：

找到 xadmin.views.dashboard.WidgetTypeSelect 类，修改其中的方法：

```python
# 原始方法
def render(self, name, value, attrs=None)
# 修改后的方法，增加 renderer=None 参数
def render(self, name, value, attrs=None, renderer=None)
```



### 7、将现有模型纳入管理

在子应用目录下新建 adminx.py：

```python
from .models import Student, Classes
import xadmin

# 默认管理
xadmin.site.register(Classes)


# 装饰器注册，注意是 xadmin.sites.register ，其中的 sites 有个 s
@xadmin.sites.register(Student)
class StudentAdmin(object):
    list_display = ['name', 'age', "sex"]
    
    
# 普通注册，上面已经注册了，所以注释掉了， 注意是 xadmin.site.register , 其中 site
# xadmin.site.register(Student，StudentAdmin)
```



## 8、节流

​	节流又叫限流，限制访问。就是一个用户多次发送一个请求（页面或链接）的时候，单位时间内有允许访问次数限制，超过限制就会出现访问受限，提示譬如：离下一次访问还有多久之类等的字样



### 1.throttles.py

在子应用根目录下新建 throttles.py：

```python
from rest_framework.throttling import SimpleRateThrottle


class AnonymousThrottle(SimpleRateThrottle):
    # 如果有配置了多个缓存，默认使用'default'，可以通过 cache 属性指定
    # cache = caches['alternate']
    
    scope = "anonymous"

    def get_cache_key(self, request, view):
        return self.get_ident(request)


class UserThrottle(SimpleRateThrottle):
    scope = "user"

    def get_cache_key(self, request, view):
        return request.user.username
```

说明：

- 2个类，都继承自 SimpleRateThrottle 类，因为该类实现了很多通用的节流功能

- 都必须实现 get_cache_key 方法，返回该类用于节流的key（需要确保能够区分每个请求用户），

  这里：

  - AnonymousThrottle的get_cache_key：获取的请求的IP
  - UserThrottle的get_cache_key：登录用户的用户名

- scope：节流配置的key，用于在 配置 中对应 DEFAULT_THROTTLE_RATES 的配置

- cache：默认使用django项目配置的default缓存保存 客户端识别的信息，如果没有配置就保存在内存中

- 都是通过SimpleRateThrottle  类的 allow_request(self, request, view) 方法做的限制，可以自定义该方法进行覆盖，该方法返回boolean值



### 2.settings.py

配置节流信息：

```python
# 在REST 配置中增加配置项
REST_FRAMEWORK = {
    "DEFAULT_THROTTLE_CLASSES": ["rest_app.throttles.UserThrottle"],
    "DEFAULT_THROTTLE_RATES": {
        "anonymous": '5/m',
        "user": '10/m',
    }
}
```

说明：

- DEFAULT_THROTTLE_CLASSES：配置默认的节流类，列表，可以配置多个
- DEFAULT_THROTTLE_RATES： 节流频率的规则，字典，key是第一步中节流类的 scope 属性，值是 '5/m'： 
  - 5 是指允许的访问次数 
  - m 是指单位时间，总共4种，检测的代码：`{'s': 1, 'm': 60, 'h': 3600, 'd': 86400}[period[0]]`，后面的数字表示秒数，官方文档是用：second，minute，hour或day，其实从代码可以看出，只有第一个字符起作用



### 3.views.py

在视图中应用节流类：

```python
# 视图类
class StudentsView(generics.ListCreateAPIView):

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # 标识匿名用户访问
    throttle_classes = [throttles.AnonymousThrottle]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

        
# 视图函数，仅仅是示例，项目中没有使用
@api_view(['GET'])
@throttle_classes([throttles.AnonymousThrottle])
def example_view_func(request, format=None):
    content = {
        'status': 'request was permitted'
    }
    return Response(content)
```

说明：

- 增加throttle_classes = [throttles.AnonymousThrottle] 属性，值是节流类列表，可以配置多个，设置了此属性后，不会再应用默认节流类
- 没有设置 throttle_classes  属性的 APIView 视图类子类或@api_view装饰的视图函数，都使用第2步配置的默认节流类 



### 4.内置节流类

​	rest_framework.throttling下，除了有 SimpleRateThrottle 这个简单的节流类外，还有3个内置的类：

- AnonRateThrottle：处理未经授权的用户，请求的IP地址用于生成用于限制的唯一键 

- UserRateThrottle：处理授权的用户，用户标识用于生成要限制的唯一键。未经身份验证的请求将回退到使用传入请求的IP地址生成一个唯一的密钥来限制 

- ScopedRateThrottle：当正在访问的视图包含 throttle_scope 属性时，才会应用此限制，用法如下

  ```python
  #views：
  class ContactListView(APIView):
      throttle_scope = 'contacts'
      #...
  
  class ContactDetailView(APIView):
      throttle_scope = 'contacts'
      #...
  
  class UploadView(APIView):
      throttle_scope = 'uploads'
      #...
      
      
  # settings：
  REST_FRAMEWORK = {
      'DEFAULT_THROTTLE_CLASSES': [
          'rest_framework.throttling.ScopedRateThrottle',
      ],
      'DEFAULT_THROTTLE_RATES': {
          'contacts': '1000/day',
          'uploads': '20/day'
      }
  }
  ```

  说明：

  - ContactListView或ContactDetailView将限制为每天允许1000个请求
  - UploadView将限制为每天允许20个请求



## 9、版本

​	在RESTful 规范中，有关版本的问题，用restful规范做开放接口的时候，用户请求API，系统返回数据。但是难免在系统发展的过程中，不可避免的需要添加新的资源，或者修改现有资源。因此，改动升级必不可少，但是，作为平台开发者，应该知道：一旦API开放出去，有人开始用了，平台的任何改动都需要考虑对当前用户的影响。因此，做开放平台，从第一个API的设计就需要开始API的版本控制策略问题，API的版本控制策略就像是开放平台和平台用户之间的长期协议，其设计的好坏将直接决定用户是否使用该平台，或者说用户在使用之后是否会因为某次版本升级直接弃用该平台。



### 1.配置

​	有两种配置方案，一种是在settings中全局配置，第二种是在视图中指定，不过此方法一般不使用，因为版本控制大部分情况下是全局的处理情况

1. 全局配置

   settings.py：

   ```python
   REST_FRAMEWORK = {
       'DEFAULT_VERSIONING_CLASS': None,
       'DEFAULT_VERSION': None,
       'ALLOWED_VERSIONS': None,
       'VERSION_PARAM': 'version',
   }
   ```

   说明：

   - DEFAULT_VERSIONING_CLASS：指定版本控制的类，譬如：'rest_framework.versioning.NamespaceVersioning'，有多种方式，后续会详细讲解。默认为None，为None时，框架变量 request.version 将始终返回None
   - DEFAULT_VERSION：请求不存在版本控制时，request.version 返回的值
   - ALLOWED_VERSIONS：允许的版本号，譬如：['v1', 'v2']。区分大小写，如果请求的版本号不在此列表中，抛出错误，上述的 DEFAULT_VERSION 的值必须是列表中的值，None除外
   - VERSION_PARAM：版本控制参数的字符串，默认就是'version'，一般不修改

   

2. 视图配置

   views.py：

   ```python
   # 仅仅指定 版本控制类    
   class ProfileList(APIView):
       # 指定 版本控制类
       versioning_class = versioning.QueryParameterVersioning
       
   ```

   ```python
   # 通过自定义类 继承版本控制类，并且指定其余版本配置参数
   class ExampleVersioning(versioning.QueryParameterVersioning):
       default_version = 'v1'
       allowed_versions = ['v1', 'v2']
       version_param = 'version'
       
   class ExampleView(APIView):
       # 指定 版本控制类
       versioning_class = ExampleVersioning
   ```

   

### 2.AcceptHeaderVersioning

​	基于请求头的版本控制，这种方式也是最推荐的方式

1. http访问方式

   ```
   GET /bookings/ HTTP/1.1
   Host: example.com
   Accept: application/json; version=1.0
   ```

   

2. settings

   ```python
   REST_FRAMEWORK = {
   	'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.AcceptHeaderVersioning',
       'DEFAULT_VERSION': 'v1',
       'ALLOWED_VERSIONS': ['v1', 'v2'],
   }
   ```

   说明：

   - 设置版本控制类为 AcceptHeaderVersioning
   - 没有检测到version时，默认是 v1 版本
   - 允许的2个版本型号为：['v1', 'v2']

   

3. serializers

   ```python
   class StudentSerializer(serializers.ModelSerializer):
   
       classes = ClassesRelateField(read_only=True)
       owner = serializers.ReadOnlyField(source='owner.username')
   
       class Meta:
           model = Student
           fields = ['id', 'name', 'age', 'sex', 'classes', 'owner']
   
   class StudentSerializerV2(serializers.ModelSerializer):
   
       class Meta:
           model = Student
           fields = ['id', 'name', 'age', 'sex']
   ```

   说明：

   - 根据不同的版本号，可以对response返回内容进行控制，在本文档中，我们设置2个不同的Student模型的serializer类对应不同的版本

   - 2个序列化类返回的字段不同

   - StudentSerializerV2 的 fields中没有包含 classes 和 ower ，那么就应该把属性定义去掉，不然会抛出错误

     

4. views

   ```python
   class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
       permission_classes = [IsOwnerOrReadOnly]
   
       queryset = Student.objects.all()
       serializer_class = StudentSerializer
       
       def get_serializer_class(self):
           if self.request.version == 'v2':
               return StudentSerializerV2
           
           return self.serializer_class
   ```

   说明：

   - 修改StudentDetailView类，重载 get_serializer_class 方法
   - 通过 self.request.version 获取捕获到的版本号进行控制

   

5. 访问

   ```
   # 访问 v1
   curl http://127.0.0.1:8000/rest/students/4/ -i -H "Accept:application/json;version=v1"
   
   # 访问 v2
   curl http://127.0.0.1:8000/rest/students/4/ -i -H "Accept:application/json;version=v2"
   ```



### 3.URLPathVersioning

​	将版本指定为URL路径的一部分 

1. http访问方式

   ```
   GET /v1/bookings/ HTTP/1.1
   Host: example.com
   ```

   说明：

   - 版本控制出现在url路径中，但是具体的这个 v1 出现在哪个部分，取决于url路由配置中的情况

     

2. settings

   ```python
   REST_FRAMEWORK = {
   	'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.URLPathVersioning',
       'DEFAULT_VERSION': 'v1',
       'ALLOWED_VERSIONS': ['v1', 'v2'],
   }
   ```

   

3. urls

   子应用的urls.py中：

   ```python
   path('students/<int:pk>/', views.StudentDetailView.as_view()),
   path('students/<str:version>/<int:pk>/', views.StudentDetailView.as_view()),
   ```

   说明：

   - 第一行是原有的访问配置，不变更
   - 第二行是新的进行版本控制后的路由配置，设置 版本控制在最后，访问url是类似：http://127.0.0.1:8000/rest/students/v2/4/ 

   

4. 访问

   ```
   # 访问 旧版本
   curl http://127.0.0.1:8000/rest/students/4/ -i
   
   # 访问 v1， 等同 旧版本
   curl http://127.0.0.1:8000/rest/students/v1/4/ -i
   
   # 访问 v2
   curl http://127.0.0.1:8000/rest/students/v2/4/ -i
   ```



### 4.QueryParameterVersioning

​	将版本作为URL中的查询参数  

1. http访问方式

   ```
   GET /something/?version=v1 HTTP/1.1
   Host: example.com
   ```

   

2. settings

   ```python
   REST_FRAMEWORK = {
   	'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.QueryParameterVersioning',
       'DEFAULT_VERSION': 'v1',
       'ALLOWED_VERSIONS': ['v1', 'v2'],
   }
   ```

   

3. urls

   子应用的urls.py中：

   ```python
   path('students/<int:pk>/', views.StudentDetailView.as_view()),
   # path('students/<str:version>/<int:pk>/', views.StudentDetailView.as_view()),
   ```

   说明：

   - 只需要 'students/<int:pk>/' 这一个配置即可

   

4. 访问

   ```
   # 访问 旧版本
   curl http://127.0.0.1:8000/rest/students/4/ -i
   
   # 访问 v1， 等同 旧版本
   curl http://127.0.0.1:8000/rest/students/4/?version=v1 -i
   
   # 访问 v2
   curl http://127.0.0.1:8000/rest/students/4/?version=v2 -i
   ```

   

### 4.NamespaceVersioning

​	对客户来说，这个方案和URLPathVersioning一样，唯一的区别是它在Django应用程序中的配置方式，因为它使用URL命名空间而不是URL关键字参数

​	URLPathVersioning更适合于小型临时项目

​	NamespaceVersioning更容易管理大型项目

1. http访问方式

   ```
   GET v1/something/ HTTP/1.1
   Host: example.com
   ```

   

2. settings

   ```python
   REST_FRAMEWORK = {
   	'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.NamespaceVersioning',
       'DEFAULT_VERSION': 'v1',
       'ALLOWED_VERSIONS': ['v1', 'v2'],
   }
   ```

   

3. urls

   根urls.py中：

   ```python
   path('rest/', include('rest_app.urls', namespace='v1')),
   path('v1/rest/', include('rest_app.urls', namespace='v1')),
   path('v2/rest/', include('rest_app.urls', namespace='v2')),
   ```

   说明：

   - 增加了2个 v1和v2的不同的路由配置

   

4. 访问

   ```
   # 访问 旧版本
   curl http://127.0.0.1:8000/rest/students/4/ -i
   
   # 访问 v1， 等同 旧版本
   curl http://127.0.0.1:8000/v1/rest/students/4/ -i
   
   # 访问 v2
   curl http://127.0.0.1:8000/v2/rest/students/4/ -i
   ```

   

### 5.HostNameVersioning

​	主机名版本控制方案要求客户端将请求的版本指定为URL中域名的一部分，如：http://v1.example.com/bookings/，v1就是版本号，默认情况下，此实现要求域名与此简单正则表达式匹配：

```
^([a-zA-Z0-9]+)\.[a-zA-Z0-9]+\.[a-zA-Z0-9]+$
```

请注意，第一个组用括号括起来，表示这是域名的匹配部分。

​	如果有根据版本将请求路由到不同服务器的要求，则基于域名的版本控制特别有用，因为可以为不同的API版本配置不同的DNS记录。 

​	但是在开发环境下，都是用 127.0.0.1 这样的方式访问，测试起来很麻烦，本文档中就不进行演示了



### 6.自定义版本类

​	通过，并且实现 其中的 方法：

```python
class XAPIVersionScheme(versioning.BaseVersioning):
    def determine_version(self, request, *args, **kwargs):
        version = request.META.get('HTTP_X_API_VERSION', self.default_version)
        if not self.is_allowed_version(version):
            raise exceptions.NotFound(self.invalid_version_message)
        return version
```

说明：

- 继承 rest_framework.versioning.BaseVersioning
- 实现 determine_version 方法，获取版本号
- 这里通过请求中的 META 中的 HTTP_X_API_VERSION 获取版本号，而不是配置的 version_param