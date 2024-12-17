import requests

# server tabanına veri göndereceğiz ve kaydetmesini isteyeceğiz

response = requests.post("https://jsonplaceholder.typicode.com/posts", data = {
    "userId": 1,
    "title": "yeni gönderi",
    "body": "yeni gönderi açıklaması"
})

sonuc = response
print(sonuc)   # <Response [201]> : server tarafında doğru çalıştığı ve bir kaynağın oluşturulduğu anlamına gelir
print("------------")
sonuc = response.text
print(sonuc)
print("------------")
sonuc = response.json()
print(sonuc)
print("------------")
sonuc = response.headers
print(sonuc)
print("------------")