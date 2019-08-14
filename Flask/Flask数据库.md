# SQLAIchemy

## SQLAlchemy连接数据库

##### 可以使用ORM框架操作数据库

>   ORM框架 = object    relationship   mappiy  框架

##### 学习前提（软件）

>   mysql、pymysql（或者MySQLdb）、SQLAlchemy

### SQLAlchemy连接数据库

#### 步骤

-   首先导入sqlalchemy.create_engine

-   输入配置信息（服务器ip，端口号，数据库名，账户，密码）

-   传递一个满足某种格式的字符串

    -   >   dialect+driver://username:password@host:port/database?charset=utf8
        >
        >   
        >
        >   dialect：数据库的实现，比如MySQL、PostgreSQL、SQLite，并且转换成小写。
        >
        >   driver：Python对应的驱动，python3对应sqlalchemy,python2对应MySQLdb。
        >
        >   username：连接数据库的用户名
        >
        >   password：连接数据库的密码
        >
        >   host：连接数据库的域名

-   创建数据库引擎

-   创建连接

##### 代码实现

```python
from sqlalchemy import create_engine

#准备连接数据库基本信息
# 代表哪一台计算机，ip地址是多少
HOSTNAME = '127.0.0.1'
# 端口号
PORT = '3306'
# 数据库的名字，连接那个数据库
DATABASE = 'first_sqlalchemy'
# 数据库的账号和密码
USERNAME = 'root'
PASSWORD = 'root'
# 按照要求组织成一定的字符串
DB_URI = 'mysql+pymysql://{username}:{pwd}@{host}:{port}/{db}?charset=utf8'\
    .format(username =USERNAME,pwd = PASSWORD,host = HOSTNAME,port=PORT,db = DATABASE)
# 创建数据库引擎
engine = create_engine(DB_URI)
# 创建连接,如果运行之后，输入1则连接成功
with engine.connect()as con:
    rs = con.execute('SELECT 1')
    print (rs.fetchone())
```

### 拓展：用SQLAlchemy执行原生SQL

```python
from sqlalchemy import create_engine
from constants import DB_URI
#连接数据库
engine = create_engine(DB_URI,echo=True)
# 使用with语句连接数据库，如果发生异常会被捕获
with engine.connect() as con:
    # 先删除users表
    con.execute('drop table if exists authors')
    # 创建一个users表，有自增长的id和name
    con.execute('create table authors(id int primary key auto_increment,'name varchar(25))')
    # 插入两条数据到表中
    con.execute('insert into persons(name) values("abc")')
    con.execute('insert into persons(name) values("xiaotuo")')
    # 执行查询操作
    results = con.execute('select * from persons')
    # 从查找的结果中遍历
    for result in results:
        print(result)
```

## ORM框架

>   ORM：Object Relationship Mapping（对象模型与数据库表的映射）

### Python代码和SQL代码的对应关系

>   **py代码：**
>
>   class Person(object):
>
>   ​    	name = 'xx'
>
>   ​    	age = 18
>
>      	 country ='xx
>
>   对应关系：
>
>   Person类 -> 数据库中的一张表
>
>   Person类中的属性  -> 数据库中一张表字段
>
>   Person类的一个对象 -> 数据库中表的一条数据

### 使用原生sql语句的缺点

1.  SQL语句重复利用率不高，越复杂的SQL语句条件越多，代码越长，会出现很多相近的SQL语句。
2.  大型的项目是在业务逻辑中拼接出来的，如果数据库需要更改，就要去修改这些逻辑，这会很容易漏掉对某些SQL语句的修改。
3.  写SQL时容易忽略web安全问题，造成隐患。

### SQLAlchemy的优势

-   易用性：使用ORM做数据库开发可以有效减少重复SQL语句的概率，写出来的模型也更加直观、清晰
-   性能损耗小：任何操作都要通过ORM转化，确实会损耗性能，但综合考虑开发效率、代码阅读性，带来的好处远大于性能损耗，而且项目越大作用越明显。
-   设计灵活：可以轻松的写出复杂的查询
-   可移植：SQLAlchemy封装了底层的数据库实现，支持多个关系数据库引擎，可以非常轻松的切换数据库

## SQLAlchemy操作数据库

>   操作前，必须要先构建session对象！！

### 定义ROM模型映射到数据库中

#### 步骤：

1.  用**declarative_base**根据**engine**创建一个**ORM基类**。
2.  用这个**Base**类作为基类来写自己的ORM类。要定义`__tablename__`类属性，来指定这个模型映射到数据库中的表名。
3.  创建属性来映射到表中的字段，所有需要映射到表中的属性都应该为**Column类型**
4.  使用`Base.metadata.create_all()`来将模型映射到数据库中。

#### 注意：

使用create_all函数创建的表映射到数据库之后，即使改变了模型的字段，也不会重新映射了。

体现为代码中，后加的**nick**项，没有办法实现。

解决方法：每次运行时，先把之前的表全部删除之后，在创建新的表。

#### 代码实现：

```python
# 需求：创建好一个ORM类模型,并且映射到指定的数据库中成为表

# 1、用`declarative_base`根据`engine`创建一个ORM基类Base。

Base = declarative_base(engine)

# 2、用这个`Base`类作为基类来写自己的ORM类。要定义`__tablename__`类属性，来指定这个模型映射到数据库中的表名。

class Person(Base):

    __tablename__ = 't_person'

# 3、在这个ORM模型中创建一些属性，来跟表中的字段进行 一一 映射。这些属性必须是sqlalchemy给我们提供好的数据类型

    id = Column(Integer,primary_key=True,autoincrement= True)

    # nullable = True  可以为空

    name = Column(String(50),nullable=False)

    age = Column(Integer)

    country = Column(String(50))

    # 后加入的nick项

    nick = Column(String(20))

# 4、使用`Base.metadata.create_all()`来将模型映射到数据库中

# Base.metadata.create_all()

# 注意点：一旦使用`Base.metadata.create_all()`将模型映射到数据库中后，即使改变了模型的字段，也不会重新映射了。
# 解决方法：先将表全部删除之后再创建新的表
# 将Base上的ORM类模型对应的数据表都删除
Base.metadata.drop_all()
# 创建Base上的ORM类到数据库中成为表
Base.metadata.create_all()
```

### 对数据的增删改查操作（crud→增删改查）

>   crud功能指的就是增删改查。

#### 步骤：

1.  构建session对象，所有的所有和数据库的ORM操作都必须通过一个叫做`session`的会话对象来实现

2.  对表添加数据**{add(),add_all([])}**

