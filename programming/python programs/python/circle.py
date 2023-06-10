# circle

import turtle
t = turtle.Pen()

name=["circle","triangle","square","turtle"]

turtle.bgcolor("black")
colors = ["red", "yellow", "cyan", "lime"]

colors1=["blue","green","tan","purple"]

for x in range(50,250):

    t.shape(name[x%4])
    
    t.pensize(width=10)
    t.fillcolor(colors1[x%4])
    t.pencolor(colors[x%4])
    t.circle(x)
    t.left(12)
