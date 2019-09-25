# 一、django应用Celery

## 1、概述

### 1.Celery介绍

​	Celery是由Python开发、简单、灵活、可靠的分布式任务队列，是一个处理异步任务的框架，其本质是生产者消费者模型，生产者发送任务到消息队列，消费者负责处理任务。Celery侧重于实时操作，但对调度支持也很好，其每天可以处理数以百万计的任务。特点：

- 简单：熟悉celery的工作流程后，配置使用简单
- 高可用：当任务执行失败或执行过程中发生连接中断，celery会自动尝试重新执行任务
- 快速：一个单进程的celery每分钟可处理上百万个任务
- 灵活：几乎celery的各个组件都可以被扩展及自定制



​	Celery由三部分构成：

- 消息中间件(Broker)：官方提供了很多备选方案，支持RabbitMQ、Redis、Amazon SQS、MongoDB、Memcached 等，官方推荐RabbitMQ

- 任务执行单元(Worker)：任务执行单元，负责从消息队列中取出任务执行，它可以启动一个或者多个，也可以启动在不同的机器节点，这就是其实现分布式的核心 

- 结果存储(Backend)：官方提供了诸多的存储方式支持：RabbitMQ、 Redis、Memcached,SQLAlchemy, Django ORM、Apache Cassandra、Elasticsearch等

  

  架构如下： 

![](.\imgs\celery.png)



​	工作原理：

1. 任务模块Task包含异步任务和定时任务。其中，异步任务通常在业务逻辑中被触发并发往消息队列，而定时任务由Celery Beat进程周期性地将任务发往消息队列；
2. 任务执行单元Worker实时监视消息队列获取队列中的任务执行；
3. Woker执行完任务后将结果保存在Backend中;



### 2.django应用Celery

​	django框架请求/响应的过程是同步的，框架本身无法实现异步响应。

​	但是我们在项目过程中会经常会遇到一些耗时的任务, 比如：发送邮件、发送短信、大数据统计等等，这些操作耗时长，同步执行对用户体验非常不友好，那么在这种情况下就需要实现异步执行。

​	异步执行前端一般使用ajax，后端使用Celery。



## 2、项目应用

​	django项目应用celery，主要有两种任务方式，一是异步任务（发布者任务），一般是web请求，二是定时任务

​	

​	本文档使用redis数据库作为消息中间件和结果存储数据库

​	环境如下：

- celery4.3
- redis3.3.7

	​	

		PS：本文仅适用celery库进行学习，另外有一些第三方库可以提供更方便的操作，譬如：django-celery，django-celery-beat等



### 1.异步任务redis

#### 1.安装库

```
pip install celery
```



#### 2.celery.py

在主项目目录下，新建 celery.py 文件：

```python
import os
import django
from celery import Celery
from django.conf import settings

# 设置系统环境变量，安装django，必须设置，否则在启动celery时会报错
# celery_study 是当前项目名
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery_study.settings')
django.setup()

celery_app = Celery('celery_study')
celery_app.config_from_object('django.conf:settings')
celery_app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
```

PS：是和settings.py文件同目录，一定不能建立在项目根目录，不然会引起 celery 这个模块名的命名冲突



同时，在主项目的init.py中，添加如下代码：

```python
from .celery import celery_app

__all__ = ['celery_app']
```



#### 3.settings.py

在配置文件中配置对应的redis配置：

```python
# Broker配置，使用Redis作为消息中间件
BROKER_URL = 'redis://127.0.0.1:6379/0' 

# BACKEND配置，这里使用redis
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/0' 

# 结果序列化方案
CELERY_RESULT_SERIALIZER = 'json' 

# 任务结果过期时间，秒
CELERY_TASK_RESULT_EXPIRES = 60 * 60 * 24 

# 时区配置
CELERY_TIMEZONE='Asia/Shanghai'   

# 指定导入的任务模块，可以指定多个
#CELERY_IMPORTS = (     
#    'other_dir.tasks',
#)
```

PS：所有配置的官方文档：http://docs.celeryproject.org/en/latest/userguide/configuration.html 



#### 4.tasks.py

在子应用下建立各自对应的任务文件tasks.py(必须是tasks.py这个名字，不允许修改)

```python
from celery import shared_task

@shared_task
def add(x, y):
    return x + y

@shared_task
def mul(x, y):
    return x * y

@shared_task
def xsum(numbers):
    return sum(numbers)
```



