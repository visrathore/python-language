# Method Overriding Python -> 2 method with same in classes. instance of child obj method will run only

class Animal:
    def show(self):
        print("Vishal")

class Human(Animal):
    def show(self):
        print('Shikha')

h = Human()
h.show()