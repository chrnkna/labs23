def zadanie_1():
    password1 = input('Введите пароль:')
    password2 = input('Повторите пароль:')
    if password1 == password2:
        print('Пароль принят')
    else:
        print('Пароль не принят')

def zadanie_2():

    number = int(input('Введите номер вашего места: '))

    if number > 30 and number < 60:
        print('Ваше место - боковое')
    elif number < 30 and number > 0:
        print('Ваше место - купе')

    if number % 2 == 0 and number > 0 and number < 60:
        print('Ваше место - верхнее')
    elif number % 2 == 1 and number > 0 and number < 60:
        print('Ваше место - нижнее')

    if number < 1 or number > 59:
        print('перепроверьте номер билета')

def zadanie_3():

    year = (int(input('Введите год: ')))

    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print(year, 'Год високосный')
    else:
        print(year, 'Год не високосный')

def zadanie_4():

    Color1 = input('Введите первый цвет: ')
    Color2 = input('Введите второй цвет: ')

    if (Color1 != "Красный" and Color1 != "Синий" and Color1 != "Желтый") and (Color2 != "Красный" and Color2 != "Синий" and Color2 != "Желтый"):
        print('Ошибка')

    if Color1 == 'Красный' and Color2 == 'Красный':
        print('Получится - Красный')
    if Color1 == 'Синий' and Color2 == 'Синий':
        print('Получится - Синий')
    if Color1 == 'Желтый' and Color2 == 'Желтый':
        print('Получится - Желтый')
    if Color1 == 'Красный' and Color2 == 'Синий':
        print('Получится - Фиолетовый')
    if Color1 == 'Синий' and Color2 == 'Красный':
        print('Получится - Фиолетовый')
    if Color1 == 'Красный' and Color2 == 'Желтый':
        print('Получится - Оранжевый')
    if Color1 == 'Желтый' and Color2 == 'Красный':
        print('Получится - Оранжевый')
    if Color1 == 'Синий' and Color2 == 'Желтый':
        print('Получится - Зелёный')
    if Color1 == 'Желтый' and Color2 == 'Синий':
        print('Получится - Зелёный')

zadanie_1(), zadanie_2(), zadanie_3(), zadanie_4()