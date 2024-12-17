import json

# uygulama tarafında bir veriyi dosyaya kaydetmeden önce serialize etmek gerekir

product = {
    "id":2,
    "title":"Macbook Pro",
    "price": 90000,
    "rating": "4.5",
    "category": "Bilgisayar",
    "colors": ["Red","Blue"]
}

print(product)
print(product["title"])
print(type(product))  # <class 'dict'>

print("------------")
sonuc = json.dumps(product) # serialize işlemi yapılır 
# dumps: uygulama tarafında json stringine çevirmek istedeğimiz zaman kullanılır
# dosya ile iligli işlemlerde s takısı kullanılmaz (load,dump)

print(sonuc)
print(type(sonuc))  # <class 'str'>  
# print(sonuc["title"]) # hata verir, çünkü dict değil string

with open("JSON/products.json", "w", encoding="utf-8") as file:
    json.dump(product, file, ensure_ascii=False, indent=2)  # dosyaya kaydederiz
# indent=2 : düzenlenmiş halde kaydeder
# encoding="utf-8" : türkçe karakterleri de düzenli halde kaydeder

# serialize => encode, uygulama tarafında kullanılan bir objeyi bir dosyaya kaydetmek istediğimizde, json dosyası halinde stringe çevirme işlemidir. Json'a kaydetme işlemi
# deserialize => decode, uygulama tarafında kullanılabilir hale getirmek. Json'dan okuma işlemi
