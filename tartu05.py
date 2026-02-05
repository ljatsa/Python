#tartu05
failinimi = input("Sisestage failinimi: ")
fail = open(failinimi, encoding="UTF-8")

for rida in fail:   
    print(rida, end= "")
    fail.close()
