# 生成器和装饰器相关内容

## 一、生成器与列表的对照使用

### 什么是生成器？（genterator）

​	genterator:**记录一个算法，可以一边计算一边循环的一种机制**

### 生成器有什么用？

​	假如存储1-10000中所有的偶数

1. #### list

   ```python
   list1= []
   for i in range(2,10001,2):
       list1.append(i)
   print(list1)
   ```

   **列表推导公式:**

   ```python
   list1=[x for x in range(10)]
   print(list1)
   list2= [x for x in range(12) if x % 2 == 0]
   print(list2)
   list3 = [a+b for a in '123' for b in 'XYZ'] 
   # 上述list3在编写代码的过程中不提倡，意图性太差。
   print(list3)
   ```

2. #### 使用生成器

   存储数据（存数的算法）

   ##### 创建生成器：

   - g = （x for x in range(10)） 把列表的方括号变为圆括号。

     `g1 = (x for x in range(2,100,2))`

   - 在函数中用**yield**关键字转变。

     ```python
     def test():
         for x in range(5):
             yield x 
             pass
     f = test()
     print(next(f))
     ```

   ##### 生成器中元素访问：

   **如果超出生成器生成数据的范围，会报错：StopIteration**

   1. next()   
      `print(next(g))`

   2. for 循环遍历

      ```python
      for i in g :  
      	print(i)
      ```

   3. `print(g.__next__())`

   4. `print(g.send(None))` 
      使用send()访问的时候，首个参数必须为None，之后的参数可以随意给。

   

### 使用生成器的好处？

​	更省时间、更省内存。

​	列表方法所消耗时间：

```python
# 时间模块
import time
# sys系统模块
import sys
# 获取CPU开始计算的时间
time.clock()
# 简单的列表推导式
list2 = [x for x in range(2,100,2) ]
# CPU工作的时长
costTime = time.clock()
print('创建列表耗时：%g'%costTime)
print('创建列表内存开销：%d'%sys.getsizeof(list2))
```

​	生成器所用时：

```python
time.clock()
g1 = (x for x in range(2,100,2))
costTime = time.clock()
print('创建列表耗时：%g'%costTime)
print('创建列表内存开销：%d'%sys.getsizeof(g1))
```

## 二、迭代器

​	**能被next()访问，并不断返回下一个值的对象。**

### 	可迭代性（Iterable）

```python
# 实用举例
from collections.abc import Iterable
num = 100
#使用`isinstance(对象,类)`来判断对象是否为目标类。
if isinstance(num ,Iterable):
  for i in num:
    print(i)
else:
  print('num不具有可迭代性')
```

1.  **集合类元素**
    `list,str,dict,tuple`

    ```python
    #  检验：（以元组举例）
    tuple1 = (1,2,3)
    print(isinstance(tuple1,Iterable))
    ```

2.  **生成器**

    ```python
    # genterator
    g = (x for x in rang(5))
    print(type(g))
    print(isinstance(g,Iterable))
    ```

### 	迭代器 （Iterator）

​	具备可迭代性的元素，就一定是迭代器么？**不一定的！！**

```python
import collection.abd import Iterator
if isinstance(list1,Iterator):
    print('list是迭代器')
else:
    print('不是')
```

### Iter()函数

​	可以让具备可迭代性的对象变成迭代器。`list1 = iter(list1)`



## 三、闭包*

### 	什么是闭包？

​		本质上就是个**函数**，但是有点特殊。特殊在创建闭包方面。

​		**要注意的一点，就是Python中的函数是可以像普通变量一样当做参数传递给下一个函数的。举个栗子！**

![1557823618257](E:\python_document\notes\assets\1557823618257.png)



### 	如何创建闭包？

1.  嵌套函数定义（外部函数、内部函数）（一般为两层）
2.  内部函数使用外部函数定义的变量
3.  外部函数一定要有返回值，返回内部函数名。

### 	如何使用闭包？

```python
# 创建闭包，需求：求两个数之和
def funout(num1):
  def funin(num2):
    # 注意：仅限于使用不限于修改，否则会以为内部函数又定义了一个num1变量。或者用nonlocal声明。
    		# 声明以下为外部变量
    		#	nonlocal num1
    # num1 += 1
    return num1 + num2
  return funin
a = 10 
b =100
f = funout(a)
result = f(b)
print(result)
```

