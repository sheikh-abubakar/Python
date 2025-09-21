# class & object

# All classes have a method called __init__(), which is always executed when the class is being initiated.

# this = self
class Car:
    def __init__(self, brand, mymodel):
        #self.brand = brand # accessible to anyone
        self.__brand = brand # private variable
        self.model = mymodel
    
    def __str__(self):
        return f"{self.__brand} {self.model}"

    def get_brand(self):
        return self.__brand + '!'
    
    def output(self):
        return f"{self.__brand} {self.model}" #formatted str
        

c1 = Car("bmw", "corolla")
print(c1) # calls __str__ method

print(c1.get_brand())
# print(c1.brand)
# print(c1.output())
# ---------------------**********************------------------

# inheritance

# Note: Use the pass keyword when you do not want to add any other properties or methods to the class.

class ElectricCar(Car):
    def __init__(self, brand, mymodel, color):
        super().__init__(brand, mymodel) # call the parent class constructor
        self.color = color

tesla = ElectricCar("tesla", "model x", "red")
# print(tesla.output())