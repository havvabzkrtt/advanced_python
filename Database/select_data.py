import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "...",
    database = "shopdb"
)

cursor = db.cursor()

# sql = "SELECT * FROM products"  # bütün tabloyu getirir
# cursor.execute(sql)
 
# products = cursor.fetchall() # bütün kayıtları getirir
# for p in products:
#     print(p)


print("-----------")
# for p in products:
#     print(p[0], p[1])

sql = "SELECT id,name FROM products"  # tablodaki id ve name sütunlarını getirir

cursor.execute(sql)
 
# product = cursor.fetchone()  # ilk bulunan kayıtı getirir
# print(product)  # (1, 'Samsun S25')
print("-------")
products = cursor.fetchall() # bütün kayıtları getirir / kaldığı yerden devam eder
for p in products:
    print(p[0], p[1])  


 