### 	应用举例：使用闭包完成求两点之间距离

分析：两点距离公式为
$$
|d| = \sqrt{(a^2-c^2)+(b^2+d^2)}
$$

```python
# 方法一：普通函数
def getDis(x1,y1,x2,y2):
    # 求两点之间距离
    return math.sqrt((x1-x2)**2 +(y1-y2)**2)
#方法二：闭包
def getDisout(x1,y1):
    def getDisin(x2,y2):
        return math.sqrt((x1-x2)**2 +(y1-y2)**2)
    return getDisin
  
dis = getDis(0,0,10,10)
print('(10,10)距离原点的距离为：%g'%dis)
'''-------------------------------------'''
getDisIn = getDisout(0,0)
dis1 = getDisIn(10,10)
print('(10,10)距离原点的距离为：%g'%dis1)
```

### 闭包的特殊用途

​	可以**在不修改现有功能源码的前提下，增加新的功能**，比如权限认证（在下载之前，会验证当前的账户是否为付费会员），还有日志功能，以日志功能为例子（统计访问时间，访问功能，写到日志文件中）。

```python
import time
# 定义一个记录日志的函数：将访问事件以及访问的函数名写入到文件中（log.txt）
def write(fun):
    try:
        file = open('log.txt','a',encoding='utf-8')
        # 写入相关数据（访问的函数名，范文的事件）
        file.write(fun.__name__)
        file.write('\t')
        # 写入访问时间
        file.write(time.asctime())
        file.write('\t')
    except Exception as e :
        print(e.args)
    finally:
        # 关闭文件
        file.close()
# 闭包
def funout(fun):
    def funin():
        # 新增功能
        write(fun)
        fun()
    return funin  
# 这是不能动的功能。
def fun1():
    print('功能1')
def fun2():
    print('功能2')
# 闭包的调用，注意区别两个fun1的区别！！！
fun1 = funout(fun1)
fun2 = funout(fun2)
# 然后是正常的调用函数
fun1()
fun2()
```

**上述代码相关注释**：

1.  open(name[, mode[, buffering]])，用于打开或者创建一个文件。

    -   name:文件名。
    -   mode：打开的模式（只读，写入，追加等）。
    -   buffering：这个决定文件会不会被寄存。

    详细用法见<https://www.runoob.com/python/python-func-open.html>

2.  time.asctime()返回一个可读形式为:Tue Dec 11 18:07:14 2008（2008年12月11日 周二18时07分14秒）的时间字符串

在编写功能中有一个**开闭原则**：

-   开放：添加功能
-   关闭：修改源代码，也就是在编写新功能的时候尽量不要去动别人的源代码。



## 四、装饰器

​	和闭包息息相关，结合起来可以让访问更简单。

### 	装饰器运用

​	刚才的代码可以用装饰器更加简单的调用。

```python
# 闭包
def funout(fun):
    def funin():
        # 新增功能
        write(fun)
        fun()
    return funin

# 注意装饰器出现~
@funout
def fun1():
    print('功能1')
@funout
def fun2():
    print('功能2')
    
# 调用的时候就不用这么麻烦了
# fun1 = funout(fun1)
# fun2 = funout(fun2)
# 然后是正常的调用函数
fun1()
fun2()
```

### 	装饰器是什么？

​	举个很污的例子来解释下装饰器。

>   每个人都有的内裤主要功能是用来遮羞，但是到了冬天它没法为我们防风御寒，咋办？我们想到的一个办法就是把内裤改造一下，让它变得更厚更长，这样一来，它不仅有遮羞功能，还能提供保暖，不过有个问题，这个内裤被我们改造成了长裤后，虽然还有遮羞功能，但本质上它不再是一条真正的内裤了。于是聪明的人们发明长裤，在不影响内裤的前提下，直接把长裤套在了内裤外面，这样内裤还是内裤，有了长裤后宝宝再也不冷了。**装饰器就像我们这里说的长裤，在不影响内裤作用的前提下，给我们的身子提供了保暖的功效。**

​	

