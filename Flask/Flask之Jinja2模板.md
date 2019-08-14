# Flask之Jinja2模板

## 	思维导图

![image](assets\Jinja2模板.png)

## Jinja2简介和查找路径

Jinja2是Flask框架所采用的的模板，模板是一个web开发必备的模块。

### 查找路径

-   在渲染模版的时候，默认会从项目根目录下的**templates**目录下查找模版。

-   如果不想把模版文件放在**templates**目录下，那么可以在Flask初始化的时候指定**template_folder**来指定模版的路径。

    ```python
    # 如果对默认的查找路径不满意，可以用render_forder来指定末班路径
    # __name__中进行修改 template_forder = 路径
    app = Flask(__name__,template_folder= 'E:/python_work/Flask/09/demo')
    ```

    ![image](assets\Jinja2改变模板的默认路径A.png)

### 引入模板

一般是通过引入render_template模块来引入模板

```python
@app.route('/')
def hello_world():
    # return 'Hello World!'
    # 去数据库拿取数据
    # 模拟数据库的一个用户数据
    uname = 'momo'
    return render_template('index.html',content=uname)
# 查询所有的新闻信息
@app.route('/news/')
def news_list():
    return render_template('news/news_list.html')
```

## 模板传参以及技巧

### 关键字传参（针对参数少的情况）

```python
@app.route('/')
def hello_world():
    # 关键词传参，只适用于键值对形式，且参数较少的情况
    return render_template('index.html',uname='momo')
```

### 传参技巧（针对参数很多的情况）

#### 使用传参技巧

说白了就是添加一个context，然后通过‘**’来传递参数。

```python
@app.route('/list/')
def hello():
    # 如果参数太多了，可以放到一个字典中，然后在传这个字典参数的时候，使用两个星号，将字典打散成关键字参数（也叫命名参数）。
    context = {
        'uname': 'momo',
        'age': 18,
        'country': 'china',
        'childrens': {
            'name': 'mjz',
            'height': '62cm'
   				}
    }
    # 使用的传参技巧
    return render_template('index.html',**context)
```

#### 不使用传参技巧

假如不使用传参技巧，可以把context命名为c，然后可以直接传递c。

```python
# 不是用传参技巧
return render_template('index.html',c=context)
```

### 利用url_for传递参数

url_for传递参数分为两种方式，分别为路径传参和查询式传参，但是先看一下不用url_for传参的情况。

```python
不使用url_for传递参数。
python代码：
@app.route('/')
def hello_world():
    return render_template('index.html')
html代码：
<a href="/login/">登录1</a>
```

#### 路径传参

```python
# 需求：在所有和用户操作相关的地方，加上一个路径account

@app.route('/account/login/<name>')

def login():

    return render_template('login.html')
  
html代码：

		<h3>模板中url_for的传参，路径传参</h3>

    <a href="{{ url_for('login',name='tantan') }}">登录4</a>

{#    /account/login/tantan/#}
```

#### 查询式传参

```html
<h3>模板中url_for传参，查询字符串传参</h3>

<a href="{{ url_for('login',p1='lol',p2 = 'dota',name='tantan') }}">登录5</a>

{#    /account/login/tantan?p1=lol&p2=dota#}
```



## 过滤器

本质上相当于一个函数，把当前变量传入到过滤器中，然后过滤器根据自己功能那个，返回对应的值，然后再将结果渲染到页面上。

### 基本用法

过滤器是通过管道符号（|）进行使用的，例如：**{{ name|length }}**，将返回name的长度。

### 常用过滤器的功能

-   abs(value)：返回一个数值的绝对值。 例如：-1|abs。

-   default(value,default_value,boolean=false)：如果当前变量没有值，则会使用参数中的值来代替。name|default('xiaotuo')——如果name不存在，则会使用xiaotuo来替代。boolean=False默认是在只有这个变量为undefined的时候才会使用default中的值，如果想使用python的形式判断是否为false，则可以传递boolean=true。也可以使用or来替换。

-   escape(value)或e：转义字符，会将<、>等符号转义成HTML中的符号。例如：content|escape或content|e。

-   first(value)：返回一个序列的第一个元素。names|first。

-   format(value,*arags,**kwargs)：格式化字符串。例如以下代码：

  {{ "%s" - "%s"|format('Hello?',"Foo!") }}将输出：Helloo? - Foo! 

