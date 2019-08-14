#   测试工厂模式和单利模式的整合

class CarFactory:
    __obj = None    #   类属性（在定义函数之前出现的属性，贯穿整个类）
    __init_flag = True


    def create_car(self,brand):     #   构造函数，构造出变量create_car
        if brand == '奔驰':
            return Benz()
        elif brand == '宝马':
            return BMW()
        elif brand == '比亚迪':
            return BYD()
        else:
            return '品牌未知，不知道怎么搞'

    def __new__(cls, *args, **kwargs):
        if cls.__obj == None:
            cls.__obj = object.__new__(cls)

        return cls.__obj


    def __init__(self):
        if CarFactory.__init_flag:
            print('init CarFactory...')
            CarFactory.__init_flag = False
class Benz:
    pass
class BMW:
    pass
class BYD:
    pass

factory = CarFactory()
a = factory.create_car('奔驰')
b = factory.create_car('宝马')
print(a)
print(b)
