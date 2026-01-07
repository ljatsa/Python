import turtle
import math

t = turtle.Turtle()
t.speed(0)

# mõõdud
kylg = 30
rist_pikkus = 90
rist_laius = 30
alla = 20
paremale= 5
alla1 = 30

raadius = kylg/(2.1 * math.tan(math.pi / 8))

# kaheksanurk
def kaheksanurk():
    for i in range(8):
        t.forward(kylg)
        t.left(45)

# ristkülik
def ristkylik():
    for i in range(2):
        t.forward(rist_pikkus)
        t.left(90)
        t.forward(rist_laius)
        t.left(90)

# kaheksanurk
t.penup()
t.goto(-kylg/2.5, -raadius - alla)
t.pendown()
kaheksanurk()

# ristkülikud 
t.penup()
t.goto(-2.5, -alla1)
t.pendown()

for i in range(8):
    t.penup()
    t.forward(7)
    t.forward(raadius+1)
    t.pendown()
    ristkylik()
    t.penup()
    t.backward(raadius)
    t.left(45)
    t.pendown()

turtle.done()
