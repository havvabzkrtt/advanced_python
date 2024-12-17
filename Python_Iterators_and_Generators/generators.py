def counter(max):
    sayi = 1
    sayilar = []

    while sayi <= max:
        sayilar.append(sayi)
        sayi += 1

    return sayilar

sonuc = counter(20)
print(sonuc)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

print("------------------")

# million tane veriyi bir listede tutup kullanıcıya sunmak bellekte gereksiz yer işgal eder.

def counter(max):
    sayi = 1
    while sayi <= max:
        yield sayi  # return yerine yield komutu kullanılır
        sayi += 1

generator = counter(20)

print(generator)  # <generator object counter at 0x000001792937C7C0>

# print(dir(generator))

# print(next(generator)) # 1
# print(next(generator)) # 2
# print(next(generator)) # 3

# # üstteki printlerden sonra kaldığı yerden devam eder for içinde yazmaya, 1 2 3 ü tekrardan yazmaz
# for i in generator:
#     print(i)

sonuc = list(generator)
# print(sonuc)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

liste = (i for i in range(1,20))  # comprension ile de kullanabiliriz ama [] yerine () kullanılır generator yaparken
print(liste)  # <generator object <genexpr> at 0x000001A77E00CB80>

print(next(liste)) # 1
print(next(liste)) # 2

print("--------------")

# Python'da Generator (Üreteç)
"""
Generator, Python'da iterator oluşturan özel bir türdür.
Bir generator, işlevsellik açısından bir iterator gibi davranır,
ancak bütün verileri bellekte tutmak yerine gerektiğinde üretir.
Bu, özellikle büyük veri setleriyle çalışırken bellek kullanımını optimize eder.
"""

# Generator'ın Temel Özellikleri
"""
- Bellek Verimliliği: Tüm veriler aynı anda bellekte tutulmaz, ihtiyaç duyuldukça üretilir.
- Lazy Evaluation (Tembel Değerlendirme): Değerler, yalnızca talep edildiğinde hesaplanır.
- Iterator ile Benzerlik: next() fonksiyonuyla sıradaki değeri verir, StopIteration hatasıyla sona erer.
- yield Anahtar Kelimesi: Generator'lar, return yerine yield anahtar kelimesini kullanır.
"""

def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator()
print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3
# print(next(gen))  # StopIteration