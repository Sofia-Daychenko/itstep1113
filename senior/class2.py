'''
class People:
    def __init__(self,name="Passenger",age=None):
        self.name=name
        self.age=age
class Bus:
    def __init__(self,model):
        self.model=model
        self.passenger=[]
    def add(self,human):
        self.passenger.append(human)
    def info(self):
        if self.passenger!=[]:
            print("Автобус(",self.model,") має пасажирів:")
            for i in self.passenger:
                print(i.name)
        else:
            print("Автобус(", self.model, ") немає пасажирів:")

p1=People('Petro',12)
p2=People('Katy',10)
b1=Bus("Marsedes")
b1.add(p1) #взаємо зв'язок між класами
b1.add(p2)
b1.info()
'''

import random
class Human:
    def __init__(self,name,job,home,car):
        self.name=name
        self.job=job
        self.home=home
        self.car=car
    def getHome(self):
        pass
    def getJob(self):
        pass
    def getCar(self):
        pass
    def repairCar(self):
        pass
    def indexDay(self,day):
        pass
    def isLvLife(self): # стан людини
        pass
    def life(self): # рівень життя
        pass

class Auto:
    def __init__(self,model_list):
        self.model=random.choice(list(model_list)) # випадкова модель (колір, рік, об'єм двигуна)
        self.color=model_list[self.model]["колір:"]
        self.year = model_list[self.model]["рік:"]
        self.obm = model_list[self.model]["об'єм двигуна:"]

class Work:
    def __init__(self,job_list):
        self.job=random.choice(list(job_list))
        self.exp=job_list[self.job]["стаж:"]
        self.lv = job_list[self.job]["рівень:"]
        self.salary = job_list[self.job]["зп:"]

class House:
    def __init__(self):
        self.food=0

#словник dict() -> перетворити в список list()
modelCar={
    "volkswagen":{"колір:":"білий","рік:":2022,"об'єм двигуна:":1.6},
    "BMW":{"колір:":"чорний","рік:":2020,"об'єм двигуна:":2},
    "Hunda":{"колір:":"сірий","рік:":2024,"об'єм двигуна:":2.2}
}
jobHuman={
    "Розробник Python":{"стаж:":5,"рівень:":"Senior","зп:":3500},
    "веб-дизайнер":{"стаж:":3,"рівень:":"Middle","зп:":6500},
    "системний адміністратор":{"стаж:":10,"рівень:":"Senior","зп:":4000}
}