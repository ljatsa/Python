# #ülesanne 11
# #Lisett-Rosette Jätsa
import turtle
import random
def pikim_sona(list):
    pikimArv = 0
    pikimNimi = ""
    for i in list:
        if len(i) > pikimArv:
            pikimArv = len(i)
            pikimNimi = i
    return pikimNimi


def kolm_pikimat_sona(list):
    if len(nimed) > 2:
        list.sort(key = len, reverse = True)
    return list [0:3]
nimed = ["Joosep", "Joonas", "Mario", "Kivakesekesekene","Sergei"]

def viisnurk(k):
    for i in range(5):
        turtle.fd(k)
        turtle.lt(144)

def ring(r):
    turtle.circle(r)

def ruut(k):
    for i in range(4):
        turtle.fd(k)
        turtle.lt(90)

def suvaline(n):
    suv = random.randit(1,3)
    if suv==1:
        viisnurk(n)
    elif suv==2:
        ring(n)
    else:
        ruut(n)

print(kolm_pikimat_sona(nimed))
print(pikim_sona(nimed))

suvaline(100)

turtle.done()
        
