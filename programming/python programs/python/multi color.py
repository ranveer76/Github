#multicolor drawing and back ground color
import turtle

t = turtle.Pen()
turtle.bgcolor("black")
colors = ["green", "red", "blue", "purple"]
for x in range(50,150):
    t.pencolor(colors[x%4])
    t.forward(x)
    t.left(92)
