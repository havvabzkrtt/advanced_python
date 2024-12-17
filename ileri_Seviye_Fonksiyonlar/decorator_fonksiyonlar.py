
# Bir fonksiyon çağırıcaz ve bir işlevi yerine getiricez.
# Ama buun öncesi veya sonrasında çalıştırmak istediğimiz,
# otomatiğe bağlamak istediğimiz belli kodlarımız olabilir. 
# decorator fonksiyonlar bu aşamada işimize yarar.

# def gunaydin():
#     print("hoş geldiniz")
#     print("günaydın benim adım Çınar")
#     print("görüşmek üzere")

# def iyigunler():
#     print("hoş geldiniz")
#     print("iyi benim adım Çınar")
#     print("görüşmek üzere")

# # gunaydin ve iyigunler fonksiyonlarında tek fark iki kelimelik. Uzun uzun fonksiyonlar yazmak yerine bunları aşağıdaki gibi oluşturabiliriz.


# # decorator fonksiyonu
# def selamlama(fn):
#     def inner(ad):
#         print("hoş geldiniz")
#         fn(ad)  # istenilen fonksiyon gelecek
#         print("görüşmek üzere")
#     return inner

# @selamlama  # decorator olarak ekledik
# def gunaydin(ad):
#     print(f"günaydın benim adım {ad}")

# @selamlama  # decorator olarak ekledik
# def iyigunler(ad):
#     print(f"iyi günler benim adım {ad}")

# # g = selamlama(gunaydin)
# # g()
# gunaydin("Ali")    # yukarıdaki iki satırı yazmak yerine, decorator sayesinde bu satır yeterli  

# # i = selamlama(iyigunler)
# # i()
# iyigunler("Sadık") # yukarıdaki iki satırı yazmak yerine, decorator sayesinde bu satır yeterli  


print("--------------------")


import time
def zaman_olc(func, islem):
    start_time = time.time()
    def inner(islem):
        if islem == "toplama":
            func(35,56)
        if islem == "carpma":
            func(35,56)
    
    inner(islem)
    end_time = time.time()
    gecen_zaman = end_time - start_time     
    print(f"{islem} işlemi için geçen süre: {gecen_zaman}")


def func_topla(*args):
    toplam = 0
    for i in args:
        toplam += i
    print("Toplam sonucu: ", toplam)

# sonuc = zaman_olc(func_topla, "toplama")
# print(sonuc)  
# Toplam sonucu:  91
# toplama işlemi için geçen süre: 0.0

def func_carp(*args):
    carpim = 1
    for i in args:
        carpim *= i
        print(i)
    
    print("Çarpım sonucu: ", carpim)

sonuc = zaman_olc(func_carp, "carpma")
print(sonuc) 
# Çarpım sonucu:  1960
# carpma işlemi için geçen süre: 0.0009741783142089844


print("--------------------")

import time
def zaman_olc(func):
    def inner(a,b):
        start_time = time.time()
        func(a,b)
        end_time = time.time()
        gecen_zaman = end_time - start_time     
        print(f"işlem için geçen süre: {gecen_zaman}")
    return inner
    

@zaman_olc
def func_topla(*args):
    toplam = 0
    for i in args:
        toplam += i
    print("Toplam sonucu: ", toplam)

sonuc = zaman_olc(func_topla)
print(sonuc)   # <function zaman_olc.<locals>.inner at 0x000001E2C0E4D120>

sonuc = func_topla(34,64)
print(sonuc)
# Toplam sonucu:  98
# işlem için geçen süre: 0.0009963512420654297

@zaman_olc
def func_carp(*args):
    carpim = 1
    for i in args:
        carpim *= i
        print(i)
    
    print("Çarpım sonucu: ", carpim)

sonuc = func_carp(34,64)
print(sonuc)
# Çarpım sonucu:  2176
# işlem için geçen süre: 0.0010106563568115234