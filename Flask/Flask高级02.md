# 信号机制

## 概念

>   举个栗子：
>
>   类似于两方属于敌对的关系，某人在于敌方阵营交谈，一旦遇到特殊情况，某人会给家里**发送信号**，家人接收（**监听**）到他的信号后，同伙便会做出一系列的**应对策略**（前进or后退）。

## 信号步骤

>   三步走策略

### 创建信号

定义信号需要使用到blinker这个包的**Namespace**类来创建一个命名空间。比如定义一个在访问了某个视图函数的时候的信号。

>   PS：Namespace的作用是防止多人联合编写代码的时候出现命名冲突的情况

### 监听信号

监听信号使用signal对象的**connect**方法，在这个方法中需要传递一个函数，用来监听到这个信号后做该做的事情。

### 发送信号

发送信号使用signal1对象的**send**方法，这个方法可以传递一些其他参数过去。

## 信号使用场景

>   -   定义一个登录的信号，以后用户登录进来
>   -   发送一个登录信号，然后能够监听这个信号
>   -   在监听到这个信号以后，就记录当前这个用户登录的信息
>   -   用信号的方式，记录用户的登录信息即登录日志

### 编写一个signal.py文件创建登录信号

>   在监听信号的时候，要进行相应的操作，例子中是让其创建一个简单的txt 文件。

代码：

```python
from blinker import Namespace
from datetime import  datetime
from flask import request,g
# 创建一个登录信号
mySpace = Namespace()
login_signal = mySpace.signal('创建一个登录信号')
# 监听信号
def login_log():
    # 用户名   时间 ip
    uname = g.uname
    now = datetime.now()
    ip = request.remote_addr
    log_data = '{uname}*{now}*{ip}'.format(uanme=uname , now = now ,ip = ip)
    with open('login_log.txt','a')as f:
        f.write(log_data+'\n')
        f.close()
# 发送信号
login_signal.connect(login_log)
```

使用信号存储用户登录日志（app.py）

```python
from flask import Flask,request,g
from blinker import Namespace
app = Flask(__name__)
from signal import login_signal
@app.route('/')
def hello_world():
    return 'Hello World!'
@app.route('/login/')
def login():
    # 通过查询字符创的形式来传递uname这个参数
    uname = request.args.get('uname')
    if uname :
        g.uname = uname
        # 发生信号
        login_signal.send()
    else:
        return '请输入用户名'
if __name__ == '__main__':
    app.run(debug=True)
```

### 注意

使用Pycharm运行的时候可能会出现没有创建文件的情况，这是因为权限不足，咋整？

解决方法：

把cmd用管理员打开，然后通过命令模式，进入虚拟环境，并且找到代码的位置进行运行。

## 常用的内置信号

>   创建和发送信号的代码不用咱们写，只需要管**监听**这一步。

### template_rendered

>   模版渲染完成后的信号。

#### template_rendered的使用

```python
from flask import Flask,request,g,template_rendered,got_request_exception,render_template
app = Flask(__name__)
#内置信号
#模版渲染完成后的信号。
def template_rendered_func(sender,template,context):
    print(sender) #发送者
    print(template) #跳转到的模版名称
    print(context) #跳转到模版时带过去的参数
template_rendered.connect(template_rendered_func) 
@app.route('/')
def hello_world():
    return render_template("index.html",data="MGorz"去看发送信号的底层
if __name__ == '__main__':
    app.run(debug=True)
```

### before_render_template

>   模板渲染之前的信号
>

### request_started

>   请求开始之前，在到达视图函数之前发送信号
>

### request_finished

>   请求结束时，在相应发送给客户端之前发送信号
>

### request_tearing_down

>   请求对象被销毁发送的信号，即使在请求过程中发生异常也会发送信号
>

### got_request_exception

>   在请求过程中抛出异常时发送的信号，异常本身会通过**exception**传递到订阅（监听）的函数，一般可以监听这个信号来记录网站异常信息。
>

#### got_request_exception的使用

