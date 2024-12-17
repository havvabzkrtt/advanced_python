
# class => sınıf
class CartItem:
    # constructor => yapıcı metot

    # class attributes
    discount_rate = 0.8
    item_count = 0

    def __init__(self, name, price, quantity):
        # instance attributes
        self.name = name
        self.price = price 
        self.quantity = quantity
        CartItem.item_count += 1
    
    # instance methods
    def calculate_total(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * CartItem.discount_rate

# instance => nesne, örnek
item1 = CartItem("Telefon", 50000, 2)
item2 = CartItem("Bilgisayar", 70000, 1)
item3 = CartItem("kitap", 200, 2)
item4 = CartItem("kitap", 200, 2)

print(item1.__dict__)  # {'name': 'Telefon', 'price': 50000, 'quantity': 2}
print(item2.__dict__)  # {'name': 'Bilgisayar', 'price': 70000, 'quantity': 1}
print(item3.__dict__)  # {'name': 'kitap', 'price': 200, 'quantity': 2}
print(CartItem.__dict__)  # {'__module__': '__main__', 'discount_rate': 0.8, 'item_count': 4, '__init__': <function CartItem.__init__ at 0x000001CB8686E0C0>, 'calculate_total': <function CartItem.calculate_total at 0x000001CB8686D120>, 'apply_discount': <function CartItem.apply_discount at 0x000001CB8686ED40>, '__dict__': <attribute '__dict__' of 'CartItem' objects>, '__weakref__': <attribute '__weakref__' of 'CartItem' objects>, '__doc__': None}

print(CartItem.item_count) # 4 

item1.apply_discount()
print(item1.calculate_total()) # 80000.0

item2.apply_discount()
print(item2.calculate_total())  # 56000.0

item3.apply_discount()
print(item3.calculate_total())  # 320.0





