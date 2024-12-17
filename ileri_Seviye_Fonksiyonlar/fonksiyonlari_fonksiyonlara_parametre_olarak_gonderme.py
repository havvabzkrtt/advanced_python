def filter(fn, liste):
    result = []
    for item in liste:
        if fn(item):  # gönderilen fonksiyon : fn
            result.append(item)
    return result

def is_even(num):
    return num % 2 == 0

def is_positive(num):
    return num > 0


sayilar = [1,2,3,5,7,9,-5,10,34]

sonuc = filter(is_even, sayilar)
print(sonuc) # [2, 10, 34]

sonuc = filter(is_positive, sayilar)
print(sonuc)  # [1, 2, 3, 5, 7, 9, 10, 34]