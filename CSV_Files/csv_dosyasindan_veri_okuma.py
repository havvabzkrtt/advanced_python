# with open("urunler.csv") as file:
#     print(file.read())

import csv
import os
print("Current working directory:", os.getcwd())
csv_path = "C:/Users/havva/OneDrive/Desktop/advanced_python/CSV_Files/urunler.csv"
with open(csv_path) as file:
    csv_reader = csv.reader(file)
    print(csv_reader)
    # liste = list(csv_reader)
    # print(liste[1])
    next(csv_reader)
    for i in csv_reader:
        if i[3] == "True":
            print(f"id: {i[0]}, ürün adı: {i[1]}")

# DictReader