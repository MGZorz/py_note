一. 选择题（每题1分，共20分）
1. 下列哪个语句在Python中是非法的？	（ B ）
	A. x = y = z = 1	 	B. x = (y = z + 1)
	C. x, y = y, x			D. x  +=  y

2．关于Python内存管理，下列说法错误的是	（ B ）
	A. 变量不必事先声明 B. 变量无须先创建和赋值而直接使用
	C. 变量无须指定类型 D. 可以使用del释放资源

3. 在Python3中执行如下语句后得到的结果是？ ( D  )

   ```shell
   >>> world="world" 
   >>> print "hello"+ world
   ```

     A. helloworld           B. "hello"world  

     C. hello world          D. 语法错误

4. 下面哪个不是Python合法的标识符（ B  ）
    A. int32	 B. 40XL	C. self		D. __name__

5. 下列哪种说法是错误的（ AD  ）
    A. 除字典类型外，所有标准对象均可以用于布尔测试
    B. 空字符串的布尔值是False
    C. 空列表对象的布尔值是False
    D. 值为0的任何数字对象的布尔值是False

6. 下列表达式的值为True的是	（ A  ）
    A. 5+4j > 2-3j	 		B. 3>2>2	
    C. (3,2)< ('a','b')		D. 'abc'>'xyz'

7. Python不支持的数据类型是	（ A  ）
    A. char	 	B. int  	C. float 		D. list

8. type(1+2L*3.14)结果是:                   （ C ）
     A. <type ‘int’>           B. <type ‘long’> 
      C. <type ‘float’>         D. <type ‘str’> 

9. 关于字符串下列说法错误的是	（ B  ）
    A. 字符应该视为长度为1的字符串		
    B. 字符串以\0标志字符串的结束
    C. 既可以用单引号，也可以用双引号创建字符串 
    D. 在三引号字符串中可以包含换行回车等特殊字符

10. 以下不能创建一个字典的语句是	（ C  ）
    A. dict1 = {}			
    B. dict2 = { 3 : 5 }	  
    C. dict3 = dict( [2 , 5] ,[ 3 , 4 ] )
    D. dict4 = dict( ( [1,2],[3,4] ) )

11. 下面不能创建一个集合的语句是	（ C  ）
    A. s1 = set () 			B. s2 = set ("abcd")  
    C. s3 = (1, 2, 3, 4) 	D. s4 = frozenset( (3,2,1) )

12. 下列Python语句正确的是	（ D ）
    A. min = x  if  x < y  else  y 	 B. max = x > y ? x : y 
    C. if (x > y) print x		     D. while True : pass

13. 以下哪个为创建分配内存的方法	( B )
    A. __new__	()		B. __init__() 
    C. __del__() 		D. 没有正确答案

14. 以下哪个对象不属于Itarable	的	( D )
    A. list			B. tuple 
    C. dict	 		D. float

15. 关于创建进程的方式，说法错误的是  ( B )
    A. fork				B. Process 
    C. Process的子类	D. 都不对

16. 关于类型转换，说法错误的有(多选)  ( AC )
    A. int <-> float		B. tuple <-> list
    C. list<-> dict   		D. str   <-> list


17. 以下哪个类型不可以进行切片操作	( D )
	A. str			B. list
	C. tuple		D. dict

18. 以下哪个属于可变对象 ( B )
	A. 数值类型(int,float)		B. list
	C. tuple			 		D. str

19. 实现以下哪个方法可以让对象像函数一样被调用 ( C  )
	A. __str__()			B. __iter__()
	C. __call__()			D. __next__()

20. 以下哪个不属于面向对象的特征	( D	)
	A. 封装				B. 继承
	C. 多态			 	D. 复合

二. 简答题(每题5分，共40分)

1. 请简述你对面向对象的理解

  面向对象的编程---object oriented programming，简称：OOP，是一种编程的思想。OOP把对象当成一个程序的基本单元，一个对象包含了数据和操作数据的函数。面向对象的出现极大的提高了编程的效率，使其编程的重用性增高。
  python面向对象的重要术语：
  　　1.多态（polymorphism）：一个函数有多种表现形式，调用一个方法有多种形式，但是表现出的方法是不一样的。
  　　2.继承（inheritance）子项继承父项的某些功能，在程序中表现某种联系
  　　3.封装（encapsulation）把需要重用的函数或者功能封装，方便其他程序直接调用
  　　4.类：对具有相同数据或者方法的一组对象的集合
  　　5.对象：对象是一个类的具体事例

2. 简述什么是深拷贝和浅拷贝

   浅拷贝：

   对内存地址的复制，让目标对象指针和源对象指向同一片内存空间。注意：当内存销毁的时候，只想对象的指针，必须重新定义，才能够使用

   

   深拷贝：深拷贝是指，拷贝对象的具体内容，二内存地址是自主分配的，拷贝结束之后俩个对象虽然存的值是一样的，但是内存地址不一样，俩个对象页互相不影响，互不干涉

