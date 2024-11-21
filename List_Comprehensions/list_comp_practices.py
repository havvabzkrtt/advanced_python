# 1- (1-100) arasındaki sayılardan 12' e tam bölünebilen sayı listesini oluşturunuz.

oniki_tam_bolunen = [sayi for sayi in range(1,101) if sayi % 12 == 0]
print(oniki_tam_bolunen) # [12, 24, 36, 48, 60, 72, 84, 96]

oniki_tam_bolunen = [sayi for sayi in range(1,101) if sayi % 3 == 0 and sayi % 4 == 0]
print(oniki_tam_bolunen) # [12, 24, 36, 48, 60, 72, 84, 96]

oniki_tam_bolunen = [sayi for sayi in range(1,101) if sayi % 3 == 0 if sayi % 4 == 0]
print(oniki_tam_bolunen) # [12, 24, 36, 48, 60, 72, 84, 96]


# 2- Verilen text içerisindeki rakamları içeren bir liste oluşturunuz.
# text = "Hello 12345 World" => [1,2,3,4,5]

text = "Hello 12345 World"

rakamlar = [i for i in text if i.isdigit()]
print(rakamlar) # ['1', '2', '3', '4', '5']
rakamlar = [karakter for karakter in text if karakter in '123456789']
print(rakamlar) # ['1', '2', '3', '4', '5']


# 3- Sicakliklar listesinde bulunan her hava sıcaklık bilgisine göre 4 derecenin altında "buzlanma tehlikesi" yazınız.
# sicakliklar = [20,15,0,-5,-2] => [20,15,"Buzlanma Tehlikesi","Buzlanma Tehlikesi","Buzlanma Tehlikesi"]

sicakliklar = [20,15,0,-5,-2]

sicakliklar = [i if i >= 4 else "Buzlanma Tehlikesi" for i in sicakliklar]
print(sicakliklar)  # [20, 15, 'Buzlanma Tehlikesi', 'Buzlanma Tehlikesi', 'Buzlanma Tehlikesi']


# 4- ogrenciler ve notlar listelerindeki notu 50 den fazla olan kişileri ekrana dict verisinde yazdırınız.

# ogrenciler = ["ali", "ahmet", "canan"]
# notlar = [50, 60, 80]
# [("ali", 50), ("ahmet", 60), ("canan", 80)]

ogrenciler = ["ali", "ahmet", "canan"]
notlar = [50, 60, 80]


ogrenci_list = [(ogrenciler [i], notlar[i]) for i in range(0, len(ogrenciler))]

print(ogrenci_list) # [("ali", 50), ("ahmet", 60), ("canan", 80)]

ogrenci_list_dict = {key:value for (key,value) in ogrenci_list}
print(ogrenci_list_dict) # {'ali': 50, 'ahmet': 60, 'canan': 80}

ogrenci_list_dict = {key:value for (key,value) in ogrenci_list if value > 50}
print(ogrenci_list_dict) # {'ahmet': 60, 'canan': 80}

# 5- For döngüsüyle yazılan uygulamayı list comprehension ile yazınız.
 
liste = [] 
# 0 - 0
# 0 - 1
# 0 - 2
# 1 - 0
# 1 - 1
# 1 - 2

for x in range(3):
    for y in range(3):
            liste.append((x,y))

print(liste) # [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

liste = [(x, y) for x in range(3) for y in range(3)]
print(liste) # [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]


liste = []
for x in range(3):
    for y in range(3):
        for z in range(3):
            liste.append((x,y,z))

print(liste) # [(0, 0, 0), (0, 0, 1), (0, 0, 2), (0, 1, 0), (0, 1, 1), (0, 1, 2), (0, 2, 0), (0, 2, 1), (0, 2, 2), (1, 0, 0), (1, 0, 1), (1, 0, 2), (1, 1, 0), (1, 1, 1), (1, 1, 2), (1, 2, 0), (1, 2, 1), (1, 2, 2), (2, 0, 0), (2, 0, 1), (2, 0, 2), (2, 1, 0), (2, 1, 1), (2, 1, 2), (2, 2, 0), (2, 2, 1), (2, 2, 2)]

liste = [(x, y, z) for x in range(3) for y in range(3) for z in range(3)]
print(liste) # [(0, 0, 0), (0, 0, 1), (0, 0, 2), (0, 1, 0), (0, 1, 1), (0, 1, 2), (0, 2, 0), (0, 2, 1), (0, 2, 2), (1, 0, 0), (1, 0, 1), (1, 0, 2), (1, 1, 0), (1, 1, 1), (1, 1, 2), (1, 2, 0), (1, 2, 1), (1, 2, 2), (2, 0, 0), (2, 0, 1), (2, 0, 2), (2, 1, 0), (2, 1, 1), (2, 1, 2), (2, 2, 0), (2, 2, 1), (2, 2, 2)]