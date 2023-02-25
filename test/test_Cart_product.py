from utils.utils import Card_product

# Указание скидки на товар
Card_product.discount = 20

# Экземпляры класса для тестов
item1 = Card_product("СуперСмартфон", 15000, 20)
item2 = Card_product("Телефон", 1000, 25)
item3 = Card_product("iPhone", 200000, 30)

def test_apply_discount():
    assert item1.apply_discount() == 12000
    assert item2.apply_discount() == 800
    assert item3.apply_discount() == 160000

def test_calculate_total_price():
    assert item1.calculate_total_price() == 300000
    assert item2.calculate_total_price() == 25000
    assert item3.calculate_total_price() == 6000000
