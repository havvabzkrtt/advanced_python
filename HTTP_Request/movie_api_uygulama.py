# https://www.themoviedb.org/
# https://developer.themoviedb.org/reference/lists-copy

import requests

# movie_name = input("Aramak istediğiniz film ismini giriniz: ")

url = "https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page=1&sort_by=popularity.desc"



headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJlZjYwMDE1YWRjNjRlMmIyYmRmNjkwOGVjNjIxZmI5YSIsIm5iZiI6MTczMzM5OTk0NS4wMzgsInN1YiI6IjY3NTE5NTg5NTE2ZWRlYWIyOTk5MjcwMCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.43iGgYA4sjIGBOmsY2FH4uYeqWr78YidRhNmZSsDA_4",
}
# Authorization: https://www.themoviedb.org/settings/api buradan alınır 
# response = requests.get(url, headers=headers)

response = requests.get(url, headers=headers, params= {
    "id" : "912649"
})

print(response) # <Response [200]>
print("--------------------------------------------------------------------------")
print(response.text)
print("--------------------------------------------------------------------------")

# response u json dosyasına kaydetme 
sonuc = response.json()
import json 
# sonuc = json.dumps(response) # serialize işlemi yapılır 
with open("HTTP_Request/movie.json", "w", encoding="utf-8") as file:
    json.dump(sonuc, file, ensure_ascii=False, indent=2)  # dosyaya kaydederiz
print("json dosyasına kaydedili")


print("--------------------------------------------------------------------------")
"""title = sonuc["results"]["title"]
print(title)"""