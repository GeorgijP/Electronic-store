from utils.utils import Card_product

Card_product.discount = int(input('Введите размер скидки: '))

item = Card_product("Xiaomi", 1_000_000, 1_000_000)

print(item.apply_discount())
print(item.calculate_total_price())