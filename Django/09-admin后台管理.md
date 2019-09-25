# 一、admin后台管理

​	Django框架提供了一个自动化后台管理功能，对网站数据的后台维护，仅仅需要进行非常简单的配置和编写极少的代码即可实现。



## 1、配置

settings.py中：

```python
INSTALLED_APPS = [
    'django.contrib.admin',
]
```



如果需要实现后台管理的中文显示，则修改以下配置：

```python
LANGUAGE_CODE = 'zh-Hans'
USE_I18N = True
```



## 2、URL路由

​	urls.py中：

```python
urlpatterns = [
    path('admin/', admin.site.urls),
]
```



## 3、创建管理员账户

​	创建管理员账户之前，确保项目的数据库已经正确连接，并且已经将admin应用的模型进行了迁移

​	另外，如果settings中配置了 AUTH_PASSWORD_VALIDATORS，那么会对用户名和密码进行对应的检测，譬如：不能太简单，不能是纯数字等

​	

1. 项目根目录下 cmd 命令窗口运行以下命令：

```
python manage.py createsuperuser
```

 

2. 输入 用户名 并按回车：

```
Username: admin
```

 

3. 提示 电子邮件地址：

```
Email address: admin@example.com
```

 

4. 最后一步是输入密码，将被要求输入两次密码，第二次作为第一次确认：

```
Password: **********

Password (again): *********

Superuser created successfully.
```



## 4、基本模型管理

### 1、建立模型

​	在model.py中：

```python
class Student(models.Model):

    name = models.CharField(max_length=20)
    age = models.IntegerField()
```



### 2、添加模型管理

​	在admin.py中：

```python
from django.contrib import admin

from .models import Student

admin.site.register(Student)

```



### 3、在浏览器中访问

​	访问path为  /admin， 譬如：<http://127.0.0.1:8000/admin> 



### 4、进一步完善显示

```python
class Student(models.Model):
	
    # 增加 verbose_name
    name = models.CharField(max_length=20, verbose_name='姓名')
    # 增加 help_text
    age = models.IntegerField(help_text='大于18', verbose_name='年龄')

    # 增加 Meta 类
    class Meta:
	    # verbose_name_plural ： 复数形式
        verbose_name_plural = verbose_name = '学生'

    # 模型类的 字符串化
    def __str__(self):
        return f'{self.name}({self.pk})'
```

​	在 子应用下的 apps.py中：

```python
class TestAppConfig(AppConfig):

    verbose_name = '子应用名'
```



### 5、特殊下拉属性管理

```python
class Student(models.Model):
	
    SEX_CHOICES = ((1,'男')), (2, '女')
    
    # 增加 verbose_name
    name = models.CharField(max_length=20, verbose_name='姓名')
    # 增加 help_text
    age = models.IntegerField(help_text='大于18', verbose_name='年龄')
	
    # 修改已有模型，增加新字段的话，都需要设置默认值或者设置 null=True
    sex = models.IntegerField(choices=SEX_CHOICES, default=1， verbose_name='性别')
    
    # 增加 Meta 类
    class Meta:
	    # verbose_name_plural ： 复数形式
        verbose_name_plural = verbose_name = '学生'

    # 模型类的 字符串化
    def __str__(self):
        return f'{self.name}({self.pk})'
```



## 5、关系模型管理

### 1、建立模型

```python
class Place(models.Model):
    name = models.CharField(max_length=50, verbose_name='地名')
    address = models.CharField(max_length=80, verbose_name='门牌')

    def __str__(self):
        return f'{self.name}-{self.address}'

    class Meta:

        verbose_name_plural = verbose_name = '地址'

class Restaurant(models.Model):
    place = models.OneToOneField(
        Place,
        on_delete=models.CASCADE,
        primary_key=True,
        verbose_name='地址'
    )

    name = models.CharField(max_length=50, verbose_name='名字')
    # BooleanField 在数据库使用 tinyint 类型
    serves_hot_dogs = models.BooleanField(default=False, verbose_name='经营热狗')
    serves_pizza = models.BooleanField(default=False, verbose_name='经营披萨')

    def __str__(self):
        return self.name

    class Meta:

        verbose_name_plural = verbose_name = '餐馆'

class Waiter(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, verbose_name='餐馆')
    name = models.CharField(max_length=50, verbose_name='姓名')

    def __str__(self):
        return self.name

    class Meta:

        verbose_name_plural = verbose_name = '服务员'

class SchoolClass(models.Model):
    name = models.CharField(max_length=20, verbose_name='班级名')

    class Meta:

        verbose_name_plural = verbose_name = '班级'

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=10, verbose_name='姓名')
    school_class = models.ManyToManyField(SchoolClass, verbose_name='班级')

    class Meta:

        verbose_name_plural = verbose_name = '老师'

    def __str__(self):
        return self.name
```



