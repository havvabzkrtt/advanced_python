# iterable : 
# iterator : 

sayilar = [1,2,3,4,5,6]

# sayilar bir iterable nesnedir; nesnenin elemanları üzerinde tek tek dolaşılabilir

for i in sayilar:
    print(i)

print("--------------------")

# for döngüsü iterable olan neseneyi, iteratöre çevirme işlemini arka tarafta kendi yapar

# iterable nesnelerinde "dir()" fonksiyonu çalıştırıldığında içerisinde "iter" metodunun bulunduğu görülür
# her tanımlanan tip iter metodunu içermez, biz kendimiz tanımlayabiliriz

# for döngüsü yerine 
iterator = iter(sayilar)  # iterable nesneden iter metodu ile iteratör haline getiriyoruz

while True:
    try:
        sayi = next(iterator)  # next metoduna sadece iteratör nesnesi üzerinden çalışır
        print(sayi)
    except StopIteration:
        break

# print(next(iterator))
# s = "BTK AKADEMİ"
# a = 10 # int objesi iterable değildir, for döngüsünde a içerisinde dolaşılamaz


# for i in a:
#     print(i)


print("--------------------")

# 1. Iterable (Yinelenebilir):

"""
- Bir nesne, Python'da üzerinde döngü yapmaya uygun şekilde tasarlanmışsa iterable olarak adlandırılır.
- Örnekler: Listeler, demetler (tuples), stringler, sözlükler, kümeler gibi koleksiyon veri tipleri.
- Teknik olarak, bir nesne, iter() fonksiyonu çağrıldığında bir iterator döndürebiliyorsa iterable'dır.

Özellikleri:
- Döngü ile (for döngüsü gibi) tekrarlanabilir.
- iter() fonksiyonu ile bir iterator elde edilebilir.
"""

my_list = [1, 2, 3]
iterator = iter(my_list)  # Iterable'dan bir iterator oluşturulur.



# 2. Iterator (Yineleyici):

"""
- Iterator, Python'da üzerinde bir defada bir öğe olacak şekilde gezinilebilen bir nesnedir.
- next() fonksiyonu ile bir sonraki öğe alınır. Öğeler tükendiğinde StopIteration hatası fırlatır.
- Teknik olarak bir nesne, __next__() ve __iter__() metodlarını tanımlıyorsa iterator'dır.

Özellikleri: 
- Tek seferlik kullanılabilir. Öğeler tüketildikten sonra yeniden başlamak için yeni bir iterator oluşturmanız gerekir. 
- iter() fonksiyonu çağrıldığında kendisini döndürür.
"""

iterator = iter([1, 2, 3])  # Listeyi bir iterator'a dönüştürüyoruz.

print(next(iterator))  # 1
print(next(iterator))  # 2
print(next(iterator))  # 3
# print(next(iterator))  # StopIteration hatası