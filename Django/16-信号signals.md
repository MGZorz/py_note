# 一、django的signals

## 1、概述

​	信号可以在框架中的其他位置发生操作时通知分离的应用程序，简而言之，就是信号允许特定的sender通知一组receiver某些操作已经发生，这在多处代码和同一事件有关联的情况下很有用。 

​	

## 2、内置信号

内置信号的完整文档：https://docs.djangoproject.com/zh-hans/2.2/ref/signals/



模型层中定义的内置信号，在 django.db.models.signals 模块中：

1. pre_init：实例化模型时，此信号在模型的\__init__()方法的开头发送

   此信号发送的参数：

   - instance：模型类
   - args：模型初始化的位置参数
   - kwargs：模型初始化的关键字参数

2. post_init：和pre_init一样，但是这个\__init__()方法在方法完成时发送

   此信号发送的参数：

   - instance：刚刚初始化完成的模型实例

3. pre_save：在模型 save()方法开始时发送

4. post_save：在模型 save()方法完成时发送

5. pre_delete：在模型 delete()方法开始时发送

6. post_delete：在模型 delete()方法结束时发送

7. m2m_changed：多对多关系中，模型更改时发送



对web请求，也有内置信号，在 django.core.signals 模块中

1. request_started：Django开始处理HTTP请求时发送 
2. request_finished：当Django完成向客户端发送HTTP响应时发送 



## 3、定义信号

所有的信号都是django.dispatch.Signal实例

初始化参数：providing_args=None, use_caching=False

- providing_args：信号将为sender提供的参数名称列表
- use_caching：默认为False，是否使用缓存，设置为True，会为每个sender对应的接收器进行缓存（保存到sender_receivers_cache），调用 .connect() 或 .disconnect() 后会清除缓存。内置信号基本都设置为True

示例：

```python
from django import dispatch

pizza_done = dispatch.Signal(providing_args=["toppings", "size"])
```



## 4、接收器receiver

接收器可以是任何python函数或方法，参数最少必须是：sender, **kwargs，示例如下：

```python
def my_callback(sender, **kwargs):
    print("第一个接收器函数！")
    
def my_callback1(sender, arg1=None, **kwargs):
    print("第二个接收器函数！")
```

参数说明：

- sender：信号的发送对象，其实可以是任意对象，取决于发送时传递的参数
- **kwargs：信号对象定义时的providing_args指定的参数



## 5、信号注册（连接到接收器）

有两种方式可以将信号连接上接收器

1. connect方法

   使用 Signal.connect() 监听信号，发送信号时调用接收器函数，Signal是信号对象

   Signal.connect（receiver，sender = None，weak = True，dispatch_uid = None）

   参数说明：

   - receiver - 将连接到此信号的回调函数

   - sender - 指定信号的特定发送者，为None就是任何发送者都接收

   - weak - Django默认将信号处理程序存储为弱引用。因此，如果您的接收器是本地函数，它可能是垃圾收集。为了防止这种情况，请在调用信号connect()方法时设置weak=False

   - dispatch_uid - 在可能发送重复信号的情况下信号接收器的唯一标识符，就是一个不重复的字符串

     

   示例如下：

   ```python
   from django.core.signals import request_finished
   
   request_finished.connect(my_callback)
   
   ```

   

2. receiver装饰器

   receiver(signal, **kwargs)

   参数说明：

   - signal：信号对象或信号对象列表
   - **kwargs：这个装饰器也是使用的connect方法，这个关键字参数就是传递给connect方法的关键字参数

   

   receiver源码：

   ```python
   def receiver(signal, **kwargs):
       """
       A decorator for connecting receivers to signals. Used by passing in the
       signal (or list of signals) and keyword arguments to connect::
   
           @receiver(post_save, sender=MyModel)
           def signal_receiver(sender, **kwargs):
               ...
   
           @receiver([post_save, post_delete], sender=MyModel)
           def signals_receiver(sender, **kwargs):
               ...
       """
       def _decorator(func):
           if isinstance(signal, (list, tuple)):
               for s in signal:
                   s.connect(func, **kwargs)
           else:
               signal.connect(func, **kwargs)
           return func
       return _decorator
   ```

   

   使用示例如下：

   ```python
   from django.core.signals import request_finished
   from django.dispatch import receiver
   
   @receiver(request_finished)
   def my_callback(sender, **kwargs):
       print("Request finished!")
       
   ```

   

3. 只接收特定发送者发送的信号

   ```python
   # 只接收特定模型MyModel发送的信号
   @receiver(pre_save, sender=MyModel)
   def my_handler(sender, **kwargs):
       ...
   ```

   

4. 防止重复信号

   在某些情况下，将接收器连接到信号的代码可能会多次运行，这可能导致接收器功能被多次注册，因此对于单个信号事件被多次调用（例如，在保存模型时使用信号发送电子邮件时），使用唯一标识符作为dispatch_uid参数以标识接收方函数，此标识符通常使用字符串，使用后有确保接收器仅对每个唯一dispatch_uid值绑定一次信号：

   ```python
   request_finished.connect(my_callback, dispatch_uid="my_unique_identifier")
   ```



注意事项：

上述的信号定义和注册代码，理论上可以在任意代码位置，但是模型相关的信号建议避免在应用程序的根模块及其models模块中注册，以尽量减少 import 代码的副作用