### 	多重装饰器

 	如果函数允许多重装饰的话，那么在装饰的顺序是很严格的！**离得近的先执行，离得远的后执行**，举个栗子~

```python
# 需求：$《红楼梦》$ 先加书名后加doller
# 闭包1
def funcOut(func):
    def funcIn():
        return '《'+func()+'》'
    return funcIn
 # 闭包2
def funcOut2(func):
    def funcIn():
        return '$'+func()+'$'
    return funcIn
# 装饰器2（后执行）
@funcOut2
# 装饰器1（先执行）
@funcOut
def bookName():
    return '红楼梦'
print(bookName())
```

### 指定参数个数的装饰器

​	说白了就是，目标的函数里面有几个参数，那么闭包的内函数就要有几个参数。

```python
# 打酱油的新增功能？
def addfunc():
    print('我是新增功能')
# 我是闭包，这次我有三个孩子。
def funcOut(func):
    def funcIn(x,y,z):
        # 新增功能
        addfunc()
        func(x,y,z)
    return funcIn
# 装饰器就是在下
@funcOut
# 我是函数，我给你三个种，一个也不能给我丢了！！
def test(a,b,c):
    print('a=%g,b=%g,c=%g'%(a,b,c))
test(1,2,3)
```

### 通用装饰器（*args,**kwargs）

​	既然多个参数的目标函数要重新创建一个闭包，那么有没有一个闭包，可以任意个参数呢？当当当~通用装饰器登场！！！

```python
def funcOut(func):
  # 要注意啦~(*args,**kwargs)这是任意参数的意思，要记下来哦~
    def funcIn(*args,**kwargs):
        # 新功能
        print('新功能俺有回来了')
        return func(*args,**kwargs)
    return funcIn
@funcOut
def func1(a,b,c):
    print(a+b+c)
@funcOut
def func2(a,b):
    print(a+b)

func1(1,2,3)
func2(5,6)
```



### 五、Python动态添加属性（对象属性、类属性）

#### Python是什么语言？

-   动态语言：
    程序在运行的时候，可以改变其结构，比如添加属性、添加方法、删除函数等等。

-   强类型语言：
    也叫强类型定义语言，变量的类型在运行时候决定，变量的类型在运行之后是不需要强制转换的。

    

    ##### 动态语言

下面就用简单的代码来实现动态语言的相关特征。

###### 	添加对象属性

```python
# 添加对象属性。
class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age
p1 = Person('学生1',20)
#	添加对象属性方法1：
p1.address ='北京'
#	添加对象属性方法2：
setattr(p1,'gender','女')
#	运行方式1：
print('姓名为：%s,年龄为：%d,性别：%s,地址为：%s'%(p1.name,p1.age,p1.gender,p1.address))
#	运行方式2：
print('姓名为：%s,年龄为：%d,性别：%s,地址为：%s'%(p1.name,p1.age,getattr(p1,'gender'),p1.address))
```

>   总结（添加对象属性）：
>
>   -   添加属性：
>       1.  对象名.属性名 = 值
>       2.  setatter(对象名，属性名，值)
>   -   输出运行方式:
>       1.  对象名.属性名
>       2.  getattr(对象名,属性名)

要注意的是：给对象添加对象属性都是指向性的（给谁添加谁就有，其他的没有）涉及到栈内存和堆内存，见下图。

![1557886765750](E:\python_document\notes\assets\1557886765750.png)



###### 	添加类属性

```python
#  添加类属性（类名.类属性 = 值）
Person.CLS_ID = 110
print(p1.CLS_ID)
print(p2.CLS_ID)
```

###### 	添加对象方法（实例方法、成员方法）

添加对象方法，要借助一个模块（types）中的MethodType方法。**MethodType（函数名，变量）**

```python
# 导入types模块
import types
class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age
def study(self):
    print('学习使我快乐，一天不写代码，难受')
p1 = Person('学生1',18)
# 添加成员方法
p1.study = types.MethodType(study,p1)
p1.study()
```

**注意**：添加后的方法，只能给p1调用，其他对象不可以调用。

###### 	添加静态方法

静态方法就是不需要传递参数的方法，且有一个标志：**@staticmethod**，下面给类添加静态方法的代码。

