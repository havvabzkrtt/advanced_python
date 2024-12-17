# class => sınıf
class CartItem:
    # constructor => yapıcı metot
    def __init__(self, name, price, quantity):
        # instance attribues 
        self.name = name
        self.price = price
        self.quantity = quantity
    
    # instance methods
    def calculate_total(self):
        return self.price * self.quantity
    
    # instance methods   
    def apply_discount(self, rate):
        self.price = self.price * rate

# instance => nesne, örnek
item1 = CartItem("Telefon", 50000, 2)
item2 = CartItem("Bilgisayar", 70000, 1)
item3 = CartItem("kitap", 200, 2)

item1.apply_discount(0.8)
print(item1.calculate_total()) # 80000.0

item2.apply_discount(0.7)
print(item2.calculate_total()) # 49000.0

item3.apply_discount(0.9)
print(item3.calculate_total()) # 360.0
 



