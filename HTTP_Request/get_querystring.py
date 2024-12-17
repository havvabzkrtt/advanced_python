import requests

# bu şekilde de querystring ile sorgulama yapabiliriz
# response = requests.get("https://jsonplaceholder.typicode.com/todos?userId=1&completed=true")

# ve bu şekilde de querystring ile sorgulama yapabiliriz
# parametreleri dışarıdan alabiliriz ve sorguyu dinamik bir şekilde çalıştırmak isteyebiliriz
# key-value şeklinde parametre gönderilebilir
response = requests.get("https://jsonplaceholder.typicode.com/todos", params= {
    "userId": "1",  
    "completed": "true"
})

todos = response.json()

sonuc = todos
print(sonuc)
print("----------")
print(sonuc[0]["title"])  # et porro tempora
