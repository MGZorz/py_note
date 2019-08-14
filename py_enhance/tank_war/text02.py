'''
v1.03
    新增功能：
    创建游戏窗口
    用到游戏引擎上的功能模块
    官方开发文档
'''
import  pygame
# 为了命名的简化，把pygame.display = _display
_display = pygame.display
# 规定的窗口的颜色
COLOR_BLACK = pygame.Color(1,2,3)
# 主逻辑类
class MainGame():
    # 游戏主窗口
    window = None
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 500

    def __init__(self):
        pass
    # 开始游戏
    def startGame(self):
        # 模块的初始化方法
        pygame.display.init()
        # 创建窗口 加载窗口(借鉴官方文档）
        # pygame.display.set_mode()
        MainGame.window = _display.set_mode([MainGame.SCREEN_WIDTH,MainGame.SCREEN_HEIGHT])
        # 设置一下游戏标题
        # pygame.display.set_caption()
        _display.set_caption('坦克大战v1.03')
        # 让窗口持续刷新操作
        while True:
            # 给窗口完成一个填充颜色、pygame.surfave.fill()
            MainGame.window.fill(COLOR_BLACK)
            # 进行界面的刷新状态、pygame.display.update()
            _display.update()
    # 结束方法
    def endGame(self):
        print('谢谢使用')
        # 结束Python解释器
        exit()

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


game = MainGame()
game.startGame()