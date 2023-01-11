from abc import ABC, abstractmethod
fac = ''

class Product(ABC):

    @abstractmethod
    def cook(self):
        pass


class FettuccineAlfredo(Product):
    NAME = 'Fettuccine Alfredo'

    def cook(self):
        print(f"Italian main course prepared: {self.NAME}")


class Tiramisu(Product):
    NAME = 'Tiramisu'

    def cook(self):
        print(f"Italian dessert prepared: {self.NAME}")


class DuckALOrange(Product):
    NAME = "Duck À L'Orange"

    def cook(self):
        print(f"French main course prepared: {self.NAME}")


class CremeBrulee(Product):
    NAME = "Crème brûlée"

    def cook(self):
        print(f"French dessert prepared: {self.NAME}")


class Factory(ABC):

    @abstractmethod
    def get_dish(self, type_of_meal):
        pass


class ItalianDishesFactory(Factory):

    def get_dish(self, type_of_meal):
        if type_of_meal == 'main':
            return FettuccineAlfredo()
        elif type_of_meal == 'dessert':
            return Tiramisu()


class FrenchDishesFactory(Factory):
    def get_dish(self, type_of_meal):
        if type_of_meal == 'main':
            return DuckALOrange()
        elif type_of_meal == 'dessert':
            return CremeBrulee()


class FactoryProducer:

    def get_factory(self, type_of_factory):
        if type_of_factory == 'italian':
            return ItalianDishesFactory()
        elif type_of_factory == 'french':
            return FrenchDishesFactory()


fp = FactoryProducer()
fac = fp.get_factory("italian")
# main_dish = fac.get_dish("main")
# main_dish.cook()
# dessert = fac.get_dish("dessert")
# dessert.cook()
fac1 = fp.get_factory("french")
main_dish = fac1.get_dish("main")
main_dish.cook()