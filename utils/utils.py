import csv
from utils.InstantiateCSVError import InstantiateCSVError

class Card_product:
    """Класс для представления товара в магазинe"""
    products = []
    discount = 0 # В процентах

    def __init__(self, name_prod, price_prod, quantity):
        self._name_prod = name_prod
        self.price_prod = price_prod
        self.quantity = quantity
        Card_product.products.append(self)

    @classmethod
    def instantiate_from_csv(cls, name_file):
        """Создание экземпляров класса из списка файла формата csv"""
        items = []
        try:
            with open(name_file, 'r', encoding='windows-1251') as file:
                reader = csv.DictReader(file)
                for i in reader:
                    if list(i.keys()) == ["name", "price", "quantity"]:
                        name_prod = i['name']
                        price_prod = int(i['price'])
                        quantity = int(i['quantity'])
                        items.append(cls(name_prod, price_prod, quantity))
                    else:
                        raise InstantiateCSVError
        except FileNotFoundError:
            print("Отсутствует файл item.csv")
        except InstantiateCSVError:
            print("Файл item.csv поврежден")

        return items

    @property
    def name_prod(self):
        """Проверяет длину наименования продукта"""
        if len(self._name_prod) > 10:
            raise ValueError('Название длиннее 10 знаков')
        else:
            return self._name_prod

    def apply_discount(self):
        """Возвращает установленную скидку для конкретного товара"""
        self.discount = (100 - self.discount) / 100
        self.price_prod_discount = self.discount * self.price_prod
        return self.price_prod_discount

    def calculate_total_price(self):
        """Возвращает общую стоимость конкретного товара в магазине"""
        self.price_prod_total = self.quantity * self.price_prod
        return self.price_prod_total

    @staticmethod
    def is_integer(number):
        """Проверка целочисленности"""
        if number % 1 == 0:
            return int(number)
        else:
            return float(number)

    def __repr__(self):
        return f"Card_product: {self._name_prod}, {self.price_prod}, {self.quantity}"

    def __str__(self):
        return f"Наименование товара - {self._name_prod}, его цена - {self.price_prod}, сколько осталось в магазине: {self.quantity} шт."


class Phone(Card_product):
    """Класс для смартфонов/телефонов"""

    def __init__(self, name_prod, price_prod, quantity, quantity_sim):
        super().__init__(name_prod, price_prod, quantity)
        self._quantity_sim = quantity_sim

    def __add__(self, other):
        """Сложние количества товара на складе"""
        if isinstance(other, Card_product):
            return self.quantity + other.quantity
        else:
            ValueError("Только объекты Phone и Card_product")

    @property
    def quantity_sim(self):
        if self._quantity_sim % 1 > 0:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
        else:
            return self._quantity_sim

    @quantity_sim.setter
    def quantity_sim(self, value):
        self._quantity_sim = value


class MixinLanguage:
    """Отвечает за язык клавиатуры"""
    def __init__(self, *args):
        self._language = "EN"
        super().__init__(*args)

    @property
    def language(self):
        return self._language

    def change_lang(self):
        if self._language == "EN":
            self._language = "RU"
        else:
            self._language = "EN"

class Keyboard(MixinLanguage, Card_product):
    """Класс для клавиатуры"""
    pass
