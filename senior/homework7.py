result = []

def number(a, b):
    if b == 0:
        raise ZeroDivisionError("Ділити на 0 не можна")
    if a < b:
        raise ValueError("Перше число менше за друге")
    if b > 100:
        raise IndexError("Друге число більше 100")
    return a / b

while True:
    try:
        key = input("Введіть перше число (a): ")
        key = int(key)
        value = int(input("Введіть друге число (b): "))
        res = number(key, value)
        print(f"Результат ділення: {res}")
        result.append(res)
    except ValueError:
        print('Помилка!! Перше число не повинно бути менше за друге')
    except ZeroDivisionError:
        print('Помилка!! Ділити на 0 не можна')
    except IndexError:
        print('Помилка!! Друге число не повинно бути більше 100')