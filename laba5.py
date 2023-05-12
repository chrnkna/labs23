import random
from random import randint
def zadanie_1():
    print("Задание1")
    a = 5
    list = []
    for i in range(a):
        item = randint(1,99)
        list.append(item)
    n = int(input("введите число"))
    if n in list:
        print("Поздравляю, вы угадали число", *list)
    else:
        print("нет такого числа", *list)




def zadanie_2():
    print("Задание 2")
    from random import randint
    a=[randint(0,50) for i in range(5)]
    b=[c for c in a if a.count(c)>1]
    print(a)
    if len(b)<1:
        print("Повторений нет")
    else:
        c=int(b[0])
        print(c,"Повторяющееся число ", a.count(c),"повторений")



def zadanie_3():
    print("Задание 3")
    ned = ("Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс")
    d = int(input("сколько выходных?"))
    for i in ned:
        print("Рабочие", *ned[:-d])
        print("Выходные", *ned[-d:])
        break

from random import sample
def zadanie_4():
    print("Задание4")
    list =["Петров" , "Сидоров" , "Иванов"]
    list2 = ["Кошкин", "Картошкин" , "Лащев"]
    team = tuple(random.sample(list,2)+random.sample(list2,2))
    print("Первая команда: ",*list)
    print("Вторая команда: ",*list2)
    print("Общая команда: ",*team)
    print("Количество участников общей команды: ",len(team))
    team = tuple(sorted(team))
    if "Иванов" in team:
         print((team).count("Иванов"))
    else:
        print("Иванова  нет в команде")


zadanie_1(), zadanie_2(), zadanie_3(), zadanie_4()