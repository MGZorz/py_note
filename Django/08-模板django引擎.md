# 一、Django模板

​	作为一个Web框架，Django需要一种方便的方式来动态生成HTML。最常用的方法依赖于模板。模板包含所需HTML输出的静态部分以及描述如何插入动态内容的特殊语法。

​	对模板引擎的一般支持和Django模板语言的实现都存在于 django.template 命名空间中



## 1、django默认模板

### 1、配置

​	在settings中配置：

```python
# 配置模板
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

```

笔记：

- BACKEND：是实现Django模板后端API的模板引擎类的路径。内置是django.template.backends.django.DjangoTemplates和 django.template.backends.jinja2.Jinja2（使用这个需要额外安装jinja2库）
- DIRS ：按搜索顺序定义引擎应该查找模板源文件的目录列表
- APP_DIRS：告诉引擎是否应该在已安装的应用程序中查找模板，每个后端为其模板应存储在的应用程序内的子目录定义一个常规名称。
- OPTIONS：包含后端特定的设置



### 2、用法

​	假如settings中配置如下：

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            '/home/html/example.com',
            '/home/html/default',
        ],
    },
    {
        'BACKEND': 'django.template.backends.jinja2.Jinja2',
        'DIRS': [
            '/home/html/jinja2',
        ],
    },
]

```

1. get_template 

   该函数使用给定名称加载模板并返回一个 Template对象，找到第一个匹配的模板即返回

   ```python
   template = get_template('story_detail.html')
   ```

   Django将要查找的文件，依次为：

   - /home/html/example.com/story_detail.html（'django'引擎）
   - /home/html/default/story_detail.html（'django'引擎）
   - /home/html/jinja2/story_detail.html（'jinja2'引擎）

   

   示例：

   ```python
   # 最常用的render
   from django.shortcuts import render
   
   def my_view(request):
       # View code here...
       return render(request, 'myapp/index.html', {
           'foo': 'bar',
       }, content_type='application/xhtml+xml')
   
   
   # 相当于基础的get_template：
   from django.http import HttpResponse
   from django.template import loader
   
   def my_view(request):
       # View code here...
       template = loader.get_template('myapp/index.html')
       context = {'foo': 'bar'}
       # 注意，这个 render 和 快捷键 render 不是一个对象
       return HttpResponse(template.render(context, request), content_type='application/xhtml+xml')
   
   ```

   

2. select_template

   select_template() 用法类似 get_template() ，除了它需要一个模板名称的列表。它按顺序尝试每个名称并返回存在的第一个模板

   ```python
   template = select_template(['story_253_detail.html','story_detail.html'])
   ```

   Django将要查找的文件，依次为：

   - /home/html/example.com/story_253_detail.html（'django'引擎）
   - /home/html/default/story_253_detail.html（'django'引擎）
   - /home/html/jinja2/story_253_detail.html（'jinja2'引擎）
   - /home/html/example.com/story_detail.html（'django'引擎）
   - /home/html/default/story_detail.html（'django'引擎）
   - /home/html/jinja2/story_detail.html（'jinja2'引擎）



### 3、模板语言

​	Django模板只是一个文本文档或使用Django模板语言标记的Python字符串。一些结构被模板引擎识别和解释，主要的是变量( {{ 变量 }} )和标签( {% 标签 %} )。



#### 1、变量

​	一个变量从上下文中输出一个值，这是一个类似字典的对象将键映射到值。

​	变量被这样包围 ：{{变量}}  譬如：

```django
# 模板中这样写：
My first name is {{ first_name }}. My last name is {{ last_name }}.

# 传入到 模板中的变量为：
{'first_name': 'John', 'last_name': 'Doe'}

# 在浏览器中显示如下：
My first name is John. My last name is Doe.
```

​	字典查找，属性查找和列表索引查找 都用点符号实现： 

```django
# 获取字典的 value
{{ my_dict.key }}

# 获取对象的 属性
{{ my_object.attribute }}