3.  查询表中数据

    1.  全表查询  查找某个模型对应的那个表中所有的数据

        >   all_person = session.query(Person).all()

    2.  条件查询    filter_by

        >   all_person = session.query(Person).filter_by(name='momo1').all()

    3.  条件查询    filter

        >   all_person = session.query(Person).filter(Person.name=='momo1').all()

    4.  条件查询     get方法是根据id来查找的，只会返回一条数据或者None

        >   person = session.query(Person).get(primary_key)

    5.  条件查询     使用first方法获取结果集中的第一条数据

        >   person = session.query(Person).first()

4.  修改对象

    >   首先从数据库中**查找对象**，然后将这条数据**修改**为你想要的数据，最后做**commit**操作就可以修改数据了

5.  删除对象

    >   将需要删除的数据从数据库中**查找出来**，然后使用**session.delete**方法将这条数据从session中删除，最后做**commit**操作就可以了。

#### 代码实现：

```python
'''
    需求2：crud的操作
        0、前提：获取到根数据库，进行会话的对象 
        1、对表，添加数据
        2、查询表数据
        3、修改表，指定行数据
        4、删除表数据
'''
# 获取到根数据库，进行会话的对象 ，构建session对象，所有的所有和数据库的ORM操作都必须通过一个叫做`session`的会话对象来实现
# Session = sessionmaker(engine)
# session = Session()
#  下一行代码相当于上两行
session = sessionmaker(engine)()

# 1、对表，添加数据  session.add() session.add_all([])
p = Person(name='MGorz',age =18,country ='China',nick='诚哥')
session.add(p) # 一次只能插入一条数据
session.commit()
# 添加多条数据 
p2 = Person(name='Mrz',age =18,country ='China',nick='ha')
p3 = Person(name='MGz',age =18,country ='China',nick='e')
session.add_all([p2,p3])
session.commit()

# 2、查询表中数据
# 2.1   全表查询  ()中填类名,
ps = session.query(Person).all()
for p in ps :
    print(p)
# 2.2   条件查询    filter_by
# filter_by(),括号中填入想查询的。
ps = session.query(Person).filter_by(name = "MGorz").all()
for p in ps :
    print(p)
# 2.3   条件查询    filter
# 注意和filter_by的区别
ps = session.query(Person).filter(Person.name == "MGorz").all()
for p in ps :
    print(p)
# 2.4   条件查询    get
ps = session.query(Person).get(2)
print(ps)
# 2.5   条件查询    first
ps = session.query(Person).first()
print(ps)

# 3、修改制定行数据
person = session.query(Person).first()
print(person)
# 修改表数据，对象.属性 = '   '
person.name = 'hahaha'
# 别忘记要提交哦~
session.commit()

# 4、删除表数据
person = session.query(Person).get(3)
print(person)
session.delete(person)
session.commit()
```

### Column常用数据类型

​	常用的数据类型，一共是有11个。

>   注：在SQLAlchemy中不存在double数据类型，使用**DECIMAL**类型替代

让我们来分别看下这11个数据类型都有哪些？

1.  **Integer**：整型，映射到数据库中是**int**类型。

2.  **Float**：浮点类型，映射到数据库中是**float**类型。他占据的32位。

    >   浮点类型，有可能会造成精度丢失，特别是在money方面，不可原谅。

3.  Double（**SQLAlchemy中没有，代替品为DECIMAL**）：双精度浮点类型，映射到数据库中是double类型，占据64位 

4.  **String**：可变字符类型，映射到数据库中是**varchar**类型.

5.  **Boolean**：布尔类型，映射到数据库中的是**tinyint**类型。

6.  **DECIMAL**：定点类型。是专门为了**解决浮点类型精度丢失**的问题的。在存储money相关的字段的时候建议大家都使用这个数据类型。并且这个类型使用的时候需要传递两个参数，**第一个参数是用来标记这个字段总能能存储多少个数字**，**第二个参数表示小数点后有多少位**。

7.  **Enum**：枚举类型。指定某个字段只能是枚举中指定的几个值，不能为其他值。在ORM模型中，使用**Enum**来作为枚举。

8.  **Date**：存储时间，只能**存储年月日**。映射到数据库中是date类型。在Python代码中，可以使用`datetime.date`来指定。

9.  **DateTime**：存储时间，可以**存储年月日时分秒毫秒等**。映射到数据库中也是datetime类型。在Python代码中，可以使用`datetime.datetime`来指定。

10.  **Time**：存储时间，可以**存储时分秒**。映射到数据库中也是time类型。在Python代码中，可以使用`datetime.time`来指定

     >   ps：注意区分Date/DateTime/Time的储存信息！！！

11.  **Text**：存储长字符串。一般可以存储**6W**多个字符

12.  **LONGTEXT**：长文本类型，映射到数据库中是longtext类型（**不过这个只有mysql有，orcale没有**）

上述就是**11个**数据类型，因为这里把不存在的double也添加上了，所以看起来是12个。



#### 代码实现

```python
# 依次导入常用的数据类型
from sqlalchemy import create_engine, Column, Integer, String,Float,DECIMAL,Boolean,Date,DateTime,Time,Text,Enum

# 从sqlalchemy的方言模块dialects导入mysql专有的LONGTEXT,长文本类型
from sqlalchemy.dialects.mysql import LONGTEXT

# 在python3.x中有enum模块
import enum

#导入时间了
from datetime import datetime,date,time


# 用`declarative_base`根据`engine`创建一个ORM基类。
from sqlalchemy.ext.declarative import declarative_base

# 引入创建py和数据库连接的sessionmaker函数
from sqlalchemy.orm import sessionmaker



# 准备连接数据库基本信息
HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'first_sqlalchemy'
USERNAME = 'root'
PASSWORD = 'root'
DB_URI = 'mysql+pymysql://{username}:{pwd}@{host}:{port}/{db}?charset=utf8' \
    .format(username=USERNAME, pwd=PASSWORD, host=HOSTNAME, port=PORT, db=DATABASE)

# 创建数据库引擎
engine = create_engine(DB_URI)

Base = declarative_base(engine)


# 需求：常用的数据类型

# 枚举另外一种写法，导入enum模块，定义枚举类
class TagEnum(enum.Enum):
    python = "PYTHON"
    flask = 'FLASK'
    django = 'DJANGO'

class News(Base):
    __tablename__ = 'news'
    id = Column(Integer,primary_key=True,autoincrement=True)
    price1 = Column(Float)   # 不过存储数据时存在精度丢失的问题
    price2 = Column(DECIMAL(10,4))
    title = Column(String(50))
    is_delete = Column(Boolean)
    tag1 = Column(Enum('PYTHON','FLASK','DJANGO'))  # 枚举的常规写法（推荐）
    tag2 = Column(Enum(TagEnum))  # 另一种写法
    create_time1 = Column(Date)
    create_time2 = Column(DateTime)
    create_time3 = Column(Time)
    content1 = Column(Text)
    content2 = Column(LONGTEXT)


# 将Base上的ORM类模型对应的数据表都删除
# Base.metadata.drop_all()
# 创建Base上的ORM类到数据库中成为表
# Base.metadata.create_all()


# 新增数据到表news中
session = sessionmaker(engine)()
# 注意float出现的精度丢失问题      is_delete,布尔类型true：1，false:0
news1 = News(price1=1000.0078,price2=1000.0078,title='测试数据',is_delete=True,tag1="PYTHON",tag2=TagEnum.flask,   	create_time1=date(2018,12,12),create_time2=datetime(2019,2,20,12,12,30),create_time3=time(hour=11,minute=12,second=13),content1="hello",content2 ="hello   hi   nihao")


session.add(news1)
session.commit()
```

