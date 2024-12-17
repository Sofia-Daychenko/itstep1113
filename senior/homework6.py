class animals:
    def __init__(self, name, age, color):
        self.name=name
        self.age=age
        self.color=color
    def info(self):
        print("Вітаю! Це", self.name, "Йому/Їй:", str(self.age), "років", "Окрас", self.color)

class Dog(animals):
    def __init__(self, name, age, color,weight):
        super().__init__(name,age,color)
        self.weight=weight
    def Weight(self):
        return self.name +("Він/вона важить:")+str(self.weight)+"кг"

class Cat(animals):
    def __init__(self, name, age,color,coloreyes):
        super().__init__(name, age, color)
        self.coloreyes=coloreyes
    def eyes(self):
        return self.name +("Очі:")+str(self.coloreyes)+"колір"

a1=animals("Мурка", 4, "Сіро-білий")
a1.info()
d1=Dog("Бублік", 8, "Чорний", 4)
print(d1.Weight())
d1.info()
c1=Cat("Еш",3,"Сірий","Жовтий")
print(c1.eyes())
c1.info()



class Vehicle:
    def __init__(self,name,speed,move):
        self.name=name
        self.speed=speed
        self.move=move
    def info(self):
        print(self.name, "Має швидкість:", self.speed, "переміщення:", self.move)

class plain(Vehicle):
    def __init__(self,name,speed,move,size):
        super() .__init__(name,speed,move)
        self.size=size
    def Size(self):
        return self.name + (" Розмір:")+str(self.size)

class motorbike(Vehicle):
    def __init__(self,name,speed,move,color):
        super() .__init__(name,speed,move)
        self.color=color
    def Color(self):
        return self.name + (" Колір:")+str(self.color)

V1=Vehicle("Машина",240,None)
V1.info()
p1=plain("Літак", 740, None, " 5*4*30")
print(p1.Size())
p1.info()
m1=motorbike("Мотоцикл",80,None," Фіолетовий")
print(m1.Color())
m1.info()

