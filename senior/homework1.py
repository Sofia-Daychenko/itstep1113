бали=int(input("Введіть кількість балів: "))
if 0 <= бали <= 49:
    print("Незадовільно")
elif 50 <= бали <= 69:
    print("Задовільно")
elif 70 <= бали <= 89:
    print("Добре")
elif 90 <= бали <= 100:
    print("Відмінно")