### Column常用约束参数

在给数据库表指定key的时候，必然要给它们添加，例如：不可空，字节长度等等的限制，这就需要约束参数的出场了。常用的约束参数一共有**7**种

#### 常见约束参数

| 约束参数      | 描述，功能                                                   |
| ------------- | ------------------------------------------------------------ |
| primary_key   | True设置某个字段为主键                                       |
| autoincrement | True设置这个字段为自动增长的                                 |
| default       | 设置某个字段的默认值。在发表时间这些字段上面经常用           |
| nullable      | 指定某个字段是否为空。默认值是True，就是可以为空             |
| unique        | 指定某个字段的值是否唯一。默认是False。                      |
| onupdate      | 在**数据更新**的时候会**调用**这个参数指定的**值或者函数**。在*第一次插入这条数据的时候，不会用onupdate的值，只会使用default的值*。常用于是`update_time`字段（每次更新数据的时候都要更新该字段值）。 |
| name          | 指定ORM模型中某个属性映射到表中的字段名。如果**不指定**，那么会**使用这个属性的名字来作为字段名**。这个参数也可以当作位置参数，在第1个参数来指定。 |

#### 代码实现

```python
# 注意千万不能忘记要先创建session对象啊！！
# 需求：sqlalchemy中Column常用的约束参数
class News(Base):
    __tablename__ = 'news'
    id = Column(Integer,primary_key=True,autoincrement=True)
    # 这个Datetime是sqlalchemy中的
    create_time = Column(DateTime,default=datetime.now)
    read_count = Column(Integer,default=11)
    title1 = Column(String(50),name='my_title',nullable=False)
    title2 = Column('my_title22',String(50), nullable=False)# name 属性的两种方式
    telephone = Column(String(11),unique=True)
    update_time = Column(DateTime,onupdate=datetime.now,default=datetime.now)#onupdate是在数据更新的时候才会起作用，插入数据时候不起作用

# Base.metadata.drop_all()
# Base.metadata.create_all()

news1 = News(title1 ='hahah',title2 = 'womingsad')
session.add(news1)
#结束之后，必须要提交
session.commit()
```

### Query查询函数，可以传递的参数有哪些？

Query查询函数传递的参数无非就是分为**三类**，分别是**模型名、模型中的属性、聚合函数**，那下面就简单的说明，

#### 模型名

>   指定查找该模型中所有属性（对应查询为全表查询）

#### 模型中的属性

>   可以指定只查找某个模型的其中几个属性

#### 聚合函数

>   聚合函数一共有五个，都被放到了sqlalchemy的func模块中。

1.  func.count：统计行的数量
2.  func.avg：求平均值
3.  func.max：求最大值
4.  func.min：求最小值
5.  func.sum：求和

#### 代码实现

```python
# 新增测试数据

for x in range(1,6):

    a = News(title = "标题%s"%x,price = random.randint(1,100))

    session.add(a)
# 提交
session.commit()



# 三种参数
# 模型名
result = session.query(News).all()  #全表查询
print(result)

# 模型名的属性名,返回的列表中的元素是元组类型数据
result = session.query(News.title,News.price).all()
print(result)

# 聚合函数
# 统计行的数量
r = session.query(func.count(News.id)).first()
print(r)
#最大值
r = session.query(func.max(News.price)).first()
print(r)
#最小值
r = session.query(func.min(News.price)).first()
print(r)
#平均值
r = session.query(func.avg(News.price)).first()
print(r)
#求和
r = session.query(func.sum(News.price)).first()
print(r)
```

### filter条件查询过滤条件

>   **ps**:
>
>   ​	以下的写法只是针对条件查询filter而言
>
>   ​	如果想看底层转化的sql语句，打印的时候去掉frist()或者all()

-   等值查询equals（**==**），非等值查询not equals（**!=**）

    ```python
    # 这里只写区别，等值查询
    query(News).filter(News.title == "title1").first()
    # 非等值查询
    query(User).filter(User.name != 'ed')
    ```

-   模糊查询：**like**（用的较多）& **ilike**（不区分大小写）

    ```python
    # 查询字段中有ed的字段
    query(User).filter(User.name.like('%ed%'))
    ```

-   多值查询 **in_** ；取反操作 not in 

    ```python
    # 多值查询
    query(User).filter(User.name.in_(['ed','wendy','jack']))
    # 取反操作
    query(User).filter(~User.name.in_(['ed','wendy','jack']))
    ```

-   **空查询** is null & **非空查询** is not null

    ```python
    # 空查询
    query(User).filter(User.name==None)
    # 或者
    query(User).filter(User.name.is_(None))
    
    # 非空查询
    query(User).filter(User.name != None)
    # 或者
    query(User).filter(User.name.isnot(None))
    ```

-   多条件查询  and  & or

    -   并且查询  **and_** 

        ```python
        query(User).filter(and_(User.name=='ed',User.fullname=='Ed Jones'))
        # 或者，传递多个参数	
        query(User).filter(User.name=='ed',User.fullname=='Ed Jones')
        # 或者，	通过多次filter操作
        query(User).filter(User.name=='ed').filter(User.fullname=='Ed Jones')
        ```

    -   或者查询   **or_**

        ```python
        query(User).filter(or_(User.name=='ed',User.name=='wendy'))
        ```

### SQLAlchemy实现外键及其四种约束

>   实现外键以及四种约束，不得不说的就是表关系，表关系很好理解，无非就是**一对一，一对多，多对多**这三种关系，那么这三种关系后面会使用ORM来模拟的，现阶段先学习怎么样**创建外键**，以及表关系有**哪四种约束关系**。

#### 创建外键

