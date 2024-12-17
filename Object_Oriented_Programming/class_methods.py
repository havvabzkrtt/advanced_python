class CartItem:

    # class attributes 
    discount_rate = 0.8
    item_count = 0

    @classmethod  # decorator
    def display_item_count(cls):  # cls: class ı temsil eder, self gibi
        return f"{cls.item_count} tane ürün oluşturuldu."
    
    @classmethod
    def create_item(cls, data_str):
        name, price, quantity = data_str.split(",")  # data_str adlı listeden gelen elemanlar ayrılır
        return cls(name,price,quantity)

    # constructor method
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        CartItem.item_count += 1
    
    def calculate_total(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * CartItem.discount_rate

print(CartItem.display_item_count())  # 0 tane ürün oluşturuldu.
item1 = CartItem("Telefon", 50000, 2)
item2 = CartItem("Bilgisayar", 70000, 1)
print(CartItem.display_item_count()) # 2 tane ürün oluşturuldu.
item3 = CartItem("kitap", 200, 2)
item4 = CartItem("kitap", 200, 2)

CartItem.create_item("Mouse,800,3") # create_item class metodu ile bir nesen oluşturmuş olduk

print(CartItem.display_item_count())  # 5 tane ürün oluşturuldu.
