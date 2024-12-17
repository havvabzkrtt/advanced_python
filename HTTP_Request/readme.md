# HTTP Request ve Web Servisleri 

Bu döküman, Python'da HTTP Request yöntemlerini ve web servisleri kullanarak veri alışverişi yapmayı anlatır. Ayrıca JSON Placeholder ve Fixer gibi servislerle yapılan işlemler ve temel HTTP kavramları detaylandırılmıştır.

---

## **Web Servisleri ve Amaçları**
### **JSON Placeholder**
- JSON Placeholder, uygulama geliştirme sırasında test amaçlı kullanılabilecek bir web servisidir.
- Belirli bir URL'ye yapılan talepler (request), JSON formatında örnek veriler döndürür.
- Örneğin, test ortamında **https://jsonplaceholder.typicode.com/** adresine talep göndererek çeşitli JSON içerikleri alabilirsiniz.

### **Fixer**
- Fixer, döviz kurları gibi gerçek zamanlı verilere erişmek için kullanılan bir servistir.
- Uygulamanızda canlı döviz kuru hesaplamaları yapmak istiyorsanız bu API'yi veya benzer alternatifleri kullanabilirsiniz.
- **https://fixer.io/** adresi üzerinden bu servise erişebilirsiniz.

---

## **HTTP Kavramları**
### **Client (İstemci)**
- İstemci, bir talep (HTTP Request) göndererek sunucudan bilgi ister.

### **Server (Sunucu)**
- Sunucu, istemciden gelen talepleri işler ve bir yanıt (HTTP Response) döndürür.

![Client-Server İlişkisi](client_server.png)

---

## **HTTP Yanıt Kodları (Response Status Codes)**
- **2xx (Başarı):** Talep başarılı şekilde tamamlanmıştır. Örneğin: **200 OK**.
- **3xx (Yönlendirme):** Talep edilen kaynak farklı bir adrese yönlendirilmiştir.
- **4xx (İstemci Hatası):** Talep hatalı yapılandırılmıştır. Örneğin: **400 Bad Request**.
- **5xx (Sunucu Hatası):** Talep doğru şekilde gönderilmiştir ancak sunucu bir hata üretmiştir. Örneğin: **500 Internal Server Error**.

---

## **HTTP Metotları**
### **HTTP GET**
- Sunucudan bilgi almak için kullanılır.
- GET metodu veri güncellemesi yapmaz; yalnızca bilgi talep eder.
- Örneğin bütün kursları içeren bir web sayafasında sadece pyton kursları talep edilmesi.

![HTTP GET Metodu](http_get.png)

- Örnek:
  ```python
  import requests
  response = requests.get("https://jsonplaceholder.typicode.com/posts")
  print(response.json())
  ```

### **HTTP POST**
- Sunucuya veri göndermek ve işlemler yapmak için kullanılır. Örneğin: yeni bir kayıt eklemek.
- Gönderilen veriler, talebin **body** kısmında paketlenerek yer alır. Server kısmında bu bilgilerle bir ekleme, güncellem, silme gibi işlemler yapılır. İşte buna http post denir. 

![HTTP POST Metodu](http_post.png)

- Örnek:
  ```python
  import requests
  response = requests.post(
      "https://jsonplaceholder.typicode.com/posts",
      data={
          "userId": 1,
          "title": "Yeni Gönderi",
          "body": "Gönderi açıklaması"
      }
  )
  print(response.json())
  ```

---

## **Query String Parametreleri**
- Query string, URL'nin sonuna eklenen **key-value** çiftlerinden oluşur.
- Parametreler, sunucunun döndüreceği veriyi filtrelemek için kullanılır.

![Query String Parametreleri](querystring.png)

### **Örnekler**
- **https://jsonplaceholder.typicode.com/todos?userId=1**  
  - Bu istek, `userId` değeri 1 olan öğeleri döndürür.

- **https://jsonplaceholder.typicode.com/todos?userId=1&completed=true**  
  - Bu istek, `userId` değeri 1 olan ve tamamlanmış (completed) öğeleri döndürür.

---

## **API Kullanımı (API_uygulama.py)** 
### **RapidAPI**
- **https://rapidapi.com/hub** üzerinden farklı alanlarda kullanılabilecek API'leri keşfedebilirsiniz.

### **Weather API**
- **https://www.weatherapi.com/api-explorer.aspx** adresinden hava durumu gibi verileri almak için örnek talepler oluşturabilirsiniz.
- Bir hava durumu API'siyle ilgili örnek talep:
  ```python
  import requests

  response = requests.get(
      "http://api.weatherapi.com/v1/current.json",
      params={
          "key": "YOUR_API_KEY",
          "q": "London"
      }
  )
  data = response.json()
  print("Şehir:", data["location"]["name"])
  print("Hava Durumu:", data["current"]["condition"]["text"])
  print("Sıcaklık:", data["current"]["temp_c"], "°C")
  ```

![Response Body Örneği](response_body.png)

- Gönderilebilecek parametrelerin tam listesini görmek için [Weather API Dokümantasyonu](https://www.weatherapi.com/docs/) sayfasını inceleyebilirsiniz.

---

## **Sonuç**
Bu döküman, HTTP isteklerinin temel kullanımını ve web servislerinden nasıl faydalanabileceğinizi örneklerle açıklamaktadır. JSON Placeholder gibi test amaçlı servislerle uygulama geliştirirken HTTP isteklerini anlamak, gerçek API'lerle çalışırken karşılaşılabilecek sorunların çözümünü kolaylaştırır.