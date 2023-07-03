import pytest

from src.item import Item
from src.phone import Phone


def test_add():
    item1 = Item("Смартфон", 10000, 20)
    phone2 = Phone("Самсунг", 50000, 10, 1)
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert item1 + phone1 == 25
    assert phone1 + phone2 == 15


def test_repr():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"


def test_verify_number_of_sim():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    phone1.number_of_sim = 0
    return None
