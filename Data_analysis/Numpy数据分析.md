# Numpy

### 介绍

​		Numpy是科学计算基础库，提供大量科学计算相关功能，比如数据统计，随机数生成等。其提供最核心类型为多维数组类型(ndarray：`n-dimensional array object`)。numpy支持向量处理ndarray对象，提高程序运算速度。

> 官方网站：http://www.numpy.org/

###### 查看numpy的版本

```python
import numpy as np 
np.__version__
```

###### 特殊对象

```python
# In IPython 解释器提供特殊对象，用来存储输入信息，列表类型
# Out 也是一个特殊对象，用来存储输出信息，字典类型，当单元格运行后，最后一个表达式为非空时，将信息保存到out对象
```

### 数组创建

#### array([])	一维数组

```python
# 使用array方法创建一维数组，传入的参数为
# n = np.array([1,2,3])
# display(n)  python解释器不支持，ipython解释器才支持，需要使用的时候要导入
# form IPython.display import display
# print(n) 方法输出内容  ; n  则输出表格和类型

# 使用array创建多维数组，传入参数是嵌套列表
n= np.array([[1,2],[3,4]])
# display(n)
print(n)
```

#### arange() 	类似于range()

```python
# arange方法类似 python中 range()方法，传入参数也包含起始值，结束值和步长。
# 举例：
# 		n = np.arange(10)
# 		n = np.arange(1,10)
# 		n = np.arange(1,10,2)

# 步长可以是浮点型，以及负数。
n = np.arange(3,1,-0.5)
```

#### ones()/ones_like()	全为1 的数组/根据传入的数组形状创建全为1的数组

```python
# ones创建全为1的数组
# 参数：shape  整型或者元祖
#       dtype  数据类型 默认为numpy.float64
n1 = np.ones(3)
display(n1)

#  创建多维数组的时候，必须要传入元组
n2 = np.ones((3,4))
display(n2)

np.ones((3,2))

# ones_like:根据传入的数组形状创建全为1的数组
n3 = np.ones_like(n2)
display(n3) 
```

#### zeros/zeros_like	创建全为0的数组/根据传入的数组形状创建全为0的数组

```python
# zeros方法创建全为0的数组
# 一维
n1 = np.zeros(3)
display(n1)
# 多维
n2 = np.zeros((3,4))
display(n2)
# zeros_like:根据传入的数组形状创建全为0的数组
n3 = np.zeros_like(n2)
display(n3)
```

#### empty/empty_like 	创建全为空数组/根据传入的数组形状创建全为空的数组

```python
# empty创建全为空数组；
# 注意，数据并不是设置为0，而是值未初始化，需要我们自己来初始化。

# 内存方面理解：
#		先定义全为1的数组，也就在内存中生成了全为1的数组，
# 		这时对它进行None操作，断绝n1和数组的联系，在调用empty方法创造数组，
# 		内存中会自动把n1和之前创建的数组联系起来。
n1 = np.ones(3)
n1 = None
n1 = np.empty(3)
display(n1)

# empty_like 根据传入的数组形状创建全为空的数组
n2 = np.empty_like(n1)
display(n2)
```

#### full/full_like	创建全为某个指定数据的数组/根据传入数组形状创建数组，同时指定全为某个数

```python
# full(shape,fill_value) 创建全为某个指定数据的数组
# 参数： shape 数组维度或者形状
#        fill_value 指定数据

# 下列创建的数组，内容全为3，而且是两行两列的
n1 = np.full((2,2),3)
display(n1)

# full_like:根据传入数组形状创建数组，同时指定全为某个数
n2 = np.full_like(n1,4)
display(n2)
```

#### eye/identity	创建单位矩阵

```python
# eye和identity创建单位矩阵，创建的矩阵似乎都是一样的
n1 = np.eye(3)
display(n1)

n2 = np.identity(3)
display(n2)
```

#### linspace	等差数组

```python
# linspace根据一定间隔创建·等差数组·
# 参数： start stop num(为包含的数字的数量,默认为50)  
#        endpoint=True（包含终止点）  间隔 "end-start/(num-1)"
n1 = np.linspace(1,5,num=5)
display(n1)
# 1,2,3...50
n2 = np.linspace(1,50)
display(n2)

#        endpoint=False(不包含终止点)  间隔 "end-start/num"
n3 = np.linspace(1,5,num=5,endpoint=False)
display(n3)
```

