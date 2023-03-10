from utils.utils import Keyboard

item_1 = Keyboard('Клавиатура', 800, 3)
def test_change_lang():

    # По умолчанию ожидаем язык EN
    assert item_1.language == "EN"
    # Меняем язык
    item_1.change_lang()
    # Теперь ожидаем язык RU
    assert item_1.language == "RU"
