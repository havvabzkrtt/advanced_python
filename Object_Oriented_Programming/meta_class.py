# meta class lar genellikle alt seviye kod yazımında kullanılır, örneğin kütüphane veya framework yazımında


class Test():
    pass

sonuc = Test()
print(sonuc) # <__main__.Test object at 0x000001DE427BDCA0>

sonuc = Test
print(sonuc)  # <class '__main__.Test'>

sonuc = type(Test)
print(sonuc) # <class 'type'>

sonuc = type(2)
print(sonuc)  # <class 'int'>

sonuc = type(int)
print(sonuc)  # <class 'type'>

sonuc = type("2")
print(sonuc)  # <class 'str'>

sonuc = type(str)
print(sonuc)  # <class 'type'>

# Test sınıfının temel alabileceği bir sınıf oluşturulım
class BaseClass():
    def show(self):
        return "merhaba"

Test = type("Test", (BaseClass,), {})  # Test sınıfnın temel alabileceği sınıflar bu şekilde eklenir, biden fazla olabilir
t = Test()

sonuc = t.show()
print(sonuc)  # merhaba


def add_attribute(self):
    self.b = 10

Test = type("Test", (BaseClass,), {"a":5, "add_attribute": add_attribute}) # attributelar tanımlanabilir
t = Test()

sonuc = t.a
t.add_attribute()
sonuc = t.b
print(sonuc)  # 10



print("---------------------")


class Meta(type):  # type sınıfnı base olarak alır
    def __new__(self, class_name, bases, attrs):
        print(attrs)

        a = {}

        for name, val in attrs.items():
            if name.startswith("_"):
                a[name] = val
            else:
                a[name.upper()] = val

        return type(class_name, bases, a)

class Person(metaclass=Meta):
    x = 5
    y = 10
    _age = 40

    def hello(self):
        print("merhaba")

p = Person()  # {'__module__': '__main__', '__qualname__': 'Person', 'x': 5, 'y': 10, '_age': 40, 'hello': <function Person.hello at 0x000001FFA81BEE80>}

sonuc = p.X 
print(sonuc)  # 5 

sonuc = p.Y
print(sonuc) # 10

sonuc = p._age
print(sonuc)  # 40