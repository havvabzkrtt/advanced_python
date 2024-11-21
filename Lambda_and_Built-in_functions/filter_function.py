sayilar = [1,3,5,-4,-3]

def negatifSayilar(x):
    if x < 0:
        return True
    else:
        return False
    
sonuc = list(filter(negatifSayilar,sayilar))
print(sonuc) # [-4, -3]


sonuc = list(filter(lambda x: x < 0, sayilar))  # sayısal değer çıkartır
print(sonuc) # [-4, -3]

sonuc = list(map(lambda x: x < 0, sayilar)) # boolien değer çıkartır
print(sonuc) # [False, False, False, True, True]

sonuc = list(filter(lambda x: x % 2 == 1, sayilar))
print(sonuc) # [1, 3, 5, -3]

a = -3 % 2
print(a)  # 1 



isimler = ["çınar","ali","ada","yiğit","sena"]
filteredResult = list(filter(lambda x: x[0] == 'a', isimler))
sonuc = list(map(lambda x: x.upper(), filteredResult))
print(sonuc)  # ['ALI', 'ADA']


users = [
    {"username":"sadikturan", "posts": ["post 1","post 2"]},
    {"username":"senaturan", "posts": []},
    {"username":"yigitbilgi", "posts": ["post 1","post 2","post 3"]},
]

filteredUsers = list(filter(lambda u: len(u["posts"])>0, users))
sonuc = list(map(lambda u: u["username"], filteredUsers))
print(sonuc) # ['sadikturan', 'yigitbilgi'] 

# list comprehensions ile 
sonuc = [user["username"].upper() for user in users if len(user["posts"]) > 0]
print(sonuc) # ['SADIKTURAN', 'YIGITBILGI']