```python
# 添加静态方法
@staticmethod
def teststaticmetod():
    print('我是静态方法')
# 给类添加静态方法 (类名.静态方法名 = 定义的函数名)
Person.method1 = teststaticmetod
# 静态方法的调用 （对象名.静态方法名，或者类名.静态方法名（后者用的较多））
p1.method1()
Person.method1()
```

###### 	添加类方法

类方法一般就是指在类中定义的方法，不过也可以后来添加，也有一个标志：**@classmethod**，下面给类加类方法的代码。

```python
# 我是后添加的类方法
@classmethod
def testClsmethod(cls): 
  	# 类方法一定要有一个参数哦~
    print('我是类方法')
# 添加类方法 (类名.类方法名 = 定义的函数名)
Person.method2 = testClsmethod
# 访问类方法（对象名.类方法名，或者类名.类方法名（后者用的较多））
Person.method2()
p1.method2()
```

添加对象方法、静态函数、类方法的原理是基本一致的。不过要注意的是**后边是定义的函数名，而不是定义的函数名（）**

###### 	slots的作用

```
正确的用法是__slots__
```

1.  只对类对象进行限制，不对类进行限制；
2.  不仅限制类对象的属性，还限制类对象的方法；
3.  仅对当前的类起作用，对继承的子类不起作用；

# 函数式编程

## range的使用

​	range()可以创建一个整数的列表，多数用在for循环中，一般是有两种格式：

>   range(stop)	默认从0开始，直到stop-1结束。
>
>   range(start[,stop,step])	以start开始，stop结束（但是不包括stop），step是迭代的步长（隔几输出一个数）

但是要注意的是，**当start比stop小的时候，必须要把迭代的步长写上去！！**

## functools之偏函数partial的使用

​	是用于对函数固定属性的函数，也就是说把其他函数的参数给固定住的函数。

>   **作用**：
>
>   把一个函数的某些参数给固定住（也就是设置一个默认值），在返回一个新的函数，调用这个新函数会更简单

​	应用举例：

```python
# 把一串二进制的数字转化为十进制的数
# 传统方法：
str1 = '1010'
result = int(str1,2)
print(result)
# 利用偏函数：
from functools import partial
int2 = partial(int,base =2)
# 上述是构造了一个偏函数，应用的时候直接调用就ok了。
print(int2('1010'))
```

## functools之wraps的使用

​	wraps()一般是结合闭包来使用的，加闭包那么原函数的一些信息必定会有损失，那么wraps()作用是**可以将原函数对象的指定属性复制给包装函数对象，默认属性有module、name（函数名）、doc（函数的注释），或者通过参数选择。**举个栗子~

```python
# 导入wraps函数
from functools import  wraps
# 创建一个闭包
def funcOut(func):
  	# 有wraps和没有wrap功能的区别
    @wraps(func)
    def funcIn(*args,**kwargs):
        '''我就是闭包'''
        print('%s was calling'%func.__name__)
        return func(*args,**kwargs)
    return funcIn
# 闭包的装饰器
@funcOut
def test(x):
    '''求X*X的值'''
    return x * x
# 程序的入口
print(test.__name__)
print(test.__doc__)
'''
没有@wraps(func)的情况：	funcIn	我就是闭包
有@wraps(func)的情况：	test	求X*X的值
'''
```

## functools之reduce的使用

>   ​	reduce(function, iterable[, initializer])

reduce()会对参数序列（可迭代的哦）中的元素进行累计，先用function对第1、2个进行操作，得到结果再与第三个数据用function操作，依次往后推~

```python
'''需求：	随机生成5个数字，在对这5个数字求和运算'''
'''传统方法'''
import random 
list1 = []
for i in range(5):
  	rand_num = random.randint(1,100)
    list1.append(i)
sum = 0
for i in list1:
  	sum += i
print('和为：%g'%(sum))
'''利用reduce（）外加lambda匿名函数'''
from functools import reduce 
'''构建随机数列表和传统方法一样，就不赘述了'''
result = reduce(lambda x,y:x+y ,list1)
print('和为：%g'%(result))
```

## 内建函数之map的使用

>   ​	map(function , Iiterable,…)

