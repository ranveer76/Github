import turtle
t = turtle.Pen()
colors = ["yellow", "green", "red", "blue"]
turtle.bgcolor("black")
t.pensize(2)
t.speed(10)
for x in range(600):
    t.pencolor(colors[x%4])
    t.forward(x)
    t.left(94)