简而言之就是：在从**表中**增加一个字段，指定**这个字段外键**的**是哪个表的哪个字段**就可以了。需要使用**sqlalchemy.ForeignKey()**函数来创建外键

>   **注意：**从表中外键的**字段**，必须和主表的主键**字段类型保持一致。**

```python
uid = Column(Integer,ForeignKey(User.id))
uid = Column(Integer,ForeignKey('user.id'))
```

#### 四种约束（三种）

说是四种约束，其实是三种约束，因为第二种约束NO ACTION，在mysql关系型数据库中和RESTRICT一样一样的。

-   **RESTRICT**（默认项）：若子表中有父表对应的关联数据，删除父表对应数据，会阻止删除

-   **NO ACTION**：在MySQL中，同RESTRICT

-   **CASCADE**：级联删除

    >   举个栗子：
    >
    >   一个班级里面有很多个学生，假如把这个班级删除了，那么里面的学生也没了

-   SET NULL：父表对应数据被删除，子表对应数据项会设置为NULL，滞空删除

    >   只删除外键表，不删除主表里的数据

#### 代码实现

```python
# 需求 ：SQLAlchemy实现外键以及四种约束
# 用户表  
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer,autoincrement= True,primary_key=True)
    uname = Column(String(50),nullable=False)
    def __repr__(self):
        return '<id={id},uname = {uname}>'.format(id=self.id,uname = self.uname)

# 新闻表
class News(Base):
    __tablename__ = 'news'
    id = Column(Integer,autoincrement=True,primary_key=True)
    title = Column(String(80),nullable=False)
    content = Column(Text,nullable=False)
    # 创建外键 ForeignKey，    并且默认删除策略为RESTRICT
    # uid = Column(Integer,ForeignKey(User.id))
    # uid = Column(Integer,ForeignKey('user.id'))
    # 四种约束      RESTRICT、NO ACTION、CASCADE、SET NULL
    # uid = Column(Integer, ForeignKey('user.id',ondelete="RESTRICT"))
    # uid = Column(Integer, ForeignKey('user.id', ondelete="NO ACTION"))
    # uid = Column(Integer, ForeignKey('user.id', ondelete="CASCADE"))
    uid = Column(Integer, ForeignKey('user.id', ondelete="SET NULL"))
    def __repr__(self):
        return "<id = %s,title = %s,content = %s,uid=%s>"%(self.id,self.title,self.content,self.uid)

Base.metadata.drop_all()
Base.metadata.create_all()

# 添加测试数据
user = User(uname= 'MGorz')
session.add(user)
session.commit()
```

## ORM层面（relationship）

### ORM层面外键和一对多关系

>   如上例子中，想要拿到那篇文章作者是谁，用mysql的外键可以拿到，但是很麻烦，代码量也很多。
>
>   所以SQLAlchemy提供了一个**relationship**。这个类可以定义属性，以后在访问相关联的表的时候就直接可以通过属性访问的方式就可以访问得到了
>
>   **SQLAlchemy.orm.relationship**



**优化**：使用relationship时，可以把正向通过反向声明，结合backref参数。

**好处**：可以通过【新闻】导入【作者】，分支也ok。

#### 代码实现（相对于上一个代码的增加）

```python
from sqlalchemy.orm import relationship
class User(Base):
# 需求2
    # 添加属性优化两个表的查询操作
    # newss = relationship("News")
    # 上述代码优化，通常会把它通过反向声明的方式写在“多”的那一方
    
class News(Base):
# 添加属性，优化2表查询操作
    # 正向
    # author = relationship("User")
    # 最终，会把正向和反向关系写在一起
    author = relationship("User",backref = "newss")
# 需求：ORM层面外键和一对多关系
# 需求1 ：查询谋篇新闻的  作者
# news = session.query(News).first()
# print(news)
# print(news.uid) # 拿到这篇新闻是谁写的  哪个id写的
# user = session.query(User).get(news.uid  == 1)
# print(user)
# print(user.uname)
# 结论上述代码，可以实现需求，但是操作太麻烦，可以引入基于ORM模型的 relationship进行优化（查询优化）
news = session.query(News).first()
print(news.author.uname)

# 需求2 查询XX作者的全部新闻
user = session.query(User).first()
print(user.newss)


# 需求：ORM层面外键和一对多关系，引入relationship以后的好处
# 好处1 :查询更简单
# 好处2：添加数据也进行了优化
# 可以通过添加【用户】来添加【新闻】
# user = User(uname = "lulu")
# news1 = News(title= "ccc",content = '88888888')
# news2 = News(title= "bbbb",content = '9999')
# print(type(user.newss))

# 关联
# user.newss.append(news1)
# user.newss.append(news2)

# session.add(user)
# session.commit()


# 可以通过添加【新闻】来添加【用户】
news3 = News(title = "EE",content = "asdasdas")
user = User(uname = "谈谈")
news3.author = user
print(type(news3.author))
```

### ORM层面外键和一对一关系

>   在sqlalchemy中，如果想要将两个模型映射成一对一的关系，那么应该在父模型中，指定引用的时候，要传递一个**uselist=False（默认是True）**这个参数进去，告知父模型，以后引用这个模型，不再是一个列表，而是一个对象。

#### 实现一对一关系是通过参数uselist = Flase实现的

#### 具体格式

-   ##### 方式一（主从类都有代码）

-   ##### 方式二（只有从类里面有代码）（常用！！）

    >   需要sqlalchemy,orm.backref函数

#### 好处

-   添加数据
-   查询数据

#### 代码实现

```python
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer,autoincrement= True,primary_key=True)
    uname = Column(String(50),nullable=False)
    # 需求2
    # 添加属性优化两个表的查询操作
    # newss = relationship("News")
    # 上述代码优化，通常会把它通过反向声明的方式写在“多”的那一方
    #  一对一关系的表示 方式1
    # extend = relationship("UserExtend",uselist = False)
    
class UserExtend(Base):
    __tablename__ = 'user_extend'
    id = Column(Integer,autoincrement=True,primary_key=True)
    school = Column(String(50),nullable=False)
    # 外键
    uid = Column(Integer,ForeignKey(User.id))
    # 一对一关系的表示 方式1
    # user = relationship('User')
    # 方式二  用的较多 ，常用
    user = relationship('User',backref = backref('extend',uselist = False))

# 需求：基于ORM外键，怎么表示一对一
# 添加数据 （好处1） User 添加UserExtend
user = User(uname = '张三')
school = UserExtend(school = "山东大学")
user.extend = school
# print(type(user.extend))
session.add(user)
session.commit()


# 添加数据 （好处1）   反方向操作 通过UserExtend添加user
school = UserExtend(school = '清华')
user2 = User(uname = "李四")
school.user = user2
# print(type(school.user))
session.add(school)
session.commit()


# 查询数据
user3 = session.query(User).first()
print(user3)
print(user3.extend.school)
```

