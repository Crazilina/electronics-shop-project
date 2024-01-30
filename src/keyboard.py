from .item import Item

class LanguageMixin:
    """
    Миксин для управления языком клавиатуры.

    Этот класс предоставляет функционал для изменения языка клавиатуры.
    """

    def __init__(self):
        """
        Инициализирует начальный язык клавиатуры как английский (EN).
        """
        self._language = 'EN'

    def change_lang(self):
        """
        Переключает язык клавиатуры.

        Меняет язык с английского (EN) на русский (RU) и наоборот.
        """
        if self._language == 'EN':
            self._language = 'RU'
        else:
            self._language = 'EN'


class Keyboard(Item, LanguageMixin):
    """
    Класс для представления клавиатуры как товара.

    Наследует функциональность товара от класса Item и функциональность управления языком от LanguageMixin.
    """

    def __init__(self, name: str, price: float, quantity: int):
        """
        Инициализирует экземпляр клавиатуры с заданными характеристиками.

        :param name: Название клавиатуры.
        :param price: Цена клавиатуры.
        :param quantity: Количество клавиатур в наличии.
        """
        super().__init__(name, price, quantity)
        LanguageMixin.__init__(self)

    @property
    def language(self):
        """
        Возвращает текущий язык клавиатуры.
        """
        return self._language

    def __repr__(self):
        """
        Возвращает строковое представление объекта клавиатуры.

        Включает в себя название, цену, количество и текущий язык клавиатуры.
        """
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, Language: {self.language})"
