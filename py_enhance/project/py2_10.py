'''
使用自定义模块的时候：
    1、import 模块
    2、from 模块 import 变量，类，函数
        问题：如果要使用这种方案，导入模块中的所有功能，一个一个填写比较麻烦
        解决方案：
            from 模块 import *

        * 默认导入模块中的所有功能
        如果在模块中手动添加全局变量__all__ = []
        * 则不代表所有的功能
'''
# from py2_9 import add,sub
# result = add(10,20)
# print(result)
# result = sub(10,20)
# print(result)

from py2_9 import *
result = add(10,20)
print(result)
result = sub(10,20)
print(result)
result = mul(10,20)
print(result)
result = div(10,20)
print(result)