3. 请简述Python中的内存管理机制

   Python使用gc模块处理python对象以及python垃圾回收器的工作

   gc.enable()——可自动进行垃圾回收；
   gc.disable()——不可自动进行垃圾回收；
   gc.set_threshold()——设置python垃圾回收的阈值；
   gc.set_debug()——设置垃圾回收的调试标记，调试信息会被写入std.err；

   gc.get_objects()——返回收集器跟踪的所有对象的列表，不包括返回的列表。

   Python的内存管理机制主要包括三个方面：引用计数机制、垃圾回收机制、内存池机制


4. 请写出创建生成器的方式（最好用代码）

   方式一： 将列表生成式的中括号改成小括号

   列表生成式      `a = [x*2 for x in range(100000000000)]`

   生成器     `a = (x*2 for x in range(100000000000)) `

   调用的时候   `next(a)`

   ```python
   def creatnum(): 
     a,b = 0,1 
     for i in range(5): 
       yield b 
     a,b = b,a+b
   ```

5. 请简述dict的特性

   字典中key的值不可改变,value的值可以改变;

   由于字典保存数据使用的是Hash存储方式 故字典无法使用切片方式

6. 请简述4G的内存如何做到可以读取5G的数据

   ```python
   #1 使用python的生成器，一小段一小段数据读取
   # 生成器：具有yield的函数就是生成器，是一个可以返回迭代器的函数
   # 迭代器：知道遍历位置的对象，有iter()和next()方法
   # 代码举例：
    def get_lines():  # 生成器
       with open('file5G.py', 'r') as f:
           while True:
               data = f.readlines(100)
               if data:
                   yield data
               else:
                   break
   f = get_lines()  # 迭代器对象
   print(next(f))
   print(next(f))
   print(next(f))
   #2 Linux的split命令
   # 可以把文件拆成一个个小文件进行操作
   # 作用：split将一个文件分割成一个个指定大小的文件
   # 使用语法： split [–help][–version][-<行数>][-b <字节>][-C <字节>][-l <行数>][要切割的文件][输出文件名]
   # 常用的选项是-b按照字节切割，-l按照行数切割
   # 在黑窗口中输入命令，使用举例：
    python@ubuntu:~/Desktop$ split -l 2 requirements.txt re.txt 
   # 意思：按照两行切割requirements.txt文件，切割后的文件名叫re.txt。
   # 回车后会生成好多re文件，里面都是两行代码
   ```

7. 简述read. readline. readlines的区别

   假设a.txt的内容如下所示：

```
1 Hello
2 Welcome
3 What is the fuck...
```

read:读取整个文件

`read([size])`方法从文件当前位置起读取size个字节，若无参数size，则表示读取至文件结束为止，它范围为字符串对象

```python
f = open("a.txt")
lines = f.read()
print(lines)
print(type(lines))
f.close()
```

输出结果：

```shell
Hello
Welcome
What is the fuck...
<type 'str'> #字符串类型
```

readline：读取下一行，使用生成器方法。**

从字面意思可以看出，该方法每次读出一行内容，所以，读取时占用内存小，比较适合大文件，该方法返回一个字符串对象。

```python
  def pyReadLine(filename):
      file_object1 = open('a.txt','r')
      try:
        while True:
            line = file_object1.readline()
            if line:
                print ("line=",line)
            else:
                break
     finally:
         file_object1.close()
```

输出结果：

```python
<type 'str'>
Hello
Welcome
What is the fuck...
```


readlines：读取整个文件到一个迭代器以供我们遍历

readlines()方法读取整个文件所有行，保存在一个列表(list)变量中，每行作为一个元素，但读取大文件会比较占内存。

```python
f = open("a.txt")
lines = f.readlines()
print(type(lines))
for line in lines:
	print(line)
f.close()
```

输出结果：

```shell
<type 'list'>
Hello
Welcome
What is the fuck...
```

8. 简述实例属性与类属性的区别以及实例方法与类方法，静态方法的区别

   **类属性和实例属性的区别**
   在Python中一切皆对象，类是一个特殊的对象即类对象，描述类的属性称为类属性，它属于类。类属性在内存中只有一份，所有实例对象公用，在__init__外部定义。

   实例属性：用来描述类创建出来的实例对象，需要通过对象来访问，在各自对象的内存中都保存一份，在`__init__`方法内部定义

   **实例方法、类方法、静态方法的区别**
   这三种方法都是保存在类的内存中，调用者不同。

   实例方法由对象调用，至少一个self参数，self代表对象的引用。

   类方法由类调用，至少一个cls参数，并且需要装饰器@classmethod修饰

   静态方法由类调用，不需要参数，需要装饰器@staticmethod修饰

三. 上机题(每题10分，共40分)

1. 随机生成一个由100个大写字母组成的字符串，将内容写入到名称为’abc.txt’文件中
2. 从文件’abc.txt’中读取出对应内容，统计各个字母出现的次数，并打印
3. def func1():
  print("使用功能1")
  使用装饰器完成为，在不修改函数func1源代码的前提下，实现日志功能(将访问函数的时间，访问的函数的名称，写入到文件’log.txt’中)
4. 使用多进程(进程池)完成多个模拟任务(随机耗时)的执行


