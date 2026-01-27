# #ülesanne 11.1
# #Lisett-Rosette Jätsa
# 
# def pikim_sona(list):
#     pikimArv = 0
#     pikimNimi = ""
#     for i in list:
#         if len(i) > pikimArv:
#             pikimArv = len(i)
#             pikimNimi = i
#     return pikimNimi

#ülesanne 11.2
def kolm_pikimat_sona(list):
    if len(nimed) < 3:
        return sorted(nimed, key = len, reverse = True)
    return sorted(nimed, key = len, reverse = True)[:3]
nimed = ["Joosep", "Joonas", "Mario", "Kivakesekesekene","Sergei"]

print(kolm_pikimat_sona(nimed))
        
