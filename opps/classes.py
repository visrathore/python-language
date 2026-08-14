class Factory: 
    name= "Vishal" #class attribute
    def __init__(self, material, zip, pockets):
        self.material = material # instance attribute
        self.zip = zip
        self.pockets = pockets

    def show(self): # points to current object
        print(f"Your details are {self.material}, {self.zip}, {self.pockets}, {self.name}")

    @classmethod # points to only class
    def hello(cls):
        print(f"How are you brother?")

    @staticmethod # Points to no one - class or object
    def static():
        print("How are you?")

rebook = Factory('Leather', 3, 2)
rebook.show()