### ORM层面外键和多对多关系

>   把多对多分解为两个一对多的关系，这样就需要引入中间表实现。

#### 联合主键：非空且唯一

>   举个栗子：
>
>   有两个字段，字段1和字段2 ，1对应1 ，1对应2 ，2对应1 上述都是唯一的，如果第四条数据出现了字段1 和字段 1的组合，就不是联合主键，不满足主键约束

#### 步骤：

>   思想：要实现多对多的关系一定需要通过一张**中间表**来绑定他们之间的关系。

1.  首先把**两个需要做多对多的模型定义**出来。

    ```python
    class New(Base):
        __tablename__ = 'news'
        id = Column(Integer,autoincrement=True,primary_key=True)
        title = Column(String(50),nullable=False)
        
        def __repr__(self):
            return "<title = %s>"%(self.title)
    
    # 表2
    class Tag(Base):
        __tablename__ = "tag"
        id = Column(Integer,autoincrement=True,primary_key=True)
        name = Column(String(50),nullable=False)
    
        def __repr__(self):
            return "<name = %s>"%(self.name)
    ```

2.  使用**Table定义**（sqlalchemy.Table）一个中间表，中间表一般就是**包含两个模型的外键字段**就可以了，并且让他们两个来作为一个“**复合主键**”。

    ```python
    news_tag = Table(
        'news_tag',
        Base.metadata,
        # 中间表一般就是包含两个模型的外键字段就可以了，并且让他们两个来作为一个“复合主键”
        Column("news_id",Integer,ForeignKey('news.id'),primary_key=True),
        Column("tag_id",Integer,ForeignKey('tag.id'),primary_key=True),
    )
    ```

3.  在两个需要做多对多的模型中**随便选择**一个模型，定义一个**relationship**属性，来绑定三者之间的关系，在使用relationship的时候，需要传入一个**secondary=中间表对象名**

    ```python
     # c产生关系写法2
        # 本模型中定义的属性 = relationship('模型名',backref = 'tag'(ps:引号中的相当于在另一个模型中定义了这个属性)，secondary = 中间表名字)
        newss = relationship('New',backref = 'tag',secondary = news_tag)
    ```

#### 整体代码实现

```python
# 需求：orm层面 外键和多对多关系的实现

# 中间表
news_tag = Table(
    'news_tag',
    Base.metadata,
    # 中间表一般就是包含两个模型的外键字段就可以了，并且让他们两个来作为一个“复合主键”
    Column("news_id",Integer,ForeignKey('news.id'),primary_key=True),
    Column("tag_id",Integer,ForeignKey('tag.id'),primary_key=True),
)

# 表1
class New(Base):
    __tablename__ = 'news'
    id = Column(Integer,autoincrement=True,primary_key=True)
    title = Column(String(50),nullable=False)
    # 产生关系的写法1
    # tag = relationship('Tag',backref = 'news',secondary = news_tag)

    def __repr__(self):
        return "<title = %s>"%(self.title)
      
# 表2
class Tag(Base):
    __tablename__ = "tag"
    id = Column(Integer,autoincrement=True,primary_key=True)
    name = Column(String(50),nullable=False)
    # c产生关系写法2
    # 本模型中定义的属性 = relationship('模型名',backref = 'tag'(ps:引号中的相当于在另一个模型中定义了这个属性)，secondary = 中间表名字)
    newss = relationship('New',backref = 'tag',secondary = news_tag)

    def __repr__(self):
        return "<name = %s>"%(self.name)

# Base.metadata.drop_all()
# Base.metadata.create_all()

# 添加数据的好处
# newss1 = New(title = '世界第一')
# newss2 = New(title = '世界第二')

# tag1 = Tag(name = '张仨')
# tag2 = Tag(name ='李希')

# newss1.tag.append(tag1)
# newss1.tag.append(tag2)

# newss2.tag.append(tag1)
# newss2.tag.append(tag2)

# session.add_all([newss1,newss2])
# session.commit()

# 查询数据的好处
newss3 = session.query(New).first()
print(newss3.tag)

tag3 = session.query(Tag).first()
print(tag3.newss)
```

### ORM层面删除数据注意事项

1.  ORM层面删除数据后，会无视mysql级别的外键约束
2.  直接会将对应的数据删除，然后将从表中的那个外键设置为NULL
3.  如果想避免这种行为，应该将表中的外键**nullable = Flase**

#### 代码实现

```python
#若  uid = Column(Integer,ForeignKey("user.id")) 没有声明非空，删除父表能成功，会将子表数据 对应项置为空

#解决  若uid = Column(Integer,ForeignKey("user.id"),nullable=False) 会被阻止删除父表

user = session.query(User).first()

session.delete(user)

session.commit()
```

### ORM层面的relationship方法中的cascade（级联）属性使用

#### save-update

>   **默认选项**。在添加一条数据的时候，会把**其他和他相关联的数据都添加到数据库**中。这种行为就是save-update属性影响的。

#### delete

>   表示当**删除某一个模型中的数据**的时候，是否也删掉**使用relationship和他关联的数据。**

#### save-update+delete代码实现

```python
# 模块引入
from sqlalchemy import create_engine,Column,String,Integer,ForeignKey,Text
from sqlalchemy.ext.declarative  import declarative_base
from sqlalchemy.orm import sessionmaker,relationship,backref
from sqlalchemy.dialects.mysql import LONGTEXT

# 用户类
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, autoincrement=True, primary_key=True)
    uname = Column(String(50), nullable=False)
# 文章类
class Article(Base):
    __tablename__ ='article'
    id = Column(Integer, autoincrement=True, primary_key=True)
    title = Column(String(50), nullable=False)
    # 外键
    uid = Column(Integer, ForeignKey('user.id'))
    # author = relationship("User", backref='article')  # cascade默认为save-update
    # author = relationship('User', backref='article', cascade='')    # 出现警告，只添加了article，没有添加user
    # author = relationship('User', backref = 'article',cascade = 'save-update')  # 明文指定和默认的效果相同
    # cascade = delete  默认会产出此表数据，但不删除外键表数据
    # author = relationship('User', backref = 'articles',cascade = 'save-update,delete')   # 这种操作全部删除，此表+外键表
    # 验证反向影响。
    # author = relationship('User')
    # 优化双向关系的最终写法。
    author = relationship('User', backref=backref('articles',cascade ='save-update,delete' ),cascade='save-update,delete')
    # 验证反向影响（User→Article）
    # articles = relationship('Article', cascade='save-update,delete')

# 添加数据函数
def add_data():
    # 删除+创建
    Base.metadata.drop_all()
    Base.metadata.create_all()
    # # 生成用户+生成一篇文章
    user = User(uname='MGorz')
    article = Article(title='华为5G')
    # 绑定关系
    article.author = user
    # 添加+提交
    session.add(article)
    session.commit()

# 删除数据函数
def delete_data():
    # relationship 里面的cascade，可以通过Article影响User

    # article = session.query(Article).first()
    # session.delete(article)
    # session.commit()
    
    # 让user反向影响Article
    user = session.query(User).first()
    session.delete(user)
    session.commit()

if __name__ == '__main__':
    # add_data()
    delete_data()

# 总结1 ：relationship 里面的cascade，可以通过Article影响User，反过来User也可以影响Article（√）

# 总结2 ：relationship 里面的cascade,只会影响当前类User中的relationship的模型Article,不会影响别的模型(Comment)√

```

