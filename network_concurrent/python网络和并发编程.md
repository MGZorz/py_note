**（进程和线程面试的重中之重）**！！！

# 第三阶段   python网络和并发编程

## 一、 并发编程

### 1、多进程

​	首先程序开始运行的时候，会创建一个**主进程**，在主进程下我们可以创建**子进程**。子进程依赖于主进程，如果主进程结束，程序就会退出。

(元组中即使只有一个元素，也要带一个逗号)

from multiprocessing import Proces：导入进程包

p = Process(target=run, args=('test',),name= 'test')：创建进程，target表示调用对象，args表示调用对象的位置参数元组,name表示进程的名字。(后两个可以不写，但是target必须写)

p.start()：开始进程

p.join()：让主进程跟随子进程一起结束。

if --name-- == “--main--”（--表示下划线）：在windows中这个东西必须加，不然父进程执行的时候，子进程也会执行一次，加入这个避免递归运行。

### 2、进程类

##### Process类常用方法：

**p.start()**：启动进程，并调用该子进程中的p.run() 。

**p.run()**:进程启动时运行的方法，正是它去调用target指定的函数，我们自定义类的类中一定要实现该方法 。

**p.terminate()****（了解）**：强制终止进程p，不会进行任何清理操作。

**p.is_alive()**:如果p仍然运行，返回<u>True</u>.用来判断进程是否还在运行。

**p.join([timeout])**:主进程等待p终止，<u>timeout</u>是可选的<u>超时时间</u>。

##### Process类的常用属性：

**name** :当前进程的实例别名，默认为Process-N，N为从1开始递增的整数。

**pid**:当前进程实例的PID值。

### 3、多进程默认不共享数据

**global**：导用全局变量

进程之间的数据是独立的，默认情况下互不影响

```python
验证的代码
from multiprocessing import Process
num = 1
def run1():
    global num
    num += 5
    print("子进程1运行中，num = %d"%(num))
def run2():
    global num
    num += 10
    print("子进程2运行中，num = %d"%(num)) 
if __name__ == "__main__":
    print("父进程启动")
    p1 = Process(target=run1)
    p2 = Process(target=run2)
    print("子进程将要执行")
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("子进程结束")

```



### 4、子类的创建

**自定义一个类，继承Process类。**

子类继承父类的时候，父类的私有属性也能继承，但是不知道。

（例：父亲有100元私房钱，儿子继承了，但是父亲不告诉儿子有这100元私房钱，那儿子就不知道有这100元私房钱。）

```python
验证代码块
import multiprocessing
import time
class ClockProcess(multiprocessing.Process):
    def run(self):
        n = 5
        while n>0:
            print(n)
            time.sleep(1)
            n -= 1

if __name__=='__main__':
    p = ClockProcess()
    p.start()
    p.join()
```



### 5、进程池

**通过进程池来创建进程，创建多个进程**

当代码数量很多，就需要用进程池了

###### **multiprocessing.Pool常用函数解析：**

​	**apply_async(func[,args[,kwds]]):**使用非阻塞方式调用**func**(并行执行，堵塞方式必须等待上一个进程退出才能执行下一个进程)，**args**为传递给func的参数列表，**kwds**为传递给func的关键字参数列表。

​	**apply(func[,args[,kwds]])：**(了解就行基本不用)使用阻塞方式调用func。

​	**close()：**关闭Pool， 使其不再接受新的任务。

​	**terminate()：** 不管任务是否完成，立即终止。

​	**join()：** 主进程阻塞， 等待子进程的退出， 必须在close或terminate之后使用。

```python
#验证代码块
from multiprocessing import Pool
import random,time

def work(num):
    print(random.random()*num)
    time.sleep(3)

if __name__ =='__main__':
    po = Pool(3)        # po代表进程池，定义一个进程池，最大进程数为3，默认大小为CPU的核数。
    for i in range(10):
        po.apply_async(work,(i,)) # apply_async选择要调用的目标，每次循环会用空出来的子进程去调用目标。
    po.close()  #   进程池关闭之后不再接收新的请求
    po.join()   #   等待po中所有子进程结束，必须放在close后面

#   在多进程中：主进程一般用来等待，真正的任务都在子程序中执行。


```

