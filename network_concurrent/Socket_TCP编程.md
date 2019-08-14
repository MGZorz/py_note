# Socket_TCP编程

## 	TFTP协议

简单的文件传输协议，可以实现简单文件下载**（小文件）**，TFTP的端口为69。

下载文件是把文件分为很多的小部分进行复制下载，比如说分为若干个5MB的小数据块，下载是需要客户端给服务器发送一个数据请求，然后服务器给客户端一个数据包，要注意的是，数据包不能同时发送多个，需要等待客户端返回给服务器一个返回数据包ack包（通知服务器是否收到），第二个数据包才发送出去。

**注意：**服务器的69端口只用于读写操作，ack包不用发到69端口。

当出现丢包的时候：也就是没有返回值的时候，发送信息的端要等待一会，之后再次发送



### **实现TFTP下载器**

​	**下载**：从服务器讲一个文件复制到本机上

​	**下载的过程**：

1. ​	在本地创建一个空文件（和下载的文件同名）

2. ​	向里面写数据（接收到一点就向空文件写一点）

3. ​	关闭（接收完所有数据关闭文件）

   

### **TFTP格式要求**

![1556004728842](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\1556004728842.png)

服务器传送给客户单的数据包每次最大的是516（512+2+2）个字节。

当客户端接收到的数据小于516个字节，就意味着服务器发送完毕了。（如果最后一次恰好为516个字节，会在发送一个为0字节的数据包）

### struct模块

​	**可以按照指定格式将Python数据转换为字符串，该字符串为字节流。**

​	struct模块中最重要的三个函数为pack() , unpack() , calcsize()

​	**pack()**：可以将数据按照协议的要求组织为它所需要的格式，pack(fmt,v1,v2,…)，需要先给定格式**fmt**

​	**unpack()**：反向pack()，解析字符流string，转化为字符串。unpack(fmt,string)

​	**calcsize()**：计算给定的格式占用了多少字节。calcsize(fmt)。

```python
# 构造下载请求数据：'1text.jpg0octet0'
import struct
cmb_buf = struct.pack('!H8sb5sb',1,b'text.jpg',0,b'octet',0)
'''
!H8sb5sb:!表示按照网络运输数据要求的形式来组织数据（占位格式）
H表示将后边的1替代为两个字节
8s相当于8个s占了8个字节
b 占了一个字节
'''


```



## 	TFTP构建下载请求以及实现下载的功能

```python
# 代码块
'''
编写tftp下载需求的  客户端

'''
from socket import *
import struct

udpSocket = socket(AF_INET,SOCK_DGRAM)

# 构建下载请求（按照要求准备格式数据）
# 整体数据为：1text.jpg0octer0
filename = 'bag.jpg'
server_ip = '192.168.2.113'
send_data = struct.pack('!H%dsb5sb'%len(filename),1,filename.encode(),0,'cotet'.encode(),0)

# 创建一个空文件
file = open(filename,'ab')

# 向服务器发送读写请求，只能一次，服务器端服务的端口号为69
udpSocket.sendto(send_data,(server_ip,69))

# 要循环的接收服务器端返回来的数据包信息，和给服务端发送确认包的信息
while True:
    # 接收服务器端的数据包信息
    message = udpSocket.recvfrom(1024)

    # # 查看接收到信息的格式:返回的是一个元组（服务器发送的数据包的内容，（发送方ip，发送方端口号））
    # print(message)

    # 从数据包里面获取【数据块ack_num】的信息
    caozuoma, ack_num = struct.unpack('!HH', message[0][:4])
    print(caozuoma)
    print(ack_num)

    # 服务器端为当前这个客户端服务的端口号
    rand_port = message[1][1]

    # 打印程序泡的次数，以及每次所涉及的内容  操作码 数据块编号 ，每次数据内容的长度，为客户端服务的端口号
    print('操作码：%d  数据块编号：%d 每次数据内容的长度：%d  为客户端服务的端口号：%d'%(caozuoma,ack_num,len(message[0]),rand_port))

    # 额外：做一个异常处理  用操作码判断做处理
    if int(caozuoma) == 5:
        print('您下载的文件不存在！！！')
        break   # 跳出循环

    # 想创建的空文件中写数据
    file.write(message[0][4:])

    # 判断循环结束条件  用数据包的长度来判断
    if len(message[0]) < 516:
        print('文件写入完毕')
        break

    # 给服务器端发送确认包信息
    ack_data = struct.pack('!HH',4,ack_num)
    udpSocket.sendto(ack_data,(server_ip,rand_port))

file.close()
udpSocket.close()


```



## 	网络通信过程+路由器

Packet Tracer 是一个网络模拟环境，由Cisco(思科)公司开发，在Packet Tracer中模拟网络环境。

**信息在网络中通信，最低层的逻辑：**通过0、1（有电流就是1，没电流就是0）来传递。

**默认网关**：是决定一台电脑能否进出外网。

**路由器：**（至少有两个网卡）

1. ​	连接不同的网络
2. ​	确定路由路径



## 	Socket_TCP通信模型（安全、稳定、不易被攻）

在**通信之前**，必须**先等待**建立连接。（**3次握手、4次挥手**）

![1556074240090](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\1556074240090.png)

### 三次握手

1. 客户端发起，第一次握手，SYN seq = x (我想和你建议连接)，数据包。
2. 服务器端发给客户端，把x+1 ，SYN seq =y ,ACK =x+1 ，同时在客户端这边也会把x+1，如果服务器返回的ACK = 客户端的结果，就代表可以连接（我可以让你连接我）
3. 客户端发给服务器端，ACK = y+1 （我正在连接你）

### 四次挥手

分为主动关闭和被动关闭。这两种关闭时不同的。

![1556077731430](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\1556077731430.png)

1. 客户端发起，FIN seq = x+2 ACK =y+1(我要和你关闭连接了)**[主动给被动]**
2. 服务器端发起，ACK = x+3(我收到你不和我建立连接了)**[被动]**
3. 服务器端发起，FIN seq = y+1 (数据传输完毕了，我也想和你断开连接)**[被动]**
4. 客户端发起，ACK = y + 2 (那就分手吧)**[主动]**



## 	TCP协议



## 	Socket编程



## 	HTTP协议

