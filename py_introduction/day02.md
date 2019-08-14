# day02

## 	一、

0b  二进制	0o  八进制  0x 十六进制

整数转化为二进制、八进制、十六进制

​			bin	oct        hex

## 	二、利用int()实现类型转换

1、浮点数直接舍去小数部分。

2、布尔值True装为1，False转为0.

3、字符串符合证书格式直接转化。

## 	三、

round()函数可以进行四舍五入操作。

## 	四、

 浮点数除法：/    8/2   =4.0

整数除法：//     7//2 = 3

模（取余）：%     7%4 = 3

幂运算：**         2**3 = 8

 divmod(a,b)  通过这个可以同时得到 商 和 余数 .



![1553566699498](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\1553566699498.png)

## 	五、时间表示

​	Unix时间点：1970年1月1日00：00：00

​	导入：import time

​	time.time()

​	返回数字为以秒为单位的浮点数。

​	整数表示秒数、浮点数表示毫秒

## 	六、绘制点坐标、折现



## 七、比较运算符、逻辑运算符和同一运算符

### 	1、比较运算符

== 等于，比较对象的值是否相等。

！= 不等于，比较两个对象的值是否为不相等

### 	2、逻辑运算符

​	(1)	or	x or y	x为true	 返回为true	逻辑或

​						x为false	返回为false

​	(2)	and	x and y	x为true	则返回y的值

​							x为false	则不计算y，直接返回false

​	(3)	not	not x		x为true	 返回为false

​							 x为false	返回为true

## 3、同一运算符

#### 	is  、 is not 

is 比较两个变量是否引用对象为同一个，是比较对象的地址。

==  是比较两个变量引用对象的值是否相等。



#### 	整数缓存问题

python在【-5，256】之间的数，地址都是一样的，比如

a = 10

b = 10

a is b

True



#### 	is  的效率要比 “==” 高，在变量和None进行比较时，应该使用is





## 八、字符串

len() 是查字符串长度的函数。

## 九、转义字符

float()把浮点数转化成字符串

str()把其他类型的数据转化为字符串。

replace()字符串的替换。

## 十、切片slice操作、split()分割和join()合并

1、[:]，格式来截取字符串的部分

逆序排列时：【：：-1】

2、' '.join(a)  



## 十一、字符串的驻留机制

对于符合标识符规则的字符串（仅仅包括(_)，字母和数字）自动启动驻留机子。

成员操作符，（in/not in）

## 十二、常用查找方法

"".len()

startswith()

endswith()

find()

count()

isalnum()

## 十三、去除首位信息

"".strip()

lstrip()

rstrip()

## 十四、大小写转化

a.capitalize()   

a.title()

a.upper()  

a.lower()

a.swapcase()

## 十五、格式排版

center()

ljust()

rjust()

其他的小方法

isalnum() 是否为字母或者数字

 isalpha() 是否只用字母组成

 isdigit() 是否只用数字

 isspace() 是否为空白符

 isupper() 大写

 islower() 小写

## 十六、字符串的格式化

##### format()基本用法

![1553584360143](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\1553584360143.png)

##### 填充和对齐

![1553584946860](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\1553584946860.png)

^ 居中  <左对齐    >右对齐

##### 数字的格式化

浮点数用f，整数通过d进行需要的格式化。

![1553585219860](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\1553585219860.png)

##### 可变字符串

StringIO() 可变字符串

seek()指针移动到第几个字符

write（）修改字符串

## 十七、运算符优先级问题

![1553586008988](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\1553586008988.png)

![1553586445266](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\1553586445266.png)