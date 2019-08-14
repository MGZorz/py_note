'''
v1.05
    新增功能：
        实现左上角问题的提示内容

'''

import  pygame
# 为了命名的简化，把pygame.display = _display
_display = pygame.display
# 规定的窗口的颜色
COLOR_BLACK = pygame.Color(1,2,3)
COLOR_RED = pygame.Color(255,0,0)
version= 'v1.05'
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
        _display.set_caption('坦克大战'+version)

        # 让窗口持续刷新操作
        while True:
            # 给窗口完成一个填充颜色、pygame.surfave.fill()
            MainGame.window.fill(COLOR_BLACK)
            # 再循环中持续完成事件获取
            self.getEvent()
            # 将绘制文字得到的小画布，粘贴到窗口中
            MainGame.window.blit(self.getTextSurface('剩余地方坦克5辆'),(5,5))
            # 进行界面的刷新状态、pygame.display.update()
            _display.update()
    # 获取程序期间所有的时间（鼠标事件，键盘事件）
    def getEvent(self):
        # 1、获取全部事件
        evenList = pygame.event.get()
        # 2、 对事件进行判断处理（点击关闭按钮，按下键盘中的某个按键）
        for event in evenList:
            # 判断event.type是否为退出，如果是退出，直接调用程序结束方法。
            if event.type == pygame.QUIT:
                self.endGame()
            # 判断事件类型是否为按键按下，如果是，继续判断按下的是哪一个按键，来进行对应的操作
            if event.type == pygame.KEYDOWN:
                # 具体是哪个按键
                if event.key == pygame.K_LEFT:
                    print('坦克向左调头，移动')
                elif event.key == pygame.K_RIGHT:
                    print('坦克向右调头，移动')
                elif event.key == pygame.K_UP:
                    print('坦克向上调头，移动')
                elif event.key == pygame.K_DOWN:
                    print('坦克向下调头，移动')
                elif event.key == pygame.K_SPACE:
                    print('坦克发射子弹！')
    # 左上角文字的绘制功能
    def getTextSurface(self,text):
        # 初始化字体模块
        pygame.font.init()
        # 先看库中所有的字体
        # fontList = pygame.font.get_fonts()
        # print(fontList)
        # 选中合适的字体
        font = pygame.font.SysFont('kaiti',18)
        # 使用对应字符完成相关内容
        textSurface = font.render(text,True,COLOR_RED)
        return textSurface


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
# 墙壁类
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