# 测试break语句。

'''while True :
    d = input("输入Q或者q的时候推出")
    if d =="q" or d =="Q" :
        print("循环结束，推出")
        break
    else:
        print(d)
'''

# 输入员工工资，若薪资小于0 则重新输入，最后打印员工的数量以及工资明细，还有平均薪资。

'''
name = []
emnum = 0
salary = []
while True:
    a = input("请输入员工姓名。")
    b = input("请输入薪资水平，按Q或者q结束。")
    if b == "Q" or a == "q":
        break
    else:
        emnum += 1
        name.append(a)
        salary.append(b)

print("员工有{0}，各自的工资水平为{1}元".format(name,salary),end="\t")
print("共有员工{0}名".format(emnum))
'''

# empNum = 0
# salarySum = 0
# salarys = []
# for i in range(4):
#     s = input("请输入员工的薪资（按Q或者q结束)")
#
#     if s.upper() == "Q":
#         print("录入完成，推出")
#         break
#     if float(s) < 0:
#         continue
#     empNum += 1
#     salarys.append(float(s))
#     salarySum += float(s)
# else:
#     print("您已经录入全部4名员工工资。")
#     print("员工数{0}".format(empNum))
#     print("录入薪资：", salarys)
#     print("平均薪资为{0}".format(salarySum / empNum))
