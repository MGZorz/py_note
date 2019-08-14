'''
v1.16
    新增功能
        让敌方坦克发射子弹
'''


import pygame, time, random

# 为了命名的简化，把pygame.display = _display
_display = pygame.display
# 规定的窗口的颜色
COLOR_BLACK = pygame.Color(1, 2, 3)
COLOR_RED = pygame.Color(255, 0, 0)
version = 'v1.16'


# 主逻辑类
class MainGame():
    # 游戏主窗口
    window = None
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 500
    # 创建我方坦克
    TANK_P1 = None
    # 存储所有敌方坦克
    EnemyTank_list = []
    # 要创建坦克的数量
    EnemyTank_count = 6
    # 存储我方子弹的列表
    Bullet_list = []
    # 存储敌方子弹的列表
    Enemy_bullet_list = []

    def __init__(self):
        pass

    # 开始游戏
    def startGame(self):
        # 模块的初始化方法
        pygame.display.init()
        # 创建窗口 加载窗口(借鉴官方文档）
        # pygame.display.set_mode()
        MainGame.window = _display.set_mode([MainGame.SCREEN_WIDTH, MainGame.SCREEN_HEIGHT])
        # 创建我方坦克
        MainGame.TANK_P1 = Tank(350, 400)
        #   调用敌方坦克
        self.creatEnemyTank()
        # 设置一下游戏标题
        # pygame.display.set_caption()
        _display.set_caption('坦克大战' + version)
        # 让窗口持续刷新操作
        # 主逻辑！！！
        while True:
            # 给窗口完成一个填充颜色、pygame.surfave.fill()
            MainGame.window.fill(COLOR_BLACK)
            # 再循环中持续完成事件获取
            self.getEvent()
            # 将绘制文字得到的小画布，粘贴到窗口中
            MainGame.window.blit(self.getTextSurface('剩余地方坦克%d辆' % len(MainGame.EnemyTank_list)), (5, 5))
            # 将我方坦克加入到窗口中
            MainGame.TANK_P1.displayTank()
            # 循环展示敌方坦克
            self.blitEnemyTank()
            # 调用坦克的移动方法
            if MainGame.TANK_P1 and not MainGame.TANK_P1.stop:
                MainGame.TANK_P1.move()
            # 调用渲染子弹列表的一个方法
            self.blitBullet()
            # 调用渲染敌方子弹列表的一个方法
            self.blitEnemyBullet()
            # 添加一个休眠（大型的项目中最好不要这样）
            time.sleep(0.02)
            # 进行界面的刷新状态、pygame.display.update()
            _display.update()

    #   创建敌方坦克
    def creatEnemyTank(self):
        left = random.randint(1, 7)
        top = 100
        for i in range(MainGame.EnemyTank_count):
            # 移动速度，放到for循环中，是要保证每个敌方坦克的速度都是随机，不同的
            speed = random.randint(3, 6)
            # 每次随机都生成一个left值
            left = random.randint(1, 7)
            eTank = EnemyTank(left * 100, top, speed)
            MainGame.EnemyTank_list.append(eTank)

    # 将敌方坦克加入窗口中
    def blitEnemyTank(self):
        for eTank in MainGame.EnemyTank_list:
            eTank.displayTank()
            # 坦克移动的方法
            eTank.randMove()
            # 调用敌方坦克的射击
            eBullt = eTank.shot()
            # 如果子弹为None 不加入到列表中
            if eBullt:
            # 将子弹储存在敌方子弹的列表里面
                MainGame.Enemy_bullet_list.append(eBullt)

    # 将我方子弹加入到窗口中
    def blitBullet(self):
        for bullet in MainGame.Bullet_list:
            # 如果子弹还活着，绘制出来，否则直接在列表中删除
            if bullet.live:
                bullet.displayBullet()
                # 让子弹移动
                bullet.bulletMove()
            else:
                MainGame.Bullet_list.remove(bullet)
    # 敌方子弹加入窗口中
    def blitEnemyBullet(self):
        for ebullet in MainGame.Enemy_bullet_list:
            if ebullet.live:
                ebullet.displayBullet()
                # 将子弹移动
                ebullet.bulletMove()
            else:
                MainGame.Enemy_bullet_list.remove(ebullet)
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
                    # MainGame.TANK_P1.move()
                    MainGame.TANK_P1.stop = False
                elif event.key == pygame.K_RIGHT:
                    print('坦克向右调头，移动')
                    # 修改坦克的方向
                    MainGame.TANK_P1.direction = 'R'
                    # 完成移动操作（调用坦克的移动方法）
                    # MainGame.TANK_P1.move()
                    MainGame.TANK_P1.stop = False
                elif event.key == pygame.K_UP:
                    print('坦克向上调头，移动')
                    # 修改坦克的方向
                    MainGame.TANK_P1.direction = 'U'
                    # 完成移动操作（调用坦克的移动方法）
                    # MainGame.TANK_P1.move()
                    MainGame.TANK_P1.stop = False
                elif event.key == pygame.K_DOWN:
                    print('坦克向下调头，移动')
                    # 修改坦克的方向
                    MainGame.TANK_P1.direction = 'D'
                    # 完成移动操作（调用坦克的移动方法）
                    # MainGame.TANK_P1.move()
                    MainGame.TANK_P1.stop = False
                elif event.key == pygame.K_SPACE:
                    print('坦克发射子弹！')
                    if len(MainGame.Bullet_list)<3:
                        #   产生一个子弹
                        m = Bullet(MainGame.TANK_P1)
                        #   将子弹加入子弹列表
                        MainGame.Bullet_list.append(m)
                    else :
                        print('子弹数量不足')
                    print ('当前屏幕中子弹的数量为：%d'%len(MainGame.Bullet_list))

            # 结束游戏的方法
            if event.type == pygame.KEYUP:
                # 修改坦克的方向
                if (event.key == pygame.K_LEFT) or (event.key == pygame.K_RIGHT) or (event.key == pygame.K_UP) or (
                        event.key == pygame.K_DOWN):
                    # 修改坦克的方向
                    MainGame.TANK_P1.stop = True

    # 左上角文字的绘制功能
    def getTextSurface(self, text):
        # 初始化字体模块
        pygame.font.init()
        # 先看库中所有的字体
        # fontList = pygame.font.get_fonts()
        # print(fontList)
        # 选中合适的字体
        font = pygame.font.SysFont('kaiti', 18)
        # 使用对应字符完成相关内容
        textSurface = font.render(text, True, COLOR_RED)
        return textSurface

    # 结束方法
    def endGame(self):
        print('谢谢使用')
        # 结束Python解释器
        exit()


