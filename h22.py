import datetime


kp = datetime.datetime.now()
print(kp)

print(kp.strftime("%d.%m.%Y, %H:%M:%S"))

sp = datetime.datetime(2009,8,5)

vanus_paevades = kp - sp
print(f"Vanus Päevades: {vanus_paevades.days}")

vanus_aastates = vanus_paevades.days // 365
print(f"Vanus Aastates: {vanus_aastates}")

if vanus_aastates%5==0:
    print("Sul on juubel")
else:
    print("Sul pole juubel")


import csv

faili_nimi = "rentals.csv"

# Muutujad analüüsi jaoks
autode_arv = 0
kliendid = []
cross_office_rentals = 0
koik_rendid = 0
total_duration = 0

# CSV faili lugemine
with open(faili_nimi, mode='r', encoding='utf-8') as fail:
    csv_lugeja = csv.reader(fail)
    
    # Eeldame, et esimene rida sisaldab päiseid
    header = next(csv_lugeja)

    for rida in csv_lugeja:
        customer_id = rida[0]  
        pickup_office = rida[1]  
        return_office = rida[2]  
        pickup_date = rida[3]  
        return_date = rida[4]  
        age = int(rida[5])  

        total_rentals += 1

        if customer_id not in kliendid:
            kliendid.append(customer_id)

        pickup_date_obj = datetime.datetime.strptime(pickup_date, "%Y-%m-%d")
        return_date_obj = datetime.datetime.strptime(return_date, "%Y-%m-%d")
        
        rental_duration = (return_date_obj - pickup_date_obj).days
        total_duration += rental_duration

        if pickup_office != return_office:
            cross_office_rentals += 1

        if rida[6]:  
            autode_arv += 1

print(f"Rendite arv: {koik_rendid}")
print(f"Unikaalsed kliendid: {len(kliendid)}")
print(f"Risti-kontori rentimise osakaal: {cross_office_rentals / koik_rendid * 100:.2f}%")
print(f"Keskmine rentimise kestus: {total_duration / koik_rendid:.2f} päeva")
print(f"Autode arv: {autode_arv}")
