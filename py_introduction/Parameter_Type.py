# 测试参数的类型。

# def test01(a,b,c,d):
#     print("{0}-{1}-{2}-{3}".format(a,b,c,d))
#
#
# def test02(a,b,c=10,d=15):   # 默认值参数
#     print("{0}-{1}-{2}-{3}".format(a,b,c,d))
#
# test01(10,20,3,4)  # 位置参数
# # test(10,20)  参数个数不匹配
#
# test01(d=20,b=40,a=10,c=100)
# # 命名参数，通过形参名称来匹配

def f1(a,b,*c,**d):
    print (a,b,c,d)

f1(1,2,5,6,name="why",age=1)   # 两个数字，一个元组，字典。

def f2(*a):
    print(a,b,c)
f2(3,4,b=5,c=9)    # 当前面有元组或者字典的时候，后面需要强制命名。



