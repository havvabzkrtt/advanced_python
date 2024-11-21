# lambda arguments: expression

# lambda fonksiyonu, Python'da anonim (isimsiz) fonksiyonlar oluşturmanıza olanak sağlayan bir yapıdır. 
# Genellikle kısa ve tek satırlık fonksiyonlar yazarken kullanılır. 
# lambda fonksiyonları, genellikle tek bir ifade içeren ve hemen kullanılacak küçük fonksiyonlar için idealdir.

def kareAl(a):  # fonksiyona isim verilir
    return a ** 2

sonuc = kareAl(5)
print(sonuc) # 25

sonuc = (lambda a: a ** 2)(3)  # lambda ile isim verilmez, expression oluşturulur( : sonrası return işlemi) / (3) -> fonksiyona verilen argumandır
#         --fonction--      -arguman-
print(sonuc) # 9


kareAl = lambda a: a ** 2  # fonksion gibi tanımlandı 
sonuc = kareAl(4)
print(sonuc) # 16



toplama = lambda a,b,c: a + b + c
sonuc = toplama(1,2,3)
print(sonuc) # 6


def myFunc(n):
    return lambda a: a * n  # lambdaya gönderilen a ile fonksiyona gönderilen n değeri çarpılır

carpma2 = myFunc(2) # lambda a: a *2
sonuc = carpma2(3)  # 3*2 
print(sonuc) # 6

carpma3 = myFunc(3)
sonuc = carpma3(3)
print(sonuc) # 9

carpma5 = myFunc(5)
sonuc = carpma5(5)
print(sonuc) # 25 
