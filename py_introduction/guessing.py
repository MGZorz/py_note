'''
猜拳游戏
分析类：属性、方法

自己玩家：Player  选角色[“美羊羊”，“喜羊羊”,"沸羊羊"]
​         出拳 石头1 剪刀2  布3
计算机玩家：Computer 选角色[“1美羊羊”，“2喜羊羊”,"3沸羊羊"] 随机选角
​          随机出拳
game类，包含了整个游戏流程，让玩家选角色、出拳、计算机选角色、出拳、比较出拳，显示解决

再玩一次

赢+1分
可以循环玩
当游戏结束之后，可以提示计算机和玩家的分数
'''
#
# class PlayerPerson():
#     def __init__(self):
#         # 全部的可能，羊和拳头
#         self.sheep = []
#         self.punch = []
#         sheeps = ['美羊羊','喜羊羊','沸羊羊']
#         punches =['石头','剪刀','布']
#         for i in sheeps:
#             self.sheep.append(i)
#         for j in punches:
#             self.punch.append(j)

import random   #随机数模块

num = 3
d = 0
p = 0
n = 0

dict1 = {
    1:"剪刀",
    2:"石头",
    3:"布",
}
print("--------- By.Aixce 猜拳小游戏 ---------")
print ("*********************")
print ("1. 开始新游戏")
print ("2. 退出")
print ("*********************")
change = input("请选择:")
if change == '1':
    while num > 0:
        rand = random.randint(1, 3)  # 取随机数
        while True:
            i = input('请输入手势[剪刀、石头、布]：')
            k = i.strip()   #移除前后空格
            if k in dict1.values():   #判断用户输入的值是否在字典中
                break
            else:
                print("Error:“%s”是一个错误手势"%(i))

        if rand == 1:
            if k == "剪刀":
                result = ("平局")
                p += 1
            elif k == "石头":
                result = ("恭喜！你赢了。")
                n += 1

            else:
                result = ("电脑胜")
                d += 1

        elif rand == 2:
            if k == "剪刀":
                result = ("电脑胜")
                d += 1
            elif k == "石头":
                result = ("平局")
                p += 1
            else:
                result = ("恭喜！你赢了。")
                n += 1
        else:
            if k == "剪刀":
                result = ("恭喜！你赢了。")
                n += 1
            elif k == "石头":
                result = ("电脑胜")
                d += 1
            else:
                result = ("平局")
                p += 1

        print("电脑出的是：%s\n你出的是：%s\n结果是：%s"%(dict1[rand],k,result))
        num -= 1
        g = d + p + n
        if num == 0:
            print("本次猜拳的结果是：（平局：%s局、获胜：%s局、失败：%s局)"%(p,n,d))
            if n > d:
                print("经过%s个回合你赢了。"%(g))
            elif n < d:
                print("经过%s个回合电脑胜。"%(g))
            else:
                j = input("经过%s回合后未能分出胜负是否继续[y/n]："%(g))
                if j == "y" or j == "Y" or j == "是":
                   num = 3
    else:
        exit()
print("游戏结束.")


