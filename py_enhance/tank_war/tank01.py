'''
游戏引擎的安装：
    安装方式有两种：
        1、pip安装
            pip install pygame == 版本号
        2、pycharm
            file --> setting -->project --> project interpreter --> 右侧 + install --> 搜索框输入pygame  --> 下方install package
    验证pygame是否好用的验证
        import pygame

2、明白需求（基于面向对象的分析）：
    1、有哪些类：2、不同的类所具有的一些功能：
        1、主逻辑类
            开始游戏
            结束游戏
        2、坦克类（我方坦克、敌方坦克）
            移动
            射击
            展示
        3、子弹类
            移动
            展示
        4、爆炸效果类
            展示爆炸效果
        5、墙壁类
            属性：是否可以通过
        6、音效类
            播放音乐
3、 坦克大战项目框架的搭建
    涉及到的类，用代码简单的实现
'''

import  pygame

# 主逻辑类
class MainGame():
    def __init__(self):
        pass
    # 开始游戏
    def startGame(self):
        pass
    # 结束方法
    def endGame(self):
        pass
# 坦克类
class Tank():
    def __init__(self):
        pass
    # 坦克移动
    def move(self):
        pass
    # 射击方法
    def shot(self):
        pass
    # 展示坦克
    def displayTank(self):
        pass
# 我方坦克
class MyTank(Tank):
    def __init__(self):
        pass
# 敌方坦克
class EnemyTank(Tank):
    def __init__(self):
        pass
# 子弹类
class Bullet():
    def __init__(self):
        pass
    # 子弹的移动方法
    def move(self):
        pass
    # 展示子弹
    def displayBullet(self):
        pass
# 爆炸效果类
class Explode():
    def __init__(self):
        pass
    def dispalyExplode(self):
        pass
# 强壁类
class Wall():
    def __init__(self):
        pass
    # 展示墙壁的方法
    def displayWall(self):
        pass
# 音效类
class Music():
    def __init__(self):
        pass
    # 开始播放音乐
    def play(self):
        pass
