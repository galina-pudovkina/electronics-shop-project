from src.item import Item


class Phone(Item):
    """
        Класс для представления товара(телефон) в магазине.
        """

    def __init__(self, name: str, price: float, quantity: int, number_of_sim):
        super().__init__(name, price, quantity)
        self.verify_number_of_sim(number_of_sim)
        self.number_of_sim = number_of_sim

    def __add__(self, other):
        """Реализует сложение по кол-ву товара в магазине классов Item и Phone"""
        if isinstance(other, Item):
            return self.quantity + other.quantity
        raise ValueError("Возможно сложение только экземпляров класса Item и класса Phone")

    def __repr__(self):
        """Магический метод для вывода инфо о классе для разработчика"""
        return f"{self.__class__.__name__}('{self._name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    """Класс-метод реализующий проверку на кол-во поддерживаемых сим"""

    @classmethod
    def verify_number_of_sim(cls, number_of_sim):
        if number_of_sim <= 0:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
