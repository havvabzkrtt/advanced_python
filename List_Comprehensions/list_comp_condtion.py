
# List Comprehensions’ta Koşullu Durumlar #
# for item in liste:
#     if (kosul):
#         expression

# [ expression for item in liste if koşul ]

sayilar = [3,5,7,6,56,34]
sonuc = []

for sayi in sayilar:
    if(sayi % 2 == 0):
        sonuc.append(sayi)

print(sonuc) # [6, 56, 34]

sonuc = [sayi for sayi in sayilar if sayi % 2 == 0]
print(sonuc)  # [6, 56, 34] 

sonuc = [sayi if sayi % 2 == 0 else "tek sayı" for sayi in sayilar]
print(sonuc)  # ['tek sayı', 'tek sayı', 'tek sayı', 6, 56, 34]

sonuc = ["çift sayi" if sayi % 2 == 0 else "tek sayı" for sayi in sayilar]
print(sonuc) # ['tek sayı', 'tek sayı', 'tek sayı', 'çift sayi', 'çift sayi', 'çift sayi']

urun_fiyatlari = [3000,0,1000,4000,0,5000]
vergiler = []

for fiyat in urun_fiyatlari:
    if(fiyat > 0):
        vergiler.append(fiyat * 1.20)

print(vergiler)  # [3600.0, 1200.0, 4800.0, 6000.0]

vergiler = [fiyat * 1.20 for fiyat in urun_fiyatlari if fiyat > 0]
print(vergiler)  # [3600.0, 1200.0, 4800.0, 6000.0]

vergiler = [fiyat if fiyat > 0 else "vergi hesaplanmadı" for fiyat in urun_fiyatlari]
print(vergiler)  # [3000, 'vergi hesaplanmadı', 1000, 4000, 'vergi hesaplanmadı', 5000]


# iki koşul uygulandı if ve else durumları için 
vergiler = [fiyat * 1.20 if fiyat > 0 else "vergi hesaplanmadı" for fiyat in urun_fiyatlari]
print(vergiler)  # [3600.0, 'vergi hesaplanmadı', 1200.0, 4800.0, 'vergi hesaplanmadı', 6000.0]