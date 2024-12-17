# class => sınıf

class CartItem:
    # constructor => yapıcı metot
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

# self: nesne isimlerine denk gelir 

# CartItem classı ile nesneler oluşturuldu
item1 = CartItem("Telefon", 50000, 2)
item2 = CartItem("Bilgisayar", 70000, 1)
item3 = CartItem("kitap", 200, 2)


 
print(item1.name)  # Telefon
print(item2.price)  # 70000
print(item3.quantity) # 2

print(item1)  # <__main__.CartItem object at 0x000001BA013AD430>   
