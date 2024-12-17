# JSON İşlemleri Örnekleri  

JSON (JavaScript Object Notation), yapılandırılmış verilerin depolanması ve taşınması için kullanılan hafif ve kolay anlaşılır bir veri formatıdır. Genellikle API'lar ve veri transfer işlemlerinde tercih edilir. JSON formatı, verileri anahtar-değer çiftleri şeklinde düzenler.

### **JSON'un Avantajları:**

- **Hafif ve okunabilir:** İnsan tarafından kolayca okunabilir ve yazılabilir bir yapıya sahiptir.
- **Platformdan bağımsız:** Çeşitli programlama dillerinde kolaylıkla kullanılabilir.
- **Esnek:** Nesne (object), liste (array), string, sayı (number), boolean ve null gibi farklı veri türlerini destekler.

### **JSON'un Temel Kullanımları:**

- **Serialize (Encode):** Uygulamada kullanılan nesneleri JSON formatına dönüştürerek dosyalara veya ağ üzerinden taşınabilir hale getirir.
- **Deserialize (Decode):** JSON formatındaki verileri alarak uygulama içinde kullanılabilecek nesnelere dönüştürür. 

### JSON işlemlerinde kullanılan temel fonksiyonlar:  
- `json.load()`: Bir dosyadan JSON verisini okur ve Python veri türüne dönüştürür.  
- `json.loads()`: Bir JSON stringini Python veri türüne dönüştürür.  
- `json.dump()`: Python veri türünü JSON formatına dönüştürerek bir dosyaya yazar.  
- `json.dumps()`: Python veri türünü JSON stringine dönüştürür.  

--- 

## 1. `deserialize_json.py`  
### Amaç:  
JSON verilerinin Python uygulamaları tarafından **deserialize** (JSON'dan okunarak Python veri türüne dönüştürülmesi) edilmesini gösterir.  

### Özellikler:  
- Bir JSON dosyasından (`product.json`) veri okuma ve bu veriyi Python veri türlerine dönüştürme.  
- Uygulama içinde tanımlanmış JSON stringlerini Python veri türüne (`dict`) dönüştürme.  
- JSON verilerinden belirli alanlara erişim (`title`, `price`, `colors`).  

---

## 2. `serialize_json.py`  
### Amaç:  
Python'da bir sınıftan türetilen nesnelerin, JSON formatına dönüştürülerek bir dosyaya kaydedilmesini (**serialize**) ve JSON dosyalarından tekrar Python nesnelerine dönüştürülmesini (**deserialize**) gösterir.  

### Özellikler:  
- `Product` sınıfı kullanılarak nesneler oluşturulur.  
- Nesneler `.json` dosyasına kaydedilirken Python `__dict__` özelliği ile JSON formatına çevrilir.  
- Kaydedilmiş JSON verisi Python sözlüklerine (`dict`) çevrilir ve tekrar `Product` nesnelerine dönüştürülür.  

---

## 3. `json_liste.py`  
### Amaç:  
JSON formatında bir liste oluşturmayı ve bu liste üzerinde ekleme, güncelleme, silme işlemlerini göstermeyi amaçlar.  

### Özellikler:  
- JSON formatında bir liste oluşturulur ve `products_liste.json` dosyasına yazılır.  
- Listeye yeni bir ürün ekleme.  
- Listede bir ürün bilgisi güncelleme.  
- Listedeki bir ürünü silme.  

---

## 4. `json_dict.py`  
### Amaç:  
JSON formatında bir sözlük (dictionary) oluşturmayı ve bu sözlük üzerinde veri ekleme, güncelleme, silme işlemlerini göstermeyi amaçlar.  

### Özellikler:  
- JSON formatında bir sözlük oluşturulur ve `products_dict.json` dosyasına kaydedilir.  
- Sözlük üzerinden veri ekleme işlemi yapılır.  
- Sözlükteki bir verinin güncellenmesi ve silinmesi işlemleri gösterilir.  

---

## 5. `json_multiple_liste.py`  
### Amaç:  
Karmaşık bir JSON yapısı üzerinde çalışma yapmayı ve birden fazla kategori içeren verilerle çalışmayı gösterir.  

### Özellikler:  
- Kullanıcılar ve ürünler gibi farklı kategorilere ayrılmış JSON verisi oluşturulur ve `db_multiple.json` dosyasına kaydedilir.  
- JSON yapısına yeni kullanıcılar veya ürünler eklenir.  
- Mevcut kullanıcı veya ürün bilgileri güncellenir.  

---

## 6. `serialize_class.py`  
### Amaç:  
Bir Python sınıfı tarafından temsil edilen nesnelerin JSON formatına dönüştürülmesi (serialize) ve JSON formatından tekrar sınıf nesnesine dönüştürülmesini (deserialize) öğretir.  

---

### Özellikler:  
- **Sınıf Nesnesini JSON'a Dönüştürme:** Bir `Product` sınıfı nesnesi, JSON formatında dosyaya kaydedilir.  
- **Sözlük Yapısı Kullanımı:** Nesneler `__dict__` özelliği kullanılarak Python sözlüğüne çevrilir.  
- **Birden Fazla Nesneyle Çalışma:** Birden fazla nesne bir JSON dosyasında kategorilere ayrılmış şekilde saklanabilir.  
---


## Kullanım  
1. Projeyi çalıştırmadan önce `JSON` adında bir klasör oluşturduğunuzdan emin olun.  
2. Tüm dosyalar çalıştırılabilir ve her biri kendi içinde bağımsız olarak JSON dosyalarını okuma/yazma işlemleri gerçekleştirir.  

Bu dosyalar, JSON işlemleriyle ilgili temel işlemleri öğrenmek ve uygulamak için tasarlanmıştır. Daha fazla bilgi için Python [JSON Modülü Belgelendirmesi](https://docs.python.org/3/library/json.html) incelenebilir.  

---  
**Not:** Kod dosyalarını çalıştırırken, her biri için gerekli JSON dosyalarının oluşturulmuş olduğundan emin olun. Örneğin, `products_liste.json` ve `products_dict.json` dosyaları, `json_liste.py` ve `json_dict.py` dosyalarında kullanılan JSON dosyalarıdır.
