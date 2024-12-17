import json

with open("JSON/product.json") as file:
    data = json.load(file) 
    # load: json dosyasından okuma yapılır 
 
print(data)
print("----------")
print(type(data))
print("----------")
print(data["title"])
print(data["price"])
print(data["colors"])

print("--------------------------")



# json string : uygulama tarafında decode edilecek olan veri 
data = """
    {
        "id":1,
        "title":"Macbook Pro",
        "price": 90000,
        "rating": "4.5",
        "category": "Bilgisayar",
        "colors": ["Red","Blue"]
    }
"""

data = json.loads(data)  # bu kısım yapılmazsa hata alınır
# loads : uygulama tarafndaki json string deserialize ederiz, json stringten okuma yapılır


print(data)
print("----------")
print(type(data))
print("----------")
print(data["title"])
print(data["price"])
print(data["colors"])

# serialize => encode, uygulama tarafında kullanılan bir objeyi bir dosyaya kaydetmek istediğimizde, json dosyası halinde stringe çevirme işlemidir. Json'a kaydetme işlemi
# deserialize => decode, uygulama tarafında kullanılabilir hale getirmek. Json'dan okuma işlemi
