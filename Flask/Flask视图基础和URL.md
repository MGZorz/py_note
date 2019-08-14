# Flask视图基础和URL

## 思维导图

![Flask视图基础和URL](assets\Flask视图基础和URL.png)

## 认识URL

**URL** : Uniform Resource Locator  的简写，统一资源定位符。一个 URL  由以下几部分组成：

>   scheme://host:port/path/?query-string=xxx#anchor

-   **scheme**：代表的是访问的协议，一般为 http  或者 https  以及 ftp  等。
-   **host**：主机名，域名，比如 www.baidu.com。
-   **port**：端口号。当你访问一个网站的时候，浏览器默认使用80端口。
-   **path**：查找路径。比如： www.jianshu.com/trending/now，后面的 trending/now就是 path。
-   **query-string**：查询字符串，也叫请求参数，比如： www.baidu.com/s?wd=python，后面的 wd=python就是查询字符串。
-   **anchor**：锚点，后台一般不用管，前端用来做页面定位的。

**注意**： URL  中的所有字符都是 ASCII  字符集，如果出现非 ASCII  字符，比如中文，浏览器会进行编码再进行传输。

## web服务器和应用服务器以及web应用框架

web服务器：负责处理http请求，响应静态文件，常见的有 Apache，Nginx以及微软的IIS

应用服务器：负责处理逻辑的服务器。比如 php  、 python  的代码，是不能直接通过 nginx  这种web服务器来处		       理的，只能通过应用服务器来处理，常见的应用服务器有 uwsgi  、tomcat  等。

web应用框架：一般使用某种语言，封装了常用的 web 功能的框架就是web应用框架， flask、Django以及			Java中的 SSM(Spring+SpringMVC+Mybatis)  框架都是web应用框架。



**三者的应用顺序，以及职责所在**

![服务器之间的关系A](E:/python_document/notes/Flask%E6%A1%86%E6%9E%B6/assets/%E6%9C%8D%E5%8A%A1%E5%99%A8%E4%B9%8B%E9%97%B4%E7%9A%84%E5%85%B3%E7%B3%BBA.png)

## 第一个Flask框架程序（代码认识）

```python
# 从flask中导入Flask
# Flask这个类是项目的核心，以后很多操作都是基于这个类对象
# 注册url、注册蓝图等等都是基于这个类对象
from flask import Flask

app = Flask(__name__)

# 是一个装饰器，将url中/映射到hello_world这个视图函数上，
# 当以后访问这个网站的/目录是，就会执行hello_world这个函数，然后将函数的返回值返回给浏览器
# 例如:www.baidu.com/   -->   hello_world执行
@app.route('/')
def hello_world():
    print('hhah')
    return '你好呀~'

@app.route('/list/')
def my_list():
    return '我就是我哦~'


if __name__ == '__main__':
    # 默认为5000端口
    # app.run()
    app.run(port=8000)

```

## 开启Flask框架的DeBug模式

每个版本的PyCharm开启的方式不同，下面所记录是在PyCharm2017中的开启方式。

### 开启方式

-   直接在**运行**的地方，添加app.run(debug=True)

-   在**代码中间**，添加app.debug= True

-   同样是在**代码中间**，app.config.update(DEBUG=True)

-   通过**配置文件开启**

    -   创建config.py文件，先引入（import config）,然后执行app.config.form_object(config)
    -   创建config文件，不局限py文件，普通文本文件也可以，执行：app.config.form_pyfile(‘config.txt’)
    -   注意文件路径要写全名，后缀名也要写，不然会导致整个项目挂掉，**解决方式：silent =True**

    

## URL与函数映射

### 传递参数的两种方式

**/路径/参数,（就是将参数嵌入到路径中）**

代码：

```python
@app.route('/article/<id>/')
def article_detail(id):
    return '您请求的文章是：%s'% id
```

