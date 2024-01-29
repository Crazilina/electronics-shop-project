import csv
import os


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """

        # Присвоение атрибутов объекту
        self.__name = name
        self.price = price
        self.quantity = quantity

        # Добавление экземпляра в список всех экземпляров
        Item.all.append(self)

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        if len(value) > 10:
            raise Exception("Длина наименования товара превышает 10 символов.")
        else:
            self.__name = value

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @classmethod
    def instantiate_from_csv(cls, file_path: str) -> None:
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # Абсолютный путь к файлу items.csv
        absolute_file_path = os.path.join(project_root, file_path)
        cls.all.clear()  # Очистить список всех экземпляров перед добавлением новых
        with open(absolute_file_path, mode='r', encoding='windows-1251') as file:
            reader = csv.DictReader(file)
            items = list(reader)
            for item in items:
                cls(
                    name=item.get('name'),
                    price=float(item.get('price')),
                    quantity=int(item.get('quantity'))
                )

    @staticmethod
    def string_to_number(string_number: str) -> int:
        return int(float(string_number))

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self) -> str:
        return self.name

    def __add__(self, other):
        from .phone import Phone
        if isinstance(other, (Item, Phone)):
            return self.quantity + other.quantity
        return None
