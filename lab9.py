import csv
import os
from PIL import Image

def z1():
    os.mkdir('Z:\Чернейкина Юлия\lab9/obrabotka1.1')

    for filename in os.listdir("Z:\Чернейкина Юлия\lab9"): #обход всех файлов

            image = Image.open(os.path.join("Z:\Чернейкина Юлия\lab9", filename))
            image.load()
            filtered_image = image.convert("L")
            new_name = "new3_" + filename
            filtered_image.save(new_name)
            filtered_image.show()

def z2():
    os.mkdir('Z:\Чернейкина Юлия\lab9/obrabotka2.0')

    for filename in os.listdir("Z:\Чернейкина Юлия\lab9"): #обход всех файлов
        if filename.endswith('.jpg') or filename.endswith('.png'):
            image = Image.open(os.path.join("Z:\Чернейкина Юлия\lab9", filename))
            image.load()
            filtered_image = image.convert("L")
            new_name = "new3_" + filename
            filtered_image.save(new_name)
            filtered_image.show()

def z3():
    with open ('Z:\Чернейкина Юлия\lab9/data.csv') as file:
        reader=csv.reader(file)
        summ=0
        print("Нужно купить: ")
        for row in reader:
            product, number, price =row
            summ+= int(number)* int(price)
            print(f"{product}-{number} шт. за {price} руб.")
        print(f"Итоговая сумма: {summ} руб.")

z1(),z2(),z3()