```python
from flask import Flask,request,g,template_rendered,got_request_exception,render_template
app = Flask(__name__)
#内置信号
#got_request_exception：在请求过程中抛出异常时发送信号，异常本身会通过exception传递到订阅（监听）的函数中。
# 一般可以监听这个信号，来记录网站异常信息。
# def request_exception_log(sender,*args,**kwargs):  #掌握写参数技巧
#     print(sender)
#     print(args)
#     print(kwargs)
def request_exception_log(sender,exception):
    print(sender)
    print(exception) # division by zero
got_request_exception.connect(request_exception_log)
@app.route('/')
def hello_world():
    #制造bug
    a = 1/0
    return render_template("index.html",data="momo")
if __name__ == '__main__':
    app.run(debug=True)
```

### appcontext_tearing_down

>   应用上下文销毁时发送的信号
>

### appcontext_pushed

>   应用上下文被推入栈的顶部时发送的信号
>

### appcontext_popped

>   应用上下文被推出栈是发送的信号
>

### message_flashed

>   调用Flask的flash方法是发送的信号
>

# WTForms

## 介绍

**两个作用**：

1.  表单验证： 将用户提交上来的数据进行验证是否符合系统要求。（**服务器端验证**），**js的验证只是客户端验证**
2.  模板渲染 （了解）

>   Flask-wtf是WTForm的升级版，相对于WTForm要多加一些其他的功能，比如：CSRF保护，文件上传等等

## 基本使用

### 做表单验证

1.  自定义一个表单类，**继承自wtforms.Form类。**
2.  定义好需要验证的字段，字段的名字**必须**和模版中那些需要验证的input标签的name属性值**保持一致**。
3.  在需要验证的字段上，需要指定好**具体的数据类型**。（因为例子中都是字符串类型，就是用的StringField）
4.  在相关的字段上，**指定验证器**。
5.  以后在视图函数中，只需要使用这个表单类的对象，并且把需要验证的数据，也就是**request.form传给这个表单类**，**再调用表单类对象.validate()方法进行，如果返回True，那么代表用户输入的数据都是符合格式要求的，Flase则代表用户输入的数据是有问题的。如果验证失败了，那么可以通过表单类对象.errors来获取具体的错误信息。**

#### 代码

```python
from flask import Flask,request,render_template
from wtforms import Form,StringField
# StringField是wtform中的一个处理字符串的模块
from wtforms.validators import Length,EqualTo
# 引入wtforms.validators模块中的Length长度验证器,EqualTo
app = Flask(__name__)
# 定义一个表单验证类
class Register_Form(Form):
    # validators 是验证的意思，后面的列表中可以填入任意验证器
    # 对用户名进行验证，并且也要注意用户名的名字数据项的名字必须要一样。
    uname = StringField(validators=[Length(min=2,max=15,message = '用户名的长度，必须是2-15之间')])
    pwd = StringField(validators=[Length(min=6,max=15)])
    pwd2 = StringField(validators=[Length(min=6,max=15),EqualTo('pwd',message='两次输入密码不一致')])
@app.route('/')
def hello_world():
    return 'Hello World!'
# 表单验证的基本使用
@app.route('/register/',methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        # 使用表单验证对象进行验证
        form = Register_Form(request.form)
        # 这个写法相当于把从请求对象把用户提交过来的参数作为实参交给了表单验证器对象，
        # 并且对于这个对象敷个名称，利用这个对象做验证
        if form.validate():   #validate就是验证的意思   要么True  要么Flase
            return '验证成功'
        else:
            # 打印异常信息
            print(form.errors)
            return '抱歉，没通过验证'
if __name__ == '__main__':
    app.run(debug = True)
```

## WTForm中的数据项类型

-   StringField（字符串）
-   IntegerField（数字）
-   RadioField（单选框）
-   BooleanField（复选框）
-   SelectField（下拉框）
-   TextAreaField（文本域）
-   DateField（日期类型）

## 常用内置验证器

-   Length

    字符串长度限制，有min和max两个值进行限制

-   EqualTo

    验证数据是否和另外一个字段相等，常用的就是密码和确认密码两个字段是否相等。

-   Email

    验证上传的数据是否为邮箱数据格式  如：223333@qq.com。

