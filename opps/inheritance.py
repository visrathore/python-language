# Single inheritance

class Animal:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"Your name is {self.name}")

class Human(Animal):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def show(self):
        print(f"Your name is {self.name}, {self.age}")

p1 = Human('Vishal', 25)
p1.show()


# Multiple Inheritance - 2 parent and 1 child class

class Parent1:
    name1= 'Hanuman'

class Parent2:
    name2 = "Spider Man"

class Child(Parent1, Parent2):
    name3= "Superman"

obj = Child()
print(obj.name1)

# Multi-level inheritance

class Factory:
    def __init__(self, material, zips):
        self.material = material
        self.zips = zips

class BhopalFactory(Factory):
    def __init__(self, material, zips, color):
        super().__init__(material, zips)
        self.color = color

class PuneFactory(BhopalFactory):
    def __init__(self, material, zips, color, pockets):
        super().__init__(material, zips, color)
        self.pockets = pockets

