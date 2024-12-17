def usAlma(taban):
    def inner(us):
        return taban ** us
    
    return inner

# sonuc = usAlma(2)(3)   # içteki ve dıştaki fonksiyonlar için 2 tane parametre verilir
# print(sonuc)  # 8 

# fn = usAlma(2) 
# sonuc = fn(4)
# print(sonuc)  # 16

print("------------------------")

# def yetki_sorgulama(sayfa):
#     def inner(role):
#         if role == "Admin":
#             return f"{role} rolü {sayfa} sayfasına ulaşabilir."
#         else:
#             return f"{role} rolü {sayfa} sayfasına ulaşamaz."
        
#     return inner

# yetki = yetki_sorgulama("Ürün güncelleme")
# sonuc = yetki("User")
# print(sonuc)  # User rolü Ürün güncelleme sayfasına ulaşamaz.

# sonuc = yetki_sorgulama("Ürün güncelleme")("Admin")
# print(sonuc)  # Admin rolü Ürün güncelleme sayfasına ulaşabilir.

print("------------------------")

def islem(islem_adi):
    def toplam(*args):
        toplam = 0
        for i in args:
            toplam += i  # bütün girdi parametrelerini toplama işlemine sokar
        return toplam

    def carpim(*args):
        carpim = 1
        for i in args:
            carpim *= i  # bütün girdi parametrelerini çarma işlemine sokar
        return carpim
    
    if islem_adi == "toplama":
        return toplam
    else:
        return carpim

toplama = islem("toplama")
sonuc = toplama(10,20)
print(sonuc) # 30

carpma = islem("carpma")
sonuc = carpma(10,20)
print(sonuc) # 200
        
sonuc = islem("toplama")(3,5,2,6)
print(sonuc) # 16

sonuc = islem("carpma")(3,5,2,6)
print(sonuc) # 180