第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。说白了就是**用函数挨个调用后面的可迭代性模块，并且生成一个迭代器**（python2中是生成列表）。

```python
'''导入迭代器（检查模块）'''
from collections.abc import Iterator
'''两个可迭代模块'''
list1 = [1,2,3]
list2 = [4,5,6,7]
'''目标函数'''
def func1(x):
    return x * 2
def func2(x,y):
    return x*y
'''生成一个迭代器（单个可迭代模块情况）'''
it1 = map(func1,list1)
'''（多个可迭代模块情况）会以小的为基准，类似水桶原理。'''
it2 = map (func2,list1,list2)
'''检验下是不是迭代器'''
print(isinstance(it1,Iterator))
'''开始迭代'''
for i in it1:
    print(i ,end=' ')
for i in it2:
    print(i,end=' ')
'''可以省去目标函数那个环节，直接使用lambda匿名函数也能达到相应的效果'''
#	lambda匿名函数：lambda 参数：表达式
it3 = map(lambda x,y:x*y,list1,list2)
for i in it3:
    print(i,end=' ')
```

## 内建函数之filter的使用

>   filter( function or None，Iterable)

filter()可以理解为一个过滤器，先给它一个函数和一个可迭代模块，如果符合True就存放在迭代器里面，不符合Flase就过滤掉了。

```python
'''需求：筛选出列表list1中大于5的元素，并且打印出来'''
list1 = [1,5,8,3,7,9,2,10]
'''传统方式'''
for i in list1 :
  	if i >5:
      print(i,end=' ')
'''利用reduce()和lambda匿名函数'''
it1 = reduce(lambda x: x>5,list1)
for i in it1:
  	print(i,end=' ')
```

## 内建函数之sorted()的使用

>   list.sort():对原数据进行排序，无返回值
>
>   sorted():对备份出来的数据进行排序，返回数据排序备份
>
>   sorted(iterable，key =None ,reverse = Flase)

```python
'''需求1：从大到小排序列表'''
list1 = [0,6,3,4,1,8,2]
# 默认为从小到大
list2 = sorted(list1)
# reverse = True 反序已经开启
list3 = sorted(list1,reverse=True)
print(list2)
print(list3)

'''需求2：正数从小到大，负数从大到小'''
list4 = [1,0,9,-2,-3,5,8,-6,-9]
list5 = sorted(list4,key=lambda x:(x<0,abs(x)))
print(list5)
# 列表中自定义对象的排序
class Student():
    def __init__(self,name,age ):
        self.name = name
        self.age = age
stu1 = Student('aa',19)
stu2 = Student('bb',18)
stu3 = Student('cc',20)
'''按照类属性age的大小进行排序'''
list6 = [stu1,stu2,stu3]
list7 = sorted(list6,key=lambda x:x.age)
#	list7 = sorted(list6,key=lambda x:x.name)	按照name排序
for stu in list7:
    print(stu.name,stu.age)
```

# 正则表达式

![1558509131615](E:\python_document\notes\assets\1558509131615.png)

## 	概述

正则表达式是对字符串操作的一种逻辑公式，就是用事先定义好的一些特定字符、以及这些特定字符的组合，组成一个“规则字符串”，这个”规则字符串“用来表达对字符串的一种过滤逻辑（可以用来检索、截取或者替换操作）

### 简介

是对字符串和特殊字符操作的一种逻辑公式，就是用事先定义好的一些特定的字符，以及这些特定字符的组合，组成一个“规则字符串”，这个“规则字符串”用来表达对字符串的一种过滤逻辑，正则表达式是一种文本的形式，模式描述在搜索文本时候要匹配一个或多个字符串。

### 作用

1.  给定的字符串是否符合正则表达式的过滤逻辑（称为“匹配”）
2.  可以通过正则表达式，从字符串中获取我们想要的特定部分
3.  还可以对目标字符串进行替换的操作。

## 正则表达式之re模块的基本操作

### re模块之match()和search()函数的应用

>   result = re.match(正则表达式，要匹配的字符串)

​	re.match是用来正则匹配检查的方法（**但只匹配开头**），如果字符串开头的0个或者多个字符匹配正则表达式模块，则返回响应的match对象，如果不匹配，返回None(不是空字符串哦~)

