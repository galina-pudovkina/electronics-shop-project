"""Здесь надо написать тесты с использованием pytest для модуля item."""

from src.item import Item

item1 = Item("Смартфон", 20000, 5)


def test_calculate_total_price():
    assert item1.calculate_total_price() == 100000


def test_apply_discount():
    item1.pay_rate = 0.5
    assert item1.apply_discount() == 10000.0


def test_name():
    assert item1.name == 'Смартфон'


def test_string_to_number(test_num):
    assert Item.string_to_number(test_num) == 5