-   last(value)：返回一个序列的最后一个元素。示例：names|last。

-   length(value)：返回一个序列或者字典的长度。示例：names|length。

-   join(value,d=u'')：将一个序列用d这个参数的值拼接成字符串。

-   safe(value)：如果开启了全局转义，那么safe过滤器会将变量关掉转义。示例：content_html|safe。

-   int(value)：将值转换为int类型。

-   float(value)：将值转换为float类型。

-   lower(value)：将字符串转换为小写。

-   upper(value)：将字符串转换为小写。

-   replace(value,old,new)： 替换将old替换为new的字符串。

-   truncate(value,length=255,killwords=False)：截取length长度的字符串。

-   striptags(value)：删除字符串中所有的HTML标签，如果出现多个空格，将替换成一个空格。

-   trim：截取字符串前面和后面的空白字符。

-   string(value)：将变量转换成字符串。

-   wordcount(s)：计算一个长字符串中单词的个数。



### Default过滤器的使用

如果当前变量没有值，则会使用参数中的值来代替。

>   以个性签名为例

```html
py代码：
@app.route('/')
def hello_world():
    context ={
        'postion':-1,
        # 'signature':'偶买噶'
        'signature': "",
    }
    return render_template('index.html',**context)

html代码：
<h3>default过滤器的使用</h3>#}

<p>个性签名[使用过滤器]：{{ signature|default('此人很懒，暂无签名',boolean = True) }}</p>

<hr>

<p>个性签名[不是使用过滤器]：{{ signature or ('此人很懒，暂无签名') }}</p>

```

上述代码中：

-   boolean = True 表示要给value添加一些特定的值，这里表示：若signature没有值，则显示（此人很懒，暂无签名）
-   另外default可以被or**代替**。



### escape和safe过滤器（转义）

```python
py代码：

@app.route('/')
def hello_world():
    context ={
        'postion':-1,
        # 'signature':'偶买噶'
        'signature': "<script>alert('杜绝眼高手低')</script>",
    }
    return render_template('index.html',**context)
  
html代码：
{% autoescape off %}
<p>个性签名4：{{ signature|escape }}</p>
{% endautoescape  %}

<p>个性签名5：{{ signature|safe }}</p>
```

上述代码中：

-   JinJa2模板默认全局开启了**自动转义**功能   意思是：**会把'<'转换位html知识里面的实体字符'&lt'**

-   **safe**过滤器：可以关闭一个字符串的自动转义。

-   **escape**过滤器：对某一个字符串进行转义。

-   **autoescape**是Jinja标签，可以对他里面的代码块关闭或开启自动转义。

    ```jinja2
    {% autoescape off %}
    ......码块
    {% endautoescape  %}
    ```

### 常用过滤器

#### frist+last+length

```html
<p>第一个人：{{ persons|first }}</p>

<p>最后一个人：{{ persons|last }}</p>

<p>总人数：{{ persons|length }}</p>
```

#### format

```jinja2
{{ "%s" - "%s"|format('Hello?',"Foo!") }}将输出：Helloo? - Foo!

helloo对应第一个%s

Foo！对象第二个%s
```

#### int

```jinja2
{% if gender|int ==1  %}
          <p>性别：男</p>
{% else %}
           <p>性别：女</p>
{% endif %}
```

### 自定义过滤器

需要在py文件中定义一个函数，并且需要一个装饰器**@app.template_filter('过滤器名称')**

另外，可能因为编译的工具不同还要规定模式为自动加载模式，**app.config['TEMPLATES_AUTO_RELOAD']=True**

下列代码，把'十大酷刑'替换为'****'。

```python
@app.template_filter('cut')
def cut_world(value):
    value = value.replace('十大酷刑','****')
    return value
```

### 自定义时间过滤器

#### 逻辑

定义一个函数，满足下列条件：

1.  差值小于60s 返回刚刚
2.  差值大于60s小于360s  返回XX分钟之前
3.  差值大于360s小于24小时    返回XX小时前
4.  差值大于24小时    返回XX天前

#### 代码：