```python
import re
pattern = 'hello'
s = 'helloWorld hello
'''re.match()方法要注意的点：严格区分大小写（也就是说正则是大写，就必须匹配大写）
												 就匹配首位（纵使前面没有匹配目标，s中后者hello也匹配不出来）'''
v = re.match(pattern,s)
# 匹配的内容
print(v.group())
# 匹配内容的索引范围
print(v.span())

'''但是re.search()可以解决这一问题，re.search()从前到后，如果没有就往下走,但是search()只找一个。'''
v = re.search(pattern,s)
```

## 正则表达式之匹配字符

### 		语法格式：	

| 字符 | 功能（要匹配一长串，需要多个放在一起） |
| ---- | :------------------------------------- |
| .    | 匹配任意一个字符（除了换行符/n）       |
| []   | 匹配列表中的字符                       |
| \d   | 匹配数字，0-9                          |
| \D   | 匹配非数字                             |
| \s   | 匹配空白，即空格（\n,\t）              |
| \S   | 匹配非空白                             |
| \w   | 匹配单词字符，即a-z ,A-Z ,0-9          |
| \W   | 匹配非单词字符                         |

### 		代码实现

```python
'''简单的语法格式'''
import re 
pattern = '字符串'
s = '上述的字符，一个或者多个组合'
v = re.match(pattern,s)
'''或者： v = re.search(pattern,s)'''
print(v)
```

## 正则表达式之表示数量

### 		语法格式

| 字符  | 功能（和匹配字符联合使用）                                |
| ----- | --------------------------------------------------------- |
| *     | 匹配前一个字符出现0次或者无限次（可有可无）               |
| +     | 匹配前一个字符出现1次或者无限次（最少为1次）              |
| ？    | 匹配前一个字符出现的0 次或者1次（要不出现，要么出现一次） |
| {m}   | 匹配前一个字符出现的m次                                   |
| {m,}  | 匹配前一个字符至少出现的m次                               |
| {m,n} | 匹配前一个字符出现m到n次                                  |

### 	代码实现

```python
import re 
pattern = '匹配字符+表示数量'
s = '字符串'
v = re.match(pattern,s)
print(v)
'''举个栗子'''
# 匹配出一个字符串首字母为大写字符，后边都是小写字符，这些小写字符可有可无
pattern = '[A-Z][a-z]*'
s = 'Hello'
v = re.match(pattern,s)
print(v)
```

## 正则表达式之原始字符串

​	Python中字符串前面加上r表示原生字符串

### 原始字符串的使用

```python
# s = '\n123'
'''输出结果先有一行空，在下面123'''
# s = r'\n123'
s = '\\n123'
'''下面两个输出结果都是一样的'''
print(s)
'''结合正则表达式'''
# 上面一个斜号，下面就两个斜号
pattern = '\\\\n\d{3,}'
# 使用原生字符串的写法
pattern = r'\\nd{3,}'
v = re.match(pattern,s)
print(v)
```

## 正则表达式之表示边界

### 语法格式

| 字符 | 功能               |
| ---- | ------------------ |
| ^    | 匹配字符串开头     |
| $    | 匹配字符串结尾     |
| \b   | 匹配一个单词的边界 |
| \B   | 匹配非单词的边界   |

### 代码实现

```python
'''案例一：匹配QQ邮箱'''
import re 
pattern = r'[0-9]\d{5,9}@qq.com$'
s = '56451321@qq.com'
v = re.match(pattern,s)
print(v)
'''案例二：匹配单词的边界'''
'''最后一定要是一个单词，非单词就不行'''
pattern = r'.*\ber'
s = '123,eroa'
v = re.match(pattern,s)
```

## 正则表达式之匹配分组

### 语法格式

| 字符       | 功能                             |
| ---------- | -------------------------------- |
| \|         | 匹配左右任意一个表达式           |
| （ab）     | 将括号中的字符做一个分组         |
| \num       | 引用分组num匹配到的字符串        |
| (?P<name>) | 分别起组名                       |
| (?P=name)  | 引用别名为name分组匹配到的字符串 |

### 代码实现

