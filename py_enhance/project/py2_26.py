'''
property 的使用
    私有属性，提供开放接口，提供外界使用
'''
class Student():
    def __init__(self,name,age):
        self.name = name
        #私用属性
        self.__age = age
    def getAge(self):
        return self.__age
    def setAge(self,age):
        if isinstance(age,int):
            self.__age = age
        else:
            return TypeError('类型错误')
    age = property(getAge,setAge)

stu1 = Student('张伟',18)
stu1.setAge(17)
# stu1.age = 17
print(stu1.getAge())

print(stu1.age)
