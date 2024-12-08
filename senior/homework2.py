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

class Employee:
    def __init__(self,name,position,salary):
        self.name=name
        self.position=position
        self.salary=salary
    def get_salary_info(self):
        return f"Заробітна плата {self.name}: {self.salary}"
employee = Employee("Марія", "Програміст", 3900)
employee2 = Employee("Олег", "Головний відділу", 5500)
employee3 = Employee("Василь", "Веб-дизайнер", 2300)
print(employee.get_salary_info())
print(employee2.get_salary_info())
print(employee3.get_salary_info())