#### logspace	等比数组

```python
# logspace根据指数函数创建·等比数组·
# 参数： start stop（start和stop都是指数函数的幂） 
#		num base(指数函数的底)
# 1 2 4 8 
n1 = np.logspace(0,3,num=4,base=2)
display(n1)
# 1 10 100 1000
n2 = np.logspace(0,3,num=4)
display(n2)
```

### 数组ndarray和列表(List)比较

> 数组就是矩阵哦~

优势：
* 数组可与标量进行计算，数组之间可进行向量化计算。
* 数组在运算时，具有广播能力。 **广播能力就是把小的数组，广播复制（复制为和操作数组一样的维度）。**
* 数组底层使用c语言编写，运行速度快。
* 数组底层使用c数组的存储方式，节省内存空间。

```python
# 班上同学的python成绩，统一加1分
# 列表操作
scores = [90,91,92]
# 循环遍历列表
for i in range(len(scores)):
    scores[i]+=1
display(scores)

# 数组操作
scores_ndarray = np.array([90,91,92])
# 整体操作，不再需要循环遍历
scores_ndarray+=1
display(scores_ndarray)

# 多维操作
from IPython.display import display
a = np.array([1,2,3])
b = np.array([[1,1,1],[2,2,2]])
# 相应加就行了
display(a+b)
```

### 魔法命令

> 魔法命令的两种形式：
>
> - % ：行模式
> - %% ：单元格模式

#### time	统计语句执行时间

```python
# 对比与python中的计算
import time
start = time.time()
time.sleep(0.5)
end = time.time()
display(end-start)

# time用来统计语句执行时间，被统计语句只执行一次
%time time.sleep(0.5)
```

#### timeit	循环多次执行被统计语句

> 循环多次执行被统计语句，得到平均执行时间，支持行模式和单元格模式。
>
> 参数：	**–n**	 指定每轮测试次数，	**-r** 	指定测试轮数(默认为7)
>
> 注意：第一行语句（和timeit同行）为**初始化语句**，作用为后续代码中变量提供初始化功能，每轮测试都执行一次，并且不参与计时。

```python
# 输出的结果信息：46.1 ns ± 2.75 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)
# 7 runs 运行7轮
# 10000000 loops 每轮循环执行次数
# 均值是46.1ns 标准差是2.75ns
# 范围是【46.1  - 2.75ns，46.1  + 2.75ns】
%timeit a=1

# 同时也可以指定每轮循环的次数，及执行的轮数
#      -n 每轮循环的次数
#      -r 执行轮数 默认是7轮
%timeit -n 1000 -r 2 a=1

%%timeit -n 2 -r 2 print('初始化语句')
print('hello world')
# 单元格模式下，我们可以在timeit后面（同一行）使用初始化语句。
# 初始化语句也会执行，并且也会参与循环。
# 初始化语句作用：后续被统计的执行代码提供变量的初始化。
# 初始化语句执行次数，由轮数来决定。
```

#### writefile	将单元格内容写入到文件

> 如果文件不存在则创建，如果文件存在，则覆盖文件。
>
> 如果指定 –a 参数，则追加内容,不覆盖。一般都是单元格模式

```python
%%writefile  -a test.py
print('update222222....')
```

#### run	运行外部python文件

> 运行外部python文件，运行结束后，外部文件中定义的变量得到保留。  
> 格式： %run 文件路径

```python
%run test.py
```

#### memit	分析内存使用情况

> 使用之前要导入memory_profiler模块。`%load_ext memory_profiler`

```python
# 分析m1()的内存使用情况
%load_ext memory_profiler
def m1():
    print('hello world')
%memit m1()
```

#### mprun 分析内存的使用情况

> 相对于memit方法，memit方法只能分析整个模块或者整个函数占用内存的大小，mprun方法，可以分析出每个变量占用内存的大小。

注意

- 要使用的时候，`%load_ext memory_profiler`载入。
- mprun函数只能测试定义在物理文件中的函数，要利用writefile函数把函数写入文件中。
- 使用的时候也要导入物理文件。
- 修改代码后，直接运行不会对结果进行改变，需要重新导入模块才可以，可以利用`importlib`模块的`relaod`方法。

