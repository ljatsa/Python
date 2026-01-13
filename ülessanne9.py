import random
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

#9.6
# Kuva nimekirjast unikaalsed nimed:
# nimed = ['Martin', 'Tõnu', 'Andres', 'Tõnu', 'Andres', 'Andres', 'Andres', 'Tõnu', 'Marko', 'Mari', 'Jüri', 'Liis', 'Marko', 'Piret', 'Anu']
# puhas = []
# for nimi in nimed:
#     if nimi not in puhas:
#         puhas.append(nimi)
#         
# print(puhas)
# 

# #ülesanne9.8
# for i in range(11):
#     print(f"{i} * {i} = {i*i}")
#     
    
    
    
#ülesanne9.9 
# tehe = ["+","-","*","/"]
# punktid = 0
# kysimuste_arv = 10
# for _ in range(kysimuste_arv):
#     arv1 = random.randint(1,10)
#     arv2 = random.randint(1,10)
#     t = random.choice(tehe)
#     
#     if t =="+":
#         print(f"{arv1}{t}{arv2}=")
#         v = int(input("Vastus: "))
#         if arv1+arv2 == v:
#             punktid+=1
#     elif t =="-":
#         print(f"{arv1}{t}{arv2}=")
#         v = int(input("Vastus: "))
#         if arv1-arv2 == v:
#             punktid+=1
#     elif t =="/":
#         print(f"{arv1}{t}{arv2}=")
#         v = float(input("Vastus: "))
#         if round(arv1/arv2,1) == v:
#             punktid+=1
#     else:
#         print(f"{arv1}{t}{arv2}=")
#         v = int(input("Vastus: "))
#         if arv1*arv2 == v:
#             punktid+=1
# if punktid/kysimuste_arv >=0.5:
#     print (f"A - {punktid}/{kysimuste_arv}")
# else:
#     print (f"MA - {punktid}/{kysimuste_arv}")
# 
# print(punktid)



# ülesanne 11.1
 arv = 5
 for i in range(1,6):
     print(" " * i + "*" * arv)
     arv-=1
     
    
    
    
# ülesanne 11.2
 arv = 5
 for i in range(1,6):
     print("*" * arv)
     arv-=1

# ülesanne 11.3

 for i in range(1,6):
     print(" " * arv + "*" * i)
     arv-=1
    

# ülesanne 11.4
  for i in range(1,6):
      print("*" * i)












