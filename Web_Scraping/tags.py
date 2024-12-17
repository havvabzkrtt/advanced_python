# Taglere göre bir html dosyası içerisindeki istenilen elemana, etikete ulaşılır.

from bs4 import BeautifulSoup

with open("Web_Scraping/index.html") as file:
    html = file.read() # html içeriğinin string olarak elde edilir  

obj = BeautifulSoup(html, "html.parser") # string ifade, BeautifulSoup objesine dönüştürülür

# html.parser : html dosyası kaynağından bilgi alınacağı için, xml de olabilirdi kaynak

sonuc = obj
# print(sonuc)   # html içeriği döndürülür
print("--------------")
sonuc = type(obj)
print(sonuc)  # <class 'bs4.BeautifulSoup'>
sonuc = type(html)
print(sonuc)   # <class 'str'>
print("--------------")
sonuc = obj.prettify()
# print(sonuc)   # girintiler çıkıntılar içerik düzenli bir şekilde okunarak yazdırılır
print("--------------")
sonuc = obj.title  # direkt tagin tamamını döndürür
print(sonuc)   # <title>BTK Akademi Python Kursu</title>

sonuc = type(obj.title)
print(sonuc)   # <class 'bs4.element.Tag'>

sonuc = obj.title.name # tagin isim bilgisi 
print(sonuc)   # title 

sonuc = obj.title.string  # tagin içeriğini okumak için
print(sonuc)   # BTK Akademi Python Kursu
print("--------------") 

sonuc = obj.body  # sadece body etiketini getirir

sonuc = obj.body.h1  # h1 etiketi getirilir 
print(sonuc)   # <h1 id="header"> Python Kursu </h1>

sonuc = obj.body.h1.string # h1 etiketinin içeriği getirilir
print(sonuc)   # Python Kursu
  
sonuc = obj.h1.string # h1 etiketinin içeriği getirilir
print(sonuc)   # Python Kursu
print("--------------") 

# Safa üzerindeki ilk elementlere getirilir
sonuc = obj.div
print(sonuc)   
"""
<div class="item red" id="item1">
<h2>
<a href="index.html">Python OOP</a> </h2>
<ul>
<li>MenÃ¼ 1</li>
<li>MenÃ¼ 2</li>
<li>MenÃ¼ 3</li>
</ul>
</div>
"""
print("--------------") 
sonuc = obj.h2
print(sonuc)   # <h2><a href="index.html">Python OOP</a> </h2>
print("--------------") 
sonuc = obj.ul
print(sonuc) 
"""
<ul>
<li>MenÃ¼ 1</li>
<li>MenÃ¼ 2</li>
<li>MenÃ¼ 3</li>
</ul>
"""
print("--------------") 
sonuc = obj.ul.li
print(sonuc)   # <li>MenÃ¼ 1</li>
print("--------------") 