#### 5.调用任务

在 views.py 中，通过 delay 方法调用任务，并且返回任务对应的 task_id，这个id用于后续查询任务状态

```python
from . import tasks

def mul_func(request):
    ar = tasks.mul.delay(10, 3)

    return HttpResponse('返回mul任务，task_id:'+ ar.id)
```



#### 6.启动celery

在cmd窗口中，切换到项目根目录下，执行：

```
celery worker -A celery_study -l info
```

说明：

- -A celery_study：指定项目app
- worker： 表明这是一个任务执行单元
- -l info：指定日志输出级别



更多celery命令的参数，可以输入：

```
celery --help
或
celery worker --help
```



异常处理：

1. win10平台，使用celery4.x时，会出现以下错误：

```
ValueError: not enough values to unpack (expected 3, got 0)
```

解决方法：

- 先安装一个扩展 eventlet 

```
pip install eventlet
```

- 然后启动worker的时候加一个参数 -P eventlet，如下：

```
celery worker -A celery_study -l debug -P eventlet
```



2. 使用redis时，有可能会出现如下类似的异常

```
AttributeError: 'str' object has no attribute 'items'
```

这是由于版本差异，需要卸载已经安装的python环境中的 redis 库，重新指定安装特定版本（celery4.x以下适用 redis2.10.6， celery4.3以上使用redis3.2.0以上）：

```
pip install redis==2.10.6
```



#### 7.获取任务结果

在 views.py 中，通过 AsyncResult.get() 获取结果

```python
def get_result_by_taskid(request):
    task_id = request.GET.get('task_id')

    ar = result.AsyncResult(task_id)

    if ar.ready():
        return JsonResponse({'status': ar.state, 'result': ar.get()})
    else:
        return JsonResponse({'status': ar.state, 'result': ''})
```

AsyncResult类的常用的属性和方法：

- state: 返回任务状态，等同status；

- task_id: 返回任务id；

- result: 返回任务结果，同get()方法；

  

- ready(): 判断任务是否执行以及有结果，有结果为True，否则False；

- info(): 获取任务信息，默认为结果；

- wait(t): 等待t秒后获取结果，若任务执行完毕，则不等待直接获取结果，若任务在执行中，则wait期间一直阻塞，直到超时报错；

- successful(): 判断任务是否成功，成功为True，否则为False；



### 2.定时任务

​	在第一步的异步任务的基础上，进行部分修改即可



#### 1.settings.py

```python
from celery.schedules import crontab

CELERYBEAT_SCHEDULE = {
    'add_every_30_seconds': {
         # 任务路径
        'task': 'celery_app.tasks.add',
         # 每30秒执行一次
        'schedule': 30,
        'args': (14, 5)
    },
    'xsum_week1_20_20_00': {
         # 任务路径
        'task': 'celery_app.tasks.xsum',
        # 每周一20点20分执行
        'schedule': crontab(hour=20, minute=20, day_of_week=1),
        'args': ([1,2,3,4],),
    },
}
```

说明（更多内容见文档：http://docs.celeryproject.org/en/latest/userguide/periodic-tasks.html#crontab-schedules）：

- task：任务函数
- schedule：执行频率，可以是整型（秒数），也可以是timedelta对象，也可以是crontab对象，也可以是自定义类（继承celery.schedules.schedule）
- args：位置参数，列表或元组
- kwargs：关键字参数，字典
- options：可选参数，字典，任何 apply_async() 支持的参数
- relative：默认是False，取相对于beat的开始时间；设置为True，则取设置的timedelta时间



#### 2.启动celery

分别启动worker和beat

```
celery worker -A celery_study -l debug -P eventlet
celery beat -A celery_study -l debug
```



### 3.任务绑定

​	Celery可通过task绑定到实例获取到task的上下文，这样我们可以在task运行时候获取到task的状态，记录相关日志等 



代码如下：

```python
@shared_task(bind=True)
def mul(self, x, y):
    logger.info('-mul'*10)
    logger.info(self.name)
    logger.info(dir(self))
    return x * y
```

说明：

- 在装饰器中加入参数 bind=True

