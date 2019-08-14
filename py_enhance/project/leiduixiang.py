class Student:   # 创建一个类对象。
    company = 'sxt'    # 类属性
    count = 0

    def __init__(self,name,score):
        self.name = name  # 实例属性  归为具体的对象中
        self.score = score
        Student.count = Student.count +1

    def say_score(self):    # 实例方法，归为类对象中
        print("公司是{0}，薪资是：{1}",self.name)
        print('薪资是',self.score)

s1 = Student('haha','456465')
s1.say_score()


# 类方法（从属于类对象的方法）
#
# @classmethod
# def 类方法名（cls[,形参列表]）：
#     函数体
class Student :
    company = 'sxt'
    @classmethod
    def printCompany(cls):
        print(cls.company)
        # 类方法和静态方法不能调用实例对象
Student .printCompany()

# 静态方法定义    与类对象无关的方法
# @staticmenthod
class Student:
    company = 'sxt'
    @staticmethod
    def add(a,b):
        print('{0}+{1}={2}'.format(a,b,(a+b)))
