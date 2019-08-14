'''
v1.24
      新增功能
        实现坦克之间的碰撞检测
            1、我方坦克主动碰撞敌方坦克
                我方坦克停下来  stay（）
            2、敌方坦克主动碰撞我们的坦克
                敌方坦克要停下来 stay()

'''

import pygame, time, random

# 为了命名的简化，把pygame.display = _display
_display = pygame.display
# 规定的窗口的颜色
COLOR_BLACK = pygame.Color(1, 2, 3)
COLOR_RED = pygame.Color(255, 0, 0)
version = 'v1.24'


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
    # 爆炸效果列表
    Explode_list = []
    # 墙壁列表
    Wall_list = []

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
        self.creatMyTank()
        #   调用敌方坦克
        self.creatEnemyTank()
        # 调用墙壁
        self.creatWall()
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
            # 调用展示墙壁的方法
            self.blitWalls()
            if MainGame.TANK_P1 and MainGame.TANK_P1.live:
                # 将我方坦克加入到窗口中
                MainGame.TANK_P1.displayTank()
            else:
                del MainGame.TANK_P1
                MainGame.TANK_P1 = None
            # 循环展示敌方坦克
            self.blitEnemyTank()
            # 调用坦克的移动方法
            if MainGame.TANK_P1 and not MainGame.TANK_P1.stop:
                MainGame.TANK_P1.move()
                # 调用碰撞墙壁的方法
                MainGame.TANK_P1.hitWalls()
                # 我方坦克是否碰到敌方坦克
                MainGame.TANK_P1.hitEnemyTank()
            # 调用渲染子弹列表的一个方法
            self.blitBullet()
            # 调用渲染敌方子弹列表的一个方法
            self.blitEnemyBullet()
            # 调用爆炸效果的方法
            self.displayExplodes()
            # 添加一个休眠（大型的项目中最好不要这样）
            time.sleep(0.02)
            # 进行界面的刷新状态、pygame.display.update()
            _display.update()

    # 创建我方坦克
    def creatMyTank(self):
        MainGame.TANK_P1 = MyTank(350, 400)

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
    # 创建墙壁的方法
    def creatWall(self):
        for i in range(6):
            wall = Wall(130*i,240)
            MainGame.Wall_list.append(wall)

    # 将敌方坦克加入窗口中
    def blitEnemyTank(self):
        for eTank in MainGame.EnemyTank_list:
            if eTank.live:
                eTank.displayTank()
                # 坦克移动的方法
                eTank.randMove()
                # 调用敌方坦克与墙壁的碰撞机制
                eTank.hitWalls()
                # 敌方坦克是否撞到我的坦克
                # 调用敌方坦克的射击
                eBullt = eTank.shot()
                # 如果子弹为None 不加入到列表中
                if eBullt:
                    # 将子弹储存在敌方子弹的列表里面
                    MainGame.Enemy_bullet_list.append(eBullt)
            else:
                MainGame.EnemyTank_list.remove(eTank)

    # 将我方子弹加入到窗口中
    def blitBullet(self):
        for bullet in MainGame.Bullet_list:
            # 如果子弹还活着，绘制出来，否则直接在列表中删除
            if bullet.live:
                bullet.displayBullet()
                # 让子弹移动
                bullet.bulletMove()
                # 调用我方子弹与敌方子弹碰撞
                bullet.hitEnemyTank()
                # 调用判断我方子弹是否碰到墙壁的方法
                bullet.hitWalls()
            else:
                MainGame.Bullet_list.remove(bullet)

    # 敌方子弹加入窗口中
    def blitEnemyBullet(self):
        for ebullet in MainGame.Enemy_bullet_list:
            if ebullet.live:
                ebullet.displayBullet()
                # 将子弹移动
                ebullet.bulletMove()
                if MainGame.TANK_P1 and MainGame.TANK_P1.live:
                    ebullet.hitMyTank()
                # 调用敌方子弹是否碰撞到墙壁的方法
                ebullet.hitWalls()
            else:
                MainGame.Enemy_bullet_list.remove(ebullet)

    # 将墙壁加入窗口中
    def blitWalls(self):
        for wall in MainGame.Wall_list:
            if wall.live == True:
                wall.displayWall()
            else:
                MainGame.Wall_list.remove(wall)

    # 新增方法，展示爆炸效果列表
    def displayExplodes(self):
        for explode in MainGame.Explode_list:
            if explode.live:
                explode.displayExplode()
            else:
                MainGame.Explode_list.remove(explode)

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
                # 点击Esc按键让我方坦克重生
                if event.key == pygame.K_ESCAPE and not MainGame.TANK_P1:
                    # 调用创建我方坦克的方法
                    self.creatMyTank()

                if MainGame.TANK_P1 and MainGame.TANK_P1.live:
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
                        if len(MainGame.Bullet_list) < 3:
                            #   产生一个子弹
                            m = Bullet(MainGame.TANK_P1)
                            #   将子弹加入子弹列表
                            MainGame.Bullet_list.append(m)
                        else:
                            print('子弹数量不足')
                        print('当前屏幕中子弹的数量为：%d' % len(MainGame.Bullet_list))

            # 结束游戏的方法
            if event.type == pygame.KEYUP:
                # 修改坦克的方向
                if (event.key == pygame.K_LEFT) or (event.key == pygame.K_RIGHT) or (event.key == pygame.K_UP) or (
                        event.key == pygame.K_DOWN):
                    if MainGame.TANK_P1 and MainGame.TANK_P1.live:
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


