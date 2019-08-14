# Pandas

### 介绍

​		Pandas是基于Numpy库，会提供很多用于数据操作和分析的功能。

> 使用之前需要安装和导入的：
>
> pip install pandas|conda install pands   /  import pandas as pd（基本都用pd代替） 

### Series类型 	一维带标签数组对象

​		是类似numpy的一组数组，可以把它看成是一组数据与数据相关标签（索引）联合构成的。

#### 创建方法

###### 列表可迭代对象

```python
s = pd.Series([1,2,3])
```

###### ndarray数组对象

```python
# range迭代 每列都是0~4
s=pd.Series(range(5))
```

###### 字典对象

```python
# Series对象的标签为字典数据中key
s=pd.Series({'a':1,'b':2,'c':3})
```

###### 标量+索引参数

```python
# 这里用index参数指定索引
s=pd.Series(33,index=['a','b','c'])
```

#### 相关参数

- index	索引
- values	值
- shape	形状
- size	个数
- dtype	数据类型

> 说明：
>
> 1. 如果没有指定索引，那么会自动生成从0开始后的整数值索引，也可以使用index显示指定索引。
> 2. Series对象和index属性都有name属性，在**创建时候和创建之后**都可以命名。
> 3. 当其中的values较多时，可以通过**head(n)**(开头)和**tail(n)**(末尾)方法，访问前后的n个数据.
> 4. **Series对象的数组只能是一维数组类型。**

```python
# s = pd.Series([1,2,3]) 的index:起始位0，终止位3 步长为1
s = pd.Series([1,2,3],index=list('abc')) # 加上abc的索引
# 返回元素索引 
display(s.index)
# 返回元素的值
# 	ps:int64和int32的主要区别在范围，前者2**64  后者2**32
display(s.values,type(s.values))
# 返回元素的形状
display(s.shape) 
# 返回元素个数
display(s.size)
# 返回元素数据类型
display(s.dtype)
```

```python
s = pd.Series([1,2,3],index=list('abc'))
# 创建之后设置index索引。
s.name='Sereis name'
s.index.name='index name'

# 创建的时候就设置了name属性 ，和上面的结果一模一样
ind = pd.Index(['a','b','c'],name='index name')
s = pd.Series([1,2,3],index=ind,name='Series name')
```

```python
# head 查看前面的数据    tail查看的是后面的数据
s = pd.Series(np.arange(1000))
# head查看前面数据，默认5条；tail查看后面的数据，默认是5条
display(s.head(3),s.tail(3))
```

#### Series和ndarray索引引用比较

​		Series对象可以理解为带着标签的ndarry，其中标签和值类似于字典的key和value，但是不支持负数！！

```python
s = pd.Series([1,2,3])
display(s[0]) # 显示索引为0的value
# Series类似于字典的key和value方式，不支持负数访问!!
# display(s[-1])

# ndarray类似于list索引，支持负数访问~
x = np.array([1,2,3])
display(x[-1])
```

#### Series相关操作

* 支持广播与向量化运算
* 支持索引与切片
* 支持整数数组与布尔数组提取元素

```python
# Series和ndarray类似，也支持广播和向量化整体操作
s = pd.Series([1,2,3])
s2 = pd.Series([2,3,4])
display(s*s2) # 两个Series对象相乘，只是对应位置相乘。
display(s*2)  # 广播能力~

# 在Series运算的时候，是根据标签进行匹配的，如果标签不一致，则会产生空值。
# 而且空值和任何其他值运算都是空值。

# 传入空值的两种方法：float('NaN')  np.nan
s = pd.Series([1,2,3,float('NaN'),np.nan])
# 判断是否为空值的属性：isnull()是 notnull()否
display(s.isnull())
display(s.notnull())

# 那就假如运算结果中不想要空值，就可以用Series对象提供的计算方法避免。
# add()函数，将下列s2中没有的索引的值用10来填充。
s = pd.Series([1,2,3],index=[1,2,3])
s2 = pd.Series([2,3,4],index=[2,3,4])
s.add(s2,fill_value=10)

# 在统计函数中,Numpy可以处理NaN,Sereis忽略NaN
# 使用均值函数mean验证
a = np.array([1,2,3,np.nan])
s = pd.Series([1,2,3,np.nan])
display(np.mean(a))
display(np.mean(s))
# 结果为：   nan 和  20
```

