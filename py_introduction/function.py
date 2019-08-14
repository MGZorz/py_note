# 测试函数的定义和使用

# def test01():
#     print("*"*10)
#     print("@"*10)

# test01()
#
# for i in range(10):
#     test01()
#
# def printMAx(a,b):
#     if a < b :
#         print(a,"最小值")
#     else:
#         print(b,"最小值")
#
# printMAx(2,6)

# 测试形参和实参的基本用法

# def text1():
#     print("sxt")
#     print("wang")
#     return
# text1()

# def text2(a,b):
#     return a+b
#
# c = text2(3,9)
# print(c)
# print(text2(3,9)*10)

# def txs(a, b, c):
#     return [a*6,b*9,a+b+c]
# c = txs(1,2,3)
# print(txs(1,2,3)*5)


# 测试函数是针对对象的

def text01():
    print("4562123")

c = text01

print(id(text01()))
print(id(c()))