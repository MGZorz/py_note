('''绘制奥运五环了
	先导入一个模块''')
import turtle  
('''然后开始画第一个圆了''')
turtle.width(5)   # 规定线的粗细
turtle.color("blue")#  这是要给笔上色了
turtle.circle(25)  # 25为半径
# 去下一个点在画一个圆
turtle.penup()
turtle.goto(60,0)
turtle.pendown()
turtle.color("black")
turtle.circle(25)
turtle.penup()
turtle.goto(120,0)
turtle.pendown()
turtle.color("red")
turtle.circle(25)
turtle.penup()
turtle.goto(30,-25)
turtle.pendown()
turtle.color("yellow")
turtle.circle(25)
turtle.penup()
turtle.goto(90,-25)
turtle.pendown()
turtle.color("green")
turtle.circle(25)