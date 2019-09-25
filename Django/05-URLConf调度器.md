# 一、URL调度器

## 1、工作原理

​	django通过urlconf来映射视图函数，只区分路径，不区分http方法

- Django确定要使用的根URLconf模块，一般是在settings中的ROOT_URLCONF设置的值，但是如果传入 HttpRequest 对象具有一个urlconf 属性（由中间件设置），则其值将用于代替 ROOT_URLCONF设置。
- Django加载该URLconf模块并查找变量 urlpatterns，它是一个列表django.urls.path() 和 / 或django.urls.re_path()实例。
- Django按顺序遍历每个URL模式，并停在与请求的URL匹配的第一个URL模式，需要特别注意编写的顺序
- 一旦某个URL模式匹配，Django就会导入并调用给定的视图，该视图是一个简单的Python函数（或基于类的视图方法）。该视图通过以下参数传递：
  - 一个HttpRequest实例。
  - 如果匹配的URL模式没有返回任何命名组，则来自正则表达式的匹配作为位置参数提供。
  - 关键字参数由路径表达式匹配的任何命名部分组成，并由可选的kwargs参数传给 django.urls.path()或django.urls.re_path()。
- 如果没有URL模式匹配，或者在此过程中的任何点发生异常，Django将调用适当的错误处理视图



## 2、简单示例

```python
from django.urls import path

from . import views

urlpatterns = [
    path('articles/2003/', views.special_case_2003),
    path('articles/<int:year>/', views.year_archive),
    path('articles/<int:year>/<int:month>/', views.month_archive),
    path('articles/<int:year>/<int:month>/<slug:slug>/', views.article_detail),
]

```

笔记：

- 从URL中捕获值，请使用尖括号
- 捕获的值可以选择包含转换器类型。例如，用于 \<int:name>捕获，前面的int指整数参数，name是参数的名称

- 没有必要添加一个前导斜杠，因为每个URL都有，例如，使用articles而不是/articles。
- 示例请求说明：
  - **/articles/2005/03/** 匹配列表中的第三个条目。Django会调用这个函数，views.month_archive(request, year=2005, month=3)
  - **/articles/2003/** 会匹配列表中的第一个模式，而不是第二个模式，因为模式是按顺序测试的，而第一个模式是第一个要传递的测试。看看利用匹配顺序插入像这样的特殊情况。在这里，Django会调用这个函数 views.special_case_2003(request)
  - **/articles/2003** 不匹配任何这些模式，因为每种模式都要求URL以斜线结尾，不过在浏览器访问时，会自动添加 / 。
  - **/articles/2003/03/building-a-django-site/ **将匹配最终模式。Django会调用这个函数 。views.article_detail(request, year=2003, month=3, slug="building-a-django-site")



## 3、路径转换器

- str：匹配任何非空字符串，不包括路径分隔符'/'。如果转换器不包含在表达式中，这是默认值。
- int：匹配零或任何正整数。返回一个int。
- slug：匹配由ASCII字母或数字组成的字符串，以及横线和下划线字符。例如， building-your-1st-django_site。
- uuid：匹配格式化的UUID。为防止多个URL映射到同一页面，必须包含破折号，并且字母必须是小写。例如，075194d3-6885-417e-a8a8-6c931e272f00。返回一个 UUID实例。
- path：匹配任何非空字符串，包括路径分隔符 '/'，可以匹配完整的URL路径，而不仅仅是URL路径的一部分str，使用时要谨慎，因为可能造成后续的所有url匹配都失效。



## 4、自定义路径转换器

转换器是一个包含以下内容的类：

- 一个regex类属性，作为一个re匹配字符串。
- to_python(self, value)方法，它处理匹配的字符串转换成要传递到视图函数的类型。
- to_url(self, value)方法，用于处理将Python类型转换为URL中使用的字符串。



定义方式如下：

