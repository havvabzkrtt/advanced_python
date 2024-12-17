from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
from csv import writer  # dosyaya sadece yazma işlemi gerçekleştirilecek

# ChromeDriver'ın yolunu belirlemek yerine otomatik indirme
service = Service(ChromeDriverManager().install())

# WebDriver başlat
driver = webdriver.Chrome(service=service)

# URL'yi aç
driver.get("https://www.trendyol.com/sr?tag=fs_14_12_2024_12_15")

# İçeriğin yüklenmesi için bekleyin
time.sleep(5)

# Sayfanın HTML'sini alın ve BeautifulSoup ile işleyin
html = BeautifulSoup(driver.page_source, "html.parser")

flash_products = html.find(class_="search-result-wrapper").find_all(class_="p-card-chldrn-cntnr card-border")
# for product in flash_products:
#     print(product.text)
#     print("---------")

with open("Web_Scraping/trendyol_flash_prodcuts.csv","w",encoding="utf-8") as file:
    csv_writer = writer(file)
    csv_writer.writerow(["Product Link","Product Image","Product Brand","Product Title","Product Content","Product Rating Score", "Product Price"])

    for product in flash_products:
        anchor = product.a 
        link = anchor.get("href")
        print(link)
        image = anchor.img.get("src")
        
        other_div = product.find(class_= "product-down flash-sales-product-down")

        brand = other_div.find(class_= "prdct-desc-cntnr-ttl").string  # titleları alıyoruz .string ile
        print(brand)
        
        title = other_div.find(class_= "prdct-desc-cntnr-name hasRatings").string
        print(title)

        content = other_div.find(class_="product-desc-sub-text").string
        print(content)

        rating_score = other_div.find(class_="rating-score").string
        print(rating_score)

        price = other_div.find(class_="prc-box-dscntd").string
        print(price)
        # seviye = anchor.h3.find(class_="txt-secondary font-medium").string
        # # print(seviye)
        
        print("-------------")
   
        csv_writer.writerow([link, image, brand, title, content, rating_score, price]) # csv dosyasına yazdırma


# WebDriver'ı kapatın
# driver.quit()
