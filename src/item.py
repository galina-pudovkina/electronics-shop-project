import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = None
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.quantity = quantity
        self.price = price
        self.__name = name

        self.all.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        """Проверка длины наименования товара, которая должна быть не больше 10"""
        if len(new_name) >= 10:
            raise ValueError('More than 10 letters in the name')
        else:
            self.__name = new_name

    @classmethod
    def instantiate_from_csv(cls):
        """класс-метод, инициализирующий экземпляры класса `Item` данными из файла _src/items.csv"""
        cls.all.clear()
        with open("src/items.csv", "r", encoding='windows-1251') as f:
            data = csv.DictReader(f)
            for row in data:
                cls(row['name'], cls.string_to_number(row['price']), cls.string_to_number(row['quantity']))

    @staticmethod
    def string_to_number(num):
        """Статический метод, возвращающий число из числа-строки"""
        return int(float(num))

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> float:
        """
        Применяет установленную скидку для конкретного товара.
        """
        new_price = self.price * self.pay_rate
        self.price = new_price
        return self.price
