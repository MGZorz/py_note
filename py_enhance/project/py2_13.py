'''
1、模块的发布
    a、为什么要发布？
        自定义模块，切换项目中，不好用
        系统模块，切换到新的项目中，好用
        原因：

    b、sys.path
        导入模块时，搜索路径列表

        如果所有路径中 都没有要导入的模块，会导致，无法导入模块
    解决方案：
            1、将模块所在路径，手动加入到sys.path中
                @ 手动将自定义模块所在路径加到sys.path中 @
                手动添加：sys.path.append(模块所在路径)
                路径分隔符两种表示方式：1、'/' ，2、'\\'
            2、将自定义模块，发布到系统目录，
                    发布自定义模块的步骤：
                        1、确定发布的模块（目录结构）
                        | --setup .py
                        | -- package
                            |
                            --- 自定义模块
                        2、setup的编辑工作
                            setup()
                        3、构建模块
                            python setup.py build
                        4、发布模块
                            python setup.py sdist

2、模块的安装
    2.1 通过命令完成的安装（推荐） 更安全
        a.找到之前发布的压缩包，解压操作
        b.python steup.py install
            指定目录安装：
                python setup.py install --prefix = 安装路径
    2.2 暴力安装
        直接将要安装的包以及模块，复制到对应的系统目录中

'''
# import py2_9
# print(py2_9.add(10,20))
import sys
list1 = sys.path
print(type(list1))
for path in list1:
    print(path)
