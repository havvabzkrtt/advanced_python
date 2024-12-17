# def dec_selamlama(count):
#     def selamlama(fn):
#         def inner(ad):
#             for _ in range(count):
#                 fn(ad)
#         return inner
#     return selamlama

# @dec_selamlama(count=2) # decorator içinde 2 kere çalıştırılıyor 
# def gunaydin(ad):
#     print(f"günaydın benim adım {ad}")

# @dec_selamlama(count=3) # decorator içinde 3 kere çalıştırılıyor 
# def iyigunler(ad):
#     print(f"iyi günler benim adım {ad}")
    
# gunaydin("Ali")
# # günaydın benim adım Ali 
# # günaydın benim adım Ali 

# iyigunler("Sadık")
# # iyi günler benim adım Sadık
# # iyi günler benim adım Sadık
# # iyi günler benim adım Sadık

print("---------------")

import time

def dec_speed_test(count):
    def speed_test(fn):
        def inner(*args, **kwargs):
            start_time = time.perf_counter()
            print(f"{fn.__name__} metodu çalışıyor.")
            for _ in range(count):
                result = fn(*args, **kwargs)
                end_time = time.perf_counter()
                run_time = end_time - start_time
                print(f"geçen süre: {run_time}")
            return result
        return inner
    return speed_test

@dec_speed_test(count=2)
def sum_gen():    
    return sum((x for x in range(10000000)))

@dec_speed_test(count=3)
def sum_list():
    return sum([x for x in range(10000000)])


print(sum_gen())
"""
sum_gen metodu çalışıyor.
geçen süre: 0.75608739999916
geçen süre: 1.5187543999991249  # her çalışmada farklı süre üretir, bellek durumuna göre
49999995000000
"""
print(sum_list())
"""
sum_list metodu çalışıyor.
geçen süre: 0.8595932999996876
geçen süre: 1.7211521999997785
geçen süre: 2.556753800000479
49999995000000
"""