# 获取列表的 元素
{{ my_list.0 }}
```



#### 2、标签

​	标签在渲染过程中提供任意的逻辑。

​	例如，标签可以输出内容，用作控制结构，

​	例如“if”语句或“for”循环，从数据库中获取内容，甚至可以访问其他模板标签。

​	所有标签见：

​	https://docs.djangoproject.com/en/2.2/ref/templates/builtins/#ref-templates-builtins-tags



1. 基本用法

   标签被包围  {% 代码 %}  譬如：

   ```django
   # 无参数标签 csrf_token ，这个标签是用于html进行 form 表单提交时，包含一个 随机变化的字符串，在html页面中，其实就是一个 input type='hidden'
   # 作用是用于防止跨域攻击
   {% csrf_token %}
   
   # 传参的标签 cycle  ， 参数 'odd' 'even' ，空格间隔
   # 标签本身也支持 关键字参数 {% 标签 key1='value' key1='even' %}
   {% cycle 'odd' 'even' %}
   ```

   

2. 常见标签

   由于在模板中，没有办法通过代码缩进判断代码块，所以控制标签都需要有结束的标签

   1. if

      判断标签 if  endif ： 

      ```django
      # athlete_list 不为空
      {% if athlete_list %}
      	# 输出 athlete_list 的长度    | 是过滤器
          Number of athletes: {{ athlete_list|length }}
      {% elif athlete_in_locker_room_list %}
          Athletes should be out of the locker room soon!
      {% else %}
          No athletes.
      {% endif %}
      
      ```

      

   2. firstof

      输出不是False的第一个参数，所有参数都为False，则什么都不输出 

      ```django
      {% firstof var1 var2 var3 %}
      等同于
      {% if var1 %}
          {{ var1 }}
      {% elif var2 %}
          {{ var2 }}
      {% elif var3 %}
          {{ var3 }}
      {% endif %}
      
      使用默认值：
      {% firstof var1 var2 var3 "默认值" %}
      
      ```

      

   3. for

      循环遍历，for endfor结束 ，可以遍历列表，字典等

      ```django
      <ul>
      {% for athlete in athlete_list %}
          <li>{{ athlete.name }}</li>
      {% endfor %}
      </ul>
      
      反向循环：
      {% for athlete in athlete_list reversed%}
      
      字典：  data.items 这种调用方法，是不加 () 的
      {% for key, value in data.items %}
          {{ key }}: {{ value }}
      {% endfor %}
      
      设置默认值， for empty  ，类似python的  for else：
      <ul>
      {% for athlete in athlete_list %}
          <li>{{ athlete.name }}</li>
      {% empty %}
          <li>Sorry, no athletes in this list.</li>
      {% endfor %}
      </ul>
      等同于，但是比下面的写法更加简便：
      <ul>
        {% if athlete_list %}
          {% for athlete in athlete_list %}
            <li>{{ athlete.name }}</li>
          {% endfor %}
        {% else %}
          <li>Sorry, no athletes in this list.</li>
        {% endif %}
      </ul>
      
      ```

      for循环在循环中设置了许多变量：

      | **变量**                | **描述**                             |
      | ----------------------- | ------------------------------------ |
      | **forloop.counter**     | 循环的当前迭代（1索引）              |
      | **forloop.counter0**    | 循环的当前迭代（0索引）              |
      | **forloop.revcounter**  | 循环结束时的迭代次数（1索引）        |
      | **forloop.revcounter0** | 循环结束时的迭代次数（0索引）        |
      | **forloop.first**       | 如果这是通过循环的第一次，则为真     |
      | **forloop.last**        | 如果这是通过循环的最后一次，则为真   |
      | **forloop.parentloop**  | 对于嵌套循环，这是围绕当前循环的循环 |

      

   4. 布尔运算符

      and、or和not

      ```django
      {% if athlete_list and coach_list %}
          Both athletes and coaches are available.
      {% endif %}
      
      {% if not athlete_list %}
          There are no athletes.
      {% endif %}
      
      {% if athlete_list or coach_list %}
          There are some athletes or some coaches.
      {% endif %}
      
      {% if not athlete_list or coach_list %}
          There are no athletes or there are some coaches.
      {% endif %}
      
      {% if athlete_list and not coach_list %}
          There are some athletes and absolutely no coaches.
      {% endif %}
      
      ```

      允许在同一个标签中使用两个and和or子句， and优先级高于or例如：

      ```django
      {% if athlete_list and coach_list or cheerleader_list %}
      将被解释为：
      if (athlete_list and coach_list) or cheerleader_list
      
      ```

      但是在if标签中使用实际的括号是无效的语法。如果你需要它们来表示优先级，你应该使用嵌套if标签

      

   5. 逻辑运算符

      ==, !=, <, >, <=, >=, in, not in, is, 和 is not 

      ```django
      {% if somevar == "x" %}
        This appears if variable somevar equals the string "x"
      {% endif %}
      
      {% if "bc" in "abcdef" %}
        This appears since "bc" is a substring of "abcdef"
      {% endif %}
      
      {% if somevar is not True %}
        This appears if somevar is not True, or if somevar is not found in the
        context.
      {% endif %}
      
      ```

      优先级，从低到高：

      - or
      - and
      - not
      - in
      - ==，!=，<，>，<=，>=

      

   6. url

      给定视图和可选参数匹配的绝对路径引用（没有域名的URL）

      ```django
      {% url 'some-url-name' v1 v2 %}
      第一个参数是url模式名称，后面跟着的是参数，以空格分隔
      
      可以使用关键字：
      {% url 'some-url-name' arg1=v1 arg2=v2 %}
      
      如果您想检索命名空间的URL，请指定完全限定的名称：
      {% url 'myapp:view-name' %}
      
      ```

      

   7. widthratio：乘法和除法

      ```django
      {% widthratio this_value max_value max_width %}
      结果是： this_value/max_value*max_width
      如果要计算  value * 10 ： widthratio value 1 10
      如果要计算 value / 8  ： widthratio 8 1
      还可以这样使用：
      
      {% widthratio this_value max_value max_width as width %}
      The width is: {{ width }}
      
      ```

      

   8. with

      简单的名称缓存复杂变量，当访问多次耗时的方法（例如操作数据库的方法）:

      ```django
      {% with total=business.employees.count%}
          {{ total }} employee
      {% endwith %}
      
      上述的：{% with total=business.employees.count%}
          等同于：{% with business.employees.count as total %}
      
      ```

      

   9. 过滤器

      通过  |   来使用

      示例：{{ value|add:"2" }}

      value： 是模板中获取的对象

      add： 是过滤器

      “2”： 是过滤器add的参数，只支持一个参数

      

      length：messages|length这里判断 messages 不为空，并且长度大于等于100 

      ```django
      {% if messages|length >= 100 %}
         You have lots of messages today!
      {% endif %}
      ```

      

      add：相加(减法：|add:-2 ) ， 可以应用于 列表等

      ```django
      {{ value|add:"2" }}
      如果value是4，那么输出6
      
      {{ first|add:second }}
      如果first=[1,2,3] ，second=[4,5,6]，那么输出：[1,2,3,4,5,6]
      
      ```

      

      divisibleby：能否整除，返回 True和False 

      ```django
      {{ value|divisibleby:"2" }}
      ```

      

      addslashes：单引号前加 \ 

      ```django
      {{ value|addslashes }}
      value="I'm using Django"，输出："I\'m using Django".
      
      ```

      

      capfirst：首字母大写，只对字符串的第一个单词的首字母大写

      ```django
      {{ value|capfirst }}
      如果value是"django is good"，输出将是"Django is good"。
      
      ```

      

      center：将值置于给定宽度的字段中

      ```django
      "{{ value|center:"15" }}"
      如果value是"Django"，输出将是。"     Django    "，前面5个，后面4个空格
      
      ```

      

      cut：删除给定字符 

      ```django
      {{ value|cut:" " }}
      如果value是"String with spaces"，输出将是："Stringwithspaces"
      
      ```

      

      date：日期字符串 

      ```django
      格式字符  	描述	示例              输出
      b	月，文字，3个字母，小写。	'jan'
      d	每月的一天，2位数字前导零。	'01' 至 '31'
      D	星期几，文字，3个字母。	'Fri'
      e	时区名称。可能是任何格式，或者可能会返回一个空字符串，具体取决于日期时间。	''，'GMT'，'-500'，'US/Eastern'，等。
      E	月，通常用于长日期表示的区域设置特定备选表示。	'listopada'（对于波兰语区而言'Listopad'）
      f	时间在12小时和分钟之内，如果它们为零，则分钟时间不再。专有扩展。	'1'， '1:30'
      F	月，文字，长。	'January'
      g	小时，12小时制，无前导零。	'1' 至 '12'
      G	小时，24小时制，无前导零。	'0' 至 '23'
      h	小时，12小时制。	'01' 至 '12'
      H	小时，24小时制。	'00' 至 '23'
      i  	分钟。	'00' 至 '59'
      I 	夏令时，无论是否有效。	'1'  or  '0'
      J	没有前导零的月份的一天。	'1' 至 '31'
      n	月没有前导零。	'1' 至 '12'
      N   月份             'Jan.', 'Feb.', 'March', 'May'
      s    秒                  00-59
      t	给定月份的天数。	28 至 31
      T	这台机器的时区。	'EST'， 'MDT'
      u	微秒。	000000 至 999999
      U	Unix时代以来的秒数（1970年1月1日00:00:00 UTC）。	 
      w ^	没有前导零的数字。	'0'（星期日）至'6'（星期六）
      W ^	ISO-8601周数，周数从周一开始。	1， 53
      y	年，2位数字。	'99'
      Y	年，4位数字。	'1999'
      z	一年中的一天。	0 至 365
      Z	以秒为单位的时区偏移量。UTC以西时区的偏移总是负值，而UTC以东的偏移总是正值。	-43200 至 43200
      
      
      {{ value|date:"D d M Y" }}
      {{ value|date:"Y-m-d H:i:s" }}
      value：datetime.datetime.now()
      
      ```

      

   10. include

      包含另外一个模板

      模板名称可以是变量，也可以是单引号或双引号的硬编码（带引号）的字符串 

      ```django
      {% include "foo/bar.html" %}
      
      {% include template_name %}
      该变量也可以是任何具有render()接受上下文的方法的对象
      
      ```

      include传参数：

      ​	下面这个例子在页面中显示："Hello, John!"

      

      - context：

        ```python
        context = {'greeting': 'hello', 'person': 'John'}
        ```

        

      - name_snippet.html模板:

        ```django
        {{ greeting }}, {{ person|default:"friend" }}!
        ```

        

      - 原模板通过with传递参数

        ```django
        {% include "name_snippet.html" with person="John" greeting="Hello" %}
        ```

        如果只想使用include传递的参数（甚至没有参数，不使用父模板的上下文变量）渲染模板，使用only： 

        ```django
        {% include "name_snippet.html" with greeting="Hi" only %}
        ```

        ​     

### 4、静态文件

​	主要使用 css、javascript和图片文件

​	

1. settings中配置

   ```python
   # staticfiles 只在 DEBUG=True 的情况下有效，生产环境中使用 服务器（如nginx）的静态文件管理
   INSTALLED_APPS = [
       'django.contrib.staticfiles',
   ]
   
   # "/static/" or "http://static.example.com/" 这种url访问的请求都会交给 staticfiles 处理
   STATIC_URL = '/static/'
   
   # 指定静态文件保存的目录，默认是各个子应用下的 static 文件夹
   # 以下是 linux系统， windows下使用： "C:/Users/user/mysite/extra_static_content"
   STATICFILES_DIRS = [
       "/home/special.polls.com/polls/static",
       "/home/polls.com/polls/static",
       "/opt/webfiles/common",
   ]
   ```

   

2. 在子应用下建立目录 static， 存放 静态文件

   

3. 模板文件中

   ```django
   {% load static %}  # 写在模板中第一行
   
   # 图片
   <img src="{% static "images/hi.jpg" %}" alt="Hi!">
   
   # css
   <link rel="stylesheet" href="{% static 'css/mystyle.css' %}" type="text/css" media="screen">
   
   # javascript
   <script type='text/javascript' src='{% static 'js/myjs.js' %}'></script>
   
   # 设置变量
   {% static "images/hi.jpg" as myphoto %}
   <img src="{{ myphoto }}">
   ```

   

4. get_static_prefix 

   在模板中指定 settings 中配置的 STATIC_URL

   ```django
   {% load static %}
   
   <img src="{{ STATIC_PREFIX }}images/hi.jpg" alt="Hi!">
   # 等同于
   <img src="{% static "images/hi.jpg" %}" alt="Hi!">
   ```



### 5、模板继承

​	Django模板引擎中最强大，也是最复杂的部分是模板继承。模板继承允许构建一个基本“骨架”模板，其中包含您网站的所有常见元素，并定义子模板可以覆盖的 blocks
	如下，定义一个base.html， 如下：

```django
<!DOCTYPE html>
<html lang="en">
<head>
    <link rel="stylesheet" href="style.css" />
    <title>{% block title %}My amazing site{% endblock %}</title>