```python
'''1、匹配0-100之间全部的数字  分析：有两种情况，一位数+二位数 和 100，两种情况用或者“|”'''
#	| 的使用
import re 
'''r:简便，[1-9]:匹配列表中的数字，？：前一个可有可没有，因为要有一位数的，\d：匹配的数字0-9，$:匹配字符串结尾，就是个结尾符，|：或者的意思，100：是单拎出来的。'''
pattern = r'[1-9]?\d$|100$'
'''另一种写法'''
pattern = r'\d?[0-9]$|100$'
s = '100'
v = re.match(pattern,s)
print(v)

'''2、匹配一个座机号码  0411-88888888 分析：区号{3,4}-电话号{5.8}'''
# （ab）分组的使用
# 注意已经分组了，为什么要分组呢？是要保证下面group()能够准确的找到，想要的信息
pattern = r'(\d{3,4})-([1-9]\d{4,7})$'
s = '0411-88888888'
v = re.match(pattern,s)
print(v)
# 分组的作用主要在这↓↓
print(v.group(1))

'''3、匹配出网页标签内的数据，分析：<html><title></title></html>  注意：是成对出现的'''
pattern = r'<.+><.+>.+</.+></.+>'
# 但上述的正则，当s不是成对出现时，也能匹配出来，需要优化，也就用到了\num，优化后↓↓
pattern = r'<(.+)><(.+)>.+</\2></\1>'
s = '<html><title>我是标题</title></html>'
v = re.match(pattern,s)
print(v)

'''4、?P<要起的别名>(?P=起好的别名)   '''
s = '<html><h1>我是一号字体</h1></html>'
pattern = r'<(.+)><(.+)>.+</\2></\1>'
# 上述正则在数量多了之后会出现混淆的情况，可以给它起名字，优化↓↓
pattern = r'<(?P<key1>.+)><(?P<key2>.+)>.+</(?P=key2)></(?P=key1)>'

```

## re模块的高级用法

### search

​	**作用**：扫描字符串，查找正则表达式模式产生匹配的第一个位置，并返回相应的匹配对象，如果字符串中没有，则返回None

#### 	案例： 

```python
import re 
s = 'C语言阅读次数为999次,C++阅读次数为1000次，Python阅读次数为999999次'
'''这里不能用\d*'''
pattern = r'\d+'
v = re.search(pattern,s)
print(v)
# 不过这只能检索到第一个数字，也就是999.
```

### findall

​	**作用**：从左往右扫描字符串，并按照找到的顺序，如果模式中有多个，则返回一个列表。

####  	案例：

```python
# 想要检索到全部的目标，则需要使用findall了
v = re.findall(pattern,s)
print(v)
```

### sub

​	**作用**：返回通过替换repl替换字符串中最左边不重叠的模式出现而得到的字符串，如果没有找到模式，则返回字符串不变。

#### 	案例：

```python
'''sub主要用途是在于替换'''
'''例如：全部的次数都替换为100'''
v = re.sub(pattern,'100',s,count=2)
# sub(正则表达式，要替换的字符串，目标，替换个数（默认为全部）)
print(v)

# 同时替换也可以用函数来表示，就是把字符串换为函数,并且用的是最多的。
def replace(result):
  	'''里面是替换的字符串'''
  	return 'type = str'
v = re.sub(pattern,replace,s,count = 1)
'''会输出一个新的字符串，不改变原字符串。'''

```

### split 

​	**作用**：指定模式拆分字符串

#### 	案例：

```python
'''按照要求拆分字符串，下面拆分出来每个单词'''
s = 'He say:Hello,world'
pattern = r'\s|:|,'
# \s表示空格的意思哦~
v = re.split(pattern,s)
#	输出的格式为一个列表


```

## 贪婪模式和非贪婪模式

### 	什么是贪婪？什么是非贪婪？

贪婪顾名词义就是太贪了，在Python中数量词都很贪，总是尝试去匹配可能多的字符

非贪婪，就是不贪呗，尝试匹配尽可能少的字符，可以用“,”“?”“+”“{m,n}”后面加上？，就可以改变人性，变得不贪了。

### 	案例：

