## Scrapy连接数据库

### Scrapy 连接MySQL数据库
需要引入使用pymysql模块，更改Pipeline文件。
*重点在于连接数据库（connect）,以及插入数据（通过指针cursor）*

要注意的一点有：数据库中的datetime数据类型，因为爬虫爬下来的都是str类型的，所以要使用strftime等函数来回的切换。

#### 同步添加数据进入数据库（数据量很少）

- 创建PyMySqlPipeline类（名字可以任意）。
- 对其进行初始化，init函数，定义两个重要的点，connect 和 cursor

    - connect
    - cursor 
- 重写process_parse方法，可以使用原生的SQL语句添加，也可以使用sqlalchemy添加。并且要使用cursor.execute()添加和connect.commit()提交
- 定义close_spider函数关闭爬虫时，关闭指针(cursor)以及连接(connect)

```python
import pymysql
class PyMySqlPipeline(object):
    def __init__(self):
        self.connect = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            password='root',
            db='crawl',
            charset='utf8'
        )
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        print(item)
        insert_sql = "INSERT INTO book(name,star) VALUES ('%s','%s')" % (item['book_name'], item['book_star'])
        self.cursor.execute(insert_sql)
        self.connect.commit()

    def close_spider(self, spider):
        self.cursor.close()
        self.connect.close()
```

#### 异步添加数据（数据量很大）
当数据量很大的时候，爬虫拿取数据的速度要远远大于数据库读入的数据，会造成阻塞，那么就要靠*异步添加数据*来进行处理。
需要借用twisted模块来进行异步处理。
```python
import pymysql
from twisted.enterprise import adbapi
class MySQLPipeline(object):
    '''
        保存到数据库中对应的class
       1、在settings.py文件中配置
       2、在自己实现的爬虫类中yield item,会自动执行'''
    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls, settings):
        '''
        1、@classmethod声明一个类方法，而对于平常我们见到的叫做实例方法。
        2、类方法的第一个参数cls（class的缩写，指这个类本身），而实例方法的第一个参数是self，表示该类的一个实例
        3、可以通过类来调用，就像C.f()，相当于java中的静态方法
        '''
        # 读取settings中配置的数据库参数
        dbparams = dict(
            host=settings['MYSQL_HOST'],
            db=settings['MYSQL_DBNAME'],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASSWD'],
            charset='utf8',  # 编码要加上，否则可能出现中文乱码问题
            cursorclass=pymysql.cursors.DictCursor,
            use_unicode=False,
        )
        dbpool = adbapi.ConnectionPool('pymysql', **dbparams)  # **表示将字典扩展为关键字参数,相当于host=xxx,db=yyy....
        return cls(dbpool)  # 相当于dbpool付给了这个类，self中可以得到

    # 写入数据库中
    def _conditional_insert(self, tx, item):
        sql = "INSERT INTO book(name,star) VALUES ('%s','%s')" % (item['book_name'], item['book_star'])
        tx.execute(sql)

    # 错误处理方法
    def _handle_error(self, failue, item, spider):
        print(failue)

    # pipeline默认调用
    def process_item(self, item, spider):
        query = self.dbpool.runInteraction(self._conditional_insert, item)  # 调用插入的方法
        query.addErrback(self._handle_error, item, spider)  # 调用异常处理方法
        return item
```

### MongoDB插入数据
MongoDB数据库插入数据的代码量要比mysql少很多，并且MongoDB添加时惰性添加，有数据就添加，没数据就关闭，所以这里可以不用写close_spider函数
```python
import pymongo

class MongoPipeline(object):
    def open_spider(self, spider):
        self.db = pymongo.MongoClient('mongodb://localhost:27017')
        self.collection = self.db.book

    def process_item(self, item, spider):
        self.collection.book.insert_one(dict(item))
        return item

```

