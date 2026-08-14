from abc import ABC, abstractmethod

class abstract(ABC): # Whichever class inherit abstract class it should create same method as abstract otherwise it sill give errors
    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass

class Circle(abstract):
    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        print("Perimeter")

    def area(self):
        print('Area')

obj = Circle(8)
obj.perimeter()