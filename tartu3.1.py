fail = open("rebased.txt", encoding="UTF-8")
vastuvõetud = []

for rida in fail:
    vastuvõetud.append(int(rida))
    aasta = int(input("sisesta aasta 2011-2019: "))
fail.close()
print(vastuvõetud[aasta-2011])