```python
import re
# 贪婪模式
# pattern = r'(.+)(\d+)-(\d+)-(\d+)'
# 非贪婪模式
pattern = r'(.+?)(\d+)-(\d+)-(\d+)'
s = 'This is my tel:133-1234-1234'
v = re.match(pattern,s)
print(v.group(1))
```

>   对上述案例的一些解释：当我贪的时候，给后面留一个就行了，当我不贪的时候，我就一个就够了。



# 内存管理

![1558663996020](E:\python_document\notes\assets\1558663996020.png)

## 元类-使用type动态创建类

### 元类是什么？

​	python是面向对象的语言，对象呢是由类创建出来的，而类则是由元类创建，也就是元类是对象的**爷爷**。

​	**元类可以动态创建类**

### type

#### 	作用：

1.  查看目标对象的数据类型。
2.  可以使用type动态创建类。

>   语法：类 = type(‘类名’,(父类,…),{属性，方法})	

#### 	案例：

```python
class Animal():
    def __init__(self,color):
        self.color = color
    def eat(self):
        print('狗子不能吃巧克力')
def sleep(self):
    print('狗子爱上了猫咪')
'''使用type动态创建类，父类是Animal'''
Dog = type('Dog',(Animal,),{'age':3,'sleep':sleep})
dog = Dog('bad')
print(dog.age)
dog.sleep()
print(dog.color)
dog.eat()
```

## 类装饰器

​	借助类，让一个函数在不修改源码的情况下，增加新的功能。（很重要哦~）

### 	案例：

```python
'''装饰器的类，__call__(self,*args,**kwargs)函数是必须有的，而且在这个函数内要分别调用新增函数和源函数'''
class AAA():
    def __init__(self,func):
      	'''__func，是私有的func参数，也就是源函数要做这个参数'''
        self.__func = func
    def __call__(self, *args, **kwargs):
        self.test2()
        self.__func()
    def test2(self):
        print('我是额外功能哦~')
@AAA
def test1():
    print('我就是源码')
test1()
```

## 对象池

### 小整数池

​	范围是[-5,256]，在程序开始时，小整数池中的数字都会加载到内存中。LRGB（局部变量、闭包中的变量、全局变量、内建变量）只要使用的数值在小整数范围内，那么全局仅有一个，会一直在内存中常驻。

![1558059458232](E:\python_document\notes\assets\1558059458232.png)

### 大整数池

​	每创建一个不是小整数范围内的变量，都会被自动存储到大整数池中，想走了就走了。

### inern机制（字符串池）

​	每个单词（字符串），不夹杂空格或者其他特殊字符，默认开启intern机制，共享内存，靠**引用计数**来决定是否销毁

![1558059880502](E:\python_document\notes\assets\1558059880502.png)

​	特殊符号：空格/,/等等。。

## 垃圾回收--引用计数

​	如何获取一个对象的引用计数

1.  sys模块中，getrefcount()方法
2.  刚创建的对象引用计数为2

增加引用计数：

-   如果新的对象使用对象，+1
-   装进列表+1
-   作为函数参数

减少引用计数：

-   如果新对象不在使用 -1
-   从列表中移除-1
-   函数调用结束

## 垃圾回收--隔代计数

​	

```python
'''隔代回收为辅（相互引用，引动计数无法删除类似的对象）
            原理：
                随着时间的推进，程序赘余对象逐渐增多，达到一定的数量（阈值），系统进行回收

                （0代  1代  2代）

            代码：
                gc机制   import gc
                gc.get_count()  返回当前的收集计数，一个元组，也就是（0代  1代  2代） 三条链表上剩余的对象数量
                gc.disable()  返回当前收集阈值，一个元组，三个元素。
                gc.set_threshold()  设置收集阈值，将阈值设置为零的将禁用
'''
import gc
import time
class AA():
    def __new__(cls, *args, **kwargs):
        print('new')
        return super(AA, cls).__new__(cls)
    def __init__(self):
        print('object:born at %s'%hex(id(self)))

    def __del__(self):
        print('object:born at %s'%hex(id(self)))

def start():
    while True:
        a = AA()
        b = AA()
        a.v = b
        b.v = a
        del a
        del b
        print(gc.get_threshold())
        print(gc.get_count())
        time.sleep(0.1)
# 手动关闭垃圾回收机制
gc.disable()
start()
```