#### delete-orphan（几乎不用）

>   表示当对一个ORM对象**解除了父表中的关联对象**的时候，**自己便会被删除掉**。当然如果**父表中的数据被删除**，**自己也会被删除**。
>
>   注意：这个选项只能用在一对多上，并且还需要在子模型中的relationship中，增加一个single_parent=True的参数。
>
>   说的就是，当一个爸爸一个儿子的时候，如果爸爸不认儿子，那么儿子就不再是儿子就会被删除，如果爸爸的基因都木得了，那么儿子也就不存在了。

#### merge（两个维度）

>   默认选项。当在使用session.merge，合并一个对象的时候，会将使用了relationship相关联的对象也进行merge操作。

#### expunge

>   移除操作的时候，会将相关联的对象也进行移除。**这个操作只是从session中移除，并不会真正的从数据库中删除。**

#### all

>   是对save-update, merge, refresh-expire, expunge, delete几种的缩写。
>
>   **注意**：不包括delete-orphan

## join的使用—高级查询之多表查询

>   1.  join分为left join（左外连接）和right join（右外连接）以及内连接（等值连接）。
>   2.  在sqlalchemy中，使用join来完成内连接。在写join的时候，如果不写join的条件，那么**默认将使用外键来作为条件连接。**
>   3.  查询出来的字段，跟join后面的东西无关，而是取决于query方法中传了什么参数。（**模型名=全表；模型名.属性=表名.字段**）。
>   4.  在sqlalchemy中，使用**outerjoin**来完成外连接（默认是左外连接）。

#### 代码实现

```python
#找到所有的用户，按照发表的文章数量进行排序
#注意1：在sqlalchemy中，使用join来完成内连接
def oper1():
    # sql语句
    # select user.uname,count(article.id) from user join article on user.id=article.uid group by user.id order by count(article.id) desc;
    # query（内容，和Article.id连接）.join(Article中，user.id和article.id相等).group_by(根据User内id进行分组).order_by(按照articles的id倒叙排序)
    # count()聚合函数
    # result = session.query(User.uname, func.count(Article.id)).join(Article,User.id==Article.uid).group_by(User.id)\
    #     .order_by(func.count(Article.id).desc())
    # print(result) #sql语句
    result = session.query(User.uname, func.count(Article.id)).join(Article, User.id == Article.uid).group_by(
        User.id).order_by(
        func.count(Article.id).desc()).all()
    print(result)  # 结果:列表

#找到所有的用户，按照发表的文章数量进行排序
#注意2：在写join的时候，如果不写join的条件，那么默认将使用外键来作为条件连接。
def oper2():
    result = session.query(User.uname, func.count(Article.id)).join(Article).group_by(
        User.id).order_by(
        func.count(Article.id).desc()).all()
    print(result)  # 结果:列表

#找到所有的用户，按照发表的文章数量进行排序
#注意3： 查询出来的字段，跟join后面的东西无关，而是取决于query方法中传了什么参数。（模型名=全表；模型名.属性=表名.字段）
def oper3():
    result = session.query(User.uname).join(Article).group_by(
        User.id).order_by(
        func.count(Article.id).desc()).all()
    print(result)  # 结果:列表
```

## subquery的使用—高级查询之子查询

1.  将子查询按照传统的方式写好查询代码，然后在`query`对象后面执行`subquery`方法，将这个查询变成一个子查询。
2.  在子查询中，将以后需要用到的字段通过`label`方法，取个别名。
3.  在父查询中，如果想要使用子查询的字段，那么可以通过子查询的返回值上的`c`属性拿到（c=Column）。

#### 代码实现

##### 传统模式

```python
#实现思路1：传统方式
def oper1():
    # 传统模式，两次查询
    u = session.query(User).filter(User.uname == '一哥').first()
    users = session.query(User).filter(User.city==u.city,User.age==u.age).all()
    print(users)
```

##### 子查询

```python
#实现思路2：子查询方式
#原生sql：select  `user`.id,`user`.uname,`user`.city,`user`.age from user,
       # (select `user`.city,`user`.age from user where uname='一哥') as yige
       # where `user`.city=yige.city AND `user`.age=yige.age
def oper2():
    # 加上.subquery()就变成了子查询
    # stmt = session.query(User.city.label('city'), User.age.label('age')).filter(User.uname == '一哥').subquery()
    # # label
    # # 属性c
    # result = session.query(User).filter(User.city == stmt.c.city, User.age == stmt.c.age)
    # print(result) #查看sql语句
    stmt = session.query(User.city.label('city'), User.age.label('age')).filter(User.uname == '一哥').subquery()
    result = session.query(User).filter(User.city == stmt.c.city, User.age == stmt.c.age).all()
    print(result)  # 查看结果
```

## aliased的使用—高级查询之别名使用

#### 使用场景:

1.  当多表关联查询的时候
2.  有时候同一个表要用到多次

#### 代码实现

```python
from sqlalchemy.orm import aliased
# 取别名
a1 = aliased(User)
a2 = aliased(User)

def oper1():
    for uname, age1, age2 in session.query(User.uname,a1.age, a2.age).join(            a1,User.id==a1.id).join(a2,a1.id==a2.id).all():
        print(uname, age1, age2)

```

# Flask-SQLAlchemy

>   这是专门为Flask框架靠拢的，对SQLAlchemy进行简单封装的框架。
>
>   要分清楚SQLAlchemy和Flask-SQLalchemy
>
>   使得在flask中使用sqlalchemy更加简单

### 基本操作

##### 数据库连接