通常情况下：

- 信号定义：在对应子应用的signals模块中，如果使用connect注册的话，receive也定义在 signals 模块中

- 信号注册：在对应子应用的 apps 中的 AppConfig 类中的 ready 方法中实现，示例如下：

  apps.py：

  ```python
  class TestAppConfig(AppConfig):
      name = 'test_app'
  
      def ready(self):
          # 通过 get_model 来获取特定模型对象，参数 MyModel 就是 模型类的名称字符串
          pre_save.connect(receiver, sender=self.get_model('MyModel'))
  ```

  

## 6、信号断开连接

信号要断开连接，使用以下方法：

Signal.disconnect（receiver = None，sender = None，dispatch_uid = None）

参数说明见 Signal.connect

receiver参数表示已注册的接收器断开连接，当使用了dispatch_uid时，这个参数可以为None

返回值：如果有接收器被断开连接则返回True，没有则返回False



## 7、发送信号

两种发送信号的方法：

1. Signal.send(sender, **kwargs)：所有内置信号都是使用此方法发送信息。这个方法不能捕获由接收器抛出的异常; 它只是允许错误向上传播，因此，在出现错误时，不是所有接收器都可以被通知信号。

   

2. Signal.send_robust(sender, **kwargs)：捕获从Exception类派生的所有错误，并确保所有接收器都收到信号通知。如果发生错误，则会在引发错误的接收器的元组对中返回错误实例。正常的返回值是：[(receiver, response), ... ]，response是receiver的返回值，发生错误时是[(receiver, err), ... ]，错误的tracebacks保存在 err.\__traceback__属性上



## 8、项目中应用信号

### 1、应用内置信号

pre_save和post_save

1. 在子应用中新建signals.py

```python
def pre_save_receive(sender, **kwargs):
    print(f'模型保存之前:{sender},kwargs:{kwargs}')
```

2. 子应用的apps.py：

```python
@receiver(post_save，dispatch_uid="test_app_post_save_receive")
def post_save_receive(sender, **kwargs):
    print(f'模型保存之后:{sender},kwargs:{kwargs}')

from .signals import pre_save_receive

class TestAppConfig(AppConfig):
    name = 'test_app'

    verbose_name = '测试应用'

    def ready(self):
        pre_save.connect(pre_save_receive)
```

3. 当在admin后台登录之后，控制台输出：

```
模型保存之前:<class 'django.contrib.sessions.models.Session'>,kwargs:{'signal': <django.db.models.signals.ModelSignal object at 0x0000017C6D414358>, 'instance': <Session: nnq90hk1vizs2ov9pulruvwvq36lhcba>, 'raw': False, 'using': 'default', 'update_fields': None}
模型保存之后:<class 'django.contrib.sessions.models.Session'>,kwargs:{'signal': <django.db.models.signals.ModelSignal object at 0x0000017C6D4142E8>, 'instance': <Session: nnq90hk1vizs2ov9pulruvwvq36lhcba>, 'created': True, 'update_fields': None, 'raw': False, 'using': 'default'}
模型保存之前:<class 'django.contrib.auth.models.User'>,kwargs:{'signal': <django.db.models.signals.ModelSignal object at 0x0000017C6D414358>, 'instance': <User: admin>, 'raw': False, 'using': 'default', 'update_fields': frozenset({'last_login'})}
模型保存之后:<class 'django.contrib.auth.models.User'>,kwargs:{'signal': <django.db.models.signals.ModelSignal object at 0x0000017C6D4142E8>, 'instance': <User: admin>, 'created': False, 'update_fields': frozenset({'last_login'}), 'raw': False, 'using': 'default'}
模型保存之前:<class 'django.contrib.sessions.models.Session'>,kwargs:{'signal': <django.db.models.signals.ModelSignal object at 0x0000017C6D414358>, 'instance': <Session: nnq90hk1vizs2ov9pulruvwvq36lhcba>, 'raw': False, 'using': 'default', 'update_fields': None}
模型保存之后:<class 'django.contrib.sessions.models.Session'>,kwargs:{'signal': <django.db.models.signals.ModelSignal object at 0x0000017C6D4142E8>, 'instance': <Session: nnq90hk1vizs2ov9pulruvwvq36lhcba>, 'created': False, 'update_fields': None, 'raw': False, 'using': 'default'}
```



### 2、自定义信号

1. 在子应用中新建signals.py

   ```python
   from django.dispatch import receiver
   from django import dispatch
   
   # 定义信号
   index_signal = dispatch.Signal(providing_args=["request"])
   
   
   # 定义接收器，使用装饰器注册信号
   @receiver(index_signal, dispatch_uid="test_app_pre_index_request")
   def pre_index_request(sender, request=None, **kwargs):
       print(f'访问首页之前：{sender}， {kwargs}')
       print('访问IP：', request.META['REMOTE_ADDR'])
   ```

   

2. views中：

   ```python
   def index(request):
       # 发送信号
       index_signal.send(sender='index_function', request=request)
       return render(request, 'index.html')
   ```

   

3. 访问首页，控制台输出：

   ```python
   访问首页之前：index_function， {'signal': <django.dispatch.dispatcher.Signal object at 0x0000013C2B09F160>}
   访问IP： 127.0.0.1
   ```

   

   

   

