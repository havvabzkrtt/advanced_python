
class MyNumbers:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):   # iterable özelliği kazandırıyoruz
        return self
    
    # bizim oluşturduğumuz veri tipine(class), iterator özelliği tanımlamazsak hata alırız

    def __next__(self):   # bize hangi elemanları geriye getireceğini belirleri
        if self.start <= self.stop:
            x = self.start
            self.start += 1
            return x
        else: 
            raise StopIteration    # elemanların bittiğini anlamış oluruz
    

iterator = iter(MyNumbers(20,30))

while True:
    try:
        print(next(iterator))
    except StopIteration:
        break 


# print(iterator)
# print(next(iterator))

# for i in MyNumbers(20,30):
#     print(i)



print("----------------------")



class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            value = self.data[self.index]
            self.index += 1
            return value
        raise StopIteration

# Kullanımı:
my_iter = MyIterator([10, 20, 30])
for value in my_iter:
    print(value)


# yukarıda önce for döngüsü çalışırsa bu while döngüsü çalışmaz, çünkü iterableda değer kalmadı
"""
while True:
    try:
        print(next(my_iter))
    except StopIteration:
        break 
"""
