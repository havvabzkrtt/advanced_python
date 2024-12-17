import json

# json dict
data =   {
    "2": {
      "title": "Macbook Air",
      "price": 70000
    },
    "3": {
      "title": "Samsung S24",
      "price": 70000
    }
}

with open("JSON/products_dict.json", "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=2)

print("-----------------")

import json

with open("JSON/products_dict.json") as file:
    products = json.load(file)

print(products["2"])
print(products["3"])

print("-----------------")

# DICT ÜZERİNE EKLEME / SONA EKLENİR

products.update({
    "1": {
      "title": "Macbook Pro",
      "price": 80000
    }
})

# DICT ÜZERİNDE GÜNCELLEME 
products.update({
    "3": {
      "title": "Samsung S25",
      "price": 90000
    }
})


print("-----------------")

# DICT İÇERİSİNDEN SİLME 
products.pop("1")

with open("JSON/products_dict.json", "w", encoding="utf-8") as file:
    json.dump(products, file, ensure_ascii=False, indent=2)