-   InputRequired

    验证该项数据为必填项，即要求该项非空

-   NumberRange

    数值的区间，有min和max两个值限制，如果处在这两个数字之间则满足。

-   Regexp

    定义正则表达式进行验证，如验证手机号码。

-   URL

    必须是URL的形式 如http://www.baidu.com。

-   UUID(了解)

    验证数据是UUID类型

### 常用验证器使用代码

#### app代码

```python
from flask import Flask,request,render_template
# 使用验证
from formscheck import Register_Form,Register2_Form
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World!'
# 表单验证的基本使用
@app.route('/register/',methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        # 使用表单验证对象进行验证
        form = Register_Form(request.form)
        # 这个写法相当于把从请求对象把用户提交过来的参数作为实参交给了表单验证器对象，
        # 并且对于这个对象敷个名称，利用这个对象做验证
        if form.validate():   #validate就是验证的意思   要么True  要么Flase
            return '验证成功'
        else:
            # 打印异常信息
            print(form.errors)
            return '抱歉，没通过验证'
# 常用验证器的使用
@app.route('/register2/',methods=['GET','POST'])
def register2():
    if request.method == 'GET':
        return render_template('register2.html')
    else:
        form  = Register2_Form(request.form)
        if form.validate():
            return '验证成功'
        else:
            print(form.errors)
            return '验证失败'
import uuid
# 生成一个uuid
print(uuid.uuid4())
if __name__ == '__main__':
    app.run(debug = True)
```

#### 验证器代码

```python
from wtforms import Form,StringField,IntegerField
# StringField是wtform中的一个处理字符串的模块
# 引入wtforms.validators模块中的Length长度验证器,EqualTo
from wtforms.validators import Length,EqualTo,Email,InputRequired,NumberRange,Regexp,URL,UUID
# 定义一个表单验证类
class Register_Form(Form):
    # validators 是验证的意思，后面的列表中可以填入任意验证器
    # 对用户名进行验证，并且也要注意用户名的名字数据项的名字必须要一样。
    uname = StringField(validators=[Length(min=2,max=15,message = '用户名的长度，必须是2-15之间')])
    pwd = StringField(validators=[Length(min=6,max=15)])
    pwd2 = StringField(validators=[Length(min=6,max=15),EqualTo('pwd',message='两次输入密码不一致')])
# 常用验证器的使用
class Register2_Form(Form):
    email =StringField(validators=[Email()])
    uname = StringField(validators=[InputRequired()])
    # 验证整数
    age = IntegerField(validators = [NumberRange(min=18,max=80)])
    phone = StringField(validators= [Regexp(r'1[345789]\d{9}')])
    phonepage = StringField(validators=[URL()])
    uuid = StringField(validators=[UUID()])
```

## 自定义验证器（验证码的实现）

### 步骤

1.  定义一个方法，方法的名字规则是：`validate_字段名(self,field)`
2.  在方法中，使用`field.data`可以获取到这个字段的具体的值。
3.  验证时，如果数据满足条件，那么可以什么都不做。如果验证失败那么应该抛出一个`wtforms.validators.ValidationError`的异常，并且把验证失败的信息传到这个异常类中。

### 验证码实现

```python
app代码：
import random,os
app.config['SECRET_KEY'] = os.urandom(24)
# 自定义验证器：实现验证码验证
        code = random.randint(1000,9999)    #生成一个随机四位整数验证码
        # 把code变为字符串
        session['code'] = str(code)
验证器代码：
code = StringField(validators=[Length(min=4,max=4)])
    # 光有长度验证是不够的，不能满足验证码验证需求，此时需要自定义验证器来对某字段验证进行强化
    def validate_code(self,field):
        # 取字段field对象上的值做验证
        print(field.data)
        print(session.get('code'))
        # field.data等价于用户输入的值
        if field.data != session.get('code'):
            raise ValidationError('验证码不一致')
```

## WTForm渲染模板

>   可以在模板文件中直接写html的一些简单的代码，然后html文件以{{}}形式引用。
>
>   详细信息网址：https://wtforms.readthedocs.io/en/latest/index.html

# Flask上传文件

## 回顾知识点

