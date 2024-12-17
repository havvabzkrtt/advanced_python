import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "havvabzkrt41",
    database = "shopdb"
)

cursor = db.cursor()

# sql sorgusu yazılır / tabloda zorunlu olan kolon isimleri eklenmeli ve yer tutucular eklenir (%s)
sql = "INSERT INTO products (name,price,imgUrl,description) VALUES (%s,%s,%s,%s)"

# value = ("IPhone 16",70000,"3.jpg","iyi bir telefon")
# cursor.execute(sql,value)  # şuan direkt sql sorgusu çalışmaz

# db.commit() # artık sorgu veri tabanına gönderilir / bu yapılmazsa veri tabanında değişiklik gözükmez

# print(cursor.rowcount, "kayıt edildi") # kaç veri eklendiğini görebiliriz. 

# birden fazla kayıt ekleme
# values = [
#             ("IPhone 17",100000,"4.jpg","iyi bir telefon"),
#             ("IPhone 18",110000,"5.jpg","iyi bir telefon"),
#             ("IPhone 19",120000,"6.jpg","iyi bir telefon"),
# ]

# cursor.executemany(sql,values) # birden fazla kayıt için executemany
# db.commit() # artık sorgu veri tabanına gönderilir / bu yapılmazsa veri tabanında değişiklik gözükmez
# print(cursor.rowcount, "kayıt edildi")

values = [
            ("Samsung S23",80000,"7.jpg","iyi bir telefon"),
            ("Samsung S24",90000,"8.jpg","iyi bir telefon"),
            ("Samsung S25",95000,"9.jpg","iyi bir telefon"),
]

cursor.executemany(sql,values) # birden fazla kayıt için executemany

# hatalar oluşabilir
try:
    db.commit()
    print(cursor.rowcount, "kayıt edildi")
    print(f"son eklenen kaydın id: {cursor.lastrowid}")
except mysql.connector.Error as err:  # msql ile iligli bir hata 
    print("hata:", err)
finally:
    cursor.close()
    db.close()
    print("bağlantı kapatıldı")

print(cursor.rowcount, "kayıt edildi")