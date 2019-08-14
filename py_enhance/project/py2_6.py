'''
自定义异常
以及抛出自定义异常
    raise   异常对象

class 自定义异常（BaseException)
    def __init__(self):
        pass

需求：
    定义一个学生类，私有属性gender,提供对应的设置值以及访问值的方法

'''
#定义一个异常类
class GenderException(BaseException):
    def __init__(self):
        super().__init__()
        self.errMsg = '性别只能设置成男或者女'
class Student():
    def __init__(self,name,gender):
        self.name = name
        # self.__gender = gender
        self.setGender(gender)

    #   设置性别
    def setGender(self,gender):
        if gender == '男' or gender == '女':
            self.__gender = gender
        else :
            #   抛出异常（性别异常）
            raise GenderException()
    #   获取性别
    def getGender(self):
        return self.__gender
    def showInfo(self):
        print('我叫：{0} 性别：{1}'.format(self.name,self.__gender))
try:
    stu = Student('学生1','男')
    stu.showInfo()
except GenderException as e :
    print(e.errMsg)
# try:
#     stu .setGender('半女不女')
# except GenderException as e :
#     print(type(e))
#     # print(e.args)
#     print(e.errMsg)