```python
# 写入文件
%%writefile test2.py
def m():
    li1 = [i for i in range(20000)]
    li2 = [i for i in range(400000)]
# 导入mprun
%load_ext memory_profiler
# 修改代码后，需要用importlib模块中的reload函数重新导入
import importlib
importlib.reload(test2)
# 使用格式：%mprun -f 分析函数  执行语句
%mprun -f test2.m test2.m()
```

### 数组属性

​		数组常用的属性有：

1. ndim:n-dimension,维度
* shape:形状，每个维度上相应长度
* dtype:：数据类型
* size:数组元素个数
* itemsize:一个数组元素占用内存空间，字节为单位

```python
x = np.array([1,2,3])
# 输出维度
display(x.ndim)

y = np.array([[1,2,3],[2,3,4]])
display(y.ndim)

# 返回数组对象形状，每个维度上长度（返回一个元祖），y为两行三列
display(y.shape)
# 返回数据类型  
display(y.dtype)
# 返回元素个数     2*3=6
display(y.size)
# 返回一个元素占用内存空间，字节为单位，算法：数据类型为int32，8位一个字节 32/8=4
display(y.itemsize)
```

### 数组类型以及转换

> 分为四个方面：
>
> - 创建数组时候，可使用dtype指定数组中元素类型
> - 如果没有指定，根据元素类型进行推断
> - 如果类型不同，会选择兼容类型
> - 使用astype函数转换数据类型

```python
# 使用dtype指定数组中元素类型
x = np.array([1,2,3],dtype=np.float32)
display(x.dtype)

# 如果没有指定，根据元素类型进行推断 
y = np.array([1.1,2.1,3.1])
display(y.dtype)

# 如果类型不同，会选择兼容类型（向上），意思就是整型和浮点型，向上兼容为浮点型。
z = np.array([1.1,2,3,4])
display(z.dtype)

# 使用astype函数转换数据类型
# 把浮点型转化为整型，把1.1变为1 ，2.2变为2，。。。
w = np.array([1.1,2.2,3.3,-4.4])
display(w.dtype)
m = w.astype(np.int64)
display(m)
```

### 改变数组形状（reshape方法）

```python
# 一维数组改为多维数组
x = np.arange(6)
display(x)
# 转化为三行两列的多维数组
# 写法一
y=x.reshape((3,2))
# 写法二
y=x.reshape(3,2)
display(y)

# 数组对象，reshape的参数可以是元祖，也可以将元祖中内容分开传入
# np的reshape方法，只能使用元祖传入,不能将元祖中内容分开传入
# 下列不行:
# 			y = np.reshape(x,3,2)
# 			display(y) 

# 多维数组改为1维数组
x = np.array([[1,2,3],[3,4,5]])
display(x)
# 改变为1维数组，元素个数要相等
y = x.reshape((6))
# -1 表示任意的元素个数
y = x.reshape((-1))
# 写法二  
y = np.reshape(x,(-1))
# display(y)
```

### 索引与切片

在数组中的索引和切片，和列表中的类似，有相同点也有不同点。

- 相似点：数组对象也支持索引和切片
- 不同点：数组切片返回的原数组视图，如果需要复制底层数组元素，可以用数组对象的copy方法。
- 注意：使用切片得到的数组，和原数组共享底层内存中的数据。

```python
# 索引访问
x = np.arange(9).reshape(3,3)
display(x)
# 从低维获取数据
# x是2维数组，包含低维和高维，低维对应向下坐标轴，表示为0方向；高维对应向右 坐标轴，表示1方向。
# x[1]从低维度，也就是从0方向上获取数据，即访问的第一行的数据
display(x[1])
# 高维
display(x[1][1])
```

```python
# 切片访问
# 0 1 2
# 3 4 5
# 6 7 8  
x = np.arange(9).reshape(3,3)
display(x)

# 得到
# 3 4 5
# 6 7 8
# 从零行开始算，第一行到第三行（不包含第三行）
y = x[1:3]
display(y)

# 得到
# 3 4
# 6 7
# 再加上第0列到第2列的数据（不包含第二列）
y = x[1:3,0:2]
display(y)

# 得到 修改步长
# 0 1 2
# 6 7 8
# 第0行和第二行，加一个步长（0+2）
y = x[0:3:2,:]
display(y)

# 切片得到新的数组,和原有的数组共享底层内存中数据，修改其中一方都会去影响对方的数据
x = np.array([1,2,3])
y = x[:]

x[0]=200
display(x)
display(y)

# 数组对象用copy得到的新的数组，新的数组和原有数组之间不共享数据
w = x.copy()
w[0]=30
display(x)
display(w)

# 对列表切片操作,使用的是浅拷贝，修改新的列表不会影响原有的列表。
li = [1,2,3]
li2 = li[:]
li2[0] = 10
display(li)
display(li2)
```

