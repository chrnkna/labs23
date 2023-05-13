def zadacha1():
    class Restaurant:
        def __init__(self,restaurant_name):     #init - метод, позволяющий принимать аргументы для класса
            self.restaurant_name = restaurant_name      #sellf - параметр, который передаётся первым аргументом в метод класса и представляет собой ссылку на экземпляр класса
        def describe_restaurant(self):
            print("Название ресторана: ",self.restaurant_name)
    class IceCreamStand(Restaurant):
        def __init__(self,restaurant_name,flavors):
            self.restaurant_name = restaurant_name
            self.flavors = flavors
        def vivod_sortov(self):
            print("Сорта мороженного: ")
            for flavor in self.flavors:
                print(f"-{flavor}")
    newIceCreamStand = IceCreamStand("Кафе-мороженное",["Ванильное", "Шоколадное","Фисташковое","Клубничное"])
    newIceCreamStand.describe_restaurant()
    newIceCreamStand.vivod_sortov()


def zadacha2():
    class Restaurant:
        def __init__(self,restaurant_name):     #init - метод, позволяющий принимать аргументы для класса
            self.restaurant_name = restaurant_name      #self - параметр, который передаётся первым аргументом в метод класса и представляет собой ссылку на экземпляр класса
        def describe_restaurant(self):
            print("Название ресторана: ",self.restaurant_name)
    class IceCreamStand(Restaurant):
        def __init__(self,restaurant_name,adress,vremya_raboti):
            self.restaurant_name = restaurant_name
            self.flavors = []
            self.adress = adress
            self.vremya_raboti = vremya_raboti
        def opisanie(self):
            print("Местоположение: ", self.adress,"\nВремя работы: ", self.vremya_raboti)
        def vivod_sortov(self):
            print("Вкусы мороженного: ")
            for flavor in self.flavors:
                print(f"-{flavor}")
        def add_flovor(self,flavor):
            self.flavors.append(flavor)
            print(f"{flavor} добавлен в список вкусов.")
        def remove_flavor(self,flavor):
            if flavor in self.flavors:
                self.flavors.remove(flavor)
                print(f"{flavor} былo удалено из списка вкусов.")
            else:
                print(f"{flavor} - такого вкуса нет в списке!")
        def check_flavor(self, flavor):
            if flavor in self.flavors:
                print(f"{flavor} имеется в списке вкусов.")
            else:
                print(f"{flavor} НЕ имеется в списке вкусов.")
    newIceCreamStand = IceCreamStand("Кафе-мороженное","Ул.Яхтенная 77,к2", "Ежедневно с 9:00 до 22:00")
    newIceCreamStand.describe_restaurant()
    newIceCreamStand.opisanie()
    newIceCreamStand.vivod_sortov()
    newIceCreamStand.add_flovor("Ванильное")
    newIceCreamStand.add_flovor("Шоколадное")
    newIceCreamStand.add_flovor(input("Какое ещё добавить? "))
    newIceCreamStand.vivod_sortov()
    newIceCreamStand.remove_flavor(input("Какое удалить? "))
    newIceCreamStand.vivod_sortov()
    newIceCreamStand.check_flavor(input("Какое мороженное проверить в наличии? "))
