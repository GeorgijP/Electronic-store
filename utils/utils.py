class Card_product:
    """
    Класс для представления товара в магазине
    """
    products = []
    discount = 0

    def __init__(self, name_prod, price_prod, quantity):
        self.name_prod = name_prod
        self.price_prod = price_prod
        self.quantity = quantity
        Card_product.products.append(self)


    def apply_discount(self):
        """
        возвращает установленную скидку для конкретного товара
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