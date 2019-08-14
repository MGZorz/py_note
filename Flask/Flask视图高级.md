# Flask视图高级

## 了解add_url_rule和app.route的原理

### add_url_rule

>   **add_url_rule(rule,endpoint=None,view_func=None)**

这个方法用来添加url与视图函数的映射。**rule是地址必须有的**（如果没有填写endpoint，那么默认会使用view_func的名字作为endpoint）以后在使用url_for的时候，就要看在映射的时候有没有传递endpoint参数，如果传递了，那么就应该使用endpoint指定的字符串，如果没有传递，那么就应该使用view_func的名字。

### app.route

**app_route的底层原理就是add_url_rule函数。**

### 代码：

```python
from flask import Flask,url_for

app = Flask(__name__)

@app.route('/')

def hello_world():

    # 构建url  ：/list/

    # 研究app.add_url_rule()方法，若方法中【没有加】上endpoint时，可通过原来的函数名构建url，即url_for('原函数名')

    # print(url_for('my_list'))

    # 研究app.add_url_rule()方法，若方法中【加上】endpoint时，不能再通过原来的函数名构建url，而需要endpoint的值才行

    # 即url_for('endpoint值')

    print(url_for('li'))

    return 'Hello World!'

def my_list():

    return '啦啦啦啦'

#通过app对象的add_url_rule方法 来完成url与视图函数的映射

app.add_url_rule('/list/',endpoint='li',view_func=my_list)

#讨论：add_url_rule()方法  与@app.route()装饰器的关系

#结论：@app.route()装饰器 底层就是借助于add_url_rule()方法来实现的

app.debug = True
if __name__ == '__main__':
    app.run()
```

## 类视图

​	之前我们接触的视图都是函数，所以一般简称**视图函数**。其实视图也可以基于类来实现，类视图的好处是**支持继承**，但是类视图不能跟函数视图一样，写完类视图还需要通过**app.add_url_rule(url_rule,view_func)**来进行注册。

### 标准类视图

#### 使用步骤

1.  定义一个类，并且必须继承于views.View。而且也必须含有dispatch_request（）函数。
2.  注册类视图

