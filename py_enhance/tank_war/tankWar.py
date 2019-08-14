 import pygame,random

_display = pygame.display
TEXT_COLOR = pygame.Color(255, 0, 0)
COLOR_BLACK = pygame.Color(1, 2, 3)


class MainGame():
    window = None
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 500
    Tank_P1 = None
    EnemyTank_count = random.randint(6,10)
    EnemyTank_list = []


    def __init__(self):
        pass

    def startGame(self):
        pygame.display.init()
        MainGame.window = _display.set_mode([MainGame.SCREEN_HEIGHT, MainGame.SCREEN_WIDTH])
        MainGame.Tank_P1 = Tank(350, 400)
        self.creatEnemyTank()
        _display.set_caption('坦克大战鸭！')
        while True:
            MainGame.window.fill(COLOR_BLACK)
            self.getEvent()
            MainGame.window.blit(self.getText('剩余坦克的数量是（5）辆'), (5, 5))
            MainGame.Tank_P1.displayTank()
            self.blitEnemyTank()
            if MainGame.Tank_P1 and not MainGame.Tank_P1.stop:
                MainGame.Tank_P1.move()
            _display.update()

    def getEvent(self):
        Event_List = pygame.event.get()
        for event in Event_List:
            if event.type == pygame.QUIT:
                self.endGame()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    print('向上运动')
                    MainGame.Tank_P1.direction = 'U'
                    # MainGame.Tank_P1.move()
                    MainGame.Tank_P1.stop = False
                elif event.key == pygame.K_DOWN:
                    print('向下运动')
                    MainGame.Tank_P1.direction = 'D'
                    # MainGame.Tank_P1.move()
                    MainGame.Tank_P1.stop = False
                elif event.key == pygame.K_LEFT:
                    print('向左运动')
                    MainGame.Tank_P1.direction = 'L'
                    # MainGame.Tank_P1.move()
                    MainGame.Tank_P1.stop = False
                elif event.key == pygame.K_RIGHT:
                    print('向右运动')
                    MainGame.Tank_P1.direction = 'R'
                    # MainGame.Tank_P1.move()
                    MainGame.Tank_P1.stop = False
                elif event.key == pygame.K_SPACE:
                    print('发射子弹')
            elif event.type == pygame.KEYUP:
                if (event.key == pygame.K_UP) or (event.key == pygame.K_DOWN) or (event.key == pygame.K_LEFT) or (
                        event.key == pygame.K_RIGHT):
                    MainGame.Tank_P1.stop = True
    def creatEnemyTank(self):
        for i in range(MainGame.EnemyTank_count):
            left = random.randint(2, 5)
            top = random.randint(1, 2)
            speed = random.randint(2, 4)
            eTank = EnemyTank(left*100,top*100,speed)
            MainGame.EnemyTank_list.append(eTank)
    def blitEnemyTank(self):
        for eTank in MainGame.EnemyTank_list:
            eTank.displayTank()
            eTank.randMove()
    def getText(self, text):
        pygame.font.init()
        font = pygame.font.SysFont('kaiti', 18)
        Text = font.render(text, True, TEXT_COLOR)
        return Text

    def endGame(self):
        print('谢谢使用')
        exit()


class Tank():
    def __init__(self, left, top):
        self.images = {
            'U': pygame.image.load('img/p1tankU.gif'),
            'D': pygame.image.load('img/p1tankD.gif'),
            'L': pygame.image.load('img/p1tankL.gif'),
            'R': pygame.image.load('img/p1tankR.gif')
        }
        self.direction = 'U'
        self.image = self.images[self.direction]
        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.top = top
        self.speed = 5
        self.stop = True

    def move(self):
        if self.direction == 'U':
            if self.rect.top > 0:
                self.rect.top -= self.speed
        elif self.direction == 'D':
            if self.rect.top + self.rect.height < MainGame.SCREEN_HEIGHT:
                self.rect.top += self.speed
        elif self.direction == 'L':
            if self.rect.left > 0:
                self.rect.left -= self.speed
        elif self.direction == 'R':
            if self.rect.left + self.rect.width < MainGame.SCREEN_WIDTH:
                self.rect.left += self.speed

    def shot(self):
        pass

    def displayTank(self):
        # 1、重新设置坦克的图片
        self.image = self.images[self.direction]
        # 2、将坦克加入到窗口中
        MainGame.window.blit(self.image, self.rect)


class MyTank(Tank):
    def __init__(self):
        pass


class EnemyTank(Tank):
    def __init__(self,top,left,speed):
        self.images ={
            'U':pygame.image.load('img/enemy1U.gif'),
            'D':pygame.image.load('img/enemy1D.gif'),
            'L':pygame.image.load('img/enemy1L.gif'),
            'R':pygame.image.load('img/enemy1R.gif')
        }
        self.direction = self.randDirection()
        self.image = self.images[self.direction]
        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.top = top
        self.speed = speed
        self.stop = True
        self.step = 100

    def randDirection(self):
        num = random.randint(1,4)
        if num == 1 :
            return 'U'
        elif num == 2:
            return 'D'
        elif num == 3 :
            return 'L'
        elif num == 4 :
            return 'R'
    def randMove(self):
        if self.step <=0:
            self.direction =self.randDirection()
            self.step = 100
        else:
            self.move()
            self.step -= 1




class Bullet():
    def __init__(self):
        pass

    def move(self):
        pass

    def displayBullet(self):
        pass


class Explode():
    def __init__(self):
        pass

    def displayExplde(self):
        pass


class Music():
    def __init__(self):
        pass

    def play(self):
        pass


class Wall():
    def __init__(self):
        pass

    def displayWall(self):
        pass


MainGame().startGame()
