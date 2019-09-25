# 一、DebugToolBar

##1、概述

​	Django框架的调试工具栏使用django-debug-toolbar库，是一组可配置的面板，显示有关当前请求/响应的各种调试信息，点击时，显示有关面板内容的更多详细信息。

​	官方文档：https://django-debug-toolbar.readthedocs.io/en/latest/



## 2、应用

### 1.安装

```
pip install django-debug-toolbar==1.11
```

​	本文档使用版本：1.11



### 2.settings.py配置

​	先决条件：必须确认django.contrib.staticfiles 正确安装并且启用

```python
INSTALLED_APPS = [
    # ...
    'django.contrib.staticfiles',
    # ...
    'debug_toolbar',
]

STATIC_URL = '/static/'
```



### 3.urls.py路由

在主应用下的根urls.py中的最下面添加如下代码：

```python
from django.conf import settings

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
```

说明：

- 这里使用 '\__debug__' 作为路径访问，可以设置任意的路径名，只要能轻易区分一般应用
- 如果放在子应用的urls.py下的话，会抛出NoReverseMatch  'djdt' is not a registered namespace异常



### 4.启用中间件

调试工具栏主要在中间件中实现：

```python
MIDDLEWARE = [
    # ...
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    # ...
]
```

PS：这个中间件尽可能配置到最前面，但是，必须要要放在处理编码和响应内容的中间件后面，比如我们要是使用了GZipMiddleware，就要把DebugToolbarMiddleware放在GZipMiddleware后面



### 5.设置内部IP

调试工具栏只会允许特定的ip访问，在settings的INTERNAL_IPS中配置

```
INTERNAL_IPS = [
    '127.0.0.1',
]
```



### 6.访问

访问应用的任意页面，在页面的右上角会有一个 DJDT的悬浮窗

PS：如果访问的页面是如下编写的代码，则不会出现悬浮窗，因为内容中没有 body 标签

```python
def my_view(request):
	# ......
	return HttpResponse('欢迎学习')
```



### 7.面板功能

- Versions ：代表是哪个django版本
- Timer : 用来计时的，判断加载当前页面总共花的时间
- Settings : 读取django中的配置信息
- Headers : 当前请求头和响应头信息
- Request: 当前请求的相关信息（视图函数，Cookie信息，Session信息等）
- SQL:查看当前界面执行的SQL语句
- StaticFiles：当前界面加载的静态文件
- Templates:当前界面用的模板

- Cache：缓存信息

- Signals：信号

- Logging：当前界面日志信息

- Redirects：当前界面的重定向信息



### 8.面板配置

django-debug-toolbar默认使用全面板，见第7点，

默认的全局配置在 debug_toolbar.settings.CONFIG_DEFAULTS

默认的面板配置在 debug_toolbar.settings.PANELS_DEFAULTS

```python
PANELS_DEFAULTS = [
    "debug_toolbar.panels.versions.VersionsPanel",
    "debug_toolbar.panels.timer.TimerPanel",
    "debug_toolbar.panels.settings.SettingsPanel",
    "debug_toolbar.panels.headers.HeadersPanel",
    "debug_toolbar.panels.request.RequestPanel",
    "debug_toolbar.panels.sql.SQLPanel",
    "debug_toolbar.panels.staticfiles.StaticFilesPanel",
    "debug_toolbar.panels.templates.TemplatesPanel",
    "debug_toolbar.panels.cache.CachePanel",
    "debug_toolbar.panels.signals.SignalsPanel",
    "debug_toolbar.panels.logging.LoggingPanel",
    "debug_toolbar.panels.redirects.RedirectsPanel",
]
```

如果不使用默认的全功能面板，那么在settings中配置 DEBUG_TOOLBAR_PANELS 即可，示例如下：

```
DEBUG_TOOLBAR_PANELS = [
    "debug_toolbar.panels.timer.TimerPanel",
    "debug_toolbar.panels.headers.HeadersPanel",
    "debug_toolbar.panels.request.RequestPanel",
    "debug_toolbar.panels.templates.TemplatesPanel",
]
```

说明：

- 当前只启用了4个面板：时间、头信息、请求信息和模板信息
- 可以添加默认配置中没有的面板，例如：ProfilingPanel

- 可以添加自定义面板
- 可以删除默认内置面板
- 可以改变面板的顺序



### 9.工具栏配置

在settings中配置 DEBUG_TOOLBAR_CONFIG 覆盖默认配置，分为2部分，一部分适用于工具栏本身，另一部分适用于某些特定面板

