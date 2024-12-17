# DictReader objesi aracılığıyla CSV dosyası okuma
import csv

csv_path = "C:/Users/havva/OneDrive/Desktop/advanced_python/CSV_Files/urunler.csv"

with open(csv_path) as file:
    csv_reader = csv.DictReader(file, delimiter=",") # veriler , ile ayrılır 
    for i in csv_reader:
        if i["Category"] == "Telefon" and float(i["Rating"]) >= 4.5:
            print(i["ProductName"], i["Price"])