- 在task函数中的第一个参数设置为self

  self对象是celery.app.task.Task的实例，可以用于实现重试等多种功能

  ```python
  @shared_task(bind=True)
  def mul(self, x, y):
      try:
          logger.info('-mul' * 10)
          logger.info(f'{self.name}, id:{self.request.id}')
          raise Exception
      except Exception as e:
          # 出错每4秒尝试一次，总共尝试4次
          self.retry(exc=e, countdown=4, max_retries=4)  
      return x * y
  ```



### 4.任务钩子

​	Celery在执行任务时，提供了钩子方法用于在任务执行完成时候进行对应的操作，在Task源码中提供了很多状态钩子函数如：on_success(成功后执行)、on_failure(失败时候执行)、on_retry(任务重试时候执行)、after_return(任务返回时候执行)

1. 通过继承Task类，重写对应方法即可，示例：

```python
class MyHookTask(Task):

    def on_success(self, retval, task_id, args, kwargs):
        logger.info(f'task id:{task_id} , arg:{args} , successful !')

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        logger.info(f'task id:{task_id} , arg:{args} , failed ! erros: {exc}')

    def on_retry(self, exc, task_id, args, kwargs, einfo):
        logger.info(f'task id:{task_id} , arg:{args} , retry !  erros: {exc}')
```



2. 在对应的task函数的装饰器中，通过 base=MyHookTask 指定

```python
@shared_task(base=MyHookTask, bind=True)
def mul(self, x, y):
	......
```



### 5.任务编排

​	在很多情况下，一个任务需要由多个子任务或者一个任务需要很多步骤才能完成，Celery也能实现这样的任务，完成这类型的任务通过以下模块完成：

- group: 并行调度任务
- chain: 链式任务调度
- chord: 类似group，但分header和body2个部分，header可以是一个group任务，执行完成后调用body的任务
- map: 映射调度，通过输入多个入参来多次调度同一个任务
- starmap: 类似map，入参类似＊args
- chunks: 将任务按照一定数量进行分组



​	文档：https://docs.celeryproject.org/en/latest/getting-started/next-steps.html#canvas-designing-work-flows

#### 1.group

​	urls.py:

```python
path('primitive/', views.test_primitive),
```

​	views.py：

```python
def test_primitive(request):
    # 创建10个并列的任务
    lazy_group = group(tasks.add.s(i, i) for i in range(10))
    promise = lazy_group()
    result = promise.get()
    return JsonResponse({'function': 'test_primitive', 'result': result})
```

说明：

通过task函数的  s  方法传入参数，启动任务



上面这种方法需要进行等待，如果依然想实现异步的方式，那么就必须在tasks.py中新建一个task方法，调用group，示例如下：

tasks.py：

```python
@shared_task
def group_task(num):
    return group(add.s(i, i) for i in range(num))().get()
```

urls.py：

```python
path('first_group/', views.first_group),
```

views.py:

```python
def first_group(request):
    ar = tasks.group_task.delay(10)

    return HttpResponse('返回first_group任务，task_id:' + ar.task_id)
```



#### 2.chain

​	默认上一个任务的结果作为下一个任务的第一个参数

```python
def test_primitive(request):
    # 等同调用  mul(add(add(2, 2), 5), 8)
    promise = chain(tasks.add.s(2, 2), tasks.add.s(5), tasks.mul.s(8))()
    #  72
    result = promise.get()  
    return JsonResponse({'function': 'test_primitive', 'result': result})
```



#### 3.**chord** 

​	任务分割，分为header和body两部分，hearder任务执行完在执行body，其中hearder返回结果作为参数传递给body

```python
def test_primitive(request):
    # header：  [3, 12] 
    # body: xsum([3, 12])
    promise = chord(header=[tasks.add.s(1,2),tasks.mul.s(3,4)],body=tasks.xsum.s())()
    result = promise.get()
    return JsonResponse({'function': 'test_primitive', 'result': result})
```



### 6、celery管理和监控

​	celery通过flower组件实现管理和监控功能 ，flower组件不仅仅提供监控功能，还提供HTTP API可实现对woker和task的管理 

​	官网：https://pypi.org/project/flower/

​	文档：https://flower.readthedocs.io/en/latest



1. 安装flower

   ```
   pip install flower
   ```

   

2. 启动flower

   ```
   flower -A celery_study --port=5555   
   ```

   说明：

   - -A：项目名
   - --port： 端口号

   

3. 访问

   在浏览器输入：http://127.0.0.1:5555

   

4. 通过api操作

   ```
   curl http://127.0.0.1:5555/api/workers
   ```

   