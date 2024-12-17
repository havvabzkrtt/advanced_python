import requests
import json

response = requests.get("https://jsonplaceholder.typicode.com/posts")

print(response)  # <Response [200]> : bir response objesi döndürlür, başarılı talep yapıldığı bildirilir

print("---------------------------")
sonuc = response
sonuc = type(response)
print(sonuc) # <class 'requests.models.Response'>
print("---------------------------")
sonuc = response.status_code
print(sonuc)  # 200 : success
print("---------------------------")
sonuc = response.headers
print(sonuc)  # dict döndürülür 
print("----")
sonuc = type(response.headers)
print(sonuc)  # <class 'requests.structures.CaseInsensitiveDict'>
print("---------------------------")
sonuc = response.headers["Content-Type"]  # headers içerisinden istenile bilgi alınabilir
print(sonuc)  # application/json; charset=utf-8
print("---------------------------")
sonuc = response.url
print(sonuc)  # https://jsonplaceholder.typicode.com/posts
print("---------------------------")
sonuc = response.encoding
print(sonuc)  # utf-8
print("---------------------------")
sonuc = response.text
print(sonuc)  
print("---------------------------")
sonuc = type(response.text)
print(sonuc)  # <class 'str'>
print("---------------------------")
posts = json.loads(response.text)
sonuc = posts[0]["title"]
print(sonuc)  # "cupiditate quo est a modi nesciunt soluta\nipsa voluptas error itaque dicta in\nautem qui minus magn
print("---------------------------")

# filtreleme ile çıktı alabiliriz
for item in posts:
    if item["userId"] == 1:
        print(item["title"])

"""
sunt aut facere repellat provident occaecati excepturi optio reprehenderit
qui est esse
ea molestias quasi exercitationem repellat qui ipsa sit aut
eum et est occaecati
nesciunt quas odio
dolorem eum magni eos aperiam quia
magnam facilis autem
dolorem dolore est ipsam
nesciunt iure omnis dolorem tempora et accusantium
optio molestias id quia eum
"""