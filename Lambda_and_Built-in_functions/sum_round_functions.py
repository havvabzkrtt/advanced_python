sayilar = [1,3,5,4,32,56]

sonuc = sum(sayilar)
print(sonuc) # 101
sonuc = sum(sayilar, 15)  # 101 + 15
print(sonuc) # 116


products = [
    {"title":"iphone 15", "price": 60000},
    {"title":"iphone 16", "price": 70000},
    {"title":"iphone 17", "price": 80000},
    {"title":"iphone 17", "price": 0},
]

toplamFiyat = sum([urun["price"] for urun in products]) # price değerleri toplanır
print(toplamFiyat) # 210000
urunAdeti = len([urun for urun in products if urun["price"] > 0]) # price değeri 0'dan büyük olanlar
print(urunAdeti) # 3
sonuc = toplamFiyat / urunAdeti # 210000/3
print(sonuc) # 70000.0

sonuc = round(5.3)
print(sonuc) # 5
sonuc = round(5.6)
print(sonuc) # 6
sonuc = round(5.5)
print(sonuc) # 6
sonuc = round(1.325233, 2)  # 2 basamak yuvarlanır
print(sonuc) # 1.33
sonuc = round(1.325253, 4)  # 4 basamak yuvarlanır
print(sonuc) # 1.3253