def z1():
    print("Задание 1")
    class Restaurant:
        def init(self,restaurant_name,cuisine_type):     #init - метод, позволяющий принимать аргументы для класса
            self.restaurant_name = restaurant_name      #self - параметр, который передаётся первым аргументом в метод класса и представляет собой ссылку на экземпляр класса
            self.cuisine_type = cuisine_type  #self - параметр, который передаётся первым аргументом в метод класса и представляет собой ссылку на экземпляр класса
        def describe_restaurant(self):      #метод1
            print(f"Ресторан {self.restaurant_name}, кухня - {self.cuisine_type}.")
        def open_restaurant(self):      #метод2
            print("Ресторан открыт к посещению!")
    newRestaurant = Restaurant("Астория","Итальянская")
    newRestaurant.describe_restaurant()
    newRestaurant.open_restaurant()


def z2():
    print("Задание 2")
    class Restaurant:
        def init(self, restaurant_name, cuisine_type):  #init - метод, позволяющий принимать аргументы для класса
            self.restaurant_name = restaurant_name  #self - параметр, который передаётся первым аргументом в метод класса и представляет собой ссылку на экземпляр класса
            self.cuisine_type = cuisine_type  #self - параметр, который передаётся первым аргументом в метод класса и представляет собой ссылку на экземпляр класса

        def describe_restaurant(self):
            print(f"Ресторан {self.restaurant_name}, кухня - {self.cuisine_type}.")

        def open_restaurant(self):
            print(f"Ресторан {self.restaurant_name} открыт!")

    restaurant1 = Restaurant("Италиано", "итальянская")
    restaurant2 = Restaurant("Токио", "японская")
    restaurant3 = Restaurant("Шашлычная №1", "кавказская")


    restaurant1.describe_restaurant()
    restaurant2.describe_restaurant()
    restaurant3.describe_restaurant()
def z3():
        print("Задание 3")
        class Restaurant:
            def init(self, restaurant_name, cuisine_type, rating_restaurant):
                self.restaurant_name = restaurant_name
                self.cuisine_type = cuisine_type
                self.rating_restaurant = rating_restaurant

            def describe_restaurant(self):
                print(
                    f'Название ресторана: {self.restaurant_name}, кухня: {self.cuisine_type} японская, рейтинг ресторана: {self.rating_restaurant}')

            def open_restoraunrt(self):
                print('Ресторан сейчас открыт')

            def rrating_restaurant(self):
                print(f'Новый рейтинг ресторана: {input("Введите новый рейтинг: ")}')

        new_Restaurant = Restaurant('Токио', '', 4.2)

        new_Restaurant.describe_restaurant()
        new_Restaurant.open_restoraunrt()
        new_Restaurant.rrating_restaurant()

z1(), z2(), z3()