#### 索引

##### 标签索引和位置索引

​	当Series对象的index值为非数值类型，可以使用标签和位置索引，也可以显示指定标签或者位置索引访问

- loc	标签索引访问
- iloc    位置索引访问
- 注意：
  - 通过标签或者位置数组来访问多个元素得到的是原数据的拷贝，彼此之间不会互相干扰。

```python
# s = pd.Series([1,2,3])
# 通过index指定标签信息，非数值类型标签信息
# Sereis对象既可以通过标签索引来访问，也可以通过位置索引来访问
#  Sereis对象可通过索引访问，也可以通过位置索引访问。
s = pd.Series([1,2,3],index=list('abc'))
display(s['a'])
display(s[0])

# 但是当通过index指定的标签信息为，数值类型的时候，位置标签就失效了

# Sereis对象提供iloc和loc来专门显示访问位置和标签索引
s = pd.Series([1,2,3],index=list('abc'))
# loc专门来通过标签进行访问
display(s.loc['a'])  # 结果：1
# iloc专门来通过位置进行访问
display(s.iloc[0])   # 结果：1

# 同样的可以通过标签和数组来访问多个元素
s = pd.Series([1,2,3],index=list('abc'))
display(s.loc[['a','c']]) # 第a行和第c行
display(s.iloc[[0,2]]) # 第0行和第2行 但是结果都是一样的。
```

##### 布尔数组索引

​	会对Series对象中的数据进行筛选，若OK返回True，不OK返回False。

```python
# 布尔数组索引访问Sereis中数据
s = pd.Series([1,2,3,4],index=list('abcd'))
# 每一列符合就位True
display(s>2)
display(s[s>2])# 筛选了一下，去除False项
```

#### 切片

​	和ndarray数组一样支持切片访问多个元素，并且返回的数据和原数据之间共享内存，也就是说一个改变另一个也会改变。

#### Series中的增删改查操作

- 获取值：标签或者位置索引，再或者二维数组
- 修改值：直接赋值
- 增加值：直接赋值
- 删除值：
  - del  s[‘索引’]  直接删除。
  - drop()函数     删除多个值，drop([]) 标签列表
    - 参数inplace= False ，根据原有的Series对象复制一个新的对象，更改新对象并返回。
    - 参数inplace= True,删除原有Series对象数据，并且返回None！

```python
s = pd.Series([1,2,3,4],index=list('abcd'))
# 获取值，通过标签或者位置索引（或者2维数组）
display(s.loc['a'])
display(s.iloc[0])
# 修改值
s.loc['a']=100

# 增加值，类似字典操作
s['f']=5
display(s)

# 删除值，类似字典操作
# del s['f']
# display(s)

# 删除值方法：drop()
# 参数：inplace = False ,
#       会根据原有的Series对象数据复制一个新的Series对象，然后删除目标数据并返回原有Series的拷贝。

# s2 = s.drop('f')
# display(s,s2)

#       inplace = rue，
#       删除的就是原有Sereis对象的数据，并且drop方法返回None！
# s2 = s.drop('f',inplace=True)
# display(s,s2)

# 删除多个值，drop([]),标签列表。
s.drop(['a','f'],inplace=True)
# display(s)
```

### DataFrame  二维带标签数组对象

#### 介绍

- 类似数据库中数据表，多列构成，但是每列类型可以不同。
- 二维数组类型，具有行、列索引
- 每一行，每一列都是一个Series对象

#### 创建

- 二维数据结构类型（列表，ndarray数组，DataFrame等等~）
- 字典类型（key：列名，value：一维数组结构{列表，ndarray数组，Series等等}）

