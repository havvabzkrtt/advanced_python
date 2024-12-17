import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "havvabzkrt41",
    database = "shopdb"
)

cursor = db.cursor()

# sql = "DELETE FROM products WHERE id=2"  # id'si 2 olan kayıt silinir
# cursor.execute(sql) 
# db.commit()

def deleteProductById(id):
    sql = "DELETE FROM products WHERE id=%s"  # id değerine göre kayıt silinir
    params = (id,)
    # sql = "DELETE FROM products WHERE name LIKE '%s23%'"  # belli bir aramaya göre de kayıt silinebilir / name datasında "s23" geçen kayıtlar silinir
    cursor.execute(sql, params)

    try:
        db.commit()
        print(f"{cursor.rowcount} tane kayıt silindi")
    except mysql.connector.Error as err:
        print(err)
    finally:
        db.close()
        cursor.close()

deleteProductById(3)