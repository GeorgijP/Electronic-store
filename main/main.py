from utils.utils import Card_product

Card_product.instantiate_from_csv('items.csv')

print(Card_product.products)

item_1 = Card_product(Card_product.products[4])
