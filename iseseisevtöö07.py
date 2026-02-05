import turtle

t = turtle.Turtle()
t.speed(0)
# muutujad
rist_pikkus = 90
rist_laius = 30
vahe = 30
# ristkülikud
def ristkylik():
    for i in range(4):
        t.forward(rist_laius)
        t.left(90)
        t.forward(rist_pikkus)
        t.left(90)

for i in range(8):
    ristkylik()             
    t.penup()
    t.forward(vahe)     
    t.right(360 / 8)    
    t.pendown()

turtle.done()
