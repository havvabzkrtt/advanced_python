# Uygulama tarafında veriler bir class ile taşınıyorsa, bu bilgileri nasıl bir json dosyasında serialize ediliceği öğrenilir

class Product:
    def __init__(self, id, title, price):
        self.id = id
        self.title = title
        self.price = price

import json

# serialize: uygulama tarafından json dosyasına aktarılır

p1 = Product(1, "Samsung S26", 70000)  # Product classında nesen oluşturduk # şuan json dosyasına yazdırılamaz
p2 = Product(2, "Samsung S27", 80000)


with open("JSON/products_class.json", "w") as file:
    # json.dump(p1, file) # böyle hata verir
    json.dump(p1.__dict__, file) # bu şekilde dict e dönüitürülerek yazdırılır

# # products = [p1.__dict__, p2.__dict__]

# with open("JSON/products_class.json", "w") as file:
#     json.dump(products, file)

products = {
    p1.id : p1.__dict__,
    p2.id : p2.__dict__
}


with open("JSON/products_class.json", "w") as file:
    json.dump(products, file)


# deserialize : json dosyasından uygulama tarafında veri aktarma 

with open("JSON/products_class.json") as file:
    products = json.load(file)

print(type(products)) # <class 'dict'>

urunler = []
for key, value in products.items(): 
    urunler.append(Product(key, value["title"], value["price"])) # her gelen product bilgisi urunler listesine eklenir

print(type(urunler)) # <class 'list'>

for p in urunler:
    print(p.title)