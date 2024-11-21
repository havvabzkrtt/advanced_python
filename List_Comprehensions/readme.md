# **Python'da List Comprehensions**

Bu depo, Python'da **List Comprehensions** kullanımını çeşitli örnekler ve uygulamalarla göstermektedir. List Comprehensions, döngü ve koşullu ifadeleri tek satırda birleştirerek liste oluşturmayı kolaylaştıran bir yöntemdir.

---

## İçerik  

1. **`list_comp.py`**  
   Temel list comprehension kullanımını gösterir. Geleneksel `for` döngüsü ile yazılan kodların nasıl daha kısa ve okunabilir hale getirilebileceği örneklerle açıklanmıştır.  
   Öne çıkan içerikler:  
   - Sayıların bir döngüyle işlenmesi  
   - Karakterlerin büyük harfe çevrilmesi  
   - Liste elemanlarının uzunluklarının bulunması  

2. **`list_comp_condition.py`**  
   List comprehensions'ta **koşullu ifadelerin (if-else)** nasıl kullanılacağını gösterir. Geleneksel yöntemlerle yazılmış kodlar, list comprehensions ile sadeleştirilmiştir.  
   Öne çıkan içerikler:  
   - Çift sayıları filtreleme  
   - Fiyatlara göre vergi hesaplama  
   - Koşula dayalı liste oluşturma  

3. **`list_comp_practices.py`**  
   List comprehensions ile ilgili pratik uygulamalar ve çeşitli problemleri çözme yöntemleri içerir.  
   Örnek çalışmalar:  
   - 1-100 arası 12'ye tam bölünen sayılar  
   - Metin içindeki rakamları bulma  
   - Hava sıcaklıklarına göre yorum yapma  
   - Öğrencilerin notlarını işleme  
   - Çoklu döngülerle (nested loops) liste oluşturma  

---

### **List Comprehensions Nedir?**

List Comprehensions, listeleri daha kısa ve okunabilir bir şekilde oluşturmak için kullanılan bir Python tekniğidir. Temel yapı şöyledir:

```python
# Geleneksel yöntem
sonuc = []
for i in range(10):
    sonuc.append(i * 2)

# List comprehension ile
sonuc = [i * 2 for i in range(10)]
```

### **Koşullu Kullanım**

List comprehension'lara koşullu ifadeler eklenebilir:

```python
# Sadece çift sayıları filtrelemek
cift_sayilar = [sayi for sayi in range(10) if sayi % 2 == 0]

# Koşullu olarak elemanları değiştirmek
sonuc = [sayi if sayi % 2 == 0 else "tek sayı" for sayi in range(10)]
```

