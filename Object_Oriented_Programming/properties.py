# "property" mekanizması kullanılarak bir sınıfın (class) veri üyelerine erişim ve değişim kontrol altına alınmıştır. 


class Product:
    def __init__(self, name, price):
        self.name = name
        if price >= 0:
            self._price = price
        else:  # ürün fiyatına negatif değer verilirse
            raise ValueError("ürün fiyatı için negatif değer ataması yapılmaz")
        

# 1. yöntem: "@property" ve "@property_name.setter" dekoratörleri, nesne içindeki verilerin doğruluğunu, tutarlılığını ve erişim yöntemlerini sağlamak için kullanılmaktadır.
    
    @property  # Bir özellik (attribute) gibi görünmesine rağmen, aslında arka planda bir metot çalıştırır.
    def price(self):
        return self._price
    
    @price.setter  # Bir property'nin yazılabilir (set edilebilir) olması sağlanır.
    def price(self, value):
        if value >= 0:
            self._price = value
        else:
            raise ValueError("ürün fiyatı için negatif değer ataması yapılmaz")
        

# 2. yöntem: get, set 

    # def set_price(self, value):
    #     if value >= 0:
    #         self._price = value
    #     else:
    #        raise ValueError("ürün fiyatı için negatif değer ataması yapılmaz")
        
    # def get_price(self):
    #     return self._price


p = Product("IPhone 16", 80000)
print(p.name, p.price)  # IPhone 16 80000

# p = Product("IPhone 16", -80000) # burda hata verir

# p.price = -90000 # Şuan hata verir ama 
# eğer property tanımlamadan önce bu işlem yapılsaydı, value sonradan dışarıda değiştirildi için hata vermezdi ve sistem mantığında hata oluşurdu yani ürün fiyatı negatif olurdu.
# Bu sorunun önüne geçmek için bir sınıfın (class) veri üyelerine erişim ve değişim kontrol altına alınır.

p.price = 90000  
print(p.price)  # 90000

# get,set 
# p.set_price(70000)  # 70000
# print(p.get_price())   # => p.price, p.price = 70000
# print(p.name, p.price) # IPhone 16 70000


"""
Manuel Getter ve Setter Metotları (get,set)
"get_price()" ve "set_price(value)" metotları, property kullanılmadan özelliklere erişim ve güncelleme sağlar.
Ancak modern Python'da "@property" ile yapılan işlemler, bu manuel metotların yerine tercih edilir.


Neden property Kullanmalıyız?
- Kapsülleme: Değişkenlere doğrudan erişimi kısıtlayarak kontrol sağlanır.
- Doğrulama: Setter kullanılarak değerler için kısıtlama getirilebilir.
- Kullanım Kolaylığı: Getter ve setter metotlarını çağırmak yerine, bir özellik gibi kullanabilirsiniz (obj.price).
Sonuç olarak, property Python'da temiz, güvenli ve esnek bir kod yazmak için güçlü bir araçtır.
"""