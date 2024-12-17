import mysql.connector

db = mysql.connector.connect(
    host = "localhost",  # şuanda local ir server, uzak bir serverde mysql hizmeti alınıyorsa o severın adresi girilmeli
    user = "root",
    password = "...",  # root şifresi
    database = "shopdb"  # serverdaki istenilen database bağlanılır
)

print(db)  # bir obje dönüyorsa başarılı bir bağlantı yapılmıştr
# <mysql.connector.connection_cext.CMySQLConnection object at 0x0000016CB9661370>

cursor = db.cursor() # bir sorgu oluşturmak için önce bir cursor oluşturulmalı

# cursor.execute("CREATE DATABASE exampledb")  # server üzerinde database oluşturma sripti
# cursor.execute("SHOW DATABASES")  # serverdaki databaseleri gösterme scripti

# for i in cursor:
#     print(i)  # sever üzerindeki o anki databaseleri döndürür

cursor.execute("CREATE TABLE categories2 (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))")  # yeni bir tablo oluşturma scripti
cursor.execute("SHOW TABLES")  # tabloyu gösterme

for i in cursor:
    print(i)