1. 新建一个converters.py文件，在文件中定义一个FourDigitYearConverter类：

   ```python
   class FourDigitYearConverter(object):
       regex = '[0-9]{4}'
   
       def to_python(self, value):
           return int(value)
   
       def to_url(self, value):
           return '%04d' % value
   ```

   

2. 使用register_converter()方法在URLconf中注册自定义转换器类 ：

   ```python
   from django.urls import register_converter, path
   
   from . import converters, views
   
   register_converter(converters.FourDigitYearConverter, 'yyyy')
   
   urlpatterns = [
       path('articles/2003/', views.special_case_2003),
       path('articles/<yyyy:year>/', views.year_archive)
   ]
   ```

   

## 5、使用正则表达式 

​	使用正则表达式匹配路径，请使用 re_path()而不是path()

​	在Python正则表达式中，命名正则表达式组的语法是(?P\<name>pattern)，其中name是组的名称，并且 pattern是一些要匹配的模式

​	示例：

```python
from django.urls import path, re_path

from . import views

# url() 是 re_path 的别名，不推荐使用
urlpatterns = [
    path('articles/2003/', views.special_case_2003),
path('articles/<int:year>/', views.year_archive),
re_path(r'^articles/(?P<year>[0-9]{4})/$', views.year_archive),
    re_path(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', views.month_archive),
    re_path(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<slug>[\w-]+)/$', views.article_detail),
]

```

​	注意事项：

- 匹配的URL会受到一些限制。例如，年份10000将不再匹配，因为年份整数限制为四位数字
- 无论正则表达式匹配什么类型，每个捕获的参数都以字符串的形式发送到视图
- 除了命名的组语法，例如(?P\<year>[0-9]{4})，也可以使用较短的未命名组，例如([0-9]{4})，但是不建议这样使用，会引起未知的匹配

 

嵌套参数：

```python
from django.urls import re_path

urlpatterns = [
    # 不推荐, 匹配 blog/page-3/
    re_path(r'^blog/(page-(\d+)/)?$', blog_articles),
    # 推荐 ，匹配：comments/page-2/  路径到 comments(request, page_numer)
    re_path(r'^comments/(?:page-(?P<page_number>\d+)/)?$', comments),
]

```



## 6、使用默认值

​	URLConf中：

```python
from django.urls import path

from . import views

urlpatterns = [
    # http://127.0.0.1:8000/polls/blog/ 等同于 http://127.0.0.1:8000/polls/blog/1/
    path('blog/', views.page),
    # http://127.0.0.1:8000/polls/blog/1/
    # http://127.0.0.1:8000/polls/blog/10/
    # http://127.0.0.1:8000/polls/blog/99/
    path('blog/<int:num>/', views.page),
]


```

​	views中：

```python
def page(request, num=1):
    # 编写对应的业务逻辑
```



## 7、错误处理

- handler400- 状态码400
- handler403- 状态码403
- handler404- 状态码404
- handler500- 状态码500



1. 在 settings中修改配置：

   ```python
   DEBUG = False
   
   ALLOWED_HOSTS = ['*', ]
   ```

   

2. 在主应用的urls中配置：

   ```python
   # polls是子应用
   handler404 = "polls.views.page_not_found"
   ```

   

3. 在polls应用的views中添加函数page_not_found：

   ```python
   def page_not_found(request, exception):
       return HttpResponse('自定义的404错误页面')
   ```

   

##  8、引用其他URL调度器

1. 多个 patterns

   ```python
   from django.urls import include, path
   
   extra_patterns = [
       path('reports/', credit_views.report),
       path('reports/<int:id>/', credit_views.report),
       path('charge/', credit_views.charge),
   ]
   
   urlpatterns = [
       path('', main_views.homepage),
       path('help/', include('apps.help.urls')),
       path('credit/', include(extra_patterns)),
   ]
   
   ```

   

