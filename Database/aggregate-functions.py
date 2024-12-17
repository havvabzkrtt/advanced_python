# Aggregate Functions (Hesaplama Fonksiyonları)

import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "havvabzkrt41",
    database = "shopdb"
)

cursor = db.cursor()

# sql = "SELECT COUNT(*) FROM products"    # bütün kayıt sayıları, satır toplam sayısı
# sql = "SELECT AVG(Price) FROM products"    # price sütunu ortalaması
# sql = "SELECT SUM(Price) FROM products"  # price sütunu toplamı
# sql = "SELECT MIN(Price) FROM products"  # price sütunu minimum değeri
sql = "SELECT MAX(Price) FROM products"  # price sütunu maksimum değeri
cursor.execute(sql)
result = cursor.fetchone()
print(result) 

# sql = "SELECT name,price FROM products WHERE Price = (SELECT MAX(Price) FROM products)"  # maksimum fiyatlı ürünün ismi ve fiyatı
# sql = "SELECT name,price FROM products ORDER BY price DESC"  # ürün isimleri ve fiyatları azalan şekilde sıralanaral döndürülecek
sql = "SELECT name,price FROM products ORDER BY price DESC LIMIT 1"  # ürünler azalan haldeyken ilki döndürülür
cursor.execute(sql)

result = cursor.fetchall()

print(result)