```python
DEBUG_TOOLBAR_CONFIG = {
    # Toolbar options
    "DISABLE_PANELS": {"debug_toolbar.panels.redirects.RedirectsPanel"},
    "INSERT_BEFORE": "</body>",
    "RENDER_PANELS": None,
    "RESULTS_CACHE_SIZE": 10,
    "ROOT_TAG_EXTRA_ATTRS": "",
    "SHOW_COLLAPSED": False,
    "SHOW_TOOLBAR_CALLBACK": "debug_toolbar.middleware.show_toolbar",
    # Panel options
    "EXTRA_SIGNALS": [],
    "ENABLE_STACKTRACES": True,
    "HIDE_IN_STACKTRACES": (
        "socketserver" if six.PY3 else "SocketServer",
        "threading",
        "wsgiref",
        "debug_toolbar",
        "django.db",
        "django.core.handlers",
        "django.core.servers",
        "django.utils.decorators",
        "django.utils.deprecation",
        "django.utils.functional",
    ),
    "PROFILER_MAX_DEPTH": 10,
    "SHOW_TEMPLATE_CONTEXT": True,
    "SKIP_TEMPLATE_PREFIXES": ("django/forms/widgets/", "admin/widgets/"),
    "SQL_WARNING_THRESHOLD": 500,  # milliseconds
}
```

#### 工具栏选项

- `DISABLE_PANELS`

  默认： `{'debug_toolbar.panels.redirects.RedirectsPanel'}`

  此设置是要禁用（但仍显示）的面板的完整Python路径的集合。

- `INSERT_BEFORE`

  默认： `'</body>'`

  工具栏在HTML中搜索此字符串并在之前插入。

- `RENDER_PANELS`

  默认： `None`

  如果设置为`False`，调试工具栏将把面板的内容保留在服务器上的内存中并按需加载它们。如果设置为`True`，则会在每个页面内呈现面板。这可能会降低页面呈现速度，但在多进程服务器上需要这样做，例如，如果在生产中部署工具栏（不建议这样做）。

  默认值`None`告诉工具栏自动执行正确的操作，具体取决于WSGI容器是否运行多个进程。此设置允许您在需要时强制执行不同的操作。

- `RESULTS_CACHE_SIZE`

  默认： `10`

  工具栏在内存中保持的结果缓存数量。

- `ROOT_TAG_EXTRA_ATTRS`

  默认： `''`

  此设置将注入根模板div中，以避免与客户端框架发生冲突。例如，将调试工具栏与Angular.js一起使用时，将其设置为`'ng-non-bindable'`或 `'class="ng-non-bindable"'`。

- `SHOW_COLLAPSED`

  默认： `False`

  如果更改为`True`，则默认情况下将折叠工具栏。

- `SHOW_TOOLBAR_CALLBACK`

  默认： `'debug_toolbar.middleware.show_toolbar'`

  这是用于确定工具栏是否应显示的函数路径，默认检测DEBUG设置为True，并且访问IP必须在INTERNAL_IPS中，代码如下：

  ```python
  def show_toolbar(request):
      """
      Default function to determine whether to show the toolbar on a given page.
      """
      if request.META.get("REMOTE_ADDR", None) not in settings.INTERNAL_IPS:
          return False
  
      return bool(settings.DEBUG)
  ```

  可以设置自定义的检测函数路径

  

#### 面板选项

- `EXTRA_SIGNALS`

  默认： `[]`

  面板：信号

  可能在项目中的自定义信号列表，定义为信号的Python路径。

- `ENABLE_STACKTRACES`

  默认： `True`

  面板：缓存，SQL

  如果设置为`True`，则将显示SQL查询和缓存调用的堆栈跟踪。启用堆栈跟踪会增加执行查询时使用的CPU时间。

- `HIDE_IN_STACKTRACES`

  默认值：('socketserver', 'threading', 'wsgiref', 'debug_toolbar', 'django')`

  面板：缓存，SQL

  用于消除与服务器相关的堆栈跟踪，这可能导致巨大的DOM结构和工具栏渲染延迟。

- `PROFILER_MAX_DEPTH`

  默认： `10`

  面板：剖析

  此设置会影响分析器分析中的函数调用深度。

- `SHOW_TEMPLATE_CONTEXT`

  默认： `True`

  面板：模板

  如果设置为`True`则模板的上下文将包含在模板调试面板中。如果项目中拥有大型模板上下文，或者具有不希望被评估的惰性数据结构的模板上下文，则关闭此选项非常有用。

- `SKIP_TEMPLATE_PREFIXES`

  默认： `('django/forms/widgets/', 'admin/widgets/')`

  面板：模板

  收集渲染的模板和上下文时，将跳过以这些字符串开头的模板。默认情况下会跳过基于模板的表单小部件，因为面板的HTML可以轻松地增长到数百兆字节，包含许多表单字段和许多选项。

- `SQL_WARNING_THRESHOLD`

  默认： `500`

  面板：SQL

  SQL面板突出显示执行时间超过这段时间（以毫秒为单位）的查询

