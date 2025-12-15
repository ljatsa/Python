# #Ülesanne 9.2
# #15.12.2025
# #Lisett-Rosette Jätsa
# import random
# # Genereeri ja kuva 20 suvalist arvu vahemikus 1-99
# # import random
# # random.randint(min, max)
# 
# for i in range(20):
#     print(random.randint(1, 99))
#     
#     
#     
# # Kuva arvud 1-42
# # Arvud, mis jagunevad 3, lisa tekst TIK (näiteks 3 TIK)
# # Arvud, mis jagunevad 5, lisa tekst TAK (näiteks 5 TAK)
# # Kui jagunevad mõlemaga, siis lisa tekst TIKTAK (näiteks 15 TIKTAK)
# 
# for i in range(1, 43):
#     print(i)
#     if i%3==0 and i%5==0:
#         print("TIKTAK")
#     elif i%3==0:
#         print("TIK")
#     elif i%5==0:
#         print("TAK")
#         


# Kuva nimekirjast unikaalsed nimed:
nimed = ['Martin', 'Tõnu', 'Andres', 'Tõnu', 'Andres', 'Andres', 'Andres', 'Tõnu', 'Marko', 'Mari', 'Jüri', 'Liis', 'Marko', 'Piret', 'Anu']
puhas = []
for nimi in nimed:
    if nimi not in puhas:
        puhas.append(nimi)
        
print(puhas)