
# sorted fonksiyonu bir sıralama fonksiyonudur
sayilar = [1,53,4,5,65,23]

sayilar.sort()
print(sayilar)  # [1, 4, 5, 23, 53, 65]


sonuc = sorted(sayilar) # default olarak artana göre sıralar
print(sonuc) # [1, 4, 5, 23, 53, 65]
sonuc = sorted(sayilar, reverse=True) # azalana göre sıralar
print(sonuc) # [65, 53, 23, 5, 4, 1]  


users = [
    {"username":"sadikturan", "posts": ["post 1", "post 2"],"email":"info@abc.com","phone":"1234"},
    {"username":"ahmetyilmaz", "posts": ["post 1"],"email":"info@abcd.com"},
    {"username":"cananyilmaz", "posts": ["post 1", "post 2", "post 3"]}
]

sonuc = sorted(users, key=len)  # key bilgilerinin sayısına göre bir sıralama yapılır
print(sonuc) # [{'username': 'cananyilmaz', 'posts': ['post 1', 'post 2', 'post 3']}, {'username': 'ahmetyilmaz', 'posts': ['post 1'], 'email': 'info@abcd.com'}, {'username': 'sadikturan', 'posts': ['post 1', 'post 2'], 'email': 'info@abc.com', 'phone': '1234'}]
sonuc = sorted(users, key=len, reverse=True)  # azalana göre yapıldı
print(sonuc) # [{'username': 'sadikturan', 'posts': ['post 1', 'post 2'], 'email': 'info@abc.com', 'phone': '1234'}, {'username': 'ahmetyilmaz', 'posts': ['post 1'], 'email': 'info@abcd.com'}, {'username': 'cananyilmaz', 'posts': ['post 1', 'post 2', 'post 3']}]

sonuc = sorted(users, key=lambda user: user["username"])  # alfabetik olarak sıralar 
print(sonuc)  # [{'username': 'ahmetyilmaz', 'posts': ['post 1'], 'email': 'info@abcd.com'},{'username': 'cananyilmaz', 'posts': ['post 1', 'post 2', 'post 3']}, {'username': 'sadikturan', 'posts': ['post 1', 'post 2'], 'email': 'info@abc.com', 'phone': '1234'}]

sonuc = sorted(users, key=lambda user: len(user["posts"]))  # posts sayılarına göre sıralar 
sonuc = sorted(users, key=lambda user: len(user["posts"]), reverse=True) 

sonuc = list(map(lambda user: user["username"],sorted(users, key=lambda user: len(user["posts"]))))  # posts sayılarına  göre sıraladıktan sonra username ler alınır
print(sonuc) # ['ahmetyilmaz', 'sadikturan', 'cananyilmaz']


kurslar = [
    {"title":"python","count":10000},
    {"title":"web geliştirme","count":20000},
    {"title":"javascript","count":5000},
]

sonuc = sorted(kurslar, key= lambda kurs: kurs["count"]) # count değerine göre sıralanır
print(sonuc)
sonuc = sorted(kurslar, key= lambda kurs: kurs["count"], reverse=True) # count değerinin artanına göre sıralanır
print(sonuc)
sonuc = list(map(lambda kurs: kurs["title"], sorted(kurslar, key= lambda kurs: kurs["count"], reverse=True))) # count değerinin artanına göre sıralanır sonrasında title değerleri alınır
print(sonuc)  # ['web geliştirme', 'python', 'javascript']