>   数据库初始化不再是通过create_engine。
>
>   1.  跟sqlalchemy一样，定义好数据库连接字符串**DB_URI**。
>
>   2.  将这个定义好的数据库连接字符串DB_URI，通过**`SQLALCHEMY_DATABASE_URI`这个key名配置到`app.config`中。**
>
>       代码：app.config["SQLALCHEMY_DATABASE_URI"] = DB_URI
>
>   3.   使用`**flask_sqlalchemy.SQLAlchemy`这个类定义一个对象，并将`app`传入进去。**
>
>       代码：db = SQLAlchemy(app)

##### 创建ORM模型类	

>   之前都是通过Base = declarative_base()来初始化一个基类，然后再继承，在Flask-SQLAlchemy中更加简单了。
>
>   1.  还是跟使用sqlalchemy一样，定义模型。现在不再是需要使用`delarative_base`来创建一个基类。而是使用`**db.Model**`来作为基类。
>   2.    在模型类中，**`Column`、`String`、`Integer`以及`relationship`等，都不需要导入了，直接使用`db`下面相应的属性名就可以了。**
>   3.    （不是很推荐哦）**在定义模型的时候，可以不写`__tablename__`，那么`flask_sqlalchemy`会默认使用当前的模型的名字转换成小写来作为表的名字，并且如果这个模型的名字用到了多个单词并且使用了驼峰命名法，那么会在多个单词之间使用下划线来进行连接，虽然flask_sqlalchemy给我们提供了这个特性，但是不推荐使用。（增强代码可读性，提高团队合作效率）

##### 将ORM模型映射到数据库表

>   写完模型类后，要将模型映射到数据库的表中，使用以下代码即可
>
>   ​        删除数据库表：**db.drop_all()**
>
>   ​        创建数据库表：**db.create_all()**

##### session的使用

>   以后session也不需要使用`sessionmaker`来创建了，
>
>   ​        直接使用`**db.session**`就可以了，
>
>   ​        操作这个session的时候就跟之前的`sqlalchemy`的`session`是一样一样的。

##### 查询数据

>    1.**单表查询**
>
>   ​          查询数据不再是之前的session.query方法了，而是将query属性放在了db.Model上，
>
>   ​          所以查询就是通过“模型名.query”的方式进行查询了，`query`就跟之前的sqlalchemy中的query方法是一样用的。
>
>    2.**多表查询**     
>
>   ​          如果查找数据涉及多个模型，只能使用db.session.query(模型名).all() 这种方式

##### 修改数据+删除数据+添加数据

>   和之前的没有区别，只是session成为了一个db的属性

#### 代码实现

```python
from flask import Flask
from flask_sqlalchemy import  SQLAlchemy

app = Flask(__name__)

HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'first_sqlalchemy'
USERNAME = 'root'
PASSWORD = 'root'
DB_URI ="mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8".format(username=USERNAME,password=PASSWORD,host=HOSTNAME,port=PORT,db=DATABASE)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI

#1.连接数据库
db = SQLAlchemy(app)

#2.创建ORM模型
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    uname = db.Column(db.String(50),nullable=False)
    def __repr__(self):
        return "<User(uname: %s)>" % self.uname
      
class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    title = db.Column(db.String(50),nullable=False)
    uid = db.Column(db.Integer,db.ForeignKey("user.id"))
    author = db.relationship("User",backref="articles")

#3.删除表
db.drop_all()

#4.创建表
db.create_all()

#5.添加数据
user = User(uname='莫莫')
article = Article(title='华为5G  算法突破了，俄罗斯小伙突破的')
article.author = user
db.session.add(article)
db.session.commit()

#6.查询数据
# users = User.query.all()  #等价于 db.session.query(User).all()
# print(users)
# 在query属性之后  可以用 order_by 、 filter、filter_by、group_by、having等方法进行更复杂的单表查询
# 若要进行更复杂的多表查询，只能使用db.session.query(User).all() 这种方式
#如 order_by
users = User.query.order_by(User.id.desc()).all()
print(users)

#7.修改数据
user = User.query.filter(User.uname=='露露').first()
user.uname = '探探'
db.session.commit()

#8.删除数据
user = User.query.filter(User.uname=='探探').first()
db.session.delete(user)
db.session.commit()

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
```

# alembic数据迁移工具

## 迁移步骤（ORM-->迁移文件-->映射到数据库中）

1.  连接数据库+创建ORM模型

    ```python
    # 创建一个model.py模块，在其中定义需要的模型（User），包含id/name/age/gender,gender是后加上的。
    
    # 引入相应的模块，函数
    from sqlalchemy import  String,Integer,Column,create_engine
    from sqlalchemy.ext.declarative import  declarative_base
    
    # 连接数据库操作
    HOSTNAME = '127.0.0.1'
    PORT = '3306'
    DATABASE = 'alembic_demo'
    USERNAME = 'root'
    PASSWORD = 'root'
    
    DB_URI = 'mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8'\
        .format(username = USERNAME,password = PASSWORD,host=HOSTNAME,port=PORT,db=DATABASE)
    
    # 创建Base类
    engine = create_engine(DB_URI)
    Base = declarative_base(engine)
    
    # 创建ORM模型
    class User(Base):
        __tablename__ = 'user'
        id = Column(Integer,autoincrement=True,primary_key=True)
        name = Column(String(50),nullable=False)
        age = Column(Integer,nullable=False)
        gender = Column(String(50))
    ```

2.  利用dos窗口，输入指令，创建仓库

    >   1.  打开dos窗口 window+R cmd
    >   2.  找到项目所在文件 cd 文件目录
    >   3.  运行虚拟python环境 workon 虚拟环境名
    >   4.  创建alembic仓库  alembic init [仓库名字（推荐alembic）]

3.  修改配置文件，把app.py文件导入

    >   1、修改alembic.ini文件中的sqlalchemy.url项，设置为**sqlalchemy.url = driver://user:password@localhost/dbname?charset=utf8**格式
    >
    >   2、修改**alembic/env.py**文件中的**target_metadata = （model中的Base**
    >
    >   **.metadata）**
    >
    >   3、引入相对路径，以及app.py文件
    >
    >   **import sys,os**
    >
    >   **sys.path.append(os.path.dirname(os.path.dirname(__file__)))**
    >
    >   **import  app.py文件名**

4.  自动生成迁移文件

    >   在dos窗口输入：**alembic revision  --autogenerate -m "提示信息"**
    >
    >   注意：提示信息两边必须是双引号，单引号不行哦~

5.  映射到数据库中

    >   dos窗口**alembic upgrade head**，把生成的迁移文件，映射到数据库中。
    >
    >   如果要降级，使用**alembic.downgrade head**

6.  如果要修改ORM模型中的字段，需要重新进行自动生成以及映射步骤

## 常用的alembic命令和参数解释

