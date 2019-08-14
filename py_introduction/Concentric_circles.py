# 绘制同心圆。
import turtle
p = turtle.Pen()
pen_color = ("red","green","blue","yellow","black")
p.speed(0)
p.width(5)
for i in range(10):
    p.penup()
    p.goto(0, -i * 10)
    p.pendown()
    p.color(pen_color[i % len(pen_color)])
    p.circle(10+i*10)


turtle.done()