from src.phone import Phone
from src.item import Item
import pytest


# Тестирование создания экземпляра класса Phone
def test_phone_creation():
    phone = Phone("Телефон", 50000, 10, 2)
    assert phone.name == "Телефон"
    assert phone.price == 50000
    assert phone.quantity == 10
    assert phone.number_of_sim == 2


# Тестирование сеттера и геттера number_of_sim
def test_number_of_sim():
    phone = Phone("Телефон", 50000, 10, 2)
    assert phone.number_of_sim == 2

    phone.number_of_sim = 1
    assert phone.number_of_sim == 1

    with pytest.raises(ValueError):
        phone.number_of_sim = 0


# Тестирование метода __add__
def test_add_phones():
    phone1 = Phone("Телефон1", 30000, 5, 1)
    phone2 = Phone("Телефон2", 40000, 10, 2)

    assert phone1 + phone2 == 15


def test_add_phone_item():
    phone = Phone("Телефон", 50000, 10, 2)
    item = Item("Аксессуар", 500, 30)

    assert phone + item == 40
    assert item + phone == 40


def test_add_phone_with_non_item():
    phone = Phone("Телефон", 50000, 10, 2)
    non_item = 123  # Это может быть любой объект, не являющийся Item или Phone

    assert (phone + non_item) is None


# Тестирование метода __repr__
def test_phone_repr():
    phone = Phone("Телефон", 50000, 10, 2)
    expected_repr = "Phone('Телефон', 50000, 10, 2)"
    assert repr(phone) == expected_repr


# Тестирование метода __str__
def test_phone_str():
    phone = Phone("Телефон", 50000, 10, 2)
    assert str(phone) == "Телефон"
