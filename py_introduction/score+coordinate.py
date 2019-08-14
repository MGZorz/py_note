
'''b = []
if not b :
    print("空列表是False")
'''

'''c = "False"  # 非空字符串也是：True
if  c :
    print("c")'''

'''d = 0
if d:
    print("d")'''

'''  if 3<c and(c==20):   条件表达式不能是出现“=”
      print("赋值符不能出现在条件表达式中")'''

'''a = input("请输入一个数字")
if int(a)<10:
    print("a是小于10的数字")
else:
    print("a是一个大于10的数字")
# 测试三元运算符
print("a是一个小于10的数字"if int(a)<10 else "a是一个大浴室的数字")
'''
score = int(input("请输入一个成绩"))
('''if score<60:
    print("不及格")
elif score<79:
    print("及格")
elif score<89:
    print("良好，继续加油")
else:
    print("非常棒哦！优秀")
''')
grade=""
if score<0:
    grade="你真是个人才啊"
elif score<60:
    grade = "不及格"
elif score<79:
    grade = "及格"
elif score<89:
    grade = "良好"
else:
    grade = "优秀"
print("你的成绩是"+str(score)+"，"+grade+"。")


x = int(input("请输入一个横坐标"))
y = int(input("请输入一个纵坐标"))
if x>0 and y>0:
    print("坐标在第一象限")
elif x>0 and y<0:
    print("坐标在第四象限")
elif x<0 and y>0:
    print("坐标在第二象限")
elif x==0 :
    if y==0:
        print("坐标在原点")
    else :
        print("坐标在Y轴")
elif y==0:
    if x!=0:
        print("坐标在X轴")
else:
    print("坐标在第三象限")

