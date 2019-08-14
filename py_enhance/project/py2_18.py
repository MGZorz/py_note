'''
模块引入的问题：
    1、那些模块可以被引入
    builtins
    sys.path:
        列表，存储一系列目录

        文件路径问题：

    2、被引入之后的模块，更新问题
        模块重载：
            1、from imp import reload
            2\reload (目标模块)
            3、重新调用就ok了

'''
import  random
import sys

result = sys.path
print(type(result))
for tempPath in result:
    print(tempPath)
