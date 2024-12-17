class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        print("person sınıfı türetildi.")

    def intro(self):
        print(self.name, self.surname, self.age)

class Student(Person):
    def __init__(self, name, surname, age, number):
        super().__init__(name, surname, age)  # temel sınftaki özellikleri set ediyoruz
        self.number = number 
        print("student sınıfı türetildi.")    

    def study(self):
        print(f"{self.name} ders çalışıyor.")

    # Temel sınıfta üretilen metotlar child sınıfta tekrar üretilirse eziliyor, yani artık child sınıfınnın nesnesi için ilgili metot için child sınıfında üretilen kullanılır
    def intro(self):
        print(self.name, self.surname, self.age, self.number)

class Teacher(Person):
    def __init__(self, name, surname, age, branch):
            super().__init__(name, surname, age)  # temel sınftaki özellikleri set ediyoruz
            self.branch = branch
            print("teacher sınıfı türetildi.") 

    def teach(self):
         print(f"{self.name} {self.branch} dersi anlatıyor.") 

p1 = Person("Sadık","Turan", 40)
p1.intro()

s1 = Student("Çınar","Turan",7, 105)
s1.intro() # Çınar Turan 7 105
s1.study()  # Çınar ders çalışıyor.
print(s1.number) # 105

t1 = Teacher("Ali","Korkmaz",35,"fizik")
t1.intro() # Ali Korkmaz 35
print(t1.branch) # fizik
t1.teach()  # Ali fizik dersi anlatıyor.