### 整数数组进行索引

> ​		当选取的元素不连续的时候，可以提供一个索引数组选择(或修改)对应索引位置元素。
> 注意：
>
> - 通过整数数组索引，返回的是原数组拷贝
> - 可以提供多个一维数组索引，此时会将每个数组中内容对应作为索引，返回对应的元素

```python
x = np.arange(20).reshape(5,4)
# 获取第0 2 3,不连续数据
y = x[[0,2,3]]

# 获取0 2 8 10 四个数
# 返回（0,0）（0,2）（2,0）（2,2）
# [0,0,2,2]  [0,2,0,2] 分别对应
y= x[[0,0,2,2],[0,2,0,2]]
```

### 布尔数组进行索引

> 获取数据原则：为True，获取对应位置，为False，不获取。
>
> 注意：
>
> - 索引布尔数组通过对现有数组计算得到
> - 逻辑运算符和python不同:and->&， or->|，not->~,条件组合时候，条件需用小括号

```python
x = np.arange(12).reshape(4,3)
display(x)
# 使用布尔数组获取第0行 1行数据 
#  第一个True表示0方向（竖），第0行要
#  第一个False表示0方向（竖），第2行不要
y=x[[True,True,False,False]]
display(y)

# 大于5  得到一个布尔数组，当>5都为True 反之都为False
# x>5
# 把全部的True返回一个一维数组。
# x[x>5]

# 大于1小于5数据返回 and变为&  注意写法
# x[(x>1) & (x<5)]
```

### 数组扁平化（ravel(np.ravel) / flatten）

两者区别在于：**ravel**返回数组原数组**共享数据**，而**flatten**返回原数组拷贝**不共享****

```python
x = np.arange(12).reshape(3,2,2)

# 返回的数组和原数组共享数据，修改返回数组影响原有数组
# y = np.ravel(x)
y=x.ravel()


# 返回的原数组拷贝，修改返回数组不影响原有数组
y = x.flatten()
```

### 数组存储顺序（order）

> - C: 按照行存储
> - F: 按照列存储
> - 注意：order存储数据作用于两个步骤。第一：先数据扁平化（抽取数据），第二：数据填充（数据构建）顺序。

```python
x = np.array([1,2,3,4]).reshape((2,2),order='C')
y = np.array([1,2,3,4]).reshape((2,2),order='F')
# C 先紧着 行 先把行填满
# F 先紧着 列 先把列填满
x = np.array([[1,2],[3,4]]).reshape((2,2),order='C')
y = np.array([[1,2],[3,4]]).reshape((2,2),order='F')
# order 是有两个步骤的，如果为多维数组，那么首先需要对数组进行扁平化处理，
# 然后在对数组进行构建填充
```

### 通用函数

> * abs/fabs ：绝对值/浮点取绝对值
> * cell/floor ：取整 
> * exp ：指数
> * log/log2/log10 ：对数
> * modf ：分别获取小数和整数部分
> * sin/sinh/cos/cosh ：三角函数
> * sqrt ：平方根函数

```python
# 举例说明
x = np.array([-1.2,10,1.5])
display(x)

# 分为两个数组，整数和小数分开了
np.modf(x)
```

### 统计函数

> * mean/sum ：均值/取和
> * max/min ：最大/最小
> * argmax/argmin ：最大值对应的索引/最小值对应的索引
> * std/var ：标准差/方差
> * cumsum/cumprod ：累加和/累乘

```python
# 统计函数如果只传入数组对象的话，它会对数组首先做一个扁平化处理，再对扁平化后的一维数组的所有的数据进行统计
```

### 轴（axis）

> - 可以指定axis参数改变统计的轴。在二维数组中，0表示竖直方向操作，1表示沿着水平方向操作。
> - 超过二维的多维数组，轴相对复杂，可认为沿着轴所指定坐标变化方向，其他轴坐标不变。进行操作。比如轴是0，则根据第0个坐标变化方向

