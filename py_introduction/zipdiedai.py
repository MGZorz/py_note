# 测试zip（）运行迭代

for i in [1,2,3]:
    print(i)

names = ("1","2","3","4")
ages = (15,6,7,9)
jobs = ("teacher","player")
for name,age,job in zip(names,ages,jobs):
     print("{0}-{1}-{2}".format(name,age,job))
