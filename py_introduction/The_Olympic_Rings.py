('''绘制奥运五环''')
import turtle

turtle.width(10)

turtle.color("blue")
turtle.circle(50)

turtle.penup()
turtle.goto(120,0)
turtle.pendown()

turtle.color("black")
turtle.circle(50)
turtle.penup()
turtle.goto(240,0)
turtle.pendown()
turtle.color("red")
turtle.circle(50)
turtle.penup()
turtle.goto(60,-50)
turtle.pendown()
turtle.color("yellow")
turtle.circle(50)
turtle.penup()
turtle.goto(180,-50)
turtle.pendown()
turtle.color("green")
turtle.circle(50)








('''绘制奥运五环了
	先导入一个模块''')
import turtle  
('''然后开始画第一个圆了''')
turtle.circle(100)  # 50为半径
# 去下一个点在画一个圆

turtle.goto(100,0)