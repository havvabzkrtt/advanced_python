# attributelara göre seçme işlemi yapılır
from bs4 import BeautifulSoup

with open("Web_Scraping/index.html", encoding="utf-8") as file:
    html = file.read()

# index.html'de attribute değerlerinin isimleri farklı olmalıdır
obj = BeautifulSoup(html, "html.parser")

sonuc = obj.div
sonuc = obj.find("div") # ilk div elementini getirir
print(sonuc)
print("-------------")
sonuc = obj.find(id="item1")  # id attribute u item1 olan ilk elementi getirir 
print(sonuc)
print("-------------")
sonuc = obj.find(id="item2")
print(sonuc)
print("-------------")
sonuc = obj.find(id="header")
print(sonuc)
print("-------------")
sonuc = obj.find(class_="item") # class attribute u item olan elementi getirir 
print(sonuc)
print("-------------")
sonuc = obj.find_all(class_="item")
print(sonuc)
print("-------------")
sonuc = obj.find_all(class_="item")[1]
print(sonuc)
print("--------------------------------------------------------")

sonuc = obj.select("#header")  # select metodu aracılığıyla id(#) si header olan bütün elementleri getirir
print(sonuc)
print("-------------")
sonuc = obj.select("#item1")
print(sonuc)
print("-------------")
sonuc = obj.select(".item")  # select metodu aracılığıyla class(.) ı item olan bütün elementleri getirir
print(sonuc)
print("--------------------------------------------------------")

sonuc = obj.select_one(".item") # select_one metodu ile class(.) ı item olan ilk elementi getirir
print(sonuc)
print("-------------")
sonuc = obj.select_one("#item1")# select_one metodu ile id(#) ı item1 olan ilk elementi getirir
print(sonuc)
print("--------------------------------------------------------")


print("attrs metot")
sonuc = obj.div.attrs["id"] # attrs metodu ile ilk div elementinde bulunan attributeların(id veya class) isimleri getirilir
print(sonuc) # item1
print("-------------")
sonuc = obj.div.attrs["class"]
print(sonuc) # ['item', 'red']
print("--------------------------------------------------------")

sonuc = obj.ul.get_text(strip=True, separator="-")  # get_text metodu ile bulunan ilk ul elementinin bütün text bilgileri getirilir
print(sonuc)  # Menü 1-Menü 2-Menü 3
print("-------------")

for a in obj.div.find_all("a"): # bulunan ilk div elementindeki a elementlerini getirir
    # print(a.get("href")) # a elentlerinin link bilgileri getirilir
    print(a["href"])