### 6、进程间通信—Queue(1)

​	多进程之间，默认是不共享数据的，通过**Queue（队列Q）**可以实现进程间的数据传递。Q本身是一个消息队列，如何添加消息（**入队操作**）：

```python
from multiprocessing import Queue
q = Queue(3)      #初始化一个Queue对象，最多可接受3条消息
q.put(“消息1”)     #添加的消息数据类型不限
q.put("消息2")
q.put("消息3")
print(q.full())
```

​	可以使用**multiprocessing**模块的**Queue**实现多进程之间的数据传递。初始化**Queue()**对象时（例如： q=Queue()） ， 若括号中没有<u>指定最大可接收的消息数量</u>（ 或数量为负值）， 那么就代表可接受的消息数量没有<u>上限</u> 。

**Queue.qsize()：**返回当前队列包含的消息数量。
**Queue.empty()：** 如果队列为空， 返回True， 反之False 。
**Queue.full()：** 如果队列满了， 返回True,反之False。
**Queue.get([block[, timeout]])**： 获取队列中的一条消息， 然后将其从列队中移除， block默认值为True。
	(1)  如果<u>block</u>使用默认值， 且没有设置<u>timeout</u>（单位秒） ， 消息列队如果为空， 此时程序将被**阻塞**（停在读取状态） ， 直到从消息列队读到消息为止，如果设置了timeout， 则会等待<u>timeout</u>秒， 若还没读取到任何消息， 则抛出"**Queue.Empty**"异常 
	(2)  如果block值为False， 消息列队如果为空， 则会立刻抛出“**Queue.Empty**”异常。

**Queue.get_nowait()**:相当Queue.get(Flase)。

**Queue.put(item,[block[,timeout]]):**将item消息写入队列中，block默认为True。

​	(1) 如果block使用默认值，且没有设置timeout(单位秒)，消息列队如果已经没有空间可写入，此时程序将被阻塞（停在写入状态），直到从消息列队腾出空间位置，如果设置了True和timeout，则会等待timeout秒，若还没有空间，则抛出‘Queue.Full'异常。

​	(2)如果block值为Flase,消息列队如果没有可用空间写入，则会立刻抛出‘Queue.Full'异常。

**Queue.put_nowait(item)：**相当于Queue.put(item,False)

```python
# 代码块
from multiprocessing import Queue,Process
import time
def write(q):
    for value in ['a','b','c']:
        print('开始写入：',value)
        q.put(value)
        time.sleep(1)

def read(q):
    while True:
        if not q.empty():
            print('读取到的是',q.get())
            time.sleep(1)
        else:
            break
if __name__ =='__main__':
    q = Queue()
    pw = Process(target= write,args =(q,))
    pr = Process(target = read ,args = (q,))
    pw.start()
    pw.join()
    pr.start()
    pr.join()
    print('接受完毕')
```

### 7、进程间通信—Queue(2)

​	进程池创建的进程之间通信：如果要使用Pool创建进程，就需要使用**multiprocessing.Manager()**中的**Queue()**了

​	否则就会得到错误消息：<u>RuntimeError</u>

```python
# 代码块
from multiprocessing import Manager,Pool
import time
def writer(q):
    for i in 'welcome':
        print('开始写入',i)
        q.put(i)
def reader(q):
    time.sleep(3)
    for i in range(q.size()):
        print('得到消息',q.get())

if __name__ == '__main__':
    print('主进程启动')
    q = Manager().Queue()
    po = Pool()
    po.apply_async(writer,(q,))
    po.apply_async(reader,(q,))
    po.close()
    po.join()

```

### 