```python
scores = np.array([[90,92],[85,100]])
# axis=0，从竖直方向统计数据，获得语文的最高分，以及数学的最高分
display(np.max(scores,axis=0))

#  如果我们指定轴为0，第一个维度的坐标变化的，第二个维度的坐标不变
#  如果我们指定轴为1，第一个维度的坐标不变，第二个维度的坐标变化
#  具体的意思见列公式
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/20190717182044582.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjAxODY3MQ==,size_16,color_FFFFFF,t_70)

### 连接和拆分函数

> * np.concatenate对多个数组按指定轴方向进行连接，默认制定轴为0
> * np.vstack/np.hstack   垂直连接/水平连接
> * np.split    切分
> * np.hsplit/np.vsplit   横向/垂直 

```python
x = np.array([[95,100],
 [96,98]])
y = np.array( [[97,98],
 [96,99],
 [95,94]])

# 对101班和102班成绩进行垂直连接，列数一致
w = np.concatenate((x,y),axis=0)
# 方法二
w = np.vstack((x,y))


# 对w进行横向切分，将数据切分2部分
z = np.split(w,2,axis=1)

# 对w进行纵向切方，得到3部分数据 第0，1行，第2，3行  第4行
# 也可以传一个列表，对2处理，是由0~1，接着 4处理，是2~3，最后剩下第四行
z = np.split(w,[2,4],axis=0)
```

```python
# 对101班zs和ls成绩和身高及体重数据水平连接，保证行数一致
x = np.array([[95,100],
 [96,98]])
y = np.array( [[175,65],
 [177,70]])
# 制定轴为1
w = np.concatenate((x,y),axis=1)
# 方法二
w = np.hstack((x,y))

# 把w切分为2部分，方向轴为0
z = np.split(w,2,axis=0)
display(z)
```

### 其他函数

> * any/all 类似于或者和并且的意思
> * transpose  转置
> * dot   矩阵的乘法（点积运算）
> * np.sort  排序
> * np.argsort   对数组内容对应的下标进行排序

```python
# any和all运算时，数组元素为0 False 空返回False，其他返回True
# any有一个数组元素返回True，any返回True

x = np.array([0,0,False])
display(x.any(),x.all())
# 上述代码 any()和all()返回Flase 
```

```python
# transpose对数组数据进行装置（行变列）
x = np.arange(1,5).reshape(2,2)
display(x.transpose())

# 简便方法，T
display(x.T)

# 数组转置本质上轴的颠倒，对于二维数组a[i][j]-->a[j][i]  a[0][1]-->a[1][0]
# 传入参数，指定轴的颠倒顺序
y = np.arange(1,13).reshape(3,2,2)
display(y)
# 如果tanspose方法不传入参数，默认前后颠倒  a[i][j][k]-->a[k][j][i]
# transpose(0,2,1)    a[i][j][k]-->a[i][k][j]

display(y.transpose(0,2,1))
```

```python
x = np.array([[1,2],[3,4]])
y = np.array([[2,3],[1,2]])
display(x,y)
# 不是矩阵乘法运算
# display(x*y)
# 使用dot实现矩阵乘法（点积）运算
# display(x.dot(y))
display(x.dot(3))
```

```python
# sort 排序 
# -1是1轴 -2 是0轴
x = np.array([3,-1,2])
# display(np.sort(x))
y=np.array([[3,2],[1,2]])
display(y)
# sort对数组内容进行排序，默认按照最后一个轴的方向排序，如果是二维，按照水平方向排序，从小到大
# display(np.sort(y,axis=1))
# argsort 对数组内容对应的下标进行排序，
display(np.argsort(y))
```

### 归一化矩阵

> 将矩阵值转化为0到1区间  
> * 归一化公式：x-min/max-min  
> * max为每列最大值，min为每列最小值
> * 步骤：构建出一个max-min的对应矩阵，构建max对应矩阵，最后进行运算。

```python
x = np.array([[90,1],[80,2],[70,2]])
# 得到0方向最大值
max = x.max(0)
# 得到0方向最小值
min = x.min(0)
# 得到max-min的范围值
range = max-min

# 矩阵减去min在0方向的复制，除以范围在0方向上复制
shape = x.shape
y = x - np.tile(min,(shape[0],1))
y = y/np.tile(range,(shape[0],1))
```

