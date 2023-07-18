"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item
from src.phone import Phone
from src.item import InstantiateCSVError


def test_calculate_total_price():
    item1 = Item("Смартфон", 20000, 5)
    assert item1.calculate_total_price() == 100000


def test_apply_discount():
    item1 = Item("Смартфон", 20000, 5)
    item1.pay_rate = 0.5
    assert item1.apply_discount() == 10000.0


def test_name():
    item1 = Item('Смартфон', 1000, 1)

    with pytest.raises(ValueError):
        item1.name = 'СуперСмартфон'


def test_string_to_number(test_num):
    assert Item.string_to_number(test_num) == 5


def test_info1():
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"


def test_info2():
    item1 = Item("Смартфон", 10000, 20)
    assert str(item1) == 'Смартфон'


def test_add():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("СмартТВ", 50000, 10)
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert item1 + phone1 == 25
    assert item1 + item2 == 30


def test_instantiate_from_csv():
    assert Item.instantiate_from_csv(file="src.csv") == None


def test_test_instantiate_from_csv2():
    assert Item.instantiate_from_csv(file="../src/items2.csv") == None
