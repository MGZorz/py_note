'''
package
    模块
    __init__.py

    类中，__init__初始化方法

    包中，__init__初始化模块

    首次使用包中模块时，__init__.py模块会被执行一次

__init__.py中可以存放什么？
    可以存放同普通模块一样的代码
    变量、类、函数。。。都是ok的

一般会写一些辅助代码：
    让你更方便导入包或者文件，使用模块

    在测试文件中
        import package
    在包的__iniy__.py模块
        import 模块
    这种方式等价于：在测试文件中， 使用 import 包.模块
    -------------------------------------------

    在测试文件中
        from 包 imporu *
        在 __init__.py中
        from .模块 import *

        这种方式等价于：在测试文件中使用from 包.模块 import *
'''
# import package.py2_9
# import package
# import package.py2_9
# result = package.py2_9.add(2,32)
# print(result)

from package import *
result = add(10,20)
print(result)