其中的<id>，尖括号是固定用法，语法为<variable>,variable默认的数据类型是字符串（string），如果想要指定数据类型，则要写成<converter : variable>，其中的converter的类型有如下的六种：

-   string：字符串，如果没有指定具体的数据类型，那么默认为字符串

-   int

-   float

-   path：path数据类型和字符串类型类似，区别在与一点，就是对于‘/’右斜杠的处理。

-   uuid：`uuid`是一个全宇宙都唯一的字符串，一般可以用来作为**表的主键**。

-   any：数据类型可以在一个`url`中指定多个路径。例如：

    ```python
    @app.route('/<any(user,blog):url_path>/<id>')
    def detail(url_path,id):
        if url_path=='blog':
            return "博客详情：%s" %id
        else :
            return "用户详情：%s" %id
    ```



**/路径?参数名1=参数值1&参数名2=参数值2...**

代码：

```python
from flask import request,render_template
# 第二种:/路径?参数名1=参数值1&参数名2=参数值2...，
# @app.route('/list7')  # 这种写法只支持get请求方式，不支持post请求方式
@app.route('/list7',methods=['GET','POST'])
# 这种写法及支持get有支持post
def list7():
    if request.method=='GET':
        uname = request.args.get('uname')
        pwd = request.args.get('pwd')
        return  render_template('login.html')
    elif request.method =='POST':
        uname = request.form.get('uname')
        pwd = request.form['pwd']
        return 'POST方式接收到的参数为；%s,%s'%(uname,pwd)
```

要注意，两种请求方式的区别！！！



## url_for的使用详解

之前都是用一个url调用函数，这次反过来了，给定函数生成url，这个功能的实现依托于url_for。

url_for接收两个以上的参数，并且接收到的函数名作为第一个参数（这个是规定），然后接收对应的URL规则命名参数，如果还有其他的参数，会自动添加到URL后面作为查询参数。

使用代码：

```python
@app.route('/')
def hello_world():
    # return 'Hello World!'
    # 希望返回页面一个指定的url,如'/list/'
    # return '/list/'
    # 使用url_for函数构建url
    # 这么做的好处：如果将来修改了url 但是没有修改url对应的函数名，就不用了到处替换url了(路径变化概率要大于函数名变化)
    # return url_for('list1')  #******
    # 构建url 如/list2/3/
    # return url_for('list2',page=3)  #******
    # 构建url 如：/list2/4/?num=8&pwd=123  了解
    # return url_for('list2',page=4,num=8,pwd=123)
    # 这么做的好处：url_for()  函数会转义一些特殊字符和 unicode  字符串，这些事情 url_for  会自动的帮我们搞定。

    return url_for('list1',next='/')
```



## 参数底层的原理

Flask项目中，底层是如何实现参数类型格式判断的呢？

根据werkzeug.routing模块中的BaseConverter类中的每个分类确定的。

每个数据类型都是调用werkzeug.routing模块中的对应类来做格式判断的！

![了解URL参数类型底层原理](E:/python_document/notes/Flask%E6%A1%86%E6%9E%B6/assets/%E4%BA%86%E8%A7%A3URL%E5%8F%82%E6%95%B0%E7%B1%BB%E5%9E%8B%E5%BA%95%E5%B1%82%E5%8E%9F%E7%90%86.png)

## 自定义URL转换器

步骤：

1.  实现一个类，继承自`BaseConverter`。

2.  在自定义的类中，重写`regex`，也就是这个变量的正则表达式。

3.  将自定义的类，映射到`app.url_map.converters`上。理解为加入字典DEFAULT_CONVERTERS中

    书写格式：app.url_map.converters[**'tel'**]=TelephoneConveter

代码：

```python
# 需求1：希望路径中能匹配一个电话号码类型的参数
class TelephoneConverter(BaseConverter):
    regex = r"1[345789]\d{9}"

app.url_map.converters['tel']=TelephoneConverter

# 使用自定义转换器实现需求
@app.route('/telephone/<tel:pnum>')
def my_telephone(pnum):
    return '您请求过来的电话号码值为：%s'%pnum
```

