class CartItem:
    discount_rate = 0.8
    item_count = 0

    @classmethod
    def display_item_count(cls):
        return f"{cls.item_count} tane ürün oluşturuldu."
    
    @classmethod
    def create_item(cls, data_str):
        name, price, quantity = data_str.split(",")
        return cls(name,price,quantity)

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        CartItem.item_count += 1
    
    def calculate_total(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * CartItem.discount_rate


# apply_coupon fonksiyonu için 
class Coupon:
    def __init__(self, code, discount):
        self.code = code
        self.discount = discount

c1 = Coupon("code1", 0.8)
c2 = Coupon("code2", 0.7)
c3 = Coupon("code3", 0.9)
 
item1 = CartItem("Telefon", 50000, 2)
item2 = CartItem("Bilgisayar", 70000, 1)
item3 = CartItem("Kitap", 500, 2)


# CartItem sınıfdan üretilen nesneleri yönetecek olan ShoppingCart class ı tanımlanır 
class ShoppingCart:

    coupon_list = [c1, c2, c3]

    def __init__(self, liste):
        self.liste = liste
        
    def add_item(self, item):
        self.liste.append(item)


    def display_items(self):
        for i in self.liste:
            print(f"{i.name} {i.price}")
        

    def calculate_totals(self):
        return sum([item.price * item.quantity for item in self.liste])
    
    def remove_item(self, cart_item):
        self.liste = [item for item in self.liste if item != cart_item]
        # silincek eleman dışındaki elemanları tekrar göndermek istiyoruz
    
    def clear(self):
        print("Liste boş.")
        self.liste = []

    @classmethod
    def get_coupons(cls):
        return [coupon.code for coupon in cls.coupon_list]
    

    @classmethod
    def get_coupon(cls, code):
        return  next(filter(lambda c: c.code == code, ShoppingCart.coupon_list))
        # liste (ShoppingCart.coupon_list) içerisinde gelen her bir kupon, 
        # yukarıdan gönderilien kod (code) eşitse geriye filtrelenmiş liste gönderilir.
        # next fonksiyonu ile bulunan ilk kupon gönderilir bu şekilde tek nesne alınmış olur.
        # next ile tekrar çağırısak 2. sini ondan sonra tekrar çağırırsak 3. sünü alacak şekilde devam eder.

    def apply_coupon(self, code):
        # geçerli bir kod değilse hata alınır
        if code not in ShoppingCart.get_coupons():
            raise ValueError(f"geçersiz kupon kodu: {code}") # hata 
        
        # geçerli bir kupon ise
        coupon = ShoppingCart.get_coupon(code)

        # her bir ürünün price değeri güncellenir
        for index in range(0, len(self.liste)):
            self.liste[index].price = self.liste[index].price * coupon.discount



sc = ShoppingCart([item1, item2])
sc.display_items()  
"""
Telefon 50000
Bilgisayar 70000
"""  

print("-----------------")
sc.add_item(item3)
sc.display_items()
"""
Telefon 50000
Bilgisayar 70000
Kitap 500
"""
print("-----------------")  

print(sc.calculate_totals()) # 171000

print("-----------------")

sc.remove_item(item1)
sc.display_items()

"""
Bilgisayar 70000
Kitap 500
"""
print(sc.calculate_totals())  # 71000

print("-----------------")
print(sc.calculate_totals())  # 71000
sc.apply_coupon("code1")

sc.display_items() # 56800.0
"""
Bilgisayar 56000.0
Kitap 400.0
"""
print(sc.calculate_totals()) # 56800.0

print("-----------------") 

sc.apply_coupon("code2")  
sc.display_items()

"""
Bilgisayar 39200.0
Kitap 280.0
"""
print(sc.calculate_totals()) # 39760.0

print("-----------------") 
sc.clear()
sc.display_items()  # Liste boş.


print("-----------------") 
print(ShoppingCart.get_coupons()) # ['code1', 'code2', 'code3']
print(ShoppingCart.get_coupon("code1")) # <__main__.Coupon object at 0x0000027E140F8620>

print("-----------------") 