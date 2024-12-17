#try:
#    n1=int(input('Число №1: '))
#    n2=int(input('Число №2: '))
#    if n1<0 or n2<0:
#        raise TypeError
#    print(n1/n2)
#except ValueError:
#    print('Потрібно вести число!')
#except ZeroDivisionError:
#    print('Ділення на 0 неможливо!')
#except TypeError:
#    print('Потрібно вводити лише додатні числа!')
#except Exception:
#    print('Щось пішло не так..7 Щось ввели не вірно... Помилка 404')
#finally:
#    print('='*10,'END','='*10)



banknota={
    20:'Іван Франко',
    50:'Михайло Грушевський',
    100:'Тарас Шевченко',
    200:'Леся Українка',
    500:'Григорій Сковорода',
    1000:'Володимир Вернадський',
}
ans='1'
while ans=='1':
    try:
        nominal = str(input('Введіть номінал банкноти: '))
        if nominal.isdigit():
            nominal=int(nominal)
            print('На банкноті\033[35m', nominal,'\033[36mзображено видатну людину -',banknota[nominal],"\033[0m")
        else:
            for key, value in banknota.items():
                if value==nominal:
                    print('\033[36m',nominal,'\033[0mзображено на купюрі',key,'\033[0m')
                    break
            else:
                raise ValueError
    except ValueError:
        print('Неіснуяча видатна людина на банкноті')
    except KeyError:
        print('Неіснуюча банкнота')
ans=input('Продовжити програму? \nТак-1, Ні-0')
#try:
#    nominal=int(nominal)
#    print('На банкноті\033[35m', nominal,'\033[36mзображено видатну людину -',banknota[nominal],"\033[0m")
#except ValueError:
#    print('Сталася помилка.. ви ввели не число...')
#except KeyError:
#    print('Неіснучая банкнота')