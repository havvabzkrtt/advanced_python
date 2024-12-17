class Person: # base class
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        print("person sınıfı türetildi.")

    def intro(self):
        print(self.name, self.surname, self.age)

class Student(Person):  # child class
    # Person sınıfının özellik ve metotoları dışında ekstra özellik ve metotlar eklenebilir
    pass    

class Teacher(Person):  # child class
    # Person sınıfının özellik ve metotoları dışında ekstra özellik ve metotlar eklenebilir
    pass

p1 = Person("Sadık","Turan", 40)
p1.intro() # Sadık Turan 40

s1 = Student("Çınar","Turan",7)
s1.intro()  # Çınar Turan 7

t1 = Teacher("Ali","Korkmaz",35)
t1.intro()  # Ali Korkmaz 35