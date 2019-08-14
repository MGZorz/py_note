'''1、第一题
x = input("请输入三个数字，第一个：")
y = input("第二个：")
z = input("第三个：")

if x == max(x,y,z):
    if y == max(y,z):
        print("从大到小排序为{0}，{1},{2}".format(x,y,z))
    else:
        print("从大到小排序为{0}，{1},{2}".format(x,z,y))
elif y == max(x,y,z):
    if x == max(x,z):
        print("从大到小排序为{0}，{1},{2}".format(y,x,z))
    else:
        print("从大到小排序为{0}，{1},{2}".format(y,z,x))
else:
    if y == max(x,y):
        print("从大到小排序为{0}，{1},{2}".format(z,y,x))
    else:
        print("从大到小排序为{0}，{1},{2}".format(z,x,y))
'''


'''第二题 星期一：Monday 星期二：Tuesday 星期三：Wednesday
    星期四：Thursday 星期五：Friday 星期六：Saturday 星期日：Sunday
# 如果是w 、m、f都是指定的 t、s需要第二个字母

x = input("请输入星期几的第一个字母")
if x in [ 'w','m','f','s','t']:
    print("让我想想")
    if x in ['w','m','f']:
        if x =='w':
            print("Wednesday")
        elif x =='m':
            print("Monday")
        else:
            print("Friday ")
    else:
        y = input("请输入星期几的第二个字母")
        if y =='h'and x == 't':
            print("Thursday")
        elif y =='u'and x =='t' :
            print("Tuesday")
        elif y=='a'and x =='s':
            print("Saturday")
        else:
            print("Sunday")
else :
    print("你怕是在刷我吧")

'''
'''第三题
num = int(input("输入数字"))
if num <1000:
    y = num
elif num <2000:
    y = 0.9*num
elif num <3000:
    y = 0.8*num
else:
    y = 0.7*num
print("算得{0}".format(y))

'''
'''第四题
# 先问男女、再问年级。
peopleNum = 0
for i in range(3):
    gender = input("请输入孩子的性别，女孩是f,男孩是m")
    age = int(input("孩子今年多大了？"))
    if gender == 'f'and age>=10 and age<=12 :
        peopleNum += 1
else:
    print("全部招完了，合格人数为{0}".format(peopleNum))

'''

'''第五题

x = int(input("输入三个数，第一个"))
y = int(input("第二个"))
z = int(input("第san个"))
listNum = [x,y,z]
print("最大值为{0},最小值为{1}".format(max(listNum),min(listNum)))

'''

'''第六题
grade_all = 0
grade = []
y =''
average = 0
while y !='q':
    x = int(input("请输入成绩"))
    y = input("是否结束输入,按q结束输入，否则按0继续")
    grade.append(x)
    grade_all += x
else:
    average = grade_all/len(grade)
    print("平均成绩为{0}".format(average))
    if average<60:
        print("不及格")
    elif average<70:
        print("及格")
    elif average<80:
        print("中")
    elif average<90:
        print("良")
    else:
        print("优")
'''

'''第七题
for i in range(1,10):
    for m in range(1,i+1):
        print("{0}*{1}={2}".format(i,m,(i*m)),end="\t")
    print()
'''

'''第八题、9、10、11'''
'''for i in range(1,10):
    print(" "*(10-i)+"*"*i +"*"*i)
'''
'''
for i in range(1,10):
    print(" "*(10-i)+"*"*i +"*"*(i-1))
for m in range(1, 10):
    print(" " * i + "*" * (10-i) + "*" * (9 - i ))
'''


# print(" "*10+"*"*1+"*"*0)
# print(" "*9+"*"*2+"*"*1)
# for i, n in zip(range(1, 10, 2),  range(1, 10)):
#     print(" " * (9-n) + "*" * 2 + " " * i + "*" * 2)
# for m, p in zip(range(1,10,2), range(4,10)):
#     print(" " * p + "*" * 2 + " " * (10-m) + "*" * 2)
# print(" " * 9 + "*" * 2 + "*" * 1)
# print(" " * 10 + "*" * 1 + "*" * 0)

# print("*"*9)
# for i in range(9):
#     if i == 0 or i==8:
#         print("*",end='')
#     else:
#         print(' ',end='')

# 第十二题
'''
import random
answer = []
while True:
    value = random.randrange(1, 101)
    ask = input("请您猜一下现在的数字，范围是（1,101）")
    if int(ask) == value:
        print("恭喜你猜对啦，真聪明")
    else:
        answer.append(ask)
        if len(answer) >= 3:
            print("游戏结束，小笨蛋")
            break
'''
# 第13题
'''
print("脑残社区账号登录")
print("用户名：admin")
flase = []
while True:
    key = input("请输入密码")
    if int(key) == 123:
        print("登录成功，请畅游脑残社区！！")
        break
    else:
        flase.append(key)
        if len(flase) == 1:
            print("还有两次机会，一共三次。")
            continue
        elif len(flase) == 2:
            print("还有一次机会，一共三次。")
            continue
        else:
            print("三次错误，已锁定账户")
            break
'''
# 第14题
'''
lis = []
x = 2
for x in range(2, 100):
    y = 2
    for y in range(2,x):
        if x%y == 0:
            break
    else:
        lis.append(x)
print(lis)
'''

# 第15题













