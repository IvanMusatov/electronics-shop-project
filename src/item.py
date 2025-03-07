import csv
import os


class InstantiateCSVError(Exception):
    """
    Класс-исключение для ошибок при чтении файла item.csv.
    """
    pass


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
        self.name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.name

    def __add__(self, other):
        if isinstance(self, Item):
            return self.quantity + other.quantity

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self, pay_rate=None) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        if pay_rate is None:
            pay_rate = Item.pay_rate
        self.price *= pay_rate

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if len(value) <= 10:
            self._name = value
        else:
            print("Длина наименования товара превышает 10 символов.")

    @classmethod
    def instantiate_from_csv(cls):
        file_path = os.path.join(os.path.dirname(__file__), 'items.csv')
        try:
            with open(file_path, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    item = cls(row['name'], cls.string_to_number(row['price']), int(row['quantity']))
                    cls.all.append(item)
        except FileNotFoundError:
            raise FileNotFoundError("Отсутствует файл items.csv")
        except KeyError:
            raise InstantiateCSVError("Файл items.csv поврежден")

    @staticmethod
    def string_to_number(value):
        return int(float(value))
