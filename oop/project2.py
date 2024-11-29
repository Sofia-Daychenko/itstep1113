class Student:
    # print("Hello!, make class")
    def __init__(self,name="Sofia",group="1113",age=14): #self - посилатися на себе на класс
        self.name=name
        self.group=group
        self.age=age

    def __str__(self):
        return("Ім'я студента: "+self.name+"навчається у групі: "+self.group+"вік: "+str(self.age))

st1=Student() #Об'єкт
#print(st1.name,st1.group,st1.age)
st2=Student(name="Egor",group="1113",age=14)
#print(st2.name,st2.group,st2.age)
print(st1)
print(st2)
