# a => public access
# _a => protected access (No use in python)
# __a => private access (Cannot be accesses in child or by instance of class)
# Encapsulation is achieved by access modifiers - public, protected, private

class Factory:
    __a = "Pune"

    def show(self):
        print(self.__a);
        print(Factory.__a);

obj = Factory()
obj.show()