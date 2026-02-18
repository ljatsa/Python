import turtle
import random

# Ekraan
aken = turtle.Screen()
aken.bgcolor("lightblue")
aken.setup(width=600, height=600)
aken.tracer(0)

# Ristkülik
ristkylik = turtle.Turtle()
ristkylik.shape("square")
ristkylik.shapesize(stretch_wid=1, stretch_len=5)
ristkylik.penup()
ristkylik.color("black")
ristkylik.goto(ristkylik.xcor(), -250)

# Ring
ring = turtle.Turtle()
ring.shape("circle")
ring.penup()
ring.speed('fastest')
ring.setheading(random.randint(0, 360))

# kiirused
ristkyliku_kiirus = 20
kiirus = 10
punktid = 0


def mäng_lõppeb():
    global punktid
    ring.hideturtle()
    ristkylik.hideturtle()
    aken.clear()
    aken.bgcolor("black")
    aken.update()
    aken.bye() 

def kuva_punktid():
    global punktid
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(0, 260)
    turtle.color("black")
    turtle.write(f"Punktid: {punktid}", align="center", font=("Arial", 16, "normal"))
# ristküliku funktsioonid
def liigu_vasakule():
    x = ristkylik.xcor()
    if x > -280:
        ristkylik.setx(x - ristkyliku_kiirus)

def liigu_paremale():
    x = ristkylik.xcor()
    if x < 280:
        ristkylik.setx(x + ristkyliku_kiirus)
def kokkuporgub():
    global punktid
    ristkylik_x = ristkylik.xcor()
    ristkylik_y = ristkylik.ycor()
    ristkylik_width = 50  
    ristkylik_height = 20 

    ring_x = ring.xcor()
    ring_y = ring.ycor()

    if (ring_x > ristkylik_x - ristkylik_width / 2 and ring_x < ristkylik_x + ristkylik_width / 2) and \
       (ring_y > ristkylik_y - ristkylik_height / 2 and ring_y < ristkylik_y + ristkylik_height / 2):
        punktid += 1
        kuva_punktid()

        if punktid % 5 == 0:
            global kiirus, ristkyliku_kiirus
            kiirus += 2  
            ristkyliku_kiirus += 5  


def ring_liigu():
    global punktid
    ring.forward(kiirus)
    kokkuporgub()
    if ring.ycor() < -300:
        mäng_lõppeb()
    if ring.xcor() >= 300 or ring.xcor() <= -300:
        nurk = ring.heading()
        uus_nurk = 180 - nurk
        if uus_nurk < 0:
            uus_nurk += 360
        ring.setheading(uus_nurk)
    if ring.ycor() >= 300 or ring.ycor() <= -300:
        nurk = ring.heading()
        uus_nurk = 360 - nurk
        ring.setheading(uus_nurk)
    aken.update()
    aken.ontimer(ring_liigu, 20)

# klaviatuurile reageerimine
aken.listen()
aken.onkeypress(liigu_vasakule, "Left")
aken.onkeypress(liigu_paremale, "Right")

ring_liigu()
kuva_punktid()
kokkuporgub()
aken.mainloop()