```python
# 使用二维的数据结构类型(ndarray,列表)
# df = pd.DataFrame(np.array([[100,100,100],[90,90,90],[80,80,80]]))
# df = pd.DataFrame([[100,100,100],[90,90,90],[80,80,80]])

# 使用字典创建，key就是列名，value一维数据结构
df = pd.DataFrame({'语文':[100,100,100],'数学':[90,90,90],'外语':[80,80,80]})
```

##### 创建DataFrame时可以指定行列索引（index  行 / columns 列）

```python
# 未通过index  columns指定行索引和列索引，行索引和列索引默认从0开始
# index指定行索引 columns 列索引
df = pd.DataFrame([[100,100,100],[90,90,90],[80,80,80]],index=['张三','李四','王五'],columns=['语文','数学','外语'])
```

#### DataFrame 属性

* index   行索引
* columns  列索引
* values  数值
* shape   形状
* ndim    维度
* dtypes  数值类型
* 超过二维数据创建DataFrame 报错

```python
df = pd.DataFrame([[100,100,100],[90,90,90],[80,80,80]],index=['张三','李四','王五'],columns=['语文','数学','外语'])
# 返回行索引   Index(['张三', '李四', '王五'], dtype='object')
display(df.index)
# 返回列索引   Index(['语文', '数学', '外语'], dtype='object')
display(df.columns)
# 返回DataFrame对象对应ndarray数组
display(df.values)
# 返回形状  (3, 3)
display(df.shape)
# 返回维度  2
display(df.ndim)
# 返回各列数据类型
display(df.dtypes)

# 通过index修改行索引信息 直接进行赋值，覆盖
# df.index=['张三2','李四2','王五2']

# 设置行索引和列索引名称
df.index.name='index-name'
df.columns.name='columns-name'
```

#### DataFrame列操作

##### 获取列数据

* df[列索引]  获取多列数据df[索引数组]
* df.列索引  (不推荐~) 容易和属性混淆

##### 增加(修改)列

* df[列索引]=列数据

##### 删除列

* del.df[列索引]
* df.pop(列索引)
* df.drop(列索引或数组)

```python
df = pd.DataFrame([[100,100,100],[90,90,90],[80,80,80]],index=['张三','李四','王五'],columns=['语文','数学','外语'])
# 获取列数据，通过df[列索引]  单列或者单行都是单独的Series对象
display(df['语文'],type(df['语文']))
# 注意，此种方式索引被解析成列索引，获取列数据，不会解析成行索引

# 获取多列数据，  df[索引数组]  多列或者多行都为DataFrame对象
display(df[['语文','数学']],type(df[['语文','数学']]))
# 如果索引数组中索引只有一个列标签，返回的仍然是DataFrame类型
display(df[['语文']],type(df[['语文']]))

# 第二种方式访问列数据，不推荐
display(df.语文)

# 增加、修改列
# 列标签不存在话，增加一列
# df['物理']=[80,80,80]
# display(df)
# 列标签存在话，修改一列
df['语文']=[80,80,80]

# 根据已有列计算，得到新的一列
df['总分']=df['语文']+df['数学']+df['外语']

# 删除列，采用类似字典方式  del/pop
# del df['语文']
# display(df.pop('语文')) # 将 所对应的的列删除，同时返回删除的一列的信息
# display(df)

# DaraFrame提供drop方法删除,可以指定轴axis方向和inplace参数
df.drop('数学',axis=1,inplace=True)
display(df)
```

#### DataFrame行操作

###### 获取行

* df.loc    根据标签进行索引
* df.iloc   根据位置进行索引
* 多行获取，参数为**嵌套列表**

###### 增加行

- append	先定义一个形状相同的Series对象，再添加。

###### 删除行

- df.drop（）	参数
  - axis 轴  
  -  inplace 
    -  True  删除原DataFrame中的数据
    -  False  先拷贝一份，在删除拷贝的，不动原DataFrame中数据

