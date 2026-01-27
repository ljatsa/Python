#ülesanne 11
#Lisett-Rosette Jätsa

def pikim_sona(list):
    pikimArv = 0
    pikimNimi = ""
    for i in list:
        if len(i) > pikimArv:
            pikimArv = len(i)
            pikimNimi = i
    return pikimNimi


def kolm_pikimat_sona(list):
    Kui nimekirjas on rohkem kui 2:
        sorteerin nimekirja pikkuse järgi ja reverse
        tagastan list [0:3]

nimed = ["Joosep", "Joonas", "Mario", "Kivakesekesekene"]
print(pikim_sona(nimed))
print(kolm_pikimat_sona(nimed))
        