## to_python和to_url方法

to_python：可以把url拆分，并且返回txt格式的文件。

to_url：在调用url_for函数的时候，生成一个合适的url形式

代码：

```python
# 需求2：查询多个模块的数据
# 自定义转换器实现
class LiConverter(BaseConverter):
    def to_python(self, value):
        # value是自己传递过来的参数
        # 可以对value进行加工后在返回
        lm = value.split('+')
        print(lm)
        print(lm[0])
        print(lm[1])
        return lm
    def to_url(self, value):
        # 目的是要把['hots','enter']---->hots+enter
        return '+'.join(value)

app.url_map.converters['li']=LiConverter


@app.route('/news_list2/<li:moudles2>')
def news_list2(moudles2):
    print(moudles2)
    # 此时参数已经进行了拆分  slect *from news where nmoudles='hots' or nmoudles='enter'
    return "您要查询的模块是：%s" % moudles2

@app.route('/hello/')
def hello_wrold():
    # 构建url
    args = url_for('news_list2',moudles2=['hots','enter'])
    return '构建出url并返回：%s'%args

```

## 页面跳转和重定向

重定向分为暂时性重定向和永久性重定向，也就是在浏览器上会自动跳转到另一个页面。

**永久性重定向：** http  的状态码是 301  ，多用于旧网址被废弃了要转到一个新的网址确保用户的访问，最经典的就是京东网站，输入 www.jingdong.com  的时候，会被重定向到 www.jd.com。

**暂时性重定向：**http  的状态码是 302  ，表示页面的暂时性跳转。比如访问一个需要权限的网址，如果当前用户没有登录，应该重定向到登录页面，这种情况下，应该用暂时性重定向。

**Flask中的重定向**

重定向是通过 **redirect(location,code=302)**  这个函数来实现的。

​	location  表示需要重定向到的 URL，应该配合之前讲的 url_for()函数来使用。

​	code  表示采用哪个重定向，默认是 302( 暂时性重定向 ) ，可以修改成 301来实现永久性重定向。

代码：

```python
from flask import Flask,request,url_for,redirect

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

# 登录界面
@app.route('/login/')
def login():
    return '请登录'

# 页面跳转，暂时性重定向302   永久性重定向301
@app.route('/profile/')
def profile():
    if request.args.get('name'):
        return '用户中心页面'
    else:
        return redirect(url_for('login'),code=302)


app.debug=True

if __name__ == '__main__':
    app.run()
```

## Response返回值

Response是返回值的意思，类似于return的功能， 相当于一个包装，把返回的内容包装起来用于其他的操作。

**自定义`Response`对象的步骤**

-   继承自`Response`类。
-   实现方法`force_type(cls,rv,environ=None)`。
-   指定`app.response_class`为你自定义的`Response`对象。

代码：

```python
# 需求：希望将一个字典类型的数据,变成json对象返回给客户端
# 问题：视图函数不支持返回字典类型的数据
# 解决：自定义Response的子类对象来解决
# 步骤：
#     1.继承自`Response`类。
#     2.实现方法`force_type(cls, rv, environ=None)`。
#     3.指定`app.response_class`为你自定义的`Response`对象。
class JSONResponse(Response):
    @classmethod
        # 因为是类方法
    def force_type(cls, response, environ=None):
        '''
        这个方法只有视图函数返回 非字符串  非Response对象  非元组时才会调用
          response：视图函数的返回值
        '''
        if isinstance(response,dict):
            # 当返回类型为字典的时候，在加工操作
            # 希望吧一个字典对象转化为json对象
            resp = jsonify(response)
            return super(JSONResponse, cls).force_type(resp)

app.response_class = JSONResponse
@app.route('/myprofile/')
def profile():
    return {'uname':'wo','gender':'nan','school':'sxt'}
```

