import pytest

from src.item import Item
from src.phone import Phone


def test_add_():
    item_one = Item('Телевизор', 20_000, 10)  # создаем объект класса Item
    item_two = Phone('Телефон', 15_000, 35, 2)  # создаем объект класса Phone
    assert item_one + item_two == 45  # ожидаем в выводе 45


def test_number_of_sim():
    with pytest.raises(ValueError):
        phone = Phone('Phone3', 1000, 3, 0)  # ожидаем ValueError, так как number_of_sim равно 0
    phone1 = Phone('Phone3', 1000, 3, 1)  # создаем объект, number_of_sim больше 0
    assert phone1.number_of_sim == 1