# 坦克类
class Tank():
    def __init__(self, left, top):
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
        # 新增属性:坦克移动的开关
        self.stop = True

    # 坦克移动
    def move(self):
        if self.direction == 'L':
            # self.rect.left -= self.speed
            if self.rect.left > 0:
                self.rect.left -= self.speed
        elif self.direction == 'R':
            if self.rect.left + self.rect.width < MainGame.SCREEN_WIDTH:
                self.rect.left += self.speed
        elif self.direction == "U":
            if self.rect.top > 0:
                self.rect.top -= self.speed
        elif self.direction == 'D':
            if self.rect.top + self.rect.height < MainGame.SCREEN_HEIGHT:
                self.rect.top += self.speed

    # 射击方法
    def shot(self):
        return Bullet(self)

    # 展示坦克（将坦克这个surface绘制到窗口中)
    def displayTank(self):
        # 1、重新设置坦克的图片
        self.image = self.images[self.direction]
        # 2、将坦克加入到窗口中
        MainGame.window.blit(self.image, self.rect)


# 我方坦克
class MyTank(Tank):
    def __init__(self):
        pass


# 敌方坦克
class EnemyTank(Tank):
    def __init__(self, left, top, speed):
        # 加载图片路径
        self.images = {
            'U': pygame.image.load('img/enemy1U.gif'),
            'D': pygame.image.load('img/enemy1D.gif'),
            'L': pygame.image.load('img/enemy1L.gif'),
            'R': pygame.image.load('img/enemy1R.gif')
        }
        # 随机方向
        self.direction = self.randDirection()
        self.image = self.images[self.direction]
        # 坦克所在的区域  Rect->
        self.rect = self.image.get_rect()
        # 指定坦克初始化位置，分别距X ,Y轴的位置
        self.rect.left = left
        self.rect.top = top
        # 新增速度属性
        self.speed = speed
        # 新增属性:坦克移动的开关
        self.stop = True
        # 新增步数属性，用来控制敌方坦克
        self.step = 20

    def randDirection(self):
        num = random.randint(1, 4)
        if num == 1:
            return 'U'
        elif num == 2:
            return 'D'
        elif num == 3:
            return 'L'
        elif num == 4:
            return 'R'

    #   直接调用父类中的函数
    # def displayEnemtTank(self):
    #     super().displayTank()
    # 随机运动
    def randMove(self):
        if self.step <= 0:
            self.direction = self.randDirection()
            self.step = 20
        else:
            self.move()
            self.step -= 1
    # 重写了父类的shot()方法
    def shot(self):
        num = random.randint(1,1000)
        if num <= 35 :
            return Bullet(self)

# 子弹类
class Bullet():
    def __init__(self, tank):
        # 图片
        self.image = pygame.image.load('img/enemymissile.gif')
        # 方向(坦克方向)
        self.direction = tank.direction
        # 位置
        self.rect = self.image.get_rect()
        if self.direction == 'U':
            self.rect.left = tank.rect.left + tank.rect.width / 2 - self.rect.width / 2
            self.rect.top = tank.rect.top - self.rect.height
        elif self.direction == 'D':
            self.rect.left = tank.rect.left + tank.rect.width / 2 - self.rect.width / 2
            self.rect.top = tank.rect.top + tank.rect.height
        elif self.direction == 'L':
            self.rect.left = tank.rect.left - self.rect.width
            self.rect.top = tank.rect.top + tank.rect.width / 2 - self.rect.width / 2
        elif self.direction == 'R':
            self.rect.left = tank.rect.left + tank.rect.width
            self.rect.top = tank.rect.top + tank.rect.width / 2 - self.rect.width / 2
        # 速度
        self.speed = 7
        # 用来记录子弹时候可以消失
        self.live =True


    # 子弹的移动方法
    def bulletMove(self):
        if self.direction == 'U':
            if self.rect.top > 0:
                self.rect.top -= self.speed
            else:
                # 修改状态值
                self .live = False

        elif self.direction == 'D':
            if self.rect.top < MainGame.SCREEN_HEIGHT - self.rect.height:
                self.rect.top += self.speed
            else:
                # 修改状态值
                self.live = False
        elif self.direction == 'L':
            if self.rect.left > 0:
                self.rect.left -= self.speed
            else:
                # 修改状态值
                self.live = False
        elif self.direction == 'R':
            if self.rect.left < MainGame.SCREEN_WIDTH - self.rect.height:
                self.rect.left += self.speed
            else:
                # 修改状态值
                self.live = False

    # 展示子弹
    def displayBullet(self):
        MainGame.window.blit(self.image, self.rect)


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