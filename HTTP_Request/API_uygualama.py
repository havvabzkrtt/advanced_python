import requests

url = "http://api.weatherapi.com/v1/current.json"
key = "a8e380abe945444cbf8113900240512"  # https://www.weatherapi.com adresinden alınır

konum = input("konum: ")

response = requests.get(url, params= {
    "key" : key,
    "q" : konum,
    "lang": "tr"   # dil bilgisi için parametre
})

# https://www.weatherapi.com/docs/ : üzerinden gönderebileceğimiz request paramlarını görebiliriz
sonuc = response.json()
print(sonuc)
print("-----------")
sehir = sonuc["location"]["name"]
havadurumu = sonuc["current"]["temp_c"]
text = sonuc["current"]["condition"]["text"]

print(f"{sehir} şu anda {havadurumu} derece ve {text}")