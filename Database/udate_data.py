import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "havvabzkrt41",
    database = "shopdb"
)

cursor = db.cursor()

# sql = "UPDATE products SET name='Samsung S25-Udate' WHERE id=1"  # id'si 1 olan ürünün göre name sütunundaki değer güncellenir
# cursor.execute(sql)
# db.commit()


# Dinamil güncelleme sorgusu
def updateProduct(id,name,price):
    sql = "UPDATE products SET name=%s,price=%s WHERE id=%s"  # id'sine göre name ve price sütunalarındaki değerler güncellenir
    params = (name, price, id)

    cursor.execute(sql, params)

    try:
        db.commit()
        print(f"{cursor.rowcount} tane kayıt güncellendi.")
    except mysql.connector.Error as err:
        print(err)
    finally:
        db.close()
        cursor.close()


updateProduct(2,"Samsung S26-updated", 20000)