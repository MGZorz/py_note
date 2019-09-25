# 一、django配置

## 1、整体介绍

django项目创建后，在主应用中，会有一个settings.py文件，这个就是该项目的配置文件

- settings文件包含Django安装的所有配置
- settings文件是一个包含模块级变量的python模块，所以该模块本身必须符合python规则，并且可以使用python的语法
- settings中的所有配置项的key必须全部大写
- settings中每一个配置项都有默认值，默认配置内容在django/conf/global_settings.py中可以查看到，项目中不需要导入该模块，django框架会自动获取
- settings中可以添加自定义的配置项



## 2、应用settings文件

1. manage.py启动

   默认在manage.py中配置：

   ```python
   if __name__ == "__main__":
       os.environ.setdefault("DJANGO_SETTINGS_MODULE", "firstdjangopycharm.settings")
   
   ```

   

2. 手动指定配置文件位置

   cmd命令启动如下：

   ```
   python manage.py runserver 0.0.0.0:8000 --settings=firstdjangopycharm.settings
   ```

   

3. 服务器部署启动

   在wsgi.py中配置：

   ```python
   os.environ.setdefault("DJANGO_SETTINGS_MODULE", "firstdjangopycharm.settings")
   ```

   

## 3、常用配置项

```python
import os


"""
    当前文件所在文件夹的上一级目录的绝对路径
    切记2个 os.path.dirname
"""
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

"""
    用于加密session，一个随机的字符串
    这样生成：
    from django.core.management import utils
    utils.get_random_secret_key()
"""
SECRET_KEY = '=*f&bx760nyar7@8lb8!w$9h(3ea6p3apl$iua!td1q%-u5r4='

# 调试模式，可以看到错误的所有相信信息，部署时一定要修改为False
DEBUG = True

"""
    允许访问的域名设置
    开发环境不用理会
    运行环境，配置 DEBUG = False后，
    如果允许所有域名访问，则设置 ALLOW_HOSTS = ['*']
    如果指定某些域名可以访问，则设置 ALLOW_HOSTS = ['*.baidu.com']
"""
ALLOWED_HOSTS = []


"""
    应用的配置，
    如：'polls.apps.PollsConfig'
    如果没有 PollsConfig ，那么可以配置为  'polls'
"""
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles', # 只有 DEBUG = Ture 才有效
    
    'polls'  # 子应用必须配置，否则不起作用
]

"""
    中间层配置
    自己编写的 中间层 需要配置在最后
    譬如：
    mymidlle.md.TestMiddleware
"""
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

# 配置基础的urls
ROOT_URLCONF = 'firstdjangopycharm.urls'

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

# 服务器部署的WSGI配置
WSGI_APPLICATION = 'firstdjangopycharm.wsgi.application'


"""
    数据库配置
    mysql在python3的使用，需要在 __init__.py 中加入以下代码：
    import pymysql

    pymysql.install_as_MySQLdb()
"""
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_test1',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}


"""
    用户密码验证
"""
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# 语言选择 ， zh-Hans 为中文
LANGUAGE_CODE = 'en-us'

# 时区 Asia/Shanghai 是中国时区
TIME_ZONE = 'UTC'

# 国际化
USE_I18N = True

# 本地化
USE_L10N = True

# 使用时区，配套TIME_ZONE使用，必须设置为 False
USE_TZ = False

"""
    静态文件的路径，默认是 static
    如果在各自项目的static目录以外，还有目录存放静态文件，需要添加如下属性：
    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, "common_static1"),
        '/var/www/static/',
    )
"""
STATIC_URL = '/static/'

```



## 4、程序中获取settings中的配置项

​	如果在项目代码中需要获取settings中的配置项，这样获取：

```python
# 切记不要导入具体的settings模块的路径，会形成高耦合
# 这样的方式是不可取的：from mysite import settings
from django.conf import settings

d = settings.DEBUG

```



## 