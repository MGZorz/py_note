# class Student:          #  类名一般首字母大写，朵儿单词采用驼峰原则.
#
#     def __init__(self,name,score):  # self 必须位于第一个参数。
#         self.name = name
#         self.score = score
#     def say_score(self): # self 必须位于第一个参数
#         print('{0}的分数是：{1}'.format(self.name,self.score))
#
# s1 = Student('wa',123132)
# s1.say_score()

class Student:

    def __init__(self,name,score):
        self.name = name
        self.score = score
    def say_score(self):
        print('{0}的分数是：{1}'.format(self.name,self.score))
s1 = Student('jkasjdal','aslkdlkad')
s1.say_score()

s1.age = 123
s1.salary = 30000

#del s1
print(s1.salary)

s2 = Student('dasde','hsjai')
s2.say_score()
Student.say_score(s2)  # 和上一行的结果是一样的，这是实际编辑器的指令

print(dir(s2))

#  获得对象的所有属性和方法

print(s2.__dict__)  # 获得我们定义的属性

class Man:
    pass
# pass空字符，什么都没有

print(isinstance(s2,Student))
# 判断对象是不是和类型是一样的

stu2 = Student

