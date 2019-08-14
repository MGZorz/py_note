'''
导入自定义模块
    1、import模块
        问题： 在导入模块的时候，模块中的代码会执行一遍
        解决方案：
            在自定义模块中：
                新增控制代码：
                    if __name__ = '__main__':
                        源代码执行
    2、from 模块 import 函数 ...

'''
# import py2_9
x = 10
y = 20
# print('和：%g'%py2_9.add(x,y))

from py2_9 import  add,sub,mul,div

print('和为：%g'%add(x,y))