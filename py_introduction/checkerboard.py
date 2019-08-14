import turtle
p = turtle.Pen()
p.speed(5) # 绘制速度
p.width(5) # 绘制宽度
p_color = ("blue","yellow","red","green")  # 绘制颜色
for i in range(11): # 0 1 2 3...
    p.penup()
    p.goto(0, i*20)    # 0 1 2 3
    p.pendown()
    p.color(p_color[i%len(p_color)])
    p.forward(200)
    p.right(90)
for x in range(11):
    p.penup()
    p.goto(x*20,200)
    p.pendown()
    p.color(p_color[x % len(p_color)])
    p.forward(200)
turtle.done()