'''
装饰器：
简化私有属性的访问方式
@ porperty
@ 属性.setter

'''
@ property
@money.setter
class Account():
    def __init__(self):
        self.__money = 0
    @poperty
    def money(self):
        return self.__money
    @money.setter
    def money(self,money):
        if isinstance(money,int):
            self.__money = money
        else:
            raise Exception('金钱类型有误')

m = Account()
m.money = 100
print(m.money)