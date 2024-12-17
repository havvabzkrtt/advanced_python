import json

# json listesi olması içim "köşeli parantez" kullanılmalı aşağıdaki gibi 
data = [
    {
        "id": 1,
        "title": "Macbook Pro",
        "price": 80000
    },
    {
        "id": 2,
        "title": "Macbook Air",
        "price": 70000
    }
]

with open("JSON/products_liste.json", "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=2)

print("dosya oluşturuldu")
print("-----------------")

import json

product = {
        "id": 3,
        "title": "Samsung S23",
        "price": 50000
    }


# LİSTEYE YENİ ÜRÜN EKLEME 
with open("JSON/products_liste.json") as file:
    products = json.load(file)  # dosyayı okuyoruz

products.append(product) # hazırlanmış olan product eklenir
print("yeri product eklendi")
# tekrar dosyayı kaydediyoruz
with open("JSON/products_liste.json", "w", encoding="utf-8") as file:
    json.dump(products, file, ensure_ascii=False, indent=2)

print("-----------------")

# LİSTE ÜZERİNDE GÜNCELLEME 

with open("JSON/products_liste.json") as file:
    products = json.load(file)  # dosyayı okuyoruz

for p in products:
    if p["title"] == "Samsung S23":
        p["title"] = "Samsung S24"
        print("title güncellendi")

# tekrar dosyayı kaydediyoruz
with open("JSON/products_liste.json", "w", encoding="utf-8") as file:
    json.dump(products, file, ensure_ascii=False, indent=2)

print("-----------------")

# LİSTE ÜZERİNDEN ELEMAN SİLME 

with open("JSON/products_liste.json") as file:
    products = json.load(file)  # dosyayı okuyoruz

products.remove(products[0])
print("product silindi")

# tekrar dosyayı kaydediyoruz
with open("JSON/products_liste.json", "w", encoding="utf-8") as file:
    json.dump(products, file, ensure_ascii=False, indent=2)
