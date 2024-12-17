import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "...",
    database = "shopdb"
)

cursor = db.cursor()

# sql = "SELECT name,categoryid FROM products"
# sql = "SELECT name FROM categories"

# INNER JOIN ifadesi kullanarak iki tablo arasında bir ilişki kurar ve her iki tablodan seçilen sütunları birleştirerek sonuç döndürür. 
# sql = "SELECT products.name,categories.name from products inner join categories on products.categoryid=categories.id"

# sql = "SELECT p.name,c.name from products p inner join categories c on p.categoryid=c.id"
# sql = "SELECT p.name,c.name from products p inner join categories c on p.categoryid=c.id WHERE c.name='Bilgisayar'"  # sadecde Bilgisayarlar

# sql = "SELECT products.name AS product_name, categories.name AS category_name FROM products LEFT JOIN categories ON products.categoryid = categories.id"
# LEFT JOIN, sol (ilk belirtilen) tablodaki tüm satırları döndürür ve sağ tablodaki eşleşmeyenler için NULL döndürür.

sql = "SELECT products.name AS product_name, categories.name AS category_name FROM products RIGHT JOIN categories ON products.categoryid = categories.id"
# RIGHT JOIN, sağ (ikinci belirtilen) tablodaki tüm satırları döndürür ve sol tablodaki eşleşmeyenler için NULL döndürür.
cursor.execute(sql)

result = cursor.fetchall()

print(result)
