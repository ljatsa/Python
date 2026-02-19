# Kirjutage Pythoni skript, mis tervitab kasutajat, kuvab praeguse töökataloogi, loob uusi katalooge vastavalt kasutaja soovile ning küsib,
# millist kataloogi soovitakse kustutada.
# Skript tervitab kasutajat tema operatsioonisüsteemi sisselogimisnime alusel
# Skript kuvab kasutajale praeguse töökataloogi tee
# Kataloogide loomine:
# Skript küsib kasutajalt, mitu kataloogi ta soovib luua


import os
from datetime import date
print(f"Hello {os.getlogin()}")
print(f"Sinu kataloogitee:{os.getcwd()}")
today = date.today()
os.mkdir(str(today))
# Kataloogid luuakse praegusesse töökataloogi kuupäevaga märgistatud kataloogi sees, nummerdatuna (nt “1”, “2”)
mitu = int(input("Mitu kataloogi tahad teha: "))
for i in range (mitu):
    os.mkdir(str(today)+"/"+str(i+1))
    print(f"Kataloogid 1-{mitu}tehtud")

kustuta = input(f"Kustuta valikust 1-{mitu}:")
path = os.getcwd()+'\\'+str(today)+'\\'+ kustuta
# print(path)
isdir = os.path.isdir(path)
if isdir:
    os.rmdir(path)
# Kataloogi kustutamine:
# Pärast kataloogide loomist küsib skript kasutajalt, millist äsja loodud või olemasolevat kataloogi soovitakse kustutada, esitades kataloogi
# nime 1, 2 jne
# Kui sisestatud kataloogi nimi eksisteerib, kustutatakse see
# Kuva kuupäeva kasutas olevad kataloogid