# 衔接类(继承精灵类）
class BaseIem(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)


# 坦克类
class Tank(BaseIem):
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
        # 新增属性，用来记录坦克时候或者
        self.live = True
        # 新增属性，移动之前的坐标（让坦克不能穿墙）、用于坐标还原用途
        self.oldLeft = self.rect.left
        self.oldTop =self.rect.top
    # 坦克移动
    def move(self):
        # 先记录移动之前的坐标
        self.oldLeft = self.rect.left
        self.oldTop = self.rect.top
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
    # 还原方法：(穿墙）
    def stay(self):
        self.rect.left = self.oldLeft
        self.rect.top = self.oldTop
    # 新增坦克碰撞墙壁的方法
    def hitWalls(self):
        for wall in MainGame.Wall_list:
            if pygame.sprite.collide_rect(wall,self):
                self.stay()

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
    def __init__(self,left,top):
        super(MyTank, self).__init__(left,top)
    # 新增主动碰撞到敌方坦克的方法
    def hitEnemyTank(self):
        for eTank in MainGame.EnemyTank_list:
            if pygame.sprite.collide_rect(eTank,self):
                self.stay()


# 敌方坦克
class EnemyTank(Tank):
    def __init__(self, left, top, speed):
        # 引用父类的__init__()函数用super（）
        super(EnemyTank, self).__init__(left, top)
        # 再给自己增加一个属性也可以的
        # self.live = True
        self.live = True

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
        num = random.randint(1, 1000)
        if num <= 35:
            return Bullet(self)
    # 碰撞我方坦克的方法
    def hitMyTank(self):
        if pygame.sprite.collide_rect(self,MainGame.TANK_P1):
            # 碰撞之后要让敌方坦克停下来 stay()
            self.stay()

# 子弹类
class Bullet(BaseIem):
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
        self.live = True

    # 子弹的移动方法
    def bulletMove(self):
        if self.direction == 'U':
            if self.rect.top > 0:
                self.rect.top -= self.speed
            else:
                # 修改状态值
                self.live = False

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

    # 新增我方子弹碰撞敌方坦克的方法
    def hitEnemyTank(self):
        for eTank in MainGame.EnemyTank_list:
            if pygame.sprite.collide_rect(eTank, self):
                # 产生一个爆炸效果
                explode = Explode(eTank)
                # 将爆炸效果加入到爆炸效果中
                MainGame.Explode_list.append(explode)
                self.live = False
                eTank.live = False

    # 新增敌方子弹与我方坦克的碰撞方法
    def hitMyTank(self):
        if pygame.sprite.collide_rect(self, MainGame.TANK_P1):
            # 产生爆炸效果，并加入爆炸效果的列表中
            explode = Explode(MainGame.TANK_P1)
            MainGame.Explode_list.append(explode)
            # 修改子弹的状态
            self.live = False
            # 修改我方坦克的状态
            MainGame.TANK_P1.live = False

    #   新增子弹与墙壁的碰撞
    def hitWalls(self):
        for wall in MainGame.Wall_list:
            if pygame.sprite.collide_rect(wall,self):
                # 修改子弹的属性
                self.live = False
                # 让墙壁可以被打掉
                wall.hp -= 1
                if wall.hp <= 0 :
                    wall.live = False

# 爆炸效果类
class Explode():
    def __init__(self, tank):
        self.rect = tank.rect
        self.live = True
        self.step = 0
        self.images = [
            pygame.image.load('img/blast0.gif'),
            pygame.image.load('img/blast1.gif'),
            pygame.image.load('img/blast2.gif'),
            pygame.image.load('img/blast3.gif'),
            pygame.image.load('img/blast4.gif')
        ]
        self.image = self.images[self.step]

    # 展现爆炸效果
    def displayExplode(self):
        if self.step < len(self.images):
            MainGame.window.blit(self.image, self.rect)
            self.image = self.images[self.step]
            self.step += 1
        else:
            self.live = False
            self.step = 0


# 墙壁类
class Wall():
    def __init__(self,left,top):
        self.image = pygame.image.load('img/steels.gif')
        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.top =top
        # 判断墙壁是否应该在窗口中展示
        self.live = True
        # 墙壁的血量，记录墙壁打几次才能消掉
        self.hp = 3

    # 展示墙壁的方法
    def displayWall(self):
        MainGame.window.blit(self.image,self.rect)


# 音效类
class Music():
    def __init__(self):
        pass

    # 开始播放音乐
    def play(self):
        pass


game = MainGame()
game.startGame()