</head>

<body>
    <div id="sidebar">
        {% block sidebar %}
        <ul>
            <li><a href="/">Home</a></li>
            <li><a href="/blog/">Blog</a></li>
        </ul>
        {% endblock %}
    </div>
    <div id="content">
        {% block content %}{% endblock %}
    </div>
</body>
</html>

```

上面这个模板中，定义了3个 block ：

- title
- sidebar
- content

block的基本使用方法：{% **block** title %}  {% **endblock** %}

 

​       子页面detail.html继承上面这个base.html，内容如下：

```django
{% extends "base.html" %}

{% block title %}My amazing blog{% endblock %}

{% block content %}
{% for entry in blog_entries %}
    <h2>{{ entry.title }}</h2>
    <p>{{ entry.body }}</p>
{% endfor %}
{% endblock %}

```

​	使用{% extends "base.html" %} 继承 base.html，本页面有2个block，对应base.html的2个block，会在base.html中，使用本detail.html的对应内容进行替换，而block sidebar 并没有对应的block，因此继续使用base.html的 sidebar 的内容



​	继承的技巧：

- 如果在模板中使用，[**{% extends %}**](https://docs.djangoproject.com/en/2.0/ref/templates/builtins/#std:templatetag-extends)必须是该模板中的第一个模板标签。否则模板继承将不起作用。
- 基本模板中的越多[**{% block %}**](https://docs.djangoproject.com/en/2.0/ref/templates/builtins/#std:templatetag-block)标签越好。子模板不必定义所有父块，因此可以在多个块中填写合理的默认值 
- 如果发现自己在多个模板中复制了内容，则可能意味着您应该将该内容移至父模板的 **{% block %}** 中
- 如果需要从父模板中获取块的内容，则使用 {{ block.super }}

```django
{% block sidebar %}
    {{ block.super }}
    新的内容
{% endblock %}

```

- 在使用模板标签语法之外创建的变量不能在块[**{% block% }**](https://docs.djangoproject.com/en/2.0/ref/templates/builtins/#std:templatetag-block)内使用。例如，该模板不会呈现任何内容

```django
{% trans "Title" as title %}
{% block content %}{{ title }}{% endblock %}

```

- 为了增加可读性，您可以选择为您的结束标签 命名。例如：**{% endblock** content **%}**

```django
{% block content %}

{% endblock content %}

```

​        