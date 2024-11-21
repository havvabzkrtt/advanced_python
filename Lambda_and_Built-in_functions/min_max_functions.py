sayilar = [1,4,6,32,23,12]
harfler = ['a','c','v','z']
isimler = ['ahmet','ali','sena','yiğit']

sonuc = min(sayilar)
print(sonuc) # 1
sonuc = max(sayilar)
print(sonuc) # 32

sonuc = min(harfler) # alfabetik sıraya göre
print(sonuc) # a 
sonuc = max(harfler)
print(sonuc) # z 

sonuc = min(isimler) # alfabetik sıraya göre sıralanarak
print(sonuc) # ahmet
sonuc = max(isimler) 
print(sonuc) # yiğit


sonuc = min([len(isim) for isim in isimler]) # isimlerin uzunluklarının min i
print(sonuc) # 3
sonuc = max(isimler, key = lambda isim: len(isim))
print(sonuc) # ali

sonuc = max([len(isim) for isim in isimler]) # isimlerin uzunluklarının max ı 
print(sonuc) # 5
sonuc = min(isimler, key = lambda isim: len(isim))
print(sonuc) # ahmet



urunler = [
    {"title":"samsung s23", "price": 70000},
    {"title":"samsung s24", "price": 80000},
    {"title":"samsung s25", "price": 90000}
]

sonuc = min(urunler, key = lambda urun: urun["price"]) # price değeri min olan
print(sonuc) # {'title': 'samsung s23', 'price': 70000}

sonuc = max(urunler, key = lambda urun: urun["price"]) # price değeri max olan
print(sonuc["title"]) # samsung s25

sonuc = max(urunler, key = lambda urun: urun["price"])["title"] # price değeri max olanın title ı 
print(sonuc) # samsung s25


# min-max fonksiyonu olmasaydı
max = 0
for urun in urunler:
    if(urun["price"] > max):
        max = urun["price"]

print(max)  # 90000
print(sonuc) # samsung s25