```python
@app.template_filter('time_to_time')

def time_to_time(time):

    if isinstance(time,datetime):

        now = datetime.now()

        timestap = (now-time).total_seconds()

        if timestap<60:

            return '刚刚'

        elif timestap>60 and timestap<60*60:

            minutes = timestap//60

            return '%s分钟之前'%minutes

        elif timestap>60*60 and timestap<60*60*24:

            hours = timestap//(60*60)

            return  '%s小时之前'%hours

        elif timestap>60*60*24:

            days = timestap//(60*60*24)

            return  '%s天之前'%days

        else:

            return time .strftime('%Y/%m/%d %H:%M')

    else:

        return time
```



### 控制语句

>   所有的控制语句都是放在{%.......%}中的。

#### if语句

##### 格式：

>   {% if statement(条件语句)%}
>
>   ...(里面加elif或者else都可以)
>
>   {% endif %}

##### 应用案例1（简单案例）：

1、如果名字是momo，就打印出来。

```jinja2
{% if name=='momo' %}

    <p>姓名：momo</p>

{% endif %}
```

2、大于18岁才能进网吧。

```jinja2
{% if age>=18 %}

    <p>年龄大于{{ age }}可以进入网吧</p>

{% else %}

    <p>未成年（年龄小于{{ age }}）不可以进网吧</p>

{% endif %}
```

3、考试分数，90分以上A,80分以上B ,60分以上C,之下不及格。

```jinja2
{% if score>=90 %}

    <p>{{ name }}的成绩为：A</p>

{% elif score>=80 %}

    <p>{{ name }}的成绩为：B</p>

{% elif score>=60 %}

    <p>{{ name }}的成绩为：C</p>

{% else %}

    <p>{{ name }}不及格</p>

{% endif %}
```

##### 应用案例2（多选案例）：

户籍和性别选择。

```jinja2
<form action="#" method="post">
        户籍：
            {% if addr=='bj' %}
                <select name="addr">
                <option value="-1">-请选择-</option>
                <option value="bj" selected="selected">-北京市-</option>
                <option value="sh">-上海市-</option>
                <option value="cq">-重庆市-</option>
                </select>
            {% elif addr== 'cq' %}
                <select name="addr">
                <option value="-1">-请选择-</option>
                <option value="bj" >-北京市-</option>
                <option value="sh">-上海市-</option>
                <option value="cq" selected="selected">-重庆市-</option>
                </select>
            {% else %}
                <select name="addr">
                <option value="-1" selected="selected">-请选择-</option>
                <option value="bj" >-北京市-</option>
                <option value="sh">-上海市-</option>
                <option value="cq" >-重庆市-</option>
                </select>
    {% endif %}
        <br>
        性别：
        {% if gender|int==1 %}
                    <input type="radio" name="sex" value="1" checked="checked">男
            <input type="radio" name="sex" value="0" >女
            {% else %}
            <input type="radio" name="sex" value="1">男
            <input type="radio" name="sex" value="0" checked="checked">女
        {% endif %}
```

#### for语句

>   **注意在Jinja2的for语句中是没有break和contiune语句的**

for语句就是遍历，遍历大致分为两种类型，列表遍历和字典遍历。

##### 列表遍历

```jinja2
{% for user in users %}

        <li>{{ user }}</li>

{%	else	%}

		<li>没有任何用户</li>

{% endfor %}
```

##### 字典遍历

```jinja2
 {% for key in person.keys()[或者values(),item()] %}

        <td>{{ key }}</td>

 {% endfor %}
```

##### 反向遍历（reverse）

```jinja2
{% for user in users | reverse %}

    <li>{{ user }}</li>

{%	else	%}

		<li>没有任何用户</li>

{% endfor %}
```

##### 小知识

>   | loop.index | 当前迭代的索引（从1开始） |
>
>   | loop.index0 | 当前迭代的索引（从0开始） |
>
>   | loop.first | 是否是第一次迭代，返回True或False | 
>
>   | loop.last | 是否是最后一次迭代，返回True或False | 
>
>   | loop.length | 序列的长度 |

##### for语句案例（Python）

