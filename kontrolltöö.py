# 2. Carts
#  • Kuva ühe ostukorvi toodete nimed ja kogused (products) 
#  • Arvuta ostukorvide keskmine summa
#  • Leia ostukorvide kogusumma (total) 
#  • Leia ostukorv, kus on kõige rohkem tooteid (totalProducts) 
import json
import requests

def cart_summa(cart):
    return cart["price"] * cart["stock"]

def keskmine_kart_summa(products):
    total_sum = 0
    for product in products:
        total_sum += cart_summa(product)
    return total_sum / len(products)

url = f"https://dummyjson.com/products"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()  
    products = data["products"]
    print("Ühe ostukorvi tooted ja kogused:")
    for product in products:
        print(f'{product["title"]}: {product["stock"]} tk, hind: {product["price"]} €')

    avg_total = keskmine_kart_summa(products)  
    print(f"\nOstukorvide keskmine summa on: {avg_total:.2f} €")
    total_sum = 0
    for product in products:
        total_sum += cart_summa(product)
    print(f"\nOstukorvide kogusumma on: {total_sum:.2f} €")
    max_quantity_product = max(products, key=lambda x: x["stock"])
    print(f"\nOstukorv, kus on kõige rohkem tooteid: {max_quantity_product['title']} ({max_quantity_product['stock']} tk)")
else:
    print("Päring ebaõnnestus. Status:", response.status_code)