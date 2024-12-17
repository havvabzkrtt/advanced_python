import requests
from bs4 import BeautifulSoup
from csv import writer  # dosyaya sadece yazma işlemi gerçekleştirilecek


# # STATİK YÜKLEME
# # # Statik olarak yüklenince hata alıyorum, id ve classları bulamıyor
# url = "https://www.btkakademi.gov.tr/portal/catalog?categoryId=353"
# # site güncellendiği zaman uygulama da güncellenmeli, url falan

# headerParams = {"user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}
# # headerParams, tarayıcıyı taklit etmeye yarar
# # response = requests.get(url, headers=headerParams)
# response = requests.get(url)
# print(response.status_code)  # Çoğu durumda bu yeterli olabilir
# html = BeautifulSoup(response.text, "html.parser")  
# print(html.prettify())

# kurslar = html.find(id="gbt_catalog-main-right-course").find_all(class_="ant-ribbon-wrapper")
# # id ve class a göre seçtik 

# # print(kurslar[0])

# with open("kurslar.csv","w",encoding="utf-8") as file:
#     csv_writer = writer(file)
#     csv_writer.writerow(["link","image","title","seviye","like","ogrenci"])

#     for kurs in kurslar:
#         anchor = kurs.a
#         link = anchor.get("href")
#         image = anchor.img.get("src")
#         title = anchor.find(class_="font-medium text-base").string
#         seviye = anchor.find(class_="txt-secondary font-medium").string
#         # print(seviye)
#         sayilar = anchor.next_sibling.next_sibling.get_text(separator="-").split("-")
#         like = sayilar[0]
#         ogrenci = sayilar[1]

#         csv_writer.writerow([link, image, title, seviye, like, ogrenci])



# DİNAMİK YÜKLEME

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

# ChromeDriver'ın yolunu belirlemek yerine otomatik indirme
service = Service(ChromeDriverManager().install())

# WebDriver başlat
driver = webdriver.Chrome(service=service)

# URL'yi aç
driver.get("https://www.btkakademi.gov.tr/portal/catalog?categoryId=353")

# İçeriğin yüklenmesi için bekleyin
time.sleep(5)  # time.sleep() ile sayfanın tamamen yüklenmesi beklenir.

# Sayfanın HTML'sini alın ve BeautifulSoup ile işleyin
html = BeautifulSoup(driver.page_source, "html.parser")
# print(html.prettify())

kurslar = html.find(id="gbt_catalog-main-right-course").find_all(class_="ant-ribbon-wrapper")
# id ve class a göre seçtik 

print(kurslar[0])

with open("Web_Scraping/kurslar.csv","w",encoding="utf-8") as file:
    csv_writer = writer(file)
    csv_writer.writerow(["link","image","title","seviye","like","ogrenci"])

    for kurs in kurslar: 
        anchor = kurs.a # anchor tag: a etiketine denir
        link = anchor.get("href")
        image = anchor.img.get("src")
        title = anchor.find(class_="font-medium text-base").string
        seviye = anchor.find(class_="txt-secondary font-medium").string
        # print(seviye)

        sayilar = anchor.next_sibling.next_sibling.get_text(separator="-").split("-")
        like = sayilar[0]
        ogrenci = sayilar[1]

        csv_writer.writerow([link, image, title, seviye, like, ogrenci]) # csv dosyasına yazdırma



"""
Kurs bilgileri kurslar.csv dosyasına şu formatta kaydedilir:

link: Kursun detay sayfasına yönlendiren bağlantı.
image: Kursun önizleme görseli bağlantısı.
title: Kursun başlığı.
seviye: Kursun seviyesi (örn. Başlangıç, Orta).
like: Kursun aldığı beğeni sayısı.
ogrenci: Kursa kayıtlı öğrenci sayısı.


"""