### 2、添加模型管理

```python
admin.site.register(Place)
admin.site.register(Restaurant)
admin.site.register(Waiter)
admin.site.register(Teacher)
admin.site.register(SchoolClass)
```



## 6、自定义模型管理类

​	之前使用的 admin.site.register(Student) 是用的 Django 默认的管理类，也可以自定义：

```python
class StudentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Student, StudentAdmin)
```



​	自定义管理类的属性：

```python
class StudentAdmin(admin.ModelAdmin):
	
    # 显示的属性列表， 值是 属性名
    list_display = ['name', 'age']
    # 排序的 属性 列表 ， 默认是升序，如果需要降序：['-age']
    ordering = ['age']

admin.site.register(Student, StudentAdmin)
```



​	使用装饰器注册：

```python
# 该装饰器使用的是 admin.register ， 不是 admin.site.register
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
	
    list_display = ['name', 'age']
    ordering = ['age']
```



​	自定义模型管理类的属性：

```python
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    
    # 属性为空时，在网页上显示的内容，默认是： -
    empty_value_display = '-empty-'
    # 管理的字段， 和 exclude冲突
    fields = ('name',)
    # 不管理的字段，和 fields冲突
    exclude = ('age',)
```



​	多对多关系，默认是 select多选框，一般使用 filter_horizontal 或者 filter_vertical

```python
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):

    ordering = ('name', )

    filter_horizontal = ('school_class', )
```



## 7、增加额外批量操作

​	在admin.py中：

1. 动作函数是单独的模块函数：

```python
# 定义动作函数
def age_add_one(modeladmin, request, queryset):
    queryset.update(age=F('age')+1)
# 给动作函数添加描述
age_add_one.short_description = "年龄增加一岁"

class StudentAdmin(admin.ModelAdmin):
    # 在当前自定义管理类中，添加新的动作：age_add_one
    actions = [age_add_one]

admin.site.register(Student, StudentAdmin)
```



2. 动作函数写在自定义管理类中作为一个方法：

```python
class StudentAdmin(admin.ModelAdmin):
    # 这里必须是函数名的字符串
    actions = ['age_add_one']
	
    # 类方法也同样是3个参数！
    def age_add_one(modeladmin, request, queryset):
        queryset.update(age=F('age') + 1)

    age_add_one.short_description = "年龄增加一岁"

admin.site.register(Student, StudentAdmin)
```



## 8、覆盖admin默认模板

​	如果我们要在admin管理页面中，增加自己的功能，那么我们需要覆盖admin的默认模板，通过以下步骤实现：



### 1、admin允许覆盖的页面

- app_index.html
- change_form.html
- change_list.html
- delete_confirmation.html
- object_history.html
- popup_response.html



### 2、admin管理模板目录

​	django库下的 contrib/admin/templates/admin 目录，可以查看django自带的所有模板



### 3、自定义模板

​	需要修改admin的哪个内置模板，则继承哪个模板，并且在其基础上进行修改，我们以app_index.html为例：

​	原始模板是：

```django
{% extends "admin/index.html" %}
{% load i18n %}

{% block bodyclass %}{{ block.super }} app-{{ app_label }}{% endblock %}

{% if not is_popup %}
{% block breadcrumbs %}
<div class="breadcrumbs">
<a href="{% url 'admin:index' %}">{% trans 'Home' %}</a>
&rsaquo;
{% for app in app_list %}
{{ app.name }}
{% endfor %}
</div>
{% endblock %}
{% endif %}

{% block sidebar %}{% endblock %}

```



### 4、建立对应模板

​	在settings中配置的templates目录下，建立admin目录，并且在admin目录下，建立mysite目录（mysite是你的应用名，假设mysite是children，那么目录结构如下图）

![](.\imgs\admin_customize_templates.png)



​	我们不需要修改原始模板所有的block，只需要在我们要添加功能的地方，进行继承，并且修改就行了，如下： 

```python
{% extends "admin/app_index.html" %}

{% block sidebar %}
    <a href="{% url 'children:customize' %}">自定义功能页面</a>
{% endblock %}

```



### 5、修改 urls

```python
path('customize/', views.customize, name='customize'),
```



### 6、修改 views

```python
def customize(request):
    
    """
        编写你自己的自定义管理功能
    :param request: 
    :return: 
    """
    
    return redirect('/admin/children/')

```