2. 使用include消除重复前缀

   ```python
   from django.urls import path
   from . import views
   
   urlpatterns = [
       path('<page_slug>-<page_id>/history/', views.history),
       path('<page_slug>-<page_id>/edit/', views.edit),
       path('<page_slug>-<page_id>/discuss/', views.discuss),
       path('<page_slug>-<page_id>/permissions/', views.permissions),
   ]
   
   # 修改为：
   from django.urls import include, path
   from . import views
   
   urlpatterns = [
       path('<page_slug>-<page_id>/', include([
           path('history/', views.history),
           path('edit/', views.edit),
           path('discuss/', views.discuss),
           path('permissions/', views.permissions),
       ])),
   ]
   
   ```

   

3. 传递捕获的参数

   在主urls中配置：

   ```python
   urlpatterns = [
       path('admin/', admin.site.urls),
       # 这里捕获username参数，类型为字符串
       path('<username>/polls/', include('polls.urls'))
   ]
   ```

   

   对应的 polls 应用下的urls中配置：

   ```python
   urlpatterns = [
       path('arg_test/', views.arg_test),
   ]
   ```

   

   对应的 polls 应用下的views中编写函数：

   ```python
   def arg_test(request, username):
       # 编写对应的业务逻辑
       pass
   ```



## 9、额外的参数

```python
from django.urls import path
from . import views

urlpatterns = [
    # 会传递给 views.year_archive(request, year=2005, foo='bar')
    path('blog/<int:year>/', views.year_archive, {'foo': 'bar'}),
]

```



## 10、URL反向解析 

url调度器除了从用户发起请求，到匹配对应的view，还能在python程序中调用进行匹配，通过 path或re_path 中 的name属性进行解析

- 在模板中，使用url模板标签
- 在Python代码中（主要是views），使用 reverse() 函数
- 在模型实例中，使用 get_absolute_url() 方法

 

示例：

urls中配置：

```python
from django.urls import path

from . import views

urlpatterns = [
    #...
    path('articles/<int:year>/', views.year_archive, name='news-year-archive'),
    #...
]
```



1. 在模板中

```python
# 模板中：
<a href="{% url 'news-year-archive' 2012 %}">2012 Archive</a>
{# Or with the year in a template context variable: #}
<ul>
{% for yearvar in year_list %}
<li><a href="{% url 'news-year-archive' yearvar %}">{{ yearvar }} Archive</a></li>
{% endfor %}
</ul>

```



2. 在python代码中

```python
from django.urls import reverse
from django.http import HttpResponseRedirect

def redirect_to_year(request):
    # ...
    year = 2006
    # ...
    return HttpResponseRedirect(reverse('news-year-archive', args=(year,)))

```



3. 在模型中：

```python
"""
    在模型中实现方法：
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('news-year-archive', args=[str(self.id)])

    然后在 模板 中如下使用：
"""
<a href="{{ object.get_absolute_url }}">{{ object.name }}</a>

```



## 11、命名空间

​	主要用于配合第 10 点 url反向解析 使用，多个不同的urls文件中可能配置同名的 name，那么为了进行区分，给不同的urls进行不同的命名，切记同一个项目下命名空间不能重复！

​	通过在 url调度器的模块中，定义 app_name = 'polls' 来命名

```python
from django.urls import path

from . import views
# 定义，一般命名空间和子应用名相同，便于记忆
app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    ...
]

# 调用，一旦有了命名空间，调用时就必须使用 polls： 前缀
reverse('polls:index', current_app=self.request.resolver_match.namespace)

```

 

​	命名空间可以进行嵌套：

```python
# 在 urls 中配置如下：
from django.urls import path

from . import views
# 定义命名空间，一般命名空间名和子应用名相同，便于记忆
app_name = 'polls'

extra_patterns = (
    [
        path('app_name/', views.app_name, name='app_name'),
    ],
    # 此处就是嵌套的命名空间
    'extra'
)

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('extra/', include(extra_patterns)),
    ...
]


# 在模板中使用：
<a href="{% url 'polls:extra:app_name' %}">点击链接</a>
```

