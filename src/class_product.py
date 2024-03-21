# Класс Product: сами товары и их описание

class Product:
    name: str  # название товара
    description: str  # описание товара
    price: float  # цена товара
    stock: int  # количество товара в наличии

    def __init__(self, name, description, price, stock):
        self.name = name
        self.description = description
        self.__price = price
        self.stock = stock

    @classmethod
    def from_dict(cls, name, description, price, stock):
        """ Создание объекта класса Product из словаря с данными о товаре"""
        new_dict = {
            'name': name,
            'description': description,
            'price': price,
            'stock': stock
        }
        return new_dict

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
