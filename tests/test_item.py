"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item, InstantiateCSVError


def test_calculate_total_price():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)

    assert item1.calculate_total_price() == 200000
    assert item2.calculate_total_price() == 100000


def test_apply_discount():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)

    Item.pay_rate = 0.8

    item1.apply_discount()
    assert item1.price == 8000.0
    assert item2.price == 20000


def test_name_setter():
    item = Item('Телефон', 10000, 5)

    # длина наименования товара меньше 10 символов
    item.name = 'Смартфон'
    assert item._name == 'Смартфон'

    # длина наименования товара равна 10 символов
    item.name = '0123456789'
    assert item._name == '0123456789'

    # длина наименования товара больше 10 символов
    item.name = 'СуперСмартфон'
    assert item._name != 'СуперСмартфон'


def test_string_to_number():
    assert Item.string_to_number("5") == 5
    assert Item.string_to_number("5.0") == 5
    assert Item.string_to_number("5.5") == 5


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5
    assert Item.all[0].name == "Смартфон"
    assert Item.all[1].name == "Ноутбук"


def test__repr__():
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"


def test__str__():
    item1 = Item("Смартфон", 10000, 20)
    assert str(item1) == 'Смартфон'


def test_add_():
    item_one = Item('Телевизор', 20_000, 10)  # создаем объект класса Item
    item_two = Item('Телефон', 15_000, 15)  # создаем объект класса Phone
    assert item_one + item_two == 25  # ожидаем в выводе 25


def test_instantiate_from_csv_file_not_found():
    with pytest.raises(FileNotFoundError, match="Отсутствует файл items.csv"):
        Item.instantiate_from_csv()


def test_instantiate_from_csv_file_corrupted():
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv()
