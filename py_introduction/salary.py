r1 = {"name":"高小一","age":18,"job":"what","salary":30000}
r2 = {"name":"高小二","age":19,"job":"what","salary":20000}
r3 = {"name":"高小五","age":20,"job":"what","salary":10000}

tb = [r1,r2,r3]

# 获取第二行的人的薪资
print(tb[1].get('salary'))

# 打印表中所有的薪资

for i in range(len(tb)):  # i是从0~2遍历的。
	print(tb[i].get('salary'))

# 打印表的所有数据

for i in range(len(tb)):
	print(tb[i].get('name'),tb[i].get('age'),tb[i].get('job'),tb[i].get('salary'))
	
