import csv


class Card_product:
    """
    Класс для представления товара в магазине
    """
    products = []
    discount = 0

    def __init__(self, name_prod, price_prod, quantity):
        self._name_prod = name_prod
        self.price_prod = price_prod
        self.quantity = quantity
        Card_product.products.append(self)

    @property
    def name_prod(self):
        """
        Проверяет длинну наименования продукта
        """
        if len(self._name_prod) > 10:
            raise ValueError('Название длиннее 10 знаков')

    def apply_discount(self):
        """
        Возвращает установленную скидку для конкретного товара
        """
        self.discount = (100 - self.discount) / 100
        self.price_prod_discount = self.discount * self.price_prod
        return self.price_prod_discount

    def calculate_total_price(self):
        """
        возвращает общую стоимость конкретного товара в магазине
        """
        self.price_prod_total = self.quantity * self.price_prod
        return self.price_prod_total

    @classmethod
    def instantiate_from_csv(cls, name_file):
        """
        Создание экземпляров класса из списка файла формата csv
        """
        items = []
        with open(name_file, 'r', encoding='windows-1251') as file:
            reader = csv.DictReader(file)
            for i in reader:
                items.append(cls(i['name'], i['price'], i['quantity']))
        return items

    @staticmethod
    def is_integer(number):
        """
        Проверка целочисленности
        """
        if number % 1 == 0:
            return True
        else:
            return False
