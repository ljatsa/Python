# Ülesanne 10.2
# 13.01.2026
import random

def mängi_üht_mängu():
    
    arv = random.randint(1, 10)
    katse_arv = 0
    õigesti_arvatud = False

    print("Tere! Proovi ära arvata arv vahemikus 1 ja 10.")

    for _ in range(10): 
        kasutaja_arv = int(input("Sisesta oma arv: "))
        katse_arv += 1


        if kasutaja_arv < arv:
            print("Pakutud arv on liiga väike. Proovi uuesti!")
        elif kasutaja_arv > arv:
            print("Pakutud arv on liiga suur. Proovi uuesti!")
        elif kasutaja_arv == arv:
            print(f"Õige! Arvasite arvu ära {katse_arv}. katsega.")
            break
    
    else:
        print("Kahjuks ei suutnud sa õiget arvu ära arvata. Proovi uuesti!")

    return katse_arv

def mängu_algus():
    kõik_katsed = []  

    for i in range(10):  
        katse_arv = mängi_üht_mängu()
        kõik_katsed.append(katse_arv)

        uuesti = input("Kas soovid uuesti mängida? (jah/ei): ").strip().lower()
        if uuesti != "jah":
            print("\nMängu tulemused:")
            for j, katse in enumerate(kõik_katsed, 1):
                print(f"Mäng {j}: Arvasite ära {katse}. katsega.")
            print("Aitäh mängimast!")
            break

    print()  
mängu_algus()