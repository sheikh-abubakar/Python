class Car:
    def __init__(self, model = "bmw", color = "black"):
        self.__model = model
        self.color = color

    def get_model(self):
        return self.__model

    def set_model(self, model):
        self.model = model
    
    def fuel_type(self):
        return "diesel"
    def __dir__(self):
        return f"{self.__model}"


class ElectricCar(Car):
    def __init__(self, model, color, brand):
        super().__init__(model, color)
        self.brand = brand
    def fuel_type(self):
        return "electric battery"

c1 = Car()
c1.set_model("corolla")
print(c1.get_model())

print("-------------------------------")

e = ElectricCar("model x", "red", "tesla")

c = e

print(c.fuel_type())

c.fuel_type()

print(e.fuel_type())

print(c1.fuel_type())

# @staticmethod->decorators -> does not reuire self parametr
# if we want any attribute do not overirde so use @property decorator
# with the same attribute name as method name 