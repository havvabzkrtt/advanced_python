def double(fn):
    def inner(*args, **kwargs): # değişken sayıda parametre ve sözlük veri yapısı gönderilebilir veya hiç gönderilmeyebilir
        # fn(*args, **kwargs) # ikişer defa yazdırılabilir
        return fn(*args, **kwargs)
    return inner

@double
def merhaba():
    print("merhaba")

@double
def selam(isim):
    print("selam ", isim)

@double
def iyigunler():
    return "iyi günler"

merhaba()
# merhaba 
# merhaba 

selam("Ali")
# selam  Ali
# selam  Ali

print(iyigunler())
# iyi günler