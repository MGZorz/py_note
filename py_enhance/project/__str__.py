# 测试重写object的__str__()

class Person:

    def __init__(self,name):
        self.name = name

# p = Person('Elroy')
# print(p)

    def __str__(self):    # 重写生效了！！
        return '名字是：{0}'.format(self.name)

p = Person('Elroy')
print(p)

