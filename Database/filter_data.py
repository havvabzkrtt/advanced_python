import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "havvabzkrt41",
    database = "shopdb"
)

cursor = db.cursor()

# sql = "SELECT * from products WHERE id=1"   # id'si 1 olan kayıt getirilir
# result = cursor.fetchone()
# sql = "SELECT * from products WHERE id>=1"  # id 1'den büyük olan kayıtlar getirilir
# sql = "SELECT * from products WHERE name='Samsung S25'"
# sql = "SELECT * from products WHERE name='Samsung S25' and price=50000" 
# sql = "SELECT * from products WHERE name='Samsung S25' or price=50000"
# sql = "SELECT * from products WHERE name='Samsung S25' or price=50000"
# sql = "SELECT * from products WHERE name='Samsung S25' or price=50000"
# sql = "SELECT * from products WHERE name LIKE '%Samsung%'"  # name sütunundaki data %Samsung% şeklinde(Samsung kelimesinin geçmesi) ise getirilir
# sql = "SELECT * from products WHERE name LIKE 'Samsung%'"  # Samsung ile başlayan kayıtlar
# sql = "SELECT * from products WHERE name LIKE '%Samsung'"  # Samsung ile biten kayıtlar
sql = "SELECT * from products WHERE name LIKE '%Samsung%' or description LIKE '%iyi%'" # name sütunundaki data %Samsung% şeklinde veya description sütunundaki data %iyi% şekilde ise getirilir

cursor.execute(sql)

result = cursor.fetchall()

for p in result:
    print(p)

print("-----------")

# dinamik bir sorgu fonksiyonu
def getProductById(id):
    sql = "SELECT * from products WHERE id=%s"  # istenilen id ye sahip kayıt getirilir
    params = (id,)
    cursor.execute(sql,params)
    result = cursor.fetchall()
    print(result)

getProductById(3)
getProductById(7)

# dinamik bir sorgu fonksiyonu
def getPriceNameById(id):
    sql = "SELECT name, price from products WHERE id=%s"  # istenilen id ye sahip kayıt getirilir
    params = (id,)
    cursor.execute(sql,params)
    result = cursor.fetchall()
    for i in result:
        name = i[0]
        price = i[1]
    print(f"{id} id'li ve {name} adlı ürünün fiyatı {price} TL'dir.")
    # print(result)

id_valuse = input("Fiyatını merak ettiğiniz ürünün id'sini giriniz: ")
getPriceNameById(id_valuse)