-   init：创建一个alembic仓库

    >   在创建仓库的时候使用：alembic inin [仓库名]

-   revision：创建一个新的版本文件

    >   一般和 --autogenerate，以及-m函数一起用哦~
    >
    >   alembic revision --autogenerate -m "信息"

-   --autogenrate：自动将当前模型的修改，生成迁移脚本

-   -m ：本次迁移做了哪些修改，用户可以指定这个参数，方便回顾

-   upgrade：将指定的迁移文件映射到数据库中，会执行版本文件中的upgrade函数

    >   作用在映射到数据库的最后一步
    >
    >   一般和head连用alembic upgrade head
    >
    >   本身upgarde后面加的是版本号，但是head就代表最新的版本号，可以这样使用

-   downgrade：会执行指定版本的迁移文件中的downgrade函数

-   [head]：代表最新的迁移脚本的版本号

-   heads：展示head指向的脚本文件的版本号

    >   用法  ：alembic heads

-   history：列出所有的迁移脚本的版本和信息

-   current：展示当前数据库中的版本号

## 常见的错误以及解决方法

1.  创建新版本时候报错 FAILED：Target database is not up to date
    -   **原因**：只要是heads和current不同，current落后于heads版本
    -   **解决方法**： 将current移动到head上，alembic upgrade head
2.  创建新版本时报错 KeyError: 'bb747b02cda0' 或者 FAILED: Can't locate revision identified by 'a65ff5195bc0'
    -   **原因**：数据库中存的版本号不在迁移文件中
    -   **解决方法**：删除versions中的所有迁移文件，删除数据库的所有表

# Flask-SQLAlchemy和alembic联合使用

-   创建连接数据库配置文件+导入

    >   结尾处：SQLALCHEMY_DATABASE_URI = DB_URI

-   创建引擎+ORM模块

    ```python
    # ②，创建引擎
    app.config.from_object(config)
    # 创建db文件哦
    db = SQLAlchemy(app)
    
    class User(db.Model):
        __tablename__ = 'user'
        id = db.Column(db.Integer, autoincrement=True, primary_key=True)
        name = db.Column(db.String(50), nullable=False)
        age = db.Column(db.Integer)
        gender = db.Column(db.String(2))
    ```

-   利用dos窗口，输入指令，创建仓库

    -   打开dos窗口 window+R cmd
    -   找到项目所在文件 cd 文件目录
    -   运行虚拟python环境 workon 虚拟环境名
    -   创建alembic仓库  alembic init [仓库名字（推荐alembic）]

-   修改配置文件，把app.py文件导入

    >   -   修改alembic.ini文件中的sqlalchemy.url项，设置为：sqlalchemy.url = driver://user:password@localhost/dbname?charset=utf8格式
    >   -   修改alembic/env.py文件中的target_metadata = app.db.Model.metadata
    >   -   引入相对路径，以及app.py文件
    >       import sys,os
    >       sys.path.append(os.path.dirname(os.path.dirname(__file__)))
    >       import  app.py文件名

-   自动生成迁移文件

    -   >   在dos窗口输入：**alembic revision  --autogenerate -m "提示信息"**
        >
        >   注意：提示信息两边必须是双引号，单引号不行哦~

-   映射到数据库中

    -   >   dos窗口**alembic upgrade head**，把生成的迁移文件，映射到数据库中。
        >
        >   如果要降级，使用**alembic.downgrade head**

-   如果要修改ORM模型中的字段，需要重新进行自动生成以及映射步骤

# Flask-Script

>   Flask-Script的作用是可以通过命令行的形式来操作Flask。

## 基本使用

1.  创建一个manager.py文件（manager的代码）

2.  导入Manager模块，主app文件中的app

    -   >   from flask_script import Manager
        >
        >   from app import app
        >
        >   manager = Manager(app)

3.  创建manager=Manager(app)

4.  编写manager方法

    -   ```python
        # 1、命令执行
        @manager.command
        def hello():
            print('你好，hello')
        
        # 2、命令执行（带参数）
        @manager.option('-p','-province',dest = 'province')
        @manager.option('-m','-month',dest = 'month')
        def option(province,month):
            print('您请求的省会是：%s,月份是：%s'%(province,month))
        ```

## 案例：快速添加一个账户

>   分为三类，app引入config连接数据库，并创造表，一引入manager把输入的用户名和信息传入表中。

-   manager代码，实现dos窗口互动

    -   函数add_user：将输入的信息，当做ORM模块规定的字段，并返回成功的信息

    -   ```python
        # 3、快速建立后台账号
        @manager.option('-u','--uname',dest="uname")
        @manager.option('-e','--email',dest ="email")
        def add_user(uname,email):
            user = BackendUser(uname=uname,email=email)
            db.session.add(user)
            db.session.commit()
            print('上传成功')
        ```

-   config代码，连接数据库

-   app代码，程序的主页

    -   注意在这里，最开始运行一次，创建数据库就ok了

## 脚本命令的技巧

>   当manager命令慢慢增多，需要额外创建方法页，引入，并且可以给该页的方法，起一个组名，通过manager.add_commend('组名'，方法页的manager)

# Flask-Migrate

## 项目重构

>   -   原结构：把ORM模块全部放入app主py文件，代码可读性降低，需要额外创建一个models文件，放ORM模板，但是因为python不支持双向导入，models引入app中db，也就不可能再有app引入models中的ORM模板。
>   -   新结构：格外创建一个exts文件，单独存放db，这样就可以避免双向引用的问题了

## 介绍

>   flask-migrate是基于Alembic进行的一个封装，并集成到Flask中，所有的迁移操作其实都是Alembic做的，他能跟踪模型的变化，并将变化映射到数据库中。

## 使用

### 由于项目重构了一下，有几个需要注意的点

#### app.py文件

```python
from exts import db
# 这一步保证db能够获取到数据库的config信息
db.init_app(app)
```

#### exts.py文件

```python
from flask_sqlalchemy import SQLAlchemy	
db = SQLAlchemy()   # 注意此时没有吧app对象传递进来，db无话获取数据可配置信息
```

### config.py文件

```python
# 不加这个会显示出很多警告
SQLALCHEMY_TRACK_MODIFICATIONS = False
```

### manager.py文件

```python
from flask_script import Manager
from app import app
from exts import db
from flask_migrate import Migrate,MigrateCommand

# 要把映射到数据库中的模型导入到manager.py中
# 必须要导入user,不然不能实现功能
from models import User
manager = Manager(app)

#绑定app和db到flask-migrate
Migrate(app,db)
# 添加Migrate的所有命令到db下
manager.add_command("db",MigrateCommand)

if __name__ == '__main__':
    manager.run()
```

