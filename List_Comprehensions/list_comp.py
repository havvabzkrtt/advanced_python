sayilar = []

for i in range(5):
    sayilar.append(i * 2)

print(sayilar)

# list-comp
sayilar2 = [i * 2 for i in range(5)]
print(sayilar2)


kurum = "Btk Akademi"

for i in kurum:
    print(i.upper())

sonuc = [i.upper() for i in kurum]
print(sonuc)

sonuc = ''.join(sonuc).strip()  # Listeyi stringe dönüştürüp boşluğu temizler
print("birlesmiş liste: ", sonuc)



# Geleneksel for döngüsü ile yazılmış hali
words = ["apple", "banana", "cherry"]
lengths = []
for word in words:
    lengths.append(len(word))

print(lengths) # [5, 6, 6]

lengths = [len(word) for word in words]
print(lengths) # [5, 6, 6]