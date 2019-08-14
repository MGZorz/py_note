# 测试mro()方法解析顺序

# 多重继承

class  A:
    def aa(self):
        print('aa')
    def say(self):
        print('say AAA!!')

class B :
    def bb(self):
        print('bb')
    def say(self):
        print('say,BBB!')

class C(B,A):  # (A,B)
    def __init__(self,nn):
        self.nn = nn
    def cc(self):
        print('cc')

c = C(3)
print(C.mro()) #    打印类的层次结构

c.say()
#   解释器寻找的方向“从左往右”的方式寻找，此时会执行B类中的say()

print(dir(c))  #    获得C的所有属性
print(c.__dict__) #
print(c.__class__) # 确定是哪个类
print(C.__bases__) # C 的父类都有谁
print(C.mro())
print(A.__subclass__())