```python
from flask import Flask,render_template
app = Flask(__name__)
# 功能实现：
#    1、编历所有的用户
#    2、编历个人信息
#    3、编历所有图书信息{（）（）}
@app.route('/')
def hello_world():
    # 模拟数据
    datas = {
        'users': ['momo', 'lulu', 'tantan'],
        # 'users':[],
        'person': {
            'name': '默默',
            'age': 18,
            'gender': '男',
            'nick': '莫帅'
            },
        'books': [
            {
                'name': '我是1',
                'price': 89,
                'author': '不知道'
            },
            {
                'name': '墨菲定律',
                'price': 100,
                'author': '墨菲'
            },
            {
                'name': '我是3',
                'price': 89,
                'author': '不知道'
            },
            {
                'name': '我是3',
                'price': 89,
                'author': '不知道'
            }
                ]
            }
    return render_template('index.html',**datas)
app.debug = True
if __name__ == '__main__':
    app.run()
```

##### for语句案例（Jinja2）

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <h2>学习Jinja2模板语言的for循环使用</h2>
<h3>1、编历所有的用户 [] 列表</h3>
    <ul>
        {% for user in users|reverse %}
            <li>{{ user }}</li>
            {% else %}
            <li style="color:red;background-color:yellow;width: 100px;">没有任何用户</li>
        {% endfor %}
    </ul>
<h3>2、编历个人信息 {}  字典 key()   value()   item()</h3>
    <table>
        <tr>
            <th>姓名</th>
            <th>年龄</th>
            <th>性别</th>
            <th>昵称</th>
        </tr>
        <tr>
            <th>{{ person.name }}</th>
            <th>{{ person.age }}</th>
            <th>{{ person.gender }}</th>
            <th>{{ person.nick }}</th>
        </tr>
        <tr>
            {% for key in person.keys() %}
                <td>{{ key }}</td>
            {% endfor %}
        </tr>
        <tr>
            {% for value in person.values() %}
                <td>{{ value }}</td>
            {% endfor %}
        </tr>
         <tr>
            {% for item in person.items() %}
                <td>{{ item }}</td>
            {% endfor %}
        </tr>
    </table>