>   form表单中，一旦涉及到上传文件就要就必须要有**enctype**属性，而且必须等于**multipart/form-data.**而且提交方式为‘post’,**method = 'post'**

## 步骤

-   首先给form表单添加enctype属性和method属性

    -   >   enctype  = 'multipart/form-data'
        >
        >   method = 'post'

-   在项目的根目录中创建文件保存路径。

-   指定文件的保存路径

    -   ```python
        # os.path.dirname(__file__)获取的是app.py文件的路径，也就是在项目根目录中，然后把它放在images文件夹中
        
        UPLOAD_PATH = os.path.join(os.path.dirname(__file__),'images')
        ```

-   if..else两种情况当页面访问为get方式直接跳转，post方式进行操作

-   后台要获取上传的文件，用request.files.get('文件名')来获取

-   保存文件之前，使用**werkzeug.utils.secure_filename**来对上传上来的文件名进行一个过滤。保证不会有安全问题。 

-   获取到上传上来的文件后，使用`文件对象.save(路径)`方法来保存文件。路径=完整路径=路径名+文件名

### 代码实现

#### html代码

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>上传文件</title>
</head>
<body>
{# 但凡form中涉及到了上传文件，那么method = 'post' 和 enctype = 'multipart/form-data'#}
{# 当没有指定提交路劲时，默认向当前页面提交#}
<form action="" method="post" enctype="multipart/form-data">
<table>
    <tr>
        <td>头像：</td>
        <td><input type="file" name="pichead"></td>
    </tr>
    <tr>
        <td>心情：</td>
       <td><input type="text" name="desc"></td>
    </tr>
    <tr>
        <td></td>
       <td><input type="submit" value="提交"></td>
    </tr>
</table>
</form>
</body>
</html>
```

#### Py代码

```python
# 上传文件优化,文件名安全的意思
from werkzeug.utils import secure_filename
# os.path.dirname(__file__)获取的是app.py文件的路径，也就是在项目根目录中，然后把它放在images文件夹中
UPLOAD_PATH = os.path.join(os.path.dirname(__file__),'images')
# Flask上传文件的实现
@app.route('/upload/',methods=['POST','GET'])
def upload():
    if request.method == 'GET':
        return render_template('upload.html')
    else:
        desc = request.form.get('desc')
        # 获取pichead文件对象
        pichead = request.files.get('pichead')
        print(desc)
        # 保存到服务器
        # save方法传完整的路径和文件名
        # pichead.save(os.path.join(UPLOAD_PATH,pichead.filename))
        # 上行可以进行优化,下行是对pichead文件名进行包装，保证文件名更安全。
        filename = secure_filename(pichead.filename)     
        pichead.save(os.path.join(UPLOAD_PATH,filename))
        return '文件上传成功
```

## 访问上传成功的文件

### 原理

>   从服务器中读取，应该定义一个url与视图函数，来获取指定的文件。
>
>   在视图函数中，使用send_from_directory(文件目录，文件名)来获取。

### 实现

```python
# 访问已经上传号的服务器上的文件，要借助flask中的send_from_directory函数
from flask import send_from_directory
# 访问服务器上的文件（已经上传成功的文件）
@app.route('/images/<filename>')
def get_image(filename):
    return send_from_directory(UPLOAD_PATH,filename)
```

## 利用flask-wtf验证上传文件

### 原理

>   借用wtforms和flask_wt内的函数，验证文件

### 关键之处

-   对文件类型字段的验证，需要采用wtforms中的**FileField**这个类型
-   验证器需要从flask_wtf.file中导入，**flask_wtf.file.FileRequired**和**flask_wtf.file.FileAllowed**类型
-   FileRequired是用来验证文件上传不能为空。
-   FileAllowed用来验证上传的文件的后缀名
-   （**重要**）在视图函数中，需要使用**from werkzeug.datastructures import CombinedMultiDict**来吧from和files进行合并。
-   最后使用 if语句对**表单验证对象.validate()**进行验证

### 代码实现

#### formscheck文件

```python
from wtforms import Form,FileField,StringField
from wtforms.validators import InputRequired
# flask_wtf
from flask_wtf.file import FileRequired,FileAllowed
class UploadForm(Form):
    pichead = FileField(validators=[FileRequired(),FileAllowed(['jpg','png','gif'])])
    desc = StringField(validators=[InputRequired()])
```

#### app文件

```python
from flask import Flask,request,render_template
import os
from werkzeug.utils import secure_filename
from formscheck import UploadForm
from werkzeug.datastructures import  CombinedMultiDict
app = Flask(__name__)
UPLOAD_PATH = os.path.join(os.path.dirname(__file__),'images')
 #利用flask-wtf验证上传的文件
@app.route('/upload/',methods=['GET','POST'])
def upload():
    if request.method == 'GET':
        return render_template('upload.html')
    else:
        form = UploadForm(CombinedMultiDict([request.form,request.files]))
        if form.validate():
            # desc = request.form.get("desc")
            # pichead = request.files.get("pichead")
            desc = form.desc.data
            pichead = form.pichead.data
            filename = secure_filename(pichead.filename)
            pichead.save(os.path.join(UPLOAD_PATH,filename))
            print(desc)
            return '文件上传成功'
        else:
            print(form.errors)
            return "文件上传失败"
if __name__ == '__main__':
    app.run(debug=True)
```

# Flask_RESTful

## Restful接口规范

### 介绍

#### 什么是Restful?

>   REST：Representational State Transfer ,指的是一组架构**约束条件**和**原则**，满足这些约束条件和原则的**应用程序或者设计**就是RESTful。
>
>   是一种软件架构风格、设计风格、而不是标准，只不过是提供了设计原则和交互条件。
>
>   是主要用于客户端和服务器交互类的软件，是用于前端和后台进行通信的一套规范，使用这个规范可以让开发变得更轻松。

#### 适用场景

>   PC端，移动端，app端，ios端都适用。

#### 协议

>   http或者https协议

#### 数据格式要求

>   必须使用json格式！！！

#### url连接规则

>   -   url链接中不能有动词，只能由名词
>   -   对于一些名词，如果出现复数，那么应该在后面加news
>
>   举个栗子：
>
>   应该使用‘/news/’，而不应该是‘/get_news/’

#### HTTP请求方式（部分）

-   GET：从服务器上获取资源
-   POST：在服务器上新增或者修改一个资源（登录时除外）
-   PUT：在服务器上更新资源（客户端提供所有改变后的数据）
-   PATCH：在服务器上更新资源（客户端只提供需要改变的属性）
-   DELETE：在服务器上删除资源

>   最常用的是GET和POST，后三项不怎么用，作为了解。

#### 状态码

>   客户端返回的状态码，可以通过状态码得知，程序的运行情况。

| 状态码 | 原因描述              | 描述                                                     |
| ------ | --------------------- | -------------------------------------------------------- |
| 200    | ok                    | 服务器成功响应                                           |
| 400    | INVALID REQUEST       | 用户发出的请求有错误，服务器没有进行新建或修改数据的操作 |
| 401    | Unauthorized          | 用户没有权限访问这个请求                                 |
| 403    | Forbidden             | 因为某些原因禁止访问这个请求                             |
| 404    | NOT FOUND             | 用户请求的url不存在                                      |
| 406    | NOT Acceptable        | 用户请求不被服务器接收                                   |
| 500    | Internal server error | 服务器内部错误，比如遇到bug                              |

## 使用方式

### Flask_RESTful介绍

>   RESTful是**基于类视图**实现的，是专门用来写**restful api**的插件，可以快速集成**restful_api**接口功能，在纯api的后台中，节省开发时间。
>
>   不过在小的网站上，不需要使用RESTful，因为小网站返回的是页面（html）,而**RESTful返回的是Json数据格式**

### 基本使用

#### 步骤

-   从flask_restful中导入API，创建api对象
-   定义类视图，继承于（Response类）
    -   在这其中，使用你想要的请求方式来定义相应的方法，比如你想要将这个类视图只能采用`post`请求，那么就定义一个`post`方法。
-   使用api..add_resource来添加url和视图函数

##### 代码实现

```python
from flask import Flask,url_for
from flask_restful import Api,Resource
app = Flask(__name__)
# 定义api
api = Api(app)
@app.route('/')
def hello_world():
    return 'Hello World!'
# Flask_RESTful的基本使用
# 定义一个类视图
class LoginView(Resource):
    def get(self):
        return {"flag":"no"}
    def post(self):
        return {"flag":"yes"}
# 映射url
api.add_resource(LoginView,'/login/','/login2/',endpoint = 'login')
# 请求上下文
with app.test_request_context():
    print(url_for('login'))   # 如果不写endpoint,那么将会使用视图的名字的小写来作为endpoint
#     如果有endpoint,指定什么就必须使用endpoint值构建url
if __name__ == '__main__':
    app.run(debug=True)
```

### 注意

>   1.  flask_restful和app.route的区别，在于看你想要返回什么。
>
>       ​	想返回json数据结构→flask_restful，渲染模板→app.route
>
>   2.  在api.add_response中可以指定多个url，以及endpoint
>
>   3.  endpoint是用来给url_for反转url的时候指定的。如果不写endpoint，那么将会使用视图的名字的小写来作为endpoint。

## 功能参数验证方法

### 回顾参数验证的方法们

-   JS表单验证
-   WTForms表单验证

>   ps：RESTful和WTForms很类似，都是在服务器端做验证

## 参数解析（参数验证）

### 基本使用

1.  创建解析器对象（reqparse.RequestParser()）
2.  利用解析器对象，添加要验证的参数（add_argument）
3.  利用解析器对象，进行验证，正确则返回验证合适的参数值，错误抛出异常（parser.parse_args()）

#### 代码实现

```python
# restful中做参数验证的包。reqparse
from flask_restful import Api,Resource,reqparse
app = Flask(__name__)
api = Api(app)
# Flask_RESTful参数验证,基本用法
class RegisterView(Resource):
    def post(self):
        # 用户名
        # 1、创建一个解释器对象
        parse = reqparse.RequestParser()
        # 2、利用解析器对象，添加需要的验证的参数
        # parse .add_argument('要验证的', type=数据可是 , help='不符合规则信息' ,
        #                       required = 是否必填（True） , trim = 信息前后空格去不去（True）)
        parse .add_argument('uname', type=str , help='用户名验证错误' , required = True , trim =True)
        # 3、利用解析器对象，进行验证，若正确直接返回验证后合格的参数值，若错误，抛异常信息给客户端
        args =  parse.parse_args()
        # 若验证成功后，需要插入数据库
        print(args)
        return {'tips':'注册成功'}
api.add_resource(RegisterView,'/register/')
```

### add_argument

在add_argument函数中可以放置很多种参数，下面举一些常用的属性。

-   default：默认值

    -   >   如果这个参数没有值，那么将使用这个参数指定的默认值。

-   required：是否必须。

    -   >   默认为False，如果设置为True，那么这个参数就必须提交上来。

-   type：这个参数的数据类型

    -   >   如果指定，那么将使用指定的数据类型来强制转换提交上来的值。

    -   这里的数据类型，既包括python自带的数据类型，也可以使用flask_restful.inputs下的一些特定的数据类型来强制转换。

-   choices：固定选项。

    -   >   提交上来的值只有满足这个选项中的值才符合验证通过，否则验证不通过。

-   help：错误信息。

    -   >   如果验证失败后，将会使用这个参数指定的值作为错误信息。

-   trim：是否要去掉前后的空格

#### 代码实现

```python
# Flask_RESTful参数验证，更多用法
class RegisterView(Resource):
    def post(self):
        #用户名   密码   年龄 性别  出生日期   号码  个人主页
        # 1.创建解析器对象
        parser = reqparse.RequestParser()
        #2.利用解析器对象添加 需要验证的参数
        parser.add_argument('uname',type=str,help='用户名验证错误！',required=True,trim=True)
        parser.add_argument('pwd', type=str, help='密码验证错误！',default="123456")
        parser.add_argument('age',type=int,help='年龄验证错误！')
        parser.add_argument('gender',type=str,choices=['男','女','双性'],help= '性别只能是男或者女')
        # 注意要使用data和regex数据类型，需要到flask_restful.inputs中的。
        parser.add_argument('birthday',type=inputs.date,help='生日字段验证错误！')
        parser.add_argument('phone',type=inputs.regex(r'1[3578]\d{9}'),help = '请输入正确的电话号码')
        parser.add_argument('phomepage',type=inputs.url,help='个人中心链接验证错误！')
        #3.利用解析器对象进行验证，若正确，直接返回验证后合格的参数值，若错误，抛异常信息给客户端
        args = parser.parse_args()
        print(args)
        return {"tips":"注册成功"}
api.add_resource(RegisterView,'/register/')
```

## 返回标准化参数

### 标准化思想

>   对于一个类视图，你可以指定好一些字段作标准化用于返回。
>
>   以后使用ORM模型或者自定义模型的时候，他会自动的获取模型中的相应的字段，
>
>   生成json格式数据，然后再返回给客户端。

### 关键点（步骤）

>   -   需要导入flask_restful.marshal_with装饰器
>   -   写一个字典变量，来指定需要返回的标准化字段，以及该字段的数据类型。
>   -   在get方法中，返回自定义对象的时候，flask_restful会自动的读取对象模型上的所有属性。
>   -   组装成一个符合标准化参数的json格式字符串返回给客户端。

#### 代码实现

```python
from flask import Flask
from flask_restful import Api,Resource,fields,marshal_with
app = Flask(__name__)
api = Api(app)
#flask_restful返回标准化参数
class News(object):
    def __init__(self,title,content):
        self.title =title
        self.content =content
news = News('能力强的体现','能屈能伸')
class NewsView(Resource):
    resource_fields ={
        'title': fields.String,
        'content':fields.String
    }
# 这个装饰器是必须要用的哦~
    @marshal_with(resource_fields)
    def get(self):
        # restful规范中，要求，定义好了返回的参数个数 和 内容
        # return {'title':"世界太大",'content':"可钱包太小"}
        #好处1：体现规范化，即使content这个参数没有值，也应该返回，返回一个null回去
        # return {'title':"世界太大"}
        #好处2：体现规范化，还可以返回一个对象模型回去
        return news
api.add_resource(NewsView,'/news/')
if __name__ == '__main__':
    app.run(debug=True)
```

### 返回标准化参数强化

#### 重命名属性和默认值属性

##### 需求1：

有的时候你对外给出的属性名和模型内部的属性名不相同时，可使用 attribute可以配置这种映射。比如想要**返回模型对象user.username的值**，但是在返回给外面的时候，**想以uname返回去**。

##### 需求2：

​       在返回某些字段的时候，有时候可能没有值，但想给一个值用以提示，那么这时候可以在**指定fields的时候使用default指定默认值**。

##### 代码实现

```python
class User():
    def __init__(self,username,age ):
        self.username = username
        self.age = age
        self.signature = None
class UserView(Resource) :
    resource_fields = {
        # 1、重复名，把username重命名为uname,重点在于attribute = '原来的名字'
        'uname':fields.String(attribute='username'),
        'age':fields.Integer,
        # 2、默认值  当signature没有任何值的时候，想要默认输出一个值，default = '想要输出的内容'
        'signature':fields.String(default='没有什么')
    }
# 这个是必须加的！！！！
    @marshal_with(resource_fields)
    def get(self):
        user = User('MGorz',25)
        return user
api.add_resource(UserView,'/user/')
```

#### 复杂的参数结构

>   复杂的参数结构，无非就是key对应的value又是一个json格式或者，key对应的是一个列表，而且列表中每项都是一个json。

这是就可以使用一些特殊的字段来实现了

-   如果在一个字段中放置了一个列表，那么可以使用**fields.List**
-   如果在一个字段中下面又是一个json，那么可以使用**fields.Nested**

##### 代码实现

>   模拟环境：新闻系统后台  用户  新闻   新闻标签

```python
# 复杂的参数结构
# 实体间关系有   1：1   1:n    n:n(转为2个1:n)
# 新闻系统后台  用户  新闻   新闻标签
class User():
    def __init__(self,id,uname,age):
        self.id = id
        self.uname = uname
        self.age = age
    # __str__ 和 __repr__
    '''
    __str__打印出来只能看到地址值
    __repr__ 打印的时候，会把里面的全部显示出来
    '''
    def __str__(self):
        return "<User:{id},{uname},{age}>".format(id = self.id,uname = self.uname,age = self.age)
class News():
    def __init__(self,id,title,content):
        self.id = id
        self.title = title
        self.content = content
        self.author = None
        self.tags = []
    def __repr__(self):
        return "<News:{id},{title},{content},{author},{tags}>"\
            .format(id=self.id,title = self.title,content = self.content,author=self.author,tags = self.tags)
class NewsTag():
    def __init__(self,id,name):
        self.id = id
        self.name = name
    def __repr__(self):
        return "<NewsTag:{id},{name}>".format(id = self.id,name = self.name)
def createData():
    user = User(110,'莫莫',30)
    tag1 = NewsTag(200,"要闻")
    tag2 = NewsTag(210,"娱乐")
    news =News(300,'吴京征服了世界上海拔最高的派出所','4月23日中午11点，吴京发了一条微博，配文“世界上海拔最高的派出所”，并@了另外一名演员张译。微博中有两张图片，第一张是吴京和张译两人坐在地上的合照，背后几个大字“中国边防”。第二张则是两人与派出所民警们的合照。 ')
    news.author = user   #绑定新闻作者
    news.tags.append(tag1) #绑定新闻标签1
    news.tags.append(tag2) #绑定新闻标签2
    print(news)
    return news
class NewsView2(Resource):
    resource_fields ={
        'id':fields.Integer,
        'title':fields.String,
        'content':fields.String,
    #     如果在一个字段下面又是一个字典，那么可以使用field.Nested({...})
        'author':fields.Nested({
            'id':fields.Integer,
            'uname':fields.String,
            'age':fields.Integer,
        }),
        # 如要在一个字段中放置一个列表，那么可以使用fields.List(fields.Nested({...}))
        'tags':fields.List(fields.Nested({'id':fields.Integer,
                                          'name':fields.String
                                          }))
    }
    @marshal_with(resource_fields)
    def get(self):
        news = createData()
        return news
api.add_resource(NewsView2,'/news2/')
```

## 结合蓝图使用

>   关键点在于，创建API对象的时候，要创建蓝图对象，而不是app对象了。

##### 代码实现（部分）

```python
首先需要把所需要的代码复制粘贴到蓝图文件中。

blueprints/news.py:
from flask import Blueprint
# 定义蓝图，名字，__name__,前缀。。。。
news_bp = Blueprint('news_bp', __name__, url_prefix='/news')
# 此写法适用于在蓝图文件中使用，在蓝图文件中使用flask_restful写接口
api = Api(news_bp)

app.py：
# 导入蓝图文件
from blueprints.news import news_bp
# 注册蓝图
app.register_blueprint(news_bp)
```

## 渲染模板

>   渲染模板需要借助api.representation装饰器，把代码按照规则进行解析

##### 代码实现

```python
# 2、渲染模板
class ListView(Resource):
    def get(self):
        return render_template('index.html')
api.add_resource(ListView,'/list/')
# 不引入装饰器api.representation执行操作之前，会默认把页面的html文件当做普通的字符串展现。

# 渲染模板啦~（一般是最前边），只支持html和json，常见的为text/html和text/javascript和application/json
@api.representation('text/html')
# 渲染模板，要解析成html文件，则需要传data(全文内容)，code(状态码)，header(头部信息)，并且返回值必须是一个response对象
def out_html(data,code,headers):
    if isinstance(data,str):
        # 在representation装饰的函数中，必须返回一个Response对象
        resp = make_response(data)
        # 借助于make_response()函数可以创建一个Response对象。
        # resp =Response(data)
        return resp
    else:
        # mimetype='application/json'告诉客户端浏览器，对于相应回去的内容按照json的格式解析
        return Response(json.dumps(data),mimetype='application/json')
```

## 拓展知识

>   make_response函数可以把任何一个数据转化为Response对象