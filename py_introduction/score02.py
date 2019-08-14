score=int(input("请输入一个分数"))
level =""
if score<0 or score>100 :
    score=int(input("请输入一个正常的成绩-_-!"))
else:
    if score<60:
        level = "E"
    elif score<70:
        level = "D"
    elif score<80:
        level = "C"
    elif score<90:
        level = "B"
    else:
        level = "A"
    print("大哥，你的分数是{0}，分级是{1}".format(score,level))

print("****************************************************************")

score = int(input("请输入一个成绩"))
degree = "ABCDE"
num = 0
if score>100 or score<0:
    score=int(input("请输入一个正常的成绩-_-!"))
else:
    num = score//10
    if num <6:
        num = 5
    print("您的成绩评级为[0]".format(degree[9-num]))





