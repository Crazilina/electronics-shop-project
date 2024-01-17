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


def test_name_getter():
    item = Item("Тестовый товар", 100.0, 5)
    assert item.name == "Тестовый товар"


def test_name_setter():
    item = Item("Товар", 100.0, 5)
    # Тестирование усечения длинного имени
    item.name = "ОченьДлинноеНазвание"
    assert item.name == "ОченьДлинн"  # Первые 10 символов

    # Тестирование короткого имени
    short_name = "Короткое"
    item.name = short_name
    assert item.name == short_name


def test_instantiate_from_csv():
    Item.instantiate_from_csv('src/items.csv')
    assert len(Item.all) > 0  # Проверяем, что список не пуст


def test_string_to_number():
    assert Item.string_to_number("123") == 123
    assert Item.string_to_number("123.45") == 123
