import pytest

from utils.utils import Card_product

# Экземпляры класса для тестов
item1 = Card_product("Смартфон", 15_000, 20)
item2 = Card_product("Телефон", 1_000, 25)
item3 = Card_product("iPhone", 200_000, 30)
item4 = Card_product("СуперСмартфон", 99_000, 10)

# Указание скидки на товар
Card_product.discount = 20


def test_apply_discount():
    assert item1.apply_discount() == 12000
    assert item2.apply_discount() == 800
    assert item3.apply_discount() == 160000


def test_calculate_total_price():
    assert item1.calculate_total_price() == 300000
    assert item2.calculate_total_price() == 25000
    assert item3.calculate_total_price() == 6000000


def test_is_integer():
    assert item1.is_integer(1.0) == int(1.0)
    assert item2.is_integer(1.1) == float(1.1)


def test_name_prod():
    assert item1.name_prod == "Смартфон"
    assert item2.name_prod == "Телефон"
    assert item3.name_prod == "iPhone"
    with pytest.raises(ValueError):
        item4.name_prod()

def test_repr():
    assert item1.__repr__() == "Card_product: Смартфон, 15000, 20"
    assert item2.__repr__() == "Card_product: Телефон, 1000, 25"
    assert item3.__repr__() == "Card_product: iPhone, 200000, 30"
    assert item4.__repr__() == "Card_product: СуперСмартфон, 99000, 10"

def test_except_Card_product():
    assert Card_product.instantiate_from_csv("") == "Отсутствует файл item.csv"
    # Если файл поврежден
    assert Card_product.instantiate_from_csv("items.csv") == "Файл item.csv поврежден"

