# 一、web请求生命周期分析

## 1、概述

​	web请求是基于http协议的，而http协议是基于请求/响应的模式，即一个请求对应一个响应，那么一个web请求（或者说http请求）的生命周期就是指从发起一个web请求到得到web响应的过程

- web请求的发起：一般是指在浏览器中输入一个url地址，但是并不仅限于此，譬如我们在网页中点击一个url链接或者javascript脚本中执行一个url跳转（包括普通的和ajax方式的）等
- web响应的获取：一般是显示在浏览器中的一个页面，但是也并不仅限于此，有些是后台数据的获取，譬如javascript访问的json数据、图片、文件等



## 2、相关知识点

### 1、网络核心结构

​	计算机的网络核心结构，就是TCP/IP五层网络模型（OSI七层网络模型将应用层拆分为三层了），如下图：

![tcp_ip_model](.\imgs\tcp_ip_model.png)

- 发送请求的过程是从最顶层（应用层）出发，每一层负责封装属于自己的信息到请求中，最后将一整个请求发送给对方。

- 接收请求的过程是从最底层（网络接口层）开始，每一层的协议负责解析属于自己的东西，比如网络层(IP)处理ip信息，传输层(TCP)处理点对点的端口，应用层(HTTP)处理Request或Response的Line\Header\Body。

  

### 2、TCP协议

​	TCP(Transmission Control Protocol，传输控制协议)是一种面向连接(连接导向)的、可靠的基于字节流的传输层通信协议。TCP将用户数据打包成报文段，它发送后启动一个定时器，另一端收到的数据进行确认、对失序的数据重新排序、丢弃重复数据。



​	头格式如下(单位 bit)：

![tcp_datagram](.\imgs\tcp_datagram.jpg)

