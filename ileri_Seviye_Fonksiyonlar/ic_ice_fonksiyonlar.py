# def selam(isim):
#     return f"selam, {isim}"

# print(selam("Çınar"))  # selam, Çınar
# print(selam)  # <function selam at 0x00000135E7F0A340>

# merhaba = selam

# print(selam)  # <function selam at 0x000001D3FC7DA340>
# print(merhaba)  # <function selam at 0x000001D3FC7DA340>

# print(selam("Çınar"))  # selam, Çınar
# print(merhaba("Çınar")) # selam, Çınar

# del selam   # selam değişkeninden adres bilgisini silmiş olduk, ancak o adreste fonksiyon hala duruyor (merhaba fonksiyonu)

# print(merhaba) # <function selam at 0x000001D3FC7DA340>
# print(merhaba("Çınar"))  # selam, Çınar
# # print(selam)  # NameError: name 'selam' is not defined
# # print(selam("Çınar"))  # NameError: name 'selam' is not defined

  

# def outer(number):
#     def inner(number):
#         print(number)

#     inner(number)  # outer içerisinde inner çağrılmalıdır

# outer(10) # 10



def faktoriyel(sayi):

    if not isinstance(sayi, int):
        raise TypeError("number must be an int")
    
    if not sayi >= 0:
        raise ValueError("number must be zero or positive")

    def inner_faktoriyel(sayi):
        if sayi <= 1:
            return 1
        
        return sayi * inner_faktoriyel(sayi - 1)
    
    return inner_faktoriyel(sayi)  # faktoriyel fonksiyonu içerisinde inner_faktoriyel fonksiyonu çağrılmalıdır

sonuc = faktoriyel(5)
print(sonuc) # 120

sonuc = faktoriyel(7)
print(sonuc) # 5040

try:
    sonuc = faktoriyel("4") 
    print(sonuc)  # number must be an int
except Exception as ex:
    print(ex)