import random #随机数模块

d = 0
p = 0
c = 0

dict1 = {
    '剪刀':1,
    '石头':2,
    '布':3,
}

print('-------------猜拳游戏---------------')
print('********************')
print('1、开始进行新游戏')
print('2、退出')
print('********************')
change = int(input('请选择'))
if change == 1 :
    while True:
        rand = random.randint(1, 3)  # 取随机数
        while True :
            i = int(input('请输入手势，剪刀：1、石头：2、布：3'))
            if i in dict1.values():
                break
            else:
                print('Error:是一个错误的手势哦~')
            if rand == 1 :
                if rand == i :
                    result =('平局')
                    d += 1
                elif i ==2:
                    result =('你赢啦，积一分')
                    p += 1
                else :
                    result = ('好遗憾，你输了，下次加油')
                    c += 1
            elif rand == 2:
                if i == rand:
                    result = ('平局')
                    d += 1
                elif i ==1:
                    result = ('好遗憾，你输了，下次加油')
                    c += 1
                else:
                    result = ('你赢啦，积一分')
                    p += 1
            else :
                if i == rand:
                    result = ('平局')
                    d += 1
                elif i ==2:
                    result = ('好遗憾，你输了，下次加油')
                    c += 1
                else:
                    result = ('你赢啦，积一分')
                    p += 1
            print(result)

elif change == 2:
    print('游戏结束!\n 本次猜拳的结果为：您积{0}分'.format(p))
else:
    print('输入错误，程序暴毙！！')
