# 列表推导式
y = [x*2 for x in range(10) if x%2 == 0]
print(y)

# 字典推导式
my_text = "i love you ,i love xst,i love what "
char_count = {c:my_text.count(c) for c in my_text}
print(char_count)

# 课下作业，使用普通循环实现上面字典推导式。


# 集合推导式

b = {x for x in range(1,100) if x%9==0}
print(b)

# 生成器推导式

a = (x for x in range(1,100) if x %9==0)

# print(tuple(a))  # 只能看一次。非常重要啊

for x in a :   # a是可迭代对象
    print(x,end="\t")
