from src.item import Item


class Mixin:
    """
    Класс-примесь, реализующий дополнительный функционал по хранению и изменению раскладки клавиатуры
    """

    def __init__(self):
        self.__language = "EN"

    def change_lang(self):

        if self.__language == "RU":
            self.__language = "EN"
        elif self.__language == "EN":
            self.__language = "RU"
        return self

    @property
    def language(self):
        return self.__language


class Keyboard(Item, Mixin):
    """Класс для представления клавиатуры"""
    def change_lang(self):
        return Mixin.change_lang(self)
