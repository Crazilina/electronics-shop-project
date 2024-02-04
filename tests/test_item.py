"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item, InstantiateCSVError


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

    # Тестирование короткого имени
    short_name = "Короткое"
    item.name = short_name
    assert item.name == short_name

    # Тестирование генерации исключения для длинного имени
    with pytest.raises(Exception) as exc_info:
        item.name = "ОченьДлинноеИмяТовара"
    assert "Длина наименования товара превышает 10 символов." in str(exc_info.value)


def test_instantiate_from_csv():
    Item.instantiate_from_csv('items.csv')
    assert len(Item.all) > 0  # Проверяем, что список не пуст


def test_string_to_number():
    assert Item.string_to_number("123") == 123
    assert Item.string_to_number("-123") == -123
    assert Item.string_to_number("0") == 0


def test_repr():
    item = Item("Тестовый товар", 100.0, 5)
    expected_repr = "Item('Тестовый товар', 100.0, 5)"
    assert repr(item) == expected_repr


def test_str():
    item = Item("Тестовый товар", 100.0, 5)
    expected_str = "Тестовый товар"
    assert str(item) == expected_str


def test_add_items():
    item1 = Item("Item1", 100, 5)
    item2 = Item("Item2", 200, 10)

    assert item1 + item2 == 15


def test_add_item_with_non_item():
    item = Item("Тестовый товар", 100.0, 5)
    non_item = "не товар"  # Это может быть любой объект, не являющийся Item или Phone

    assert (item + non_item) is None


def test_instantiate_from_csv_file_not_found():
    with pytest.raises(FileNotFoundError) as e:
        # Указываем путь к несуществующему файлу
        Item.instantiate_from_csv('nonexistent.csv')
    assert "Отсутствует файл items.csv" in str(e.value)


def test_instantiate_from_csv_damaged_file():
    with pytest.raises(InstantiateCSVError) as e:
        Item.instantiate_from_csv('damaged_items.csv')
    assert "Файл item.csv поврежден" in str(e.value)
