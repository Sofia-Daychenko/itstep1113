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
+b1=Bus("Marsedes")
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
        self.money=1000
        self.satiety=50
        self.happy=50

    def getHome(self):
        self.home=House()
    def getJob(self):
        if self.car and self.car.drive():
            self.job=Work(jobHuman)
    def getCar(self):
        self.car=Auto(modelCar)
    def repairCar(self):
        self.money.random.randint(100,700)
        self.car.strenght+=random.randint(10,50)
    def workHuman(self):
        if self.car and self.car.drive():
            print("Автомобіль справний... Вчасно будете на роботі")
            self.money+=self.job.salary
            self.satiety-=random.randint(2,10)
            self.happy-=random.randint(5,10)
        else:
            print("Автомобіль не справний... Вчасно бути на роботі не вийде")
            self.repairCar()
    def indexDay(self,day):
        print('День №',day,self.name,'рабочого тижня')
        print('Кошти:',self.money,'\nРівень ситості:',self.satiety,'\nРівень щастя:', self.happy)
        print('Рівень їжі в будинку:',self.home.food,'\nРівень забрудненості в будинку:',self.home.mess)
        print(self.car.model,'\nПаливо:',self.car.fuel,'\nМіцність:',self.car.strenght)

    def isLvLife(self): # стан людини
        if self.happy<=0:
            print('Депресія...')
            return
        elif self.satiety<=0:
            print('Голодний')
        elif self.money<=-100:
            print('Банкрут...')
            return False
        return True
    def life(self,day): # рівень життя
        if not self.isLvLife():
            return False
        if not self.home:
            self.getHome()
            print(self.name,'має гарний будинок')
        if not self.car:
            self.getCar()
            print(self.name,'має ато модель')
        if not self.job:
            self.getJob()
            print(self.name,'має роботу',self.job.jobH,'зарплатня:',self.job.salary)
        self.indexDay(day)
        rnd=random.randint(1,4)
        if self.satiety<25:
            print('Хочу їсти')
        elif self.happy<25:
            if self.home.mess<15:
                print('Прибрати будинок')
                self.claerHouse()
            else:
                print('Можно відпочити')
                self.chill()
        elif self.money<=0:
            print('Треба попрацювати')
            self.workHuman()
        elif self.car.strenght<15:
            print('Потрібно відремонтувати авто')
            self.repairCar()
        if rnd==1:
            self.chill()
        elif rnd==2:
            self.workHuman()
        elif rnd==3:
            self.repairCar()
        else:
            self.claerHouse()



    def chill(self):
        print(self.name,'Час на відпочинок')
        self.happy+=random.randint(10,50)
        self.satiety-=random.randint(2,10)
    def claerHouse(self):
        self.happy -= random.randint(5, 10)
        self.home.mess=max(0,self.home.mess-25)
    def shopping(self,item):
        if self.money<10:
            print(self.name,'бракує коштів для шопінгу')
            return
        if item=='Їжа':
            self.home.food+=random.randint(1,100)
        elif item=='Речі':
            self.happy+=random.randint(10,50)
        self.money-=random.randint(100,500)
        self.money=max(self.money,-100)

class Auto:
    def __init__(self,model_list):
        self.model=random.choice(list(model_list)) # випадкова модель (колір, рік, об'єм двигуна)
        self.color=model_list[self.model]["колір:"]
        self.year = model_list[self.model]["рік:"]
        self.obm = model_list[self.model]["об'єм двигуна:"]
        self.fuel=random.randint(1,100)
        self.strenght=random.randint(1,100)

    def drive(self):
        if self.fuel>0 and self.strenght>0:
            self.fuel-=self.obm*10
            self.strenght-=random.randint(1,10)
            return True
        else:
            print("Авто не може рушити з місця")
            return False

class Work:
    def __init__(self,job_list):
        self.jobH=random.choice(list(job_list))
        self.exp=job_list[self.jobH]["стаж:"]
        self.lv=job_list[self.jobH]["рівень:"]
        self.salary=job_list[self.jobH]["зп:"]

class House:
    def __init__(self):
        self.food=50
        self.mess=0

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
persona=Human("Дмитро",None,None,None)
for day in range(1,8):
    if not persona.life(day):
        break