'''
需求：矩形与正方形两个类，求周长与面积。分别使用不继承与继承两种方式，并总结出继承的优势。


'''
# # 继承方式
# class Rectangle():
#     def __init__(self,a1,a2):
#         # 指定a1为长，a2为宽
#         self.a1 = a1
#         self.a2 = a2
#
# class Square(Rectangle):
#     def Zchang(self):
#         if self.a1 !=self.a2:
#             z = self.a1*2+self.a2*2
#             print('周长为{0}'.format(z))
#         else:
#             z = self.a1*4
#             print('周长为{0}'.format(z))
#
#     def Mji(self):
#         if self.a1 != self.a2 :
#             m = self.a1*self.a2
#             print('面积为{0}'.format(m))
#         else:
#             m = self.a1**2
#             print('面积为{0}'.format(m))
#
# z = Square(5,6)
# z.Zchang()
# z.Mji()
#
#
# # 不继承方式
# class Rectangle():
#     def __init__(self,a1,a2):
#         # 指定a1为长，a2为宽
#         self.a1 = a1
#         self.a2 = a2
#     def Zchang(self):
#         if self.a1 !=self.a2:
#             z = self.a1*2+self.a2*2
#             print('周长为{0}'.format(z))
#         else:
#             z = self.a1*4
#             print('周长为{0}'.format(z))
#
#     def Mji(self):
#         if self.a1 != self.a2 :
#             m = self.a1*self.a2
#             print('面积为{0}'.format(m))
#         else:
#             m = self.a1**2
#             print('面积为{0}'.format(m))
# z = Rectangle(5,6)
# z.Zchang()
# z.Mji()

'''
需求：编写如下的继承结构，类C继承（A，B），类D继承（B，A），类E继承（C，D）或者（D，C），会出现什么情况？

'''
# class A():
#     print('我是A')
# class B():
#     print('我是B')
# class C(A,B):
#     print('我是C')
# class D(B,A):
#     print('我是D')
# class E(C,D):
#     print('我是E')
#
# a1 = A()
# a2 = B()


'''
编写一个分页显示类，初始化传入记录总数。希望可以通过设置每页记录数和页码，可以显示当前页的信息。
其中每页记录数与页码使用property实现。注意，如果页码设置不正确（如<1或者>最大页码），提示错误信息。设计方法能够返回当前页显示的记录区间。
对象：
    1、页码的内容
'''
# class Page():
#     def __init__(self,all_pages,pagesize,currunPage):
#         self.all_pages = all_pages
#         self.pagesize = pagesize
#         self.currunPage = currunPage
#
#     def

'''
需求：编写电脑类，提供一个方法，能够与移动设备（U盘，MP3，移动硬盘）进行读写交互。如果参数类型不是移动设备的类型，则打印错误信息。MP3除了读与写之外，还额外具有一个播放音乐的功能。
对象：移动设备，电脑，
'''
class ME():
    def __init__(self,):



