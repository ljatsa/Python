import turtle

t = turtle.Turtle()
t.speed(0)

def ruut(pikkus):
    for i in range(4):
        t.forward(pikkus)
        t.left(90)

ruut(150)

t.penup()
t.forward(190)
t.right(-135)
t.forward(135)
t.left(-135)
t.pendown()

ruut(150)

turtle.done()
