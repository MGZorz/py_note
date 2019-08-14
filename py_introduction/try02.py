import time

# 测试合并符join()与"+"的用时。
time01=time.time()
a=""
for i in range(1000000):
	a +="sxt"
time02 = time.time()
print("运算时间："+str(time02-time01))

# 最好用下面的效率高的代码
time03=time.time()
li=[]
for i in range(1000000):
	li.append("sxt")
a = "".join(li)
time04=time.time()
print("运算时间："+str(time04-time03))


a = input('请输入一个三位数')
b = a[0]
c = a[1]
d = a[2]
e = '个位{2}，十位{1}，百位{0}'
f = e.format(b,c,d)
print(f)



