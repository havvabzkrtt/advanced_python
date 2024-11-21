# any: herhangi bir , all: hepsi    anlamı taşır

# all: aslında and operatörünü çağrıştırır, sadece hepsi "True" ise "True" döndürür
sonuc = all([True,True,False])  
print(sonuc) # False
sonuc = all([True,True,True])
print(sonuc) # True
sonuc = all([False,False,False])
print(sonuc) # False
sonuc = all([False,False,True])
print(sonuc) # False


# any: aslında or operatörünü çağrıştırır, herhangi biri "Trıe" ise "True" döndürür
sonuc = any([True,True,True])
print(sonuc) # True
sonuc = any([True,True,False])
print(sonuc) # True
sonuc = any([False,False,True])
print(sonuc) # True
sonuc = any([False,False,False])
print(sonuc) # False

# And => True and True => all()
# Or  => True or False => any()

print("------------")

sayilar = [1,3,5,7,6,52,0]

sonuc = [sayi for sayi in sayilar]
print(sonuc) # [1, 3, 5, 7, 6, 52, 0]
print(bool(1)) # True 
print(bool(52)) # True 
print(bool(0)) # False # sayı 0 ise False döndürülür
"""
0: Python'da 0 (sıfır), "False" olarak değerlendirilir çünkü bu, programlama bağlamında "hiçlik" veya "boş" anlamına gelir.
0 olmayan sayılar: Pozitif ya da negatif fark etmeksizin, sıfır olmayan tüm sayılar "True" olarak değerlendirilir.
"""

sonuc = all([bool(sayi) for sayi in sayilar])
print(sonuc) # False  / hepsi True değildi, bir tane False(0) değeri vardı
sonuc = any([bool(sayi) for sayi in sayilar])
print(sonuc) # True   / en az bir tane True değeri vardo
sonuc = all([sayi % 2 == 0 for sayi in sayilar])
print(sonuc) # False
sonuc = any([sayi % 2 == 0 for sayi in sayilar])
print(sonuc) # True



users = ["ahmet","çınar","hasan"]

sonuc = all([user[0] == "a" for user in users])
print(sonuc) # False
sonuc = any([user[0] == "a" for user in users])
print(sonuc) # True    