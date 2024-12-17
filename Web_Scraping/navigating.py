# Etiketler üzerinde dolaşma işlemini sağlar.
from bs4 import BeautifulSoup

with open("Web_Scraping/index.html", encoding="utf-8") as file:
    html = file.read()

obj = BeautifulSoup(html, "html.parser")

sonuc = obj.body.div.contents[3]  # contents metodu ile div elementi altındaki elementlere ulaşılabilir

# for i in obj.body.div.children: # children metodu ile div elementine ait childları içeren iteratör elde edilir,  birinci seviyedeki alt elemanlar getirilir
#     print(i)                   

# for i in obj.body.div.descendants: # descendants metodu ile div metodu altındaki, elemetlerin altındaki elementleri içeren iteratör elde edilir, alt elemanların da alt elemanları getirilir
#     print(i)

sonuc = obj.body.h2.parent # h2 elementinin parent elementi getirilir
sonuc = obj.body.h2.parent.parent # parentın parentına da gidilebilir

sonuc = obj.body.ul.next_element.next_element # ilk ul elementinden sonraki element elde edilir
sonuc = obj.body.ul.next_element # çıktı boşluk olur çünkü arada bir new line etiketi (\n) vardır

print("--------")
sonuc = obj.body.div.next_sibling.next_sibling  # div elementinde sonraki kardeş elementler getirilir
print(sonuc)
print("--------")
sonuc = obj.body.div.find_next_sibling("div") # sonraki div elementi getirilir
print(sonuc)
print("--------")
sonuc = obj.body.div.find_next_sibling("div").find_next_sibling("div")
print(sonuc)
print("--------")
sonuc = obj.body.div.find_next_sibling("div").find_next_sibling("div").find_previous_sibling("div") 
print(sonuc)
print("--------")
