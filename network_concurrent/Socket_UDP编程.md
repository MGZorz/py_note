# Socket_UDP编程

## 		概述

​	1、sendto(‘发送内容’，（（这是个元组）机器的IP,机器的端口)

- 发送的内容是**字节**，不是字符串，但是在**字符串前面+b就可以转化为字节**了，例：b‘hello’，但是用这种方法字符串不能是中文了。
- 或者调用encode()方法，转化。例子：‘hello’.encode()，但是encode()方法是用来**解决中文乱码**的，**括号中是编码的格式**，当你发送给网络调试助手的时候，编码的格式为**gbk**或者**gb2312**。

​			

​	2、**复制代码的当前行**快捷键为ctrl+D、**控制代码上下移动**为ctrl+shift+方向键

​	3、操作之后要关闭Socket对象

​	4、**发送数据给飞秋**：发送数据给飞秋，飞秋使用的是：2425端口。

- 发送普通数据，飞秋不会响应，必须发送特殊格式的内容，**例：**1:123123:吴彦祖:吴彦祖-pc:32:haha（飞秋有自己的应用层协议）

- 1，表示版本，后面的数字发送的时间（随便写），32代表发送消息

  5、**UDP和TCP 的小理解：**

  udp理解为写信（只有收件人地址），TCP理解为打电话（先拨号建立通路，需要通路稳定）

  6、**encode(指定的编码字符集类型)**方法，转化。例子：‘hello’.encode()，但是encode()方法是用来**解决中文乱码**的，当你发送给网络调试助手的时候，编码的格式为**gbk**或者**gb2312**。

  ​	**decode(指定的解码字符集类型)**方法，解码，用法和encode()相似。

  7、**bind()**给socket对象绑定一个IP地址和端口号，用法：udpSocket.bind((‘IP地址’,端口号))。

  **recvfrom(a)**: 括号中的代表这次接收消息是接收a个字节的消息。

  8、**单工、全双工、半双工**

  全双工：一个程序有接收信息和发送信息的能力，而且同时进行的。

  半双工：一个程序有接收信息和发送信息的能力，但是必须分开来做。

  单工：一个程序只具备接收信息的能力或者只具备发送信息的能力。



## UDP编程实例



​	1、echo服务器—聊天室功能的实现（半双工）

```python
'''
echo服务：得到什么就返回什么

客户端：

'''

from socket import *

s = socket(AF_INET,SOCK_DGRAM)
while True:
    # 发送消息

    data = input('请输入发送内容：')
    addr = ('192.168.2.113', 7788)
    s.sendto(data.encode(), addr)

    # 接收信息

    message = s.recvfrom(1024)
    print(message[0].decode())


# 关闭

s.close()
```

```python
'''
echo服务：发送什么，就得到什么

服务器端：
改进1：聊天室功能   把接收信息，和发射消息发到死循环中

改进2：聊天室实现灵活对话

完成情况：实现了半双工的程序

练习：实现全双工，引入多线程
'''

from socket import *
s = socket(AF_INET,SOCK_DGRAM)

# 绑定端口号

s.bind(('',7788))
while True:
    # 接收消息
    message = s.recvfrom(1024)
    print(message[0].decode())

    # 发送消息
    # 将返回的固定消息变成手动输入
    # s.sendto(message[0], message[1])
    data = input('请输入回复内容：')
    s.sendto(data.encode(), message[1])

# 关闭
s.close()
```



## UDP广播

​	![1555989946986](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\1555989946986.png)

​	广播是通过交换机发送的，广播方将数据发送给交换机，如果交换收到的是广播地址（**广播的地址为255**），则就把数据发送给接受方，实现了广播。默认情况下，UDPsocket对象是不让发送广播的。

可以通过**setsocket(SOL_SOCKET,SO_BROADCAST,1)**来修改设置，让其具有能够发送广播的功能。（这个是固定的用法，记住就好了）。

```python
'''
UDP发送广播
'''
from  socket import *
s = socket(AF_INET,SOCK_DGRAM)


# 默认情况下，UDPsocket对象是不让发送广播的
# 需要修改UDPsocket对象的设置
s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)

# 这里是固定写法。
dest = ('<broadcast>',2425)
# 发送广播的数据,发送给局域网中的所有飞秋程序
s.sendto('1:23213:吴彦祖:没有:32:中午吃饭'.encode('gbk'),dest)
# 关闭
s.close()
```

​	

​	