def zadacha2_4():
    class Restaurant:
        def __init__(self,restaurant_name):     #init - метод, позволяющий принимать аргументы для класса
            self.restaurant_name = restaurant_name      #self - параметр, который передаётся первым аргументом в метод класса и представляет собой ссылку на экземпляр класса
        def describe_restaurant(self):
            print("Название ресторана: ",self.restaurant_name)
    class IceCreamStand(Restaurant):
        def __init__(self,restaurant_name,adress,vremya_raboti):
            self.restaurant_name = restaurant_name
            self.flavors = []
            self.adress = adress
            self.vremya_raboti = vremya_raboti
        def opisanie(self):
            print("Местоположение: ", self.adress,"\nВремя работы: ", self.vremya_raboti)
        def vivod_sortov(self):
            print("Вкусы мороженного: ")
            for flavor in self.flavors:
                print(f"-{flavor}")
        def add_flovor(self,flavor):
            self.flavors.append(flavor)
            print(f"{flavor} добавлен в список вкусов.")
        def remove_flavor(self,flavor):
            if flavor in self.flavors:
                self.flavors.remove(flavor)
                print(f"{flavor} былo удалено из списка вкусов.")
            else:
                print(f"{flavor} - такого вкуса нет в списке!")
        def check_flavor(self, flavor):
            if flavor in self.flavors:
                print(f"{flavor} имеется в списке вкусов.")
            else:
                print(f"{flavor} НЕ имеется в списке вкусов.")
    class Palochka(IceCreamStand):
        def __init__(self, restaurant_name, adress, vremya_raboti):
            self.restaurant_name = restaurant_name
            self.flavors = []
            self.adress = adress
            self.vremya_raboti = vremya_raboti
            self.type = "Мороженное на палочке"
        def describe_type(self):
            print(f"Вид: {self.type}")
    class Rozhok(IceCreamStand):
        def __init__(self, restaurant_name, adress, vremya_raboti):
            self.restaurant_name = restaurant_name
            self.flavors = []
            self.adress = adress
            self.vremya_raboti = vremya_raboti
            self.type = "Мороженное в рожке"
        def describe_type(self):
            print(f"Вид: {self.type}")

    newIceCreamStand = IceCreamStand("Кафе-мороженное","Ул.Яхтенная 77,к2", "Ежедневно с 9:00 до 22:00")
    newIceCreamStand.describe_restaurant()
    newIceCreamStand.opisanie()
    newIceCreamStand = Palochka("Кафе-мороженное", "Мороженное77", "не знаю зачем")
    new2IceCreamStand = Rozhok("Кафе-мороженное", "Мороженное77","не знаю зачем")

    newIceCreamStand.add_flovor("Ванильное")
    newIceCreamStand.add_flovor("Шоколадное")

    new2IceCreamStand.add_flovor("Ягодное")
    new2IceCreamStand.add_flovor("Пломбир")

    newIceCreamStand.describe_type()
    newIceCreamStand.vivod_sortov()

    new2IceCreamStand.describe_type()
    new2IceCreamStand.vivod_sortov()


zadacha2_4()
def z5():
    import tkinter as tk

    class IceCreamStand:
        def __init__(self):
            self.ice_creams = {"Ванильное": 150, "Шоколадное": 260, "Клубничное": 170, "Фисташковое": 180}
            self.scoops = 0
            self.total_price = 0

        def add_scoop(self, flavor):
            self.scoops += 1
            self.total_price += self.ice_creams[flavor]

        def clear_order(self):
            self.scoops = 0
            self.total_price = 0

    class IceCreamApp:
        def __init__(self, master):
            self.master = master
            master.title("Айскрим")

            self.ice_cream_stand = IceCreamStand()

            self.flavors = ["Ванильное", "Шоколадное", "Клубничное", "Фисташковое"]

            self.scoop_label = tk.Label(master, text="В корзине: 0") #надпись, которую нельзя редактировать в окне
            self.scoop_label.grid(row=0, column=0)

            self.cost_label = tk.Label(master, text="Итог: 0")
            self.cost_label.grid(row=0, column=1)

            self.button_grid = tk.Frame(master) #чтобы размещать виджеты со вкусами в окне
            self.button_grid.grid(row=1, column=0, columnspan=2)

            for i, flavor in enumerate(self.flavors): #функция для фиклического перебора с автоматической индексацией
                button = tk.Button(self.button_grid, text=flavor, command=lambda f=flavor: self.add_scoop(f)) #лямбда-функция, когда используем безымянную функцию (без присваивания аргументу)
                button.grid(row=i // 2, column=i % 2)

            self.clear_button = tk.Button(master, text="Очистить корзину", command=self.clear_order)
            self.clear_button.grid(row=2, column=0, columnspan=2)

        def add_scoop(self, flavor):
            self.ice_cream_stand.add_scoop(flavor)
            self.scoop_label.config(text="В корзине: " + str(self.ice_cream_stand.scoops))
            self.cost_label.config(text="Итог: " + str(self.ice_cream_stand.total_price))

        def clear_order(self):
            self.ice_cream_stand.clear_order()
            self.scoop_label.config(text="В корзине: 0")
            self.cost_label.config(text="Итог: 0")

    root = tk.Tk()
    app = IceCreamApp(root)
    root.mainloop()


z5()