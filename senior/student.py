#симулятор життя студента
import random as r
class Student:
    def __init__(self,name):
        self.name=name
        self.progress=0 #100
        self.lvLife=True
        self.mood=50 #100
        self.money = 50  #початкові гроші

    def work(self):
        print("Час для роботи")
        self.progress+=r.randint(3,10)
        self.mood-=r.randint(1,7)
        self.money+=r.randint(1000,5000)

    def study(self): #методи класу
        print("Час для навчання")
        self.progress+=r.randint(3,10)
        self.mood-=r.randint(1,7)

    def sleep(self):
        print("Час для сну")
        self.mood+=r.randint(1,7)

    def chill(self):
        print("Час для відпочинку")
        self.mood+=r.randint(3, 10)
        self.progress-=r.randint(1,7)
        self.money-=r.randint(1,100)

    def isLvLife(self):
        if self.progress<4:
            print('Ймовірність виключення із закладу')
            self.lvLife=False
        elif self.progress<9:
            print('Підготовка до сесії\nБезсонні ночі')
            self.lvLife=False
        elif self.progress<13:
            print('Екзамен екстерном\nЗбільшення часу на відпочинок')
            self.lvLife=False

    def everyday(self):
        print("Успішність:", self.progress,"\nНастрій:",self.mood,"\nГроші:",self.money,"\033[32m")

    def lifeStud(self,day):
        day="\033[34mДень №"+str(day)+"\033[0m"
        print(day)
        rnd=r.randint(1,3)
        if rnd==1:
            self.study()
        elif rnd==2:
            self.sleep()
        elif rnd==3:
            self.chill()
            self.everyday()
            self.isLvLife()

    def Stud(self):
        if self.money < 10:
            print("Недостатньо грошей, час для роботи")
            self.work()
        elif self.progress < 2:
            print("Провал в навчанні, час для навчання")
            self.study()
        elif self.mood < 15:
            print("Поганий настрій, час для відпочинку")
            self.chill()

st1=Student("Sofia")
# print(st1.name, "Успішність:", st1.progress, st1.lvLife, "Настрій:", st1.mood)
print("\033[44mСтуденське життя:", st1.name,"\n\033[0m")#30-37 колір тексту, 40-47 колір фону
for i in range(1,365):
        if st1.lvLife==False:
            break
        st1.lifeStud(i)

st2=Student("Marina")
# print(st1.name, "Успішність:", st1.progress, st1.lvLife, "Настрій:", st1.mood)
print("\n\n\033[44mСтуденське життя:", st2.name, "\n\033[0m")#30-37 колір тексту, 40-47 колір фону
for i in range(1,365):
        if st2.lvLife==False:
            break
        st2.lifeStud(i)