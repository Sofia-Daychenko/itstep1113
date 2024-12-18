'''
class Task:
    def __init__(self, title, des, deadline):
        self.title = title
        self.des = des
        self.deadline = deadline
        self.mill = False

    def millTrue(self):
        self.mill = True

    def display(self):
        status = "Виконано" if self.mill else "Не виконано"
        return f"Завдання: {self.title}\nОпис: {self.des}\nДедлайн: {self.deadline}\nСтан: {status}\n"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add(self, title, des, deadline):
        task = Task(title, des, deadline)
        self.tasks.append(task)
        print(f"Завдання '{title}' додано.")

    def remove(self, title):
        for task in self.tasks:
            if task.title == title:
                self.tasks.remove(task)
                print(f"Завдання '{title}' видалено.")
                return
        print(f"Завдання '{title}' не знайдено.")

    def completed(self, title):
        for task in self.tasks:
            if task.title == title:
                task.millTrue()
                print(f"Завдання '{title}' відмічено як виконане.")

    def list(self):
        if self.tasks:
            print("Список завдань:")

manager = TaskManager()

manager.add("Теорія", "Записати класну роботу в зошит", "2024-12-31")
manager.add("Зробити домашнє завдання", "Завершити задачі з математики", "2024-12-20")
manager.list()
manager.completed("Теорія")
manager.list()
manager.remove("Зробити домашнє завдання")
manager.list()
'''
import random

class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def display(self):
        return f"Ім'я: {self.name}, Посада: {self.position}, Зарплата: {self.salary} грн"


class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add(self, employee):
        self.employees.append(employee)
        print(f"Співробітник {employee.name} додано до відділу {self.name}.")

    def remove(self, name):
        for employee in self.employees:
            if employee.name == name:
                self.employees.remove(employee)
                print(f"Співробітника {name} видалено з відділу {self.name}.")

    def calculate(self):
        total_salary = 0
        for employee in self.employees:
            total_salary += employee.salary
        monthly_values = [
            random.randint(5900, 10000),
            random.randint(3360, 8900),
            random.randint(5800, 13000),
            random.randint(6700, 15000),
            random.randint(3400, 10000),
            random.randint(2600, 5200),
            random.randint(3500, 9000),
            random.randint(6900, 10100),
            random.randint(2000, 4900),
            random.randint(7500, 9100),
            random.randint(8730, 12058),
            random.randint(10000, 18000)
        ]

        total_sum = sum(monthly_values)
        total_salary += total_sum

        print(f"Загальна сума зарплат співробітників за рік: {total_salary} $")
        return total_salary

    def list(self):
        if self.employees:
            print(f"Список співробітників у відділі {self.name}:")
            for employee in self.employees:
                print(employee.display())

it_department = Department("ІТ")
emp1 = Employee("Іван Іваненко", "Програміст", 9000)
emp2 = Employee("Олена Петрівна", "Тестувальник", 5000)
it_department.add(emp1)
it_department.add(emp2)
it_department.list()
it_department.remove("Олена Петрівна")
it_department.list()
it_department.calculate()