1. Source Port(源端口号）：数据发起者的端口号，16bit。
2. Destination Port(目的端口号）：数据接收者的端口号，16bit。
3. Sequence Number(顺序号码，Seq）：用于在数据通信中解决网络包乱序(reordering)问题，以保证应用层接收到的数据不会因为网络上的传输问题而乱序(TCP会用这个顺序号码来拼接数据），32bit。
4. Acknowledgment Number(确认号码，ack）：是数据接收方期望收到发送方在下一个报文段的顺序号码（Seq），因此确认号码应当是上次已成功收到顺序号码(Seq)加1，32bit。
5. Offset(TCP报文头长度)：用于存储报文头中有多少个32bit(上图的一行)，存储长度为4bit，最大可表示（2^3+2^2+2^1+1）*32bit=60bytes的报文头。最小取值5，5*32bit=20bytes。
6. Reserved(保留)：6bit, 均为0
7. TCP Flags(TCP标识位)每个长度均为1bit

​       CWR：压缩，TCP Flags值0x80。

​       ECE：拥塞，0x40。

​       URG：紧急，0x20。当URG=1时，表示报文段中有紧急数据，应尽快传送。

​       ACK：确认，0x10。当ACK = 1时，代表这是一个确认的TCP包，取值0则不是确认包。

​       PSH：推送，0x08。当发送端PSH=1时，接收端尽快的交付给应用进程。

​       RST：复位，0x04。当RST=1时，表明TCP连接中出现严重差错，必须释放连接，再重新建立连接。

​       SYN：同步，0x02。在建立连接时用来同步序号。SYN=1， ACK=0表示一个连接请求报文段。SYN=1，ACK=1表示同意建立连接。

​       FIN：终止，0x01。当FIN=1时，表明此报文段的发送端的数据已经发送完毕，并要求释放传输连接。

8. 窗口：用来控制对方发送的数据量，通知发放已确定的发送窗口上限。
9. 检验和：该字段检验的范围包括头部和数据这两部分。由发端计算和存储，并由收端进行验证
10. 紧急指针：紧急指针在URG=1时才有效，它指出本报文段中的紧急数据的字节数。
11. TCP选项：长度可变，最长可达40字节



​	三次握手（建立连接的过程，只能客户端发起）：

![](.\imgs\tcp_start.png)

1. 客户端主动发送SYN包到服务器，并进入SYN_SEND状态，等待服务器确认
2. 服务器收到SYN包并确认，发送SYN+ACK到客户端，服务器进入SYN_RECV状态
3. 客户端收到SYN+ACK包，发送ACK确认连接，发送完毕后客户端和服务端进入ESTABLISHED状态，完成三次握手



​	完成三次握手之后，TCP才可以开始进行真正的数据传输



​	四次挥手（断开连接的过程，可以是客户端发起，也可以是服务器端发起，下面以客户端演示）：

![](.\imgs\tcp_end.png)

1. 主机A主动发送FIN包，等待主机B确认
2. 主机B收到FIN包并确认，发送ACK包到主机A
3. 主机B发送FIN包到主机A，并等待主机A确认
4. 主机A收到FIN包并确认，发送ACK包到主机B，并且丢弃连接，主机B收到ACK包后，丢弃连接



### 3、http协议

​	超文本传输协议(HTTP，HyperText Transfer Protocol)是互联网上应用最为广泛的一种网络协议，所有的WWW文件都必须遵守这个标准，属于TCP/IP协议的应用层协议。

​	HTTP是一个属于应用层的面向对象的协议，由于其简捷、快速的方式，适用于分布式超媒体信息系统。它于1990年提出，经过几年的使用与发展，得到不断地完善和扩展。

- 1991年推出HTTP/0.9

- 1996年推出HTTP/1.0

- 1999年推出HTTP/1.1

- 2015年推出HTTP/2

  目前使用最广泛的还是HTTP/1.1版本



​	URL（统一资源定位符）：是一种特殊的URI（统一资源标识符），包含了用于查找某个资源的足够的信息，格式如下：

​	http://host\[:port][abs_path]?arg1=value1&arg2=value2

​	https://host\[:port][abs_path]?arg1=value1&arg2=value2

​	说明如下：

- http或https表示要通过哪个协议来定位网络资源；
- host表示合法的Internet主机域名或者IP地址；
- port指定一个端口号，为空则使用缺省端口（http是80，https是443）；
- abs_path指定请求资源的路径
- ? 之后的内容是请求参数，用于传递数据给服务器



​	http请求：由三部分组成，分别是：请求行、请求头、请求体

![](.\imgs\http_request.png)

​	示例（百度登录请求）：

```
POST /v2/api/?login HTTP/1.1
Host: passport.baidu.com
Connection: keep-alive
Content-Length: 2952
Cache-Control: max-age=0
Origin: https://www.baidu.com
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Referer: https://www.baidu.com/?tn=93882546_hao_pg
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9
Cookie: BAIDUID=311E2F4D0EBD022DEF679D1669ABDA5E:FG=1; BIDUPSID=311E2F4D0EBD022DEF679D1669ABDA5E; PSTM=1518263013; BDRCVFR[MR02hGxyoCt]=n4QtfkUpMj3XZN4pgPWQhPEUf; H_PS_PSSID=; HOSUPPORT=1; FP_UID=46c02caec5901194ab8efae92be3a433; UBI=fi_PncwhpxZ%7ETaKAT9p784t3RaHLuAic2iv9oBYbhONamuLF2uMuBXPcd5myIbqV4zYbuJyfGkNp-qoLA3f

staticpage=https%3A%2F%2Fwww.baidu.com%2Fcache%2Fuser%2Fhtml%2Fv3Jump.html&charset=UTF-8&token=dae86b918bb5266fd7d94132271a6b68&tpl=mn&subpro=&apiver=v3&tt=1518266296874&codestring=jxG4807c1f71181c16d025115c14301247f884a430735047e38&safeflg=0&u=https%3A%2F%2Fwww.baidu.com%2F%3Ftn%3D93882546_hao_pg&isPhone=&detect=1&gid=52342BA-C1AC-4062-BBD0-8C67681E0D24&quick_user=0&logintype=dialogLogin&logLoginType=pc_loginDialog&idc=&loginmerge=true&splogin=rate&username=mumuloveshine&password=KQueIucNzF0fy78bKHTPQxYb0yrvcQ341y3zq0I86foUW9e%2BjGaTwwlgd2MSmMlWCPqJwZbXoim7wqbFuySCjDtz2gFWdrcDiL9I1b2rUWLN5b7vUHBItKXDGcS7g%2FUKzrm%2FaJcQn13f8eRJfUVw4RjczfLnnegXb0ZpdSmcnkE%3D&verifycode=%E5%A5%B3%E5%AD%A9&mem_pass=on&rsakey=zYBPxF7R8Ucf8O5JkF3HPVBCnaY0hRMD&crypttype=12&ppui_logintime=20572&countrycode=&fp_uid=46c02caec5901194ab8efae92be3a433&fp_info=46c02caec5901194ab8efae92be3a433002%7E%7E%7E-r--5LhFGVwgn%7E5_u--4vhxn7nVCBTkCeT_hhxn7nVCBTkneT_V-kTsP-kTsH--sz-k-sQh0I-LXKSCbjKAe6Kn%7EcKCeLjA7YxLX8%7EAOn%7EA7qkC%7Eqjn7ojUOI%7EC74zA7q%7EnmOjUwLaCe6kC7okA7wxLVKSHl2DLVc_%7Eu-qMu-qOu-qtu-ssh0VkcX1aFX2tpXGopVChpJGgFoHWLlhyFZ82pl2tpXG%7EGVwOHEH9plGDMJCwpBCwLVHWLBsD4Ewt4JCPpVH5Gohn4EGOMJfWFlwOHJ1epVjzHJjz3tyVHEr%7EMJ1gAeogCZIj3eoKC%7Eq9Dh0lwHXGl4EGDFbjepVhiFJj94V2zMJ1gLkI%7ECmreCmYOA7q%7E4%7EczA7nIC7nV4%7E6InlHtnlGtHJHlC7FwHmywn%7ECtnmsyneFenJrl4ewy4lClHl2yAXnInXoVUlrt4eHy4e4Kn%7Eye4ecVH72l4JHwCV2wHmCOnlnVHmYln%7E2l4l5hAJcanV4%7En%7ECOn%7EFlHmohn76InXHeHecaAX2xAJ2tCmOkHJ2wCmHyHe5aHmGenXYyH7Cw4%7ET84J5zCmyeC7wOn7TaCerlH7yy47chHX4V4%7E68CVnan7L8CeyeCkjeCeLzn%7E4jH7CwCecjCloKCXre4estn%7EHOnmOhH7COAXCeHX4hnVoaAJYlCJYl4%7EOKnm5KHmTk47TjC7CtA74VUlYwHl2hpbYx4V1ipEGgMJCyFXwWpBCxCXCe4V2w4%7EYlAm5jC%7ECeCl48AXo%7ECmst4lchHJnICeweH72O4%7EYt4Vnhn%7E6KC%7Enanl68nmqhHenanmyOAJojCkjw4eFeCeTaCXo8nX6zCVreAmL%7EnV4knJnVHJYl476hHXnkC%7EOj47COAJGOC7oaA7oz4lchCVClH7TanXGyHm5zAu-sTu-syu-sxu-sW--5KhFRlTi6zI_FhxFJjPpl1kpT__-u-sG--qIu-qYu-qiu-qcu-qau-qNhV37ogCm58Cm6IAm5%7EAmLzC%7E5zC6__&loginversion=v4&dv=tk0.57134848608022451518266276367%40vAt0nmsmad9kr%7E9koc9koy9krcsmacs4ogs4rd9krjsmac24Sgs4Hz9krzs1ac2%7Eogs4Sa9krds1ayskHgsF6%7E9k0j21ay2%7ESgsF5d9ksasS__vt0lBsF0d9kqgJrtBGjuh4JeT6t2oE%7EraEjej5-Jy4WtVCAa-24rj9ksasMaysF3gsmc6o6dp63t2Ejeo6jhTs4hTEzJ%7ECEuBHKjL9kHlsFqgs%7EqyTk0yBAac9tGh43QAo6jTEjh46tvcsteTQE2L53dIOK6g2%7E0zsAa%7Eskuv9kqgJrtBGjuh4JeT6t2oE%7EraEjej5-Jy4WtVCAalB43%7E9ksasMad9kqgJrtBGjuh4JeT6t2oE%7EraEjej5-Jy4WtVCAadB4s-9ksasMa_ut0yB2F6z9kocsAay24o%7E9ma%7Eskuv2%7Eqd9kSg2kq%7EsAags%7EqyTk6-Bmay24Sgs40z2kHgJrtBGjuh4JeT6t2oE%7EraEje-CEuXCMLkO-GL9ksasMaz24rgsFSd9krjBksl9tGh43QAo6jTEjh46tvcsteTQWJyPKCdo-e3C6LVCya%7Eskuv245c9k0%7EsmacB43a2mc6o6dp63t2Ejeo6jhTs4hTEzhI5z2zOzu39ksasMa_BmmC%7Emx37ZTPhxthsAay9kHbztqQnga9F6zs4sbBkol2Fqlsk0y2k6c24rlsFH-sF5-s%7EHzht0LmPpGb5psR9yezQz5ZHWtXCp6ZH-eV9%7EebOFbds%7ESlsF6b2LeUHKeT5n5gQKd3CKCXOWJ3wtlB4og94olsmacs%7Esl9k6c2yacs%7EH-9k5-Bmacs%7EH-9kr%7E2%7E5g2Fra&traceid=54784D01&callback=parent.bd__pcbs__t0v21n
```



​	请求method必须为大写，现在一般只使用GET和POST，所有方法的说明如下：

![](.\imgs\http_method.png)



​	http响应：由三部分组成，响应行、响应头和响应体

![](.\imgs\http_response.png)

​	示例（百度登录返回）：

```
HTTP/1.1 200 OK
Access-Control-Expose-Headers: Trace-ID
Cache-Control: public
Connection: keep-alive
Content-Encoding: gzip
Content-Type: text/html
Date: Sat, 10 Feb 2018 12:38:17 GMT
Expires: 0
Last-Modified: Sat, 10 Feb 2018 12:38:16 12FebGMT
P3p: CP=" OTI DSP COR IVA OUR IND COM "
Pragma: public
Server: Apache
Strict-Transport-Security: max-age=31536000
Trace-Id: 54784D01
Tracecode: 22969190170312486410021020
Tracecode: 22969190170969169930021020
Vary: Accept-Encoding
Transfer-Encoding: chunked

<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
</head>
<body>
<script type="text/javascript">


	var href = decodeURIComponent("https:\/\/www.baidu.com\/cache\/user\/html\/v3Jump.html")+"?"

var accounts = '&accounts='

href += "err_no=7&callback=parent.bd__pcbs__t0v21n&codeString=jxG9007e2f71134c1fc023315e99801277b88a24406f10431e8&userName=mumuloveshine&phoneNumber=&mail=&hao123Param=&u=https://www.baidu.com/%3Ftn%3D93882546_hao_pg&tpl=mn&secstate=&gotourl=&authtoken=&loginproxy=&resetpwd=0&vcodetype=ae20DiYV\/qLGUUeTvt6K91W\/neFrpV1ec8WRrh0h9nSGenOd1efhUH8uDb8AFNyOeVu8G9EJLOnD1f97a3jzAj1o7zbXVVlMs3nq&lstr=&ltoken=&bckv=&bcsync=&bcchecksum=&code=&bdToken=&realnameswitch=&setpwdswitch=&bctime=&bdstoken=&authsid=&jumpset=&appealurl=&realnameverifyemail=0&traceid=54784D01&realnameauthsid="+accounts;


if(window.location){
    window.location.replace(href);
}else{
   document.location.replace(href); 
}
</script>
</body>
</html>
```



### 4、服务器相关协议

​	web协议，是web服务器和web请求处理程序之间传输数据的一种标准协议，发展史为：

CGI -> FCGI -> WSGI

​	说明如下：

- CGI：通用网关接口（Common Gateway Interface/CGI），最早的web协议

- FCGI：Fast CGI，在CGI基础上，提高了服务性能

- WSGI：Web Server Gateway Interface，专用于python程序，在CGI的基础上改进的协议

  

- uwsgi：uWSGI服务程序自有的协议（不是一个web协议），常用于在uWSGI服务器与其他网络服务器程序的数据通信，与WSGI没有关系。

  ​	uWSGI是一个Web服务器程序，它实现了WSGI、uwsgi、http等协议。uWSGI起何作用，取决于架构方式：

  - 如果架构是Nginx+uWSGI+Django， 那么uWSGI是一个中间件
  - 如果架构是uWSGI+Django，那么uWSGI是一个web服务器



### 5、nginx服务器

​	nginx是一个高性能的HTTP和反向代理服务器。

​	什么是正向代理、反向代理？

1. 正向代理，例如平时我们使用的加速器、翻墙等代理就是正向代理，客户机请求代理服务器，代理服务器转发请求到对应的目标服务器
2. 反向代理，部署在Web服务器上，代理所有外部网络对内部网络的访问。浏览器访问服务器，必须经过这个代理，是被动的。 



​	正向代理的主动方是客户端，反向代理的主动方是Web服务器。

​	

​	反向代理的作用：

1. 安全，客户端对Web服务器的访问需要先经过反向代理服务器。这样可以防止外部程序对Web服务器的直接攻击。
2. 负载均衡，反向代理服务器可以根据Web服务器的负载情况，动态地把HTTP请求交给不同的Web服务器来处理，前提是要有多个Web服务器。
3. 提升Web服务器的IO性能。一个HTTP请求的数据，从客户端传输给服务器，是需要时间的，例如N秒，如果直接传给Web服务器，Web服务器就需要让一个进程阻塞N秒，来接收IO，这样会降低Web服务器的性能。如果使用反向代理服务器，先让反向代理服务器接收完整个HTTP请求，再把请求发给Web服务器，就能提升Web服务器的性能。还有一些静态文件的请求，可以直接交给反向代理来处理，不需要经过Web服务器。



## 3、生命周期分析

### 1、客户端发送请求

1. 在浏览器输入url，譬如www.baidu.com，浏览器会自动补全协议（http），变为http://www.baidu.com，现在部分网站都实现了HSTS机制，服务器自动从http协议重定向到https协议
2. 在网页中点击超链接或javascript脚本进行url跳转，仅设置 href=‘绝对路径’，浏览器会自动使用当前url的协议、host和port，譬如在 https://tieba.baidu.com/index.html网页中，点击一个超链接 /f?kw=chinajoy ， 会自动访问 https://tieba.baidu.com/f?kw=chinajoy



### 2、路由转发

1. IP查找：因特网内每个公有IP都是唯一的，域名相当于IP的别名，因为我们无法去记住一大堆无意义的IP地址，但如果用一堆有意义的字母组成，大家就能快速访问对应网站
2. DNS解析：通过域名去查找IP，先从本地缓存查找，其中本地的hosts文件也绑定了对应IP，若在本机中无法查到，那么就会去请求本地区域的域名服务器（通常是对应的网络运营商如电信），这个通过网络设置中的LDNS去查找，如果还是没有找到的话，那么就去根域名服务器查找，这里有所有因特网上可访问的域名和IP对应信息（根域名服务器全球共13台）
3. 路由转发：通过网卡、路由器、交换机等设备，实现两个IP地址之间的通信。用到的主要就是路由转发技术，根据路由表去转发报文，还有子网掩码、IP广播等等知识点



### 3、建立连接

​	通过TCP协议的三次握手建立连接



### 4、传输报文

​	建立连接后，客户端会通过TCP依次、有序的发送一定大小的报文，其中包括了超时重传、阻塞窗口等等概念，用来保证数据包的完整、有序

- http协议使用的明文传输，所有内容都是直接可读的
- https协议是基于SSL/TLS加密，而SSL/TLS是基于TCP协议的，也就是http协议报文包装成TCP报文进行的加密，使用https协议的话，如果本地没有证书和公钥，那么会从服务器获取证书并且进行验证，流程如下：

![](.\imgs\https_download_cert.png)



### 5、nginx处理

​	当前django框架开发的web项目，主流使用的服务器架构是：nginx+uWSGI+django，本文档就以此种架构方式做分析。

​	nginx监听公网IP的某个端口，譬如80，接收到请求后，分2种情况处理请求：

1. 如果是静态资源（如javascript、css、图片等）的请求，那么nginx直接获取到该资源，返回给用户
2. 如果是动态内容的请求，那么nginx就将请求转发到uWSGI，使用的协议一般都是uwsgi，性能最好



PS：

- 有些reqeust会分多个数据包进行发送，nginx会缓存等待整个request接收完成才调用uWSGI
- 如果使用的https，那么加密、解密都在nginx中进行处理



### 6、uWSGI处理

​	uWSGI监听本机IP的某个端口，譬如3308，接收到nginx转发来的请求后，通过将http协议转换为WSGI协议，和django程序之间进行通信

​	

### 7、WSGIHandler处理

​	当django接受到一个请求时，会初始化一个WSGIHandler，可以在项目下的wsgi.py文件进行跟踪查看：

```python
class WSGIHandler(base.BaseHandler):
    request_class = WSGIRequest

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.load_middleware()

    def __call__(self, environ, start_response):
        set_script_prefix(get_script_name(environ))
        signals.request_started.send(sender=self.__class__, environ=environ)
        request = self.request_class(environ)
        response = self.get_response(request)
        
    ......
```

它接受2个参数：

- environ：是含有服务器端的环境变量
- start_response：可调用对象，返回一个可迭代对象。

这个handler控制了从请求到响应的整个过程，首先的就是加载django的settings配置，然后就是调用django的中间件开始操作



### 8、middleware的process_request

​	中间件的process_request方法列表对request对象进行处理

​	

​	django项目默认有一些自带的中间件，如下：

```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```

​	一般情况下这些中间件都会启用，如果需要增加自定义的中间件（该中间件类必须继承MiddlewareMixin），一般是添加在系统的中间件之下，如：

```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
    # 自定义中间层
    'my_app.middleware.MyMiddleware',
]
```

​	

​	中间件中主要有以下方法（一个中间件类最少需要实现下列方法中的一个）：

- process_request：处理请求对象

  参数：request

  返回：

  - response：调用process_response列表处理
  - None：调用下一个中间件的process_request处理

- process_response：处理响应对象

  参数：request, response 

  返回：

  - response：调用上一个中间件的process_response处理

    

- process_view：视图预处理，在视图函数处理之前调用

  参数：request，view_func，view_args，view_kwargs

  ​	view_func：url路由匹配到的视图函数

  ​	view_args：视图函数的可变参数

  ​	view_kwargs：视图函数的可变关键字参数

  返回：

  - response：调用process_response处理
  - None：调用下一个中间件的process_view处理

- process_exception：在视图函数或中间件处理过程抛出异常时调用

  参数：request，exception

  ​	exception：是处理过程中抛出的异常对象

  返回：

  - response：之后的process_exception都不会触发，而是调用process_response处理
  - None：调用上一个中间件的process_exception处理

- process_template_response：在视图函数完成操作后调用，默认不执行，除非视图函数返回的response中有render方法

  参数：request，response

  ​	response：不是HttpReponse，而是SimpleTemplateResponse对象，具有render方法

  返回：

  - response：SimpleTemplateResponse对象，调用上一个中间件的process_template_response处理，最后一个process_template_response处理完成后，会自动调用 response对象中的render方法，得到一个HttpResponse对象，进行返回，再调用process_response操作

  

  	中间件方法的执行时有顺序的，process_request与process_view是按照顺序去执行的，而process_response、process_exception和process_template_response是反序的 ：

![](.\imgs\django_middleware2.jpg)

​	



### 9、URLConf路由匹配

​	通过urls.py文件中的 urlpatterns 配置找到对应的 视图函数或者视图类的方法，如果没有找到匹配的方法，那么就会触发异常，由中间件的process_exception 进行处理



### 10、middleware的process_view

​	调用中间件的 process_view 方法进行预处理



### 11、views处理request

​	调用对应的视图函数或视图类的方法处理request，譬如获取GET和POST参数，并且调用特定的模型对象执行数据库操作，如果没有数据库操作，那么就直接跳到我们后续的14步了



### 12、models处理

​	视图方法中，一般情况下都需要调用模型类进行数据操作，一般是通过模型的manager管理类进行操作的，如：MyModel.objects.get(pk=1)

​	如果没有数据操作，那么这一步和下一步就忽略



### 13、数据库操作

​	如果django通过模型类执行对数据库的增删改查，那么此时整个流程就会在对应的数据库中执行



### 14、views处理数据

​	视图方法获取到数据后：

- 将数据封装到一个context字典当中，然后调用指定的template.html，通过模板中的变量、标签和过滤器等，再结合传入的数据context，会触发中间件的process_template_response方法，最终渲染成HttpResponse
- 不调用模板，直接返回数据，譬如 JsonResponse、FileResponse等
- 执行redirect，生成一个重定向的HttpResponse，触发中间件的process_response后，返回到客户端，结束该web请求的生命周期



### 15、middleware的process_response

​	调用中间件的 process_response 方法进行处理，最后一个中间件的process_response执行完成后，返回到WSGIHandler类中

​	至此，django编程的处理部分完毕



### 16、WSGIHandler处理

​	WSGIHandler类获取到response后

- 先处理response的响应行和响应头，然后调用 start_response 返回http协议的 响应行和响应头 到uWSGI，这个 start_response 只能调用一次
- 第一步处理完成后，如果是文件需要对response进行，否则就直接将response作为http协议的body部分返回给uWSGI



### 17、uWSGI处理

​	uWSGI接收到django程序的返回后，将所有内容包装成http协议的内容后，通过uwsgi协议返回给nginx服务器处理



### 18、nginx处理

​	nginx获取到uWSGI的返回后，将response通过TCP协议返回给客户端



### 19、客户端接收响应

​	客户端接收到服务器的响应后，做对应的操作，譬如：显示在浏览器中，或是javascript的处理等

​	至此，整个web请求的生命周期结束。

​	



### 