import turtle as t
c=["red","lime","blue","yellow","magenta","cyan"]
t.setup(800,700)
t.bgcolor("black")
t.width(2)
t.pensize(2)
t.tracer(10)
t.speed(0)
for i in range(25):
    for j in range(5):
        t.color(c[i%6])
        t.right(90)
        t.circle(250-i*4,90)
        t.left(90)
        t.circle(250-i*4,90)
        t.right(180)
        t.circle(50,24)
for i in range(25):
    for j in range(5):
        t.color(c[i%6])
        t.right(90)
        t.circle(250-i*4,90)
        t.left(90)
        t.circle(250-i*4,90)
        t.right(180)
        t.circle(50,24)
t.hideturtle()
t.done()
