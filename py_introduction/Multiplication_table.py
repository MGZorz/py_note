# 打印九九乘法表
for m in range(1,10):
    for n in range(1,m+1):
        print("{0}*{1}={2}".format(m,n,(m*n)),end = '\t'')
    print()

# 利用列表和字典存储表格内容

r1= dict(name="高效益",age=18,salary=30000,city="beijing")   #  dict() 创造字典。
r2= dict(name="高消二",age=20,salary=20000,city="上海")
r3= dict(name="高小吴",age=19,salary=10000,city="深圳")
tb=[r1,r2,r3]
for x in tb:
    if x.get("salary")>=15000:
        print(x)
