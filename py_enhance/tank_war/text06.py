'''
v1.07
    新增坦克类
        1、坦克类新增speed属性，用来控制坦克移动速度快慢
        2、事件处理：
            2.1 改变坦克方向
            2.2 修改坦克位置(left,top)
                取决于坦克的速度
'''

import  pygame
# 为了命名的简化，把pygame.display = _display
_display = pygame.display
# 规定的窗口的颜色
COLOR_BLACK = pygame.Color(1,2,3)
COLOR_RED = pygame.Color(255,0,0)
version= 'v1.07'
# 主逻辑类
class MainGame():
    # 游戏主窗口
    window = None
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 500
    # 创建我方坦克
    TANK_P1 = None
    def __init__(self):
        pass
    # 开始游戏
    def startGame(self):
        # 模块的初始化方法
        pygame.display.init()
        # 创建窗口 加载窗口(借鉴官方文档）
        # pygame.display.set_mode()
        MainGame.window = _display.set_mode([MainGame.SCREEN_WIDTH,MainGame.SCREEN_HEIGHT])
        # 创建我方坦克
        MainGame.TANK_P1 = Tank(350,400)
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
            # 将我方坦克加入到窗口中
            MainGame.TANK_P1.displayTank()
            # 进行界面的刷新状态、pygame.display.update()
            _display.update()
    # 获取程序期间所有的时间（鼠标事件，键盘事件）
    def getEvent(self):
        # 1、获取全部事件
        eventList = pygame.event.get()
        # 2、 对事件进行判断处理（点击关闭按钮，按下键盘中的某个按键）
        for event in eventList:
            # 判断event.type是否为退出，如果是退出，直接调用程序结束方法。
            if event.type == pygame.QUIT:
                self.endGame()
            # 判断事件类型是否为按键按下，如果是，继续判断按下的是哪一个按键，来进行对应的操作
            if event.type == pygame.KEYDOWN:
                # 具体是哪个按键
                if event.key == pygame.K_LEFT:
                    print('坦克向左调头，移动')
                    # 修改坦克的方向
                    MainGame.TANK_P1.direction = 'L'
                    # 完成移动操作（调用坦克的移动方法）
                    MainGame.TANK_P1.move()
                elif event.key == pygame.K_RIGHT:
                    print('坦克向右调头，移动')
                    # 修改坦克的方向
                    MainGame.TANK_P1.direction = 'R'
                    # 完成移动操作（调用坦克的移动方法）
                    MainGame.TANK_P1.move()
                elif event.key == pygame.K_UP:
                    print('坦克向上调头，移动')
                    # 修改坦克的方向
                    MainGame.TANK_P1.direction = 'U'
                    # 完成移动操作（调用坦克的移动方法）
                    MainGame.TANK_P1.move()
                elif event.key == pygame.K_DOWN:
                    print('坦克向下调头，移动')
                    # 修改坦克的方向
                    MainGame.TANK_P1.direction = 'D'
                    # 完成移动操作（调用坦克的移动方法）
                    MainGame.TANK_P1.move()
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
    def __init__(self,left,top):
        # 加载图片路径
        self.images = {
            'U': pygame.image.load('img/p1tankU.gif'),
            'D': pygame.image.load('img/p1tankD.gif'),
            'L': pygame.image.load('img/p1tankL.gif'),
            'R': pygame.image.load('img/p1tankR.gif')
        }
        self.direction = 'U'
        self.image = self.images[self.direction]
        # 坦克所在的区域  Rect->
        self.rect = self.image.get_rect()
        # 指定坦克初始化位置，分别距X ,Y轴的位置
        self.rect.left = left
        self.rect.top = top
        # 新增速度属性
        self.speed = 5
    # 坦克移动
    def move(self):
        if self.direction == 'L':
            self.rect.left -= self.speed
        elif self .direction == 'R':
            self.rect.left += self.speed
        elif self.direction == "U":
            self.rect.top -= self.speed
        elif self .direction == 'D':
            self.rect.top += self.speed
    # 射击方法
    def shot(self):
        pass
    # 展示坦克（将坦克这个surface绘制到窗口中)
    def displayTank(self):
        # 1、重新设置坦克的图片
        self.image = self.images[self.direction]
        # 2、将坦克加入到窗口中
        MainGame.window.blit(self.image,self.rect)
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