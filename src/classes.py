#
from typing import List


class Category:
    title: str  # название категории
    description: str  # описание категории
    goods: list  # список товаров в категории
    goods_in_category = 0  # количество товаров в категории
    unique_goods = 0  # количество уникальных товаров

    def __init__(self, title, description, goods):
        self.title = title
        self.description = description
        self.goods = goods
        self.goods_in_category = 1

        Category.unique_goods += 1


class Product:
    title: str  # название товара
    description: str  # описание товара
    price: float  # цена товара
    stock: int  # количество товара в наличии

    def __init__(self, title, description, price, stock):
        self.title = title
        self.description = description
        self.price = price
        self.stock = stock