<h3>3、编历所有图书信息 { [],[]} 字典和列表的结合</h3>
<table border="1px">
    <thead>
    <tr>
        <th>序号</th>
        <th>书名</th>
        <th>价格</th>
        <th>作者</th>
        <th>所有书的总数量</th>
    </tr>
    </thead>
    <tbody>
        {% for book in books %}
{#            对首尾行的颜色的区分#}
            {% if loop.first %}
                <tr style="background-color: rebeccapurple">
                    {% elif loop.last %}
                <tr style="background-color: darkcyan">
                    {% else %}
                <tr style="background-color: greenyellow">
            {% endif %}
                    <td>{{ loop.index }}|{{ loop.index0+1 }}</td>
                    <td>{{ book.name }}</td>
                    <td>{{ book.price }}</td>
                    <td>{{ book.author }}</td>
                    <td>书的总数量：{{ loop.length }}</td>
                </tr>
        {% endfor %}
    </tbody>
</table>
</body>
</html>
```

##### for语句实现九九乘法表

```jinja2
<h3>4、for循环嵌套案例，实现九九乘法表</h3>
<table border="1px">
    {% for x in range(1,10) %}
        <tr>
        {% for y in range(1 , x + 1) %}
            <td>{{ y }}*{{ x }} ={{ x*y }}</td>
        {% endfor %}
        </tr>
    {% endfor %}
</table>
```

## 宏

和Python中的函数类似，可以传递参数，但是不能有返回值，减少代码量。

### 使用宏和不使用宏的比较

不使用宏：

```html
<h4>正常方式创建表单域常用的标签</h4>
    <table>
        <tr>
            <td>用户名：</td>
            <td>
						<input type="text" name="name" value="">
						</td>
        </tr>
        <tr>
            <td>密码：</td>
            <td>
								<input type="password" name="pwd" value="">
						</td>
        </tr>
        <tr>
            <td></td>
            <td>
								<input type="submit" value="提交表单">
						</td>
        </tr>
    </table>
```

使用宏的情况

```html
{#  1、定义宏  #}
    {% macro input(name,type='text',value ='')%}
        <input type="{{ type }}" name="{{ name }}" value="{{ value }}">
    {% endmacro %}
<h4>使用宏创建表单域常用的标签</h4>
    {#  2、使用宏  #}
    <table>
        <tr>
            <td>用户名：</td>
            <td>
								{{ input('name') }}
						</td>
        </tr>
        <tr>
            <td>密码：</td>
            <td>
								{{ input('pwd',type = 'password') }}
						</td>
        </tr>
        <tr>
            <td></td>
            <td>
								{{ input('',type= 'submit',value='提交表单') }}
						</td>
        </tr>
    </table>
```

相比之下，对于上面的简单例子来说，用宏的代码量多一些，但是当代码增多，使用宏就会便捷很多。

但是使用宏的情况，一般不会再模板中直接定义宏，而是会把宏放在一个单独的文件中，这样就需要导入宏了。

### 宏的导入

方式一：(**注意**：当使用了【as 宏的别名】时，下面对于宏的使用都要用别名。)

>   from '宏文件的路径' import 宏的名字 [as 宏的别名]

```jinja2
{% from 'index/macros/macro1.html' import  input %}
```

方式二：

>   import "宏文件的路径" as xxx  [with  context]

```jinja2
{% import 'index/macros/macro1.html' as inp %}
```

**注意**：这种方式是导入了一个对象，宏在这个对象中，使用就需要用{{对象名.宏名}}使用。并且也不会共享参数。那么就需要使用with context 让参数共享

```jinja2
{% import 'index/macros/macro1.html' as inp with context %}
```

## Include标签使用

相当于直接将制定模板中的代码复制粘贴到当前位置。

include的路径，也是跟import一样，直接从templates根目录下去找，不要以相对路径去找。

## set+with语句以及模板中定义变量

### SET语句

在模板中，可以使用'set'语句来定义变量，并且在后面的都可以使用这个变量。（类似于全局变量）

```jinja2
{% set  uname='momo'%}

	<p>用户名：{{ uname }}</p>
```

### WITH语句

'with'语句定义的变量，只能在'with'语句块中使用，超过了这个代码块，就不能使用了。（相当于局部变量）

```jinja2
{% with classroom='python202'%}

    <p>班级：{{ classroom }}</p>

{% endwith %}
```

### 案例实现

```jinja2
<h3>在模板中定义变量：set语句  特点：全局变量</h3>
{#    观察在定义之前能否使用#}
    {% set  flag = 'yes' %}
    <p>标志1：{{ flag }}</p>
    <h3>在模板中定义变量：with语句   特点：局部变量</h3>
    {% with monitor = '张三丰' %}
        <p>班长为:{{ monitor }}</p>
        <p>啊哈哈：{{ flag }}</p>
    {% endwith %}
{#    with语句块之外能否使用#}
    <p>班长为:{{ monitor }}</p>
    <h3>在模板中定义变量：涉及变量区域有效性问题时，可以用with和set语句组合使用  了解</h3>
    {% with   %}
        {% set boss = '王总' %}
        <p>老板是：{{ boss }}</p>
    {% endwith %}
{#   出了区域#}
    <p>老板是：{{ boss }}</p>
```

## Flask中加载静态文件

### 静态文件

静态文件就是CSS  JS  图片等文件

### 加载

加载静态文件使用的是url_for函数，两个参数，第一个参数为固定值‘static’,第二个参数为filename。

>   语法：{{ url_for("static",filename='xxx') }}

```html
CSS加载：
<link href="{{ url_for('static',filename='css/index.css') }}" rel="stylesheet">
JS加载：
 <script type="text/javascript" src = "{{ url_for('static',filename= 'js/index.js') }}"></script>
图片加载：（一些简单的样式可以在标签内书写）
<img src="{{ url_for('static',filename='image/820024.png') }}"  width="1000px">
```

## 模板继承

模板继承就是把公用的代码抽离出来，放到父模板中，让子模板继承使用。

### 模板继承的语法

使用‘**extends**’语句，指明父模板的路径，（父模板的路径也是`templates`文件夹下的绝对路径）

>   **{% extends "base.html" %}**

### block语法

因为父模板要有能力提供**一个接口**，让子模板**实现功能代码**，从而引出**block**。

### super（）函数

**默认**情况下，子模板如果实现了父模版定义的block。那么子模板block中的代码就会**覆盖掉父模板中的代码**。如果想要在子模板中**仍然保持**父模板中的代码，那么可以使用**{{ super() }}**来实现。

### 相互调用不同的block

如果想要在另外一个模版中使用其他模版中的代码。那么可以通过**{{ self.其他block名字() }}**就可以了

### 注意事项

1.  要继承的时候。extends必须在html文件的第一行。
2.  子模板中，如果要实现自己的代码，应该放到block中。如果放到其他地方，那么就不会被渲染。


