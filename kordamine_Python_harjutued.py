#kordmine_Python_harjutused
# #09.12.2025
# tsitaat="'üks kord me võidae niikuinii' - heinz"
# print(tsitaat)


#ülesanne 4
# pe = "Jätsa, Lisett-Rosette"
# pe2 = pe.split(", ")
# print(pe2[0].upper())
# print(len(pe2[0]))


#ülesanne 6
# andmerida="1,Marshal,Martinovic,mmartinovic0@dedecms.com,Male,40.19.226.175"
# andmed=andmerida.split(",")
# nimi=andmed[3].split("@")[0]
# ip=andmed[-1]
# print(ip)
# print(nimi)


# #ülessanne 8
# postitused = 137
# lk = round(postitused/10)
# viimane = postitused % 10
# if viimane == 0:
#     print(10)
# else:
#     print(lk)
# print(viimane)


#Ülessanne 10
# paevad = ["Esmaspäev", "Teisipäev", "Kolmapäev", "Neljapäev", "Reede"]
# print(paevad)
# print(len(paevad))
# paevad.append("Laupäev")
# paevad.append("Pühapäev")
# print(paevad)
# paevad.sort(reverse = True)
# print(paevad[-1])


#Ülessanne 12
# tulemused = [["Alice", 25, [10.2, 9.8, 10.5]],
# ["Bob", 22, [9.5, 9.6, 9.7]],
# ["Charlie", 28, [11.1, 11.2, 11.5]]]
# for x in tulemused:
#     
#     print (x[0],max(x[2]))


#ülessanne 14
# piletityyp="soodus"
# vanus=17
# 
# if piletityyp=="tais" and vanus<18:
#     print(10)
# elif piletityyp=="tais" and vanus>=18 and vanus<=64:
#     print(20)
# elif piletityyp=="soodus" and vanus<18 or vanus >=65:
#     print(8)
# else:
#     print(15)


#ülesanne 16
# Temp=[[5, 8, 12, 10, 7, 9, 11, 14, 16, 13, 10, 6, 4, 3, 2, 4, 6, 8, 10, 12, 15,
# 17, 18, 16, 13, 10],
# [1, 4, 6, 7, 9, 11, 13, 15, 12, 9, 7, 5, 3, 2, 3, 6, 8, 10, 12, 15, 17, 19,
# 18, 16, 13, 11],
# [8, 10, 13, 15, 16, 18, 19, 20, 17, 15, 13, 11, 10, 9, 8, 10, 12, 14, 16,
# 18, 20, 22, 21, 18, 16, 14],
# [2, 5, 7, 9, 12, 15, 17, 18, 15, 13, 11, 8, 6, 5, 4, 7, 9, 12, 14, 16, 19,
# 21, 20, 18, 16, 13],
# [6, 8, 11, 14, 16, 18, 20, 21, 18, 15, 12, 10, 8, 6, 5, 8, 10, 13, 15, 18,
# 20, 22, 21, 19, 16, 13],
# [11, 14, 17, 19, 21, 23, 24, 22, 19, 16, 13, 11, 10, 9, 9, 12, 15, 18, 20,
# 23, 25, 27, 26, 24, 21, 18],
# [9, 11, 14, 16, 18, 20, 22, 21, 18, 16, 13, 11, 9, 8, 7, 10, 13, 16, 18,
# 21, 23, 24, 23, 21, 18, 15],
# [7, 10, 13, 15, 17, 20, 22, 23, 20, 17, 14, 12, 10, 9, 8, 11, 14, 17, 19,
# 22, 24, 26, 25, 23, 20, 17],
# [3, 6, 9, 11, 13, 15, 17, 18, 16, 14, 11, 9, 7, 6, 5, 8, 10, 13, 15, 17,
# 19, 21, 20, 18, 15, 12],
# [1, 3, 5, 7, 9, 11, 13, 15, 12, 9, 7, 5, 3, 2, 3, 6, 8, 10, 12, 15, 17, 19,
# 18, 16, 13, 11],
# [6, 8, 11, 14, 16, 18, 20, 21, 18, 15, 12, 10, 8, 6, 5, 8, 10, 13, 15, 18,
# 20, 22, 21, 19, 16, 13],
# [10, 13, 16, 18, 20, 22, 23, 24, 21, 18, 15, 13, 11, 10, 9, 12, 15, 18, 20,
# 23, 25, 27, 26, 24, 21, 18]]
# suurimtemp=0
# for x in Temp:
#     print(sum(x)/len(x))
#     if max(x)>suurimtemp:
#         suurimtemp=max(x)
#         
# print("Kõige suurimtemp", suurimtemp)


#Ülessanne 1
# tunnid = 2
# minutid = 38
# sekundid = 59
# kellaaeg = f"{tunnid}:{minutid}:{sekundid}PM."
# print(kellaaeg)