>   **app.add_url_route('url地址'，endpoint = '断点'，view_func= '函数名‘）。**

#### 代码实现：

```python
from flask import Flask,views,url_for

app = Flask(__name__)

@app.route('/')

def hello_world():

    return 'Hello World!'

# 定义一个类视图

class ListView(views.View):

    def dispatch_request(self):

        return '我是列表'

# 注册类视图

app.add_url_rule('/list/',endpoint='mil',view_func=ListView.as_view('my_list'))

# 获取上下文

with app.test_request_context():

    #若注册url时，没有指定endpoint，使用as_view（）方法中的名称  来构建url

    # print(url_for('my_list'))

    # # 若注册url时，有指定endpoint，就不能再使用as_view（）方法中的名称 来构建url，而要使用endpoint的值来构建url

    print(url_for('mil'))

app.debug =True

if __name__ == '__main__':

    app.run()
```

**注意：**

1.  定义类视图，必须**继承views.View类**和**dispatch_request**方法。
2.  在app.add_url_rule()函数中，若无指定endpoint，则**默认以view_func**后的名字构建url,而且要用**as_view方法进行转化。**

### 基于调度的类视图

在继承的时候，要继承views.MethodView.

#### 本质

是基于方法的类视图，是根据请求的**method**来执行不同的方法的。如果用户是发送的get请求，那么将会执行这个类的get方法。如果用户发送的是post请求，那么将会执行这个类的post方法。

PS：get和post两种请求方式的区别见：<https://www.cnblogs.com/logsharing/p/8448446.html>

#### 作用

这种方式，可以让代码更加简洁。所有和`get`请求相关的代码都放在`get`方法中，所有和`post`请求相关的代码都放在`post`方法中。就不需要跟之前的函数一样，通过`request.method == 'GET'`。

#### 基本使用

```python
#定义一个基于方法调度的  类视图
class  LoginView(views.MethodView):
    def get(self):
        return  render_template('login.html')
    def  post(self):
        #模拟实现
        #拿到前端页面传过来的  账号  和密码 去数据库做查询操作 查询到 (跳转主页面) ,反之跳转到login.html页面并给出错误提示信息
        uname = request.form['uname']
        pwd = request.form['pwd']
        if  uname=="momo"  and  pwd =="123":
            return  render_template('index.html')
        else:
            return  render_template('login.html',error="用户名或者密码错误")
# 注册类视图
app.add_url_rule('/login/', view_func=LoginView.as_view('my_login'))
```

但是上述代码是有优化的地方的。

#### 改进1（不过会让代码紊乱，做不到各回各家，各找各妈）

```python
python:

class  LoginView(views.MethodView):
    def get(self,error=None):
        return  render_template('login.html',error=error)
    def  post(self):
        #模拟实现
        #拿到前端页面传过来的  账号  和密码 去数据库做查询操作 查询到 (跳转主页面) ,反之跳转到login.html页面并给出错误提示信息
        uname = request.form['uname']
        pwd = request.form['pwd']
        if  uname=="momo"  and  pwd =="123":
            return  render_template('index.html')
        else:
            return  self.get(error="用户名或者密码错误")
                # render_template('login.html',error="用户名或者密码错误")
# 注册类视图
app.add_url_rule('/login/', view_func=LoginView.as_view('my_login'))



Jinja2:

<tr>
                <td>
                    {# <font color="red">{{ error }}</font>#}
                    {# 优化，判断#}
                    {% if error %}   {#None == False   不为None或者空的字符串和列表时，才为True#}
                            <font color="red">{{ error }}</font>
                    {% endif %}
                </td>
            </tr>
```

#### 改进2（最终写法）

```python
# 改进2：基于调度方法的类视图  ，通常get()方法处理get请求,post()方法处理post请求，为了便于管理,不推荐post方法和get方法互相调用
class  LoginView(views.MethodView):
    def __jump(self,error=None):
        return render_template('login.html', error=error)
    def get(self,error = None):
        return  self.__jump()
    def  post(self):
        #模拟实现
        #拿到前端页面传过来的  账号  和密码 去数据库做查询操作 查询到 (跳转主页面) ,反之跳转到login.html页面并给出错误提示信息
        uname = request.form['uname']
        pwd = request.form['pwd']
        if  uname=="momo"  and  pwd =="123":
            return  render_template('index.html')
        else:
            return  self.__jump(error="用户名或者密码错误")
```

### 类视图的优点：可继承

这一优点可以减少代码量，比如说两个子类都需要把字典对象转化为json对象，就可以通过继承来实现。

#### 代码：

```python
class ListView2(views.View):

    def getDate(self):

        raise  NotImplementedError

    def dispatch_request(self):

        return jsonify(self.getDate())

# 重写了父类的getDate()方法

class JSONView1(ListView2):

    def getDate(self):

        return {'name':'张善峰','age':123}

class JSONView2(ListView2):

    def getDate(self):

        return {'book':'你好','author':'我'}

app.add_url_rule('/people/',endpoint='people',view_func=JSONView1.as_view('JSONView1'))

app.add_url_rule('/book/',endpoint='book',view_func=JSONView2.as_view('JSONView2'))
```

## 类视图中的装饰器

### 装饰器

是用于拓展原来函数功能的函数，它的返回值也是一个函数，可以在不增加其源代码的前提下增加功能。

### 在视图函数中使用装饰器

```python
# 定义一个装饰器
#需求：查看设置个人信息时，只有检测到用户已经登录了才能查看，若没有登录，则无法查看并给出提示信息
def login_required(func):
# 装饰器必须要有的
    @wraps(func)
    def wrapper(*args,**kwargs):
        username = request.args.get("username")
        if username and username == 'momo':
            return func(*args,**kwargs)
        else:
            return '请先登录'
    return wrapper

# 功能函数  能够执行成功的前提条件是， 必须先登录【写代码去判断当前用户是否已经登录--》放到自定义装饰器】
@app.route('/setting/')
# 在视图函数中使用自定义装饰器，那么自己定义的装饰器必须放在`app.route`下面。否则这个装饰器就起不到任何作用。
@login_required
def setting():
    return '这是设置界面'
```

### 在类视图中使用装饰器

在类视图中使用装饰器，是需要**重写类视图中的decorators属性**，并且把装饰器加到属性中，列表、元组都可以。

```python
class ProfileView(views.View):
    # 列表或者元组都行
    decorators = [login_required]
    def dispatch_request(self):
        return '这是个人中心界面'

app.add_url_rule('/profile/',view_func=ProfileView.as_view('profile'))
```

## 蓝图(Blueprint)

### 简介

让Flask更加模块化，更好的管理项目，分层解耦（mvc结构）

### 基本使用

使用的步骤分为两个步骤

1.  导入：在蓝图文件中导入Blueprint

    ```python
    from flask import Blueprint
    users = Blueprint('users',__name__,url_prefix='/user')
    ```

2.  注册：在主py文件中执行蓝图文件中的调用

    ```python
    #（先引入  ‘.’=/）
    from blueprints.book import books
    # (在注册)
    app.register_blueprint(users)
    ```

#### url_prefix参数

如果想要某个蓝图下的**所有url都有一个url前缀**，那么可以在定义蓝图的时候，指定url_prefix参数，同时也要注意：**定义url_profix时，若后边有/，那么以后在定义url与视图函数的时候，就不要再在url前面加斜杠了**。

![蓝图的url前缀](assets\clipboard.png)

### 模板文件

#### 寻找规则

1.  如果项目中的templates文件夹中有相应的模版文件，就直接使用了。
2.  如果项目中的templates文件夹中没有相应的模版文件，那么就到在定义蓝图的时候指定的路径中寻找。并且蓝图中指定的路径可以为相对路径，相对的是当前这个蓝图文件所在的目录。比如：**news_bp = Blueprint('news',__name__,url_prefix='/news',template_folder='news_page')**

![模板文件的自定义](assets\clipboard-1560997541758.png)

#### 注意

蓝图文件查找会默认在template为根目录查找。**优先级是template目录要大于自定义目录**，所以要想自定义先把template目录中的文件删除。

### 静态文件

#### 寻找规则

##### 常规写法（必须掌握）

```html
<link rel="stylesheet" href="{{ url_for('static',filename='news_list.css') }}">
```

##### 个性化写法（了解）

如果在加载静态文件的时候，指定的蓝图的名字，比如`news.static`，那么就会到这个蓝图指定的**static_folder**下查找静态文件。

###### python:

```python
from flask import  Blueprint

news_bp=Blueprint('news',__name__,url_prefix='/news',template_folder='news_page',static_folder='news_page_static')
```

###### html

```html
<link rel="stylesheet" href="{{ url_for('news.static',filename='news_list.css') }}">
```

### url_for反转蓝图注意事项

注意：要指定蓝图的名字。

#### 场景一

url_for (‘蓝图名称.方法名')

#### 场景二

```
<a href="{{ url_for('news.news_list')}}">新闻列表 OK写法</a>
```

#### 场景三

```python
from flask import  Blueprint,render_template,url_for

news_bp = Blueprint('news',__name__,url_prefix='/news',template_folder='news_page',static_folder='news_page_static')

@news_bp.route('/list/')

def news_list():

     print(url_for('news.news_detail')) #/news/detail/

     return render_template('news_list.html')
```

### 蓝图_子域名实现

-    ip地址不能有子域名。
-   localhost也不能有子域名。

分为四个部分，蓝图文件，默认主页，子域名主页，主PY文件

#### 蓝图文件

```python
from  flask  import  Blueprint,render_template

cms_bp = Blueprint('cms',__name__,subdomain='cms')

#子域名的首页

@cms_bp.route('/')

def  hello():

    return  render_template('cms_index.html')
```

#### 默认主页

```html
<h2>系统主页  </h2>

    <hr>

    <p>ko</p>

    <p>ko</p>

    <p>ok</p>

    <a href="http://cms.momo.com:5000/">学院</a>
```

#### 子域名主页

```
<h2>子域名首页</h2>

   <p>学院</p>
```

#### 主py文件

```python
from blueprints.cms import cms_bp

app.register_blueprint(cms_bp)

app.config['SERVER_NAME']="momo.com:5000"
```

