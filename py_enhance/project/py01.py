# 测试私有属性   和  私有方法！
class Employee:


    def __init__(self,name,age):
        self.name = name
        self.__age = age  # 两个下划线开头是私有属性


    def __work(self):   # 私有方法
        print('好好工作')
        print('年龄：{0}'.format(self.__age))


e = Employee('www',55)

print(e.name)
# print(e.age)
print(e._Employee__age)   # 私有的数据调用。别忘记下划线！！！！
print(dir(e))

e._Employee__work()   # 私有属性调用


# @property()装饰器用法

class Employee:

    def __init__(self,name,score):
        self.name = name
        self.score = score


em1 = Employee('sada',8888)
print(em1.__salary)

