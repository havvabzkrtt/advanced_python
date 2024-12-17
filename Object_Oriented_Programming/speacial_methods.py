liste = [1,2,3]

print(len(liste)) # 3

# sayi = 10
# print(len(sayi))  # hata verir, int veri tipinin len adında bir fonksiyonu yoktur fakat özelleştirebiliriz istersek.

s = "Merhaba BTK Akademi"

print(len(s)) # 19 

class Movie:
    def __init__(self, title, director, year, duration):
        self.title = title
        self.director = director
        self.year = year
        self.duration = duration

    def __repr__(self):  #  (Temsil Etme): Nesnenin tanımlayıcı ve geliştiriciye yönelik bir temsilini döndürür.
        return f"{self.title}, {self.director} tarafından {self.year} yılında yayınlandı."
    
    def __len__(self):  # (Uzunluk Hesaplama): len() fonksiyonunu bir nesne için özelleştirir ve sınıfta belirtilen bir değeri döndürür.
        return self.duration    
     
    def __del__(self):  # (Nesne Silme): Nesne silindiğinde (del komutu) çağrılır ve genelde temizleme işlemleri için kullanılır.
        print("film silindi")   

m = Movie("film adı", "yönetmen", "yayın tarihi", 120)

print(m.__repr__())  # film adı, yönetmen tarafından yayın tarihi yılında yayınlandı.
print(len(m))  # 120
 
del m  # film silindi