# @property装饰器的用法

class  Employee:

    def __init__(self,name ,salary):
        self.__name = name
        self .__salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self,salary):
        if 1000 < salary < 50000:
            self.__salary = salary
        else:
            print('录入错误！薪水控制在1000

'''    
    def get_salary(self):
        return  self.__salary
    
    def set_salary(self):
        if 1000<salary<50000:
            self.__salary = salary
        else:
            print('录入错误！薪水控制在1000-50000之间')
'''
emp1 = Employee('搞起',3000)
# print(emp1.get_salary())
# emp1.salary = -20000
# print(emp1.get_salary())
