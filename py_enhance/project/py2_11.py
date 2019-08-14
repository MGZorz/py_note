'''
包的概念：package
    可以理解为文件夹，前提，文件中包含一个__init__.py
包的作用：
    1、将模块归类，方便整理
    2、防止模块名冲突。

模块中的包，名字会产生变化
    新的名字：
        包名.模块名

    MyMath

    package.MyMath

包中的模块如何使用：
    1、import 模块

    2、from 模块 import 变量，函数，类
'''

# import py2_9
# result = py2_9.add(10,20)
# import package.py2_9
# result = package.py2_9.add(10,20)
# print(result)

from package.py2_9 import *
result = add(10,20)
print(result)

result = div(10,20)
print(result)
