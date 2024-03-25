# Класс Product: сами товары и их описание

class Product:
    name: str  # название товара
    description: str  # описание товара
    price: float  # цена товара
    quantity: int  # количество товара в наличии

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def from_dict(cls, dictionary):
        """Создаёт товар и возвращает объект, который можно добавлять в список товаров"""
        return cls(**dictionary)

    @property
    def price(self):
        """ Метод для доступа к атрибуту __price """
        return self.__price

    @price.setter
    def price(self, new_price):
        """Сеттер для цены, если цена равна или ниже нуля 'Цена товара должна быть больше 0' """
        if new_price <= 0:
            print('Цена товара должна быть больше 0')
        else:
            self.__price = new_price

    def __str__(self):
        """Метод для вывода информации о товаре"""
        return f'{self.name}, {self.price} руб. Остаток: {self.quantity} шт.'

    def __add__(self, other):
        """Метод для сложения цен двух видов товара в зависимости от их количества,
        результатом является сумма количества товаров (quantity) умноженных на цену (price)"""
        return self.__price * self.quantity + other.__price * other.quantity
