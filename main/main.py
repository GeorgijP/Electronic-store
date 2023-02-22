from utils.utils import Card_product


Card_product.instantiate_from_csv('items.csv')  # создание объектов из данных файла

item1 = Card_product("СуперСмартфон", 15000, 20)
print(item1.calculate_total_price()) # выведет 300000

item2 = Card_product.products[4]
print(item2.calculate_total_price) # выведет <bound method Card_product.calculate_total_price of <utils.utils.Card_product object at 0x104d408d0>>