# map function
# listeye bir kriter ugulanacak(örneğin her eleman 2 ile bölünecek) ve geriye bir liste döndürülecek,
# ama başlangıçtaki eleman sayısıyla eşit elemana sahip liste döndürülmüş olacak. 


sayilar = [1,2,3,4,5]


kareleri = []
for sayi in sayilar:
    kareleri.append(sayi ** 2)
print(kareleri) # [1, 4, 9, 16, 25]

def kareAl(sayi):
    return sayi ** 2

sonuc = map(kareAl, sayilar) # birinci parametre olarak fonksiyon referans olarak verilir, iterable bir liste ikinci parametre olarak verilir 
print(sonuc) # <map object at 0x000001FAE20FDDE0> / bellek üzerinde bir objenin adresi döndürülür 

sonuc = list(map(kareAl, sayilar)) # listeye çevirerek adresteki sonucu görebiliriz
print(sonuc) # [1, 4, 9, 16, 25]


sonuc = list(map(lambda sayi: sayi ** 2, sayilar))
print(sonuc) # [1, 4, 9, 16, 25]

kareal = lambda sayi: sayi ** 2
sonuc = list(map(kareal, sayilar))
print(sonuc) # [1, 4, 9, 16, 25]


# int("2") # 2  # int -> hazrı fonksiyon
sayilar_str = ["1","2","3","4","5"]
sonuc = list(map(int, sayilar_str))
print(sonuc)  # [1, 2, 3, 4, 5

isimler = ["ali","hasan","ayşe","zeynep"]
sonuc = list(map(str.capitalize, isimler))
print(sonuc) # ['ali', 'ahmet']

kullanicilar = [
    {"ad":"ali", "soyad":"yılmaz"},
    {"ad":"ahmet", "soyad":"cengiz"}
]
sonuc = list(map(lambda kisi: kisi["ad"], kullanicilar))
print(sonuc) # ['ali', 'ahmet']

kisi_al = lambda kisi: kisi["ad"]
sonuc = list(map(kisi_al, kullanicilar))
print(sonuc) # ['ali', 'ahmet']


