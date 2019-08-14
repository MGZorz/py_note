# 测试全局变量、局部变量

# a = 3  # 全局变量
#
#
# def text01():
#     b = 4 # 局部变量
#     print(b*10)
#
#     global a # 如果在函数内要更改全局变量需要用global来声明。
#     a = 300
#     print(locals()) # 输出局部变量
#     print(globals()) # 打印输出全局变量
# text01()
# print(a)


# 测试局部变量和全局变量的效率。
# import time
# import math
# def test01():   # 利用全局变量
#     start = time .time()
#     for i in range(100000000):
#         math.sqrt(30)
#     end = time.time()
#     print("好使{0}".format((end-start)))
#
# def test02():   #  利用局部变量
#     b = math.sqrt
#     start = time . time()
#     for i  in range(100000000):
#         b(30)
#     end = time .time()
#     print("耗时{0}".format((end-start)))
#
#
# test01()
# test02()

#  传递可变对象[列表、字典、自定义的其他可变对象]可以直接拷贝进去，不改变引用位置。
# b = [10,20]
# print(id(b))
# def f2(m):
#     print(id(m))
#     m.append(300)
#     print(id(m))
#
# f2(b)


# 传递不可变对象，[int float、字符串、元组、布尔组]

a = 100
def f1(n):
    print("n:",id(n))
    n += 200
    print("n",id(n))
    print(n)
f1(a)
print("a:",id(a))
