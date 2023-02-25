from utils.utils import Card_product

Card_product.instantiate_from_csv('items123.csv')

item = Card_product.products[2]
print(item)