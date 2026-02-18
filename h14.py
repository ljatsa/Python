# Loo programm, mis võimaldab kasutajatel hiire abil joonistada kujundeid (vali ise ruut, ring, kolmnurk vms) ekraanile ning muuta joonistusvärvi 
# klaviatuuri abil.
# Kasutajad peaksid saama kasutada hiire vasakut nuppu joonistamiseks ja paremat nuppu joonistatud elementide kustutamiseks.
# Klaviatuuri klahvid ‘R’, ‘G’ ja ‘B’ võimaldavad vastavalt värvi muuta punaseks, roheliseks või siniseks.


import turtle
turtle.speed(0)
ekraan = turtle.Screen()
def muuda_punane():
    turtle.color("red")
def muuda_roheline():
    turtle.color("green")

def vasakKlikk(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.circle(50)

def paremKlikk(x, y):
    turtle.undo()


ekraan.onscreenclick(vasakKlikk, 1) # Vasak klõps
ekraan.onscreenclick(paremKlikk, 3) # Parem klõps
ekraan.onkey(muuda_punane, "r")
ekraan.onkey(muuda_roheline, "g")
ekraan.listen()
turtle.done()