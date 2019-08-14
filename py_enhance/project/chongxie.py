class Person:  # 定义一个父类

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def say_age(self):
        print(self.name,'的年龄是：',self.age)

    def say_name(self):
        print('我是',self.name)


class Student(Person):  # 集成父类的内容，父类（子类）

    def __init__(self,name,age,score):
        self.score = score
        Person.__init__(self,name,age)  # 构造函数中包含调用父类构造函数。


    def say_score(self):
        print(self.name,'的分数是：',self.score)

    def say_name(self):  # 重写父类的方法，重新定义了say_name的函数。
        print('报告老师，我是：',self.name)

s1 = Student('张三',15,85)
s1.say_score()
s1.say_name()
s1.say_age()