import json
import requests
url = f"https://metshein.com/kordamine/json/tooted.json"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()["tooted"]
    print(response)
# •	Leia, mitu erinevat tootekategooriat on failis esindatud.
kategooriad = set()
for toode in data:
    kategooriad.add(toode["kategooria"])
print("Kategooriaid kokku:", len(kategooriad))
# •	Leia kõige odavam ja kõige kallim toode ning nende hinnad.
odavaim = min(data, key=lambda x: x["hind"])
kalleim = max(data, key=lambda x: x["hind"])
print("\nOdavaim toode:", odavaim["nimi"], "-", odavaim["hind"], "€")
print("Kalleim toode:", kalleim["nimi"], "-", kalleim["hind"], "€")
# •	Leia, mitu toodet kuulub kategooriasse "Toidukaubad".
toidukaubad = 0
for toode in data:
    if toode["kategooria"] == "Toidukaubad":
        toidukaubad += 1
print("\nToidukaupade arv:", toidukaubad)
# •	Arvuta kõikide toodete koguväärtus laoseisu järgi.
koguvaartus = 0
for toode in data:
    koguvaartus += toode["hind"] * toode["laoseis"]
print("\nKoguväärtus laos:", koguvaartus, "€")
print("\nMadala laoseisuga tooted (<10):")
# •	Leia kõik tooted, mille laoseis on alla 10 ühiku.
for toode in data:
    if toode["laoseis"] < 10:
        print("-", toode["nimi"], "(laoseis:", toode["laoseis"], ")")
else:
    print("Viga")