'''
tuple：创建元组，元组内的元素不可变。
list:创建列表，a = list() 元素可以任意，可以改变。
dict:创建字典，键值对。键是任意不可变的数据，同时列表、字典和集合都不能作为字典的“键”
a = dict(name="",job="")
a = dict([("name","what"),("job","what")])
'''

'''
2、将字典中的键和值互换。
>>> m = {'a':1,'b':2,'c':3,'d':4}
>>> zip(m.values(),m.keys())
<zip object at 0x0000000002CD8EC8>
>>> mi = dict(zip(m.values(),m.keys()))
>>> mi
{1: 'a', 2: 'b', 3: 'c', 4: 'd'}
>>> 
'''

# 3、去除列表中的重复元素
a = [1,2,3,3,3,5,5,5,6,5,]
b = []
for x in a :
    if x not in b:
        b.append(x)
print(b)

# 4、编写分钟数，将其转化为小时和分钟显示

timeHour = 0
timeM = 0
while True:
    time_all = int(input("请输入一个分钟数，按0结束"))
    if time_all == 0:
        print("计算结束，谢谢使用。")
        break
    elif time_all<0:
        print("搞笑么？时光倒流？")
        continue
    elif time_all<60:
        print("这个还是分钟表示比较好一些吧！还是{0}分钟。".format(time_all))
    else :
        timeHour = time_all//60
        timeM = (time_all/60 - timeHour)*60
        print("总用时是{0}小时{1}分钟。".format(timeHour,timeM))

# 5 把二维列表转化一维列表

lis= [[1,2,3],[4,5]]
li = lis[0]+lis[1]
print(li)


# 6、两个字符串合并之后输出长度、7、8

list1 = ['life','is','short']
list2 = ['you','need','python']
list_all = list1 +list2
print(len(list_all))
list2[2]='python3'
print(list2)  # 索引赋值可直接更改列表中元素
del list2[2]
print(list2)

# 9、自定义元组并练习常用方法。

a = ('d','v','f')
print(len(a))
print(a[2])

# 10
L = [
['Apple', 'Google', 'Microsoft'],
['Java', 'Python', 'Ruby', 'PHP'],
['Adam', 'Bart', 'Lisa']
]
print(L[0][1])
l = L[1]
print(l[0:2])
n = l.index('Python')
print(n)