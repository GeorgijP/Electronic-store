from utils.utils import Card_product

Card_product.instantiate_from_csv("items123.csv")


item = Card_product("abc", 2.5, 3.0)

print(item._name_prod)
print(item.price_prod)
print(item.quantity)
print(item.calculate_total_price())


