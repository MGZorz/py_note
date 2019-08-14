# Day03

## 	一、序列

### 			1、列表

​				[]是列表，只是把对象的地址（id）依次存在列表中。列表的对象大小可变。

![1553602183321](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\1553602183321.png)

![1553602208725](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\1553602208725.png)

## 	二、列表的创建

##### 	1、基本语法创建

##### 	2、list（）创建

![1553602533603](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\1553602533603.png)

#### 	3、range()创建

###### 	range([start],end,[step])

​	start :可选，起始数字

​	end:必选，便是结尾数字

​	step:步长，一步几个。

#### 4、推导式

​	一般都是结合与for语句来进行的。

## 三、元素的5种添加方式。

#### 		1、append(  )方法

#### 		2、+    运算符

当大量运算符的时候，避免使用+运算符。

#### 		3、extend() 方法

​	a = [20,40]
​	a.extend([50,60])

#### 		4、insert( ) 插入

​	![1553649426330](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\1553649426330.png)

insert(a,b)    a代表位置，B代表添加元素。

#### 	5、乘法扩展

​	a = [20,30]
a*3=[20,30,20,30,20,30]

## 四、元素的删除

#### 	1、del 删除

需要制定数据的位置进行删除，实际上就是数据的拷贝。把后边元素拷贝到删除位元素的位置。

a = [1,2,3,4,6]

del.a[4]

#### 	2、pop()

删除并返回指定位元素，**若未指定位置，则默认最后一位**。

#### 	3、remove()

删除首次出现的指定元素。必须是**指定的**

## 五、列表元素的访问和计数

#### 	1、索引

#### 	2、index()

可以获取指定元素首次出现的索引位置。index(value,[start,[end]])

#### 	3、count()

返回元素在列表中出现的次数。

#### 	4、len()

获得列表的长度，元素的个数

#### 	5、成员资格判断

直接使用**“in”**就OK了，  或者count()函数也可以。



## 六、切片操作slice

​	**[起始位置：终点位置：步长]**

​	注意：步长为-1，反向提取。

###### （1）列表的遍历



## 七、列表排序

#### 1、修改原列表，不建新列表的排序

**sort()升序**

**sort(reverse=True)降序排列**

**random.shuffle() 打乱顺序**

#### 2、reversed()返回逆序迭代器

#### 3、max、min

#### 4、sum

**数值型列表的求和操作**



## 八、多维列表

####  1、二维列表



## 九、元组tuple

#### 	1、元组的创建

通过（）

#### 	2、通过tuple函数创建

和list的用法一模一样。

![1553653623497](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\1553653623497.png)

#### 	3、元组对象的访问和删除

del just like 上面。

## 十、生成器推导式创建元组

​	元祖总结

![1553656943094](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\1553656943094.png)

## 十一、字典

字典是“键值对”的无序可变序列。

定义方式

a = {'name':'gaoqi','age':15,'job':'programmer'}

键：整数、浮点数、字符串、元组，且不可重复。

不可为列表、字典、集合。

#### 1、字典的创建

通过{} 和dict{}

![1553657596847](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\1553657596847.png)

通过zip()创建![1553657562087](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\1553657562087.png)

fromkeys创建值为空的字典

## 十二、字典元素的访问

通过{}去访问。

推荐get（）获得值。

列出所有的键值对   items()

列出所有的键。

len() 键值对的个数。

检测一个“键”是否在字典中("in”)

## 十三、字典元素的添加修改和删除

新增键值对

update将新字典的所有键值对添加到字典对象是。

pop()

popitem() 随机删除和返回该键值对，依次弹出，从后到前。

## 十四、序列解包

序列解包在字典中

![1553667584902](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\1553667584902.png)

## 十五、复杂表格数据存储

![1553668335491](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\1553668335491.png)

## 十六、字典核心底层原理



## 十七、集合

​	集合是无序可变的，元素不能重复。元素都是字典中的“键对象”。

#### 1、集合的创建

1. 使用**{}**创建集合对象，并使用 **add()**方法添加元素

>>> a = {3,5,7}
>>> a
>>> {3, 5, 7}
>>> a.add(9)
>>> a
>>> {9, 3, 5, 7}
2. 使用 **set()**，将列表、元组等可迭代对象转成集合。如果原来数据存在重复数据，则只保
  留一个。
>>> a = ['a','b','c','b']
>>> b = set(a)
>>> b
>>> {'b', 'a', 'c'}
3. **remove()**删除指定元素；clear()清空整个集合
>>> a = {10,20,30,40,50}
>>> a.remove(20)
>>> a
>>> {10, 50, 30}

#### 2、集合的运算

>>> a = {1,3,'sxt'}
>>> b = {'he','it','sxt'}
>>> a|b #并集
>>> {1, 3, 'sxt', 'he', 'it'}
>>> a&b #交集
>>> {'sxt'}
>>> a-b #差集
>>> {1, 3}
>>> a.union(b) #并集
>>> {1, 3, 'sxt', 'he', 'it'}
>>> a.intersection(b) #交集
>>> {'sxt'}
>>> a.difference(b) #差集
>>> {1, 3}