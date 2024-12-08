class Car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    def get_info(self):
        return f"{self.year} {self.make} {self.model}"

car=Car("Toyota", "Camry", 2020)
car2=Car("Infiniti","fx35",2024)
car3=Car("Audi","q8",2023)
print(car.get_info())
print(car2.get_info())
print(car3.get_info())

