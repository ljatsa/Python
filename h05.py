#ülessanne 5
# Lisett-Rosette 26.11.25
import random
#5.3 Matemaatika test (randit)
arv1 = random.randint(1,10)
arv2 = random.randint(1,10)
vastus = int(input(f"{arv1} * {arv2} = "))
if vastus == arv1 * arv2:
    print("Õige")
else:
    print("Nõrk oled!")





#5.1 vanusepiiranguga üritus
piirang = 18
vanus = int(input("Sisesta oma vanus: "))

if vanus >=piirang:
    print("Saab sisse!")
else:
    print("Ei saa sisse!")