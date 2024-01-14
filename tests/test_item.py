"""Здесь надо написать тесты с использованием pytest для модуля item."""

from src.item import Item


def test_item_creation():
    item = Item("Тестовый товар", 100.0, 5)
    assert item.name == "Тестовый товар"
    assert item.price == 100.0
    assert item.quantity == 5


def test_calculate_total_price():
    item = Item("Тестовый товар", 100.0, 5)
    assert item.calculate_total_price() == 500.0


def test_apply_discount():
    item = Item("Тестовый товар", 100.0, 5)
    Item.pay_rate = 0.8  # Скидка 20%
    item.apply_discount()
    assert item.price == 80.0