```python
df = pd.DataFrame([[100,100,100],[90,90,90],[80,80,80]],index=['张三','李四','王五'],columns=['语文','数学','外语'])

# df.loc 标签索引   获取张三行value
display(df.loc['张三'])
# df.iloc 位置索引    获取第0行value
display(df.iloc[0])

# 多行获取  
display(df.loc[['张三','李四']]) # DataFrame类型

# 增加行数据
# 创建一个Sereis对象，Sereis对象通过append方法加入到DataFrame中
# Sereis对象包含 value信息，index信息，name信息，和DataFrame格式一致。
newLine= pd.Series([85,85,85],index=['语文','数学','外语'],name='赵六')
df = df.append(newLine)

# 删除行数据  行标签  轴  inplace
df.drop(['张三','李四'],axis=0,inplace=True)
display(df)
```

#### DataFrame混合操作

> 可以理解为取其中的某个具体的数值

* 先获取行，再获取列

  ```python
  df = pd.DataFrame([[100,100,100],[90,90,90],[86,80,80]],index=['张三','李四','王五'],columns=['语文','数学','外语'])
  # 三种方式，获取张三的语文成绩。
  df.loc['张三'].loc['语文']   # 推荐使用，先行(loc)再列(loc)
  df.loc['张三']['语文']  
  df.loc['张三','语文']
  ```

* 先获取列，再获取行

  ```python
  # 两种方式 		张三的语文成绩
  df['语文'].loc['张三']
  df['语文']['张三']
  # 注意，在这种思路下，df['语文','张三']这种方法，是不支持的。
  ```

#### DataFrame结构

​		DataFrame的一行或一列，都是Sereis类型对象。

- 对于行来说，Series对象**name值**就是**行索引名称**，元素值对应标签是列索引名称。
- 对于列来说，Series对象**name值**就是**列索引名称**，元素值对应标签是行索引名称。

#### DataFrame切片、布尔、标签数组索引

##### 切片

- df [切片]  ：  对行操作
- df [索引]  ：  对列操作

```python
df = pd.DataFrame([[100,100,100],[90,90,90],[86,80,80]],index=['张三','李四','王五'],columns=['语文','数学','外语'])

# 混合操作，列确定，对行切片 (标签+位置)
display(df['语文'].loc['张三':'李四'])
display(df['语文'].iloc[0:1])

# 混合操作，行确定，对列切片 (标签+位置)
display(df.loc['张三'].loc['语文':'数学'])
display(df.loc['张三'].iloc[0:1])

# 混合操作，对行切片，对列切片
display(df.loc['张三':'李四'])
display(df.loc['张三':'李四'].loc['语文':'数学'])
display(df.loc['张三':'李四','语文':'数学'])

# 仅对行进行切片操作
display(df.loc['张三':'李四'])
display(df.iloc[0:1])

# 仅对列进行切片操作
# 前面的“：”表示把所有的列全部取出来，然后在对其进行分别获取。
display(df.loc[:,'语文':'数学'])
```

##### 布尔数组（对行操作）

```python
# 一维布尔数组,对行进行操作，不是对列进行操作，是false就不显示
bArray=[True,True,False]
# 结果只显示True的部分

# 二维布尔数组，对DataFrame的每一个元素进行运算，True保留，False值设置为NaN
display(df>85)
display(df[df>85])
```

##### 标签数组（对列操作）

```python
# 标签数组，对列进行操作  筛选出语文成绩和数学成绩
lArray = ['语文','数学']
```

#### DataFrame运算

- 转置
  - 行变列，列变行
- DataFrame之间运算
  - 行索引和列索引都要对齐，不然就要产生空值
  - 避免空值，可以使用DataFrame的add函数代替运算符计算，通过参数fill_value参数指定填充值
- DataFrame和Series运算
  - 默认Series索引匹配DataFrame列索引，然后进行广播
  - 也可以通过axis参数，指定行索引匹配还是列索引匹配

```python
# 转置
df=pd.DataFrame(np.arange(1,5).reshape(2,2))
display(df,df.T)
```

