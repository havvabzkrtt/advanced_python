# find metodu yardımıyla birden fazla element aynı anda 

from bs4 import BeautifulSoup

with open("Web_Scraping/index.html", encoding="utf-8") as file:
    html = file.read()

obj = BeautifulSoup(html, "html.parser")

sonuc = obj.div  # ilk div elementi bulunur
sonuc = obj.find("div") # ilk div elemnti bulunur yine 
sonuc = obj.find_all("div") # bütün div elementleri bulunur
sonuc = len(obj.find_all("div"))  # div elementlerinin sayısını ifade eder
sonuc = obj.find_all("div")[1].h2  # 2. divin altındaki h2 elementi getirilir
sonuc = obj.find_all("div")[1].ul  # 2. divin altındaki ul elementi getirilir
sonuc = obj.find_all("div")[1].ul.find_all("li")  # 2. divin altındaki ul elementi altındaki li elemntlerini getirir
sonuc = obj.find_all("div")[1].ul.find_all("li")[2] # 2. divin altındaki ul elementi altındaki 3. li elemntini getirir
sonuc = obj.find_all("div")[1].ul.find_all("li")[2].string # 2. divin altındaki ul elementi altındaki 3. li elemntinin içeiriğini getirir

for div in obj.find_all("div"):  # bütün div elemanları
    if div.h2.a != None:
        print(div.h2.a.string.strip()) 
        # div elementlerinin altındaki h2 elementinin altındaki a elementinin içeriğine erişilir
    else:
        print(div.h2.string.strip())
        # div elementlerinin altındaki h2 elementinin içeriği
# strip ile sağ ve soldaki boşluklar silinir

print("---------------")

for a in obj.find_all("a"): # tüm a elementleri bulunur
    print(a)  
