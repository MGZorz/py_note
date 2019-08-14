'''
什么是模块：
    只要是以.py为后缀的文件，都可以称为模块
模块中可以包含什么东西？
    1、变量
    2、函数
    3、面向对象（类->对象）
    4、可执行代码

使用模块有什么好处？
    管理方便，易维护
    降低复杂度
'''
PI = 3.14
def get_area(r):
    '''
    求圆面积的方法
    :param r: 半径
    :return: 圆的面积
    '''
    return PI * r ** 2
class Student():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def show_info(self):
        '''
        展示学生信息
        :return: None
        '''
        # print('name:{0},age = {1}'.format(self.name,self.age))
        print('name:%s age:%s'%(self.name,self.age))

print(PI)
print('半径为3的圆的面积为：%g'%get_area(3))

#   类调用
stu = Student('学生1',18)
stu.show_info()