import pytest
from utils.utils import Phone, Card_product

item1 = Phone("SamsundDuo", 60_000, 4, 2)
item2 = Card_product("Смартфон", 15_000, 20)

def test_add():
    assert item1 + item2 == 24

def test_quantity_sim():
    assert item1.quantity_sim == 2
    item1.quantity_sim = 2.1
    with pytest.raises(ValueError):
        item1.quantity_sim