```python
# DataFrame对象之间操作，行索引对齐，列索引也要对齐
df = pd.DataFrame(np.ones((2,2)))
df2 = pd.DataFrame(np.ones((2,2)))
# 相加
display(df+df2)

# 不对齐的情况  运算得NaN 首先补充行索引和列索引，数据填充为NaN。
df = pd.DataFrame(np.ones((2,2)))
df2 = pd.DataFrame(np.ones((2,2)),index=[1,2],columns=[1,2])
display(df,df2)
display(df+df2)
# 如果不想要运算结果为空值的话，就可以使用函数(add)来替换操作符(+),通过fill_value参数指定填充值
display(df.add(df2,fill_value=10))
```

```python
# DataFrame和Sereis之间运算
df = pd.DataFrame(np.arange(1,5).reshape(2,2))
s = pd.Series([10,20])

# 默认Series对象标签和DataFrame的列标签匹配
# 步骤：
#      首先会把Series对象旋转一下，和列标签匹配
#      然后通过广播复制，把它自己个变成和DataFrame对象类似形式，在计算
display(df+s)

# 设置Sereis对象标签和DataFrame的行标签匹配，广播，再计算  自定义轴
display(df.add(s,axis='index'))
```

#### 排序

##### 索引排序

​		Sereis和DataFrame对象可以使用**sort_index**对索引进行排序。DataFrame还可以通过**axis指定对行还是列索引**进行排序，也可以通过**ascending参数指定升序还是降序**排序

##### 值排序

​		Sereis和DataFrame对象使用**sort_value**方法进行值排序

```python
# 索引排序
df = pd.DataFrame(np.arange(9).reshape(3,3),index=[3,1,2],columns=[6,4,5])

# 对行索引排序 默认为0，0 为纵向
display(df.sort_index())

# 对列索引排序 1 为横向
display(df.sort_index(1))

# inplace，True对原有的数据进行排序,sort_index返回None，False对拷贝得到的数据进行排序
df.sort_index(inplace=True)

# ascending指定升降序，False降序，True升序
display(df.sort_index(ascending=False))


# 值排序
df = pd.DataFrame([[100,100,100],[90,90,90],[86,80,80]],index=['张三','李四','王五'],columns=['语文','数学','外语'])

# 对列数据， 比如对外语数据进行从小到大的排序
df.sort_values('外语',axis=0,inplace=True)

# 对行数据，比如王五成绩按照从小到大排序
display(df.sort_values('王五',axis=1))

# 对多列数据进行排序，比如对语文和数学进行排序,先对语文排序，语文相等，再根据第二列数学进行排序
display(df.sort_values(['语文','数学'],axis=0))
```

#### 索引对象

Series、DataFrame的**index**或者DataFrame的**columns**都是**索引对象**。

- 索引对象可以像数组那样进行索引访问
- 索引对象内容是不可修改

```python
df = pd.DataFrame(np.arange(9).reshape(3,3))

# index和columns都是索引对象
display(df.index,type(df.index))
display(df.columns,type(df.columns))

index = df.index
display(index[0])

# 不支持修改索引对象中内容

# 支持指向一个新的索引对象，把df中的索引改为456
index2 = pd.Index([4,5,6])
df.index = index2
display(df)
```

##### 统计相关方法

- mean/sum/count   count 统计个数
- max/min
- cumsum/cumprod
- argmax/argmin
- idxmax/idxmin    返回数据最大/小值所对应的索引
- var/std

```python
df = pd.DataFrame([[np.nan,np.nan,100],[100,100,90],[86,80,80]],index=['张三','李四','王五'],columns=['语文','数学','外语'])

# 统计非NaN值的个数，默认按照列来统计
display(df.count())
# axis=1设置按照行统计
display(df.count(axis=1))

# idxmax返回数据最大值所对应的索引，默认按照列
display(df.idxmax())
# axis=1,设置按照行，找到每行最大值对应的索引
display(df.idxmax(axis=1))

# idxmin回数据最小值所对应的索引，默认按照列
display(df.idxmin())
# axis=1,设置按照行，找到每行最小值对应的索引
display(df.idxmin(axis=1))
```

