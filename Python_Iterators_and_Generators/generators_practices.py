# (1 - ∞) aralığındaki her sayının karesini getiren fonksiyon.

# sonsuz aralıkta sayı üretimi yapılamaz fakat generator ile bu gerçekleştirilebilir

# def sayi_uret():
#     sayi = 0
#     while True:
#         yield sayi ** 2
#         sayi += 1

# generator = sayi_uret()

# print(next(generator))
# print(next(generator))
# print(next(generator))

# for i in generator:
#     print(i)
#     # sonsuza kadar gider, belleğin kapasitesine göre çünkü her sayı bellek üzerinde yer kaplar 

print("-------------------------")

# Fibonacci serisini hem normal fonksiyon hem de generator fonksiyon ile oluşturun.

def fib_list(max):
    sayilar = []

    a, b = 0, 1

    while len(sayilar) <= max:
        sayilar.append(b)
        a, b = b, a + b

    return sayilar

# print(fib_list(9000))  # her sayı bellek üzerinde yer kaplar 

# generator mantığı ile 
def fib_gen(max):
    a, b = 0, 1
    count = 0
    while count <= max:
        a, b = b, a + b
        yield b
        count += 1

# for i in fib_gen(9000):
#     print(i)


# Performans testlerini yapın.

import sys  

liste = [i for i in range(10000)]  # normal olanın
print(sys.getsizeof(liste))  # 85176

gen = (i for i in range(10000))  # generator ile olanın
print(sys.getsizeof(gen))  # 192


import time

# normal olan için 
list_start_time = time.time()
sum([i for i in range(9000000)])
list_stop = time.time() - list_start_time

print(list_stop)  # 0.9170615673065186

# generator olan için
gen_start_time = time.time()
sum((i for i in range(9000000)))
gen_stop = time.time() - gen_start_time

print(gen_stop)   # 0.7299213409423828