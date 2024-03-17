# Класс Category: категории товаров
# Класс Product: сами товары и их описание


class Category:
    title: str  # название категории
    description: str  # описание категории
    goods: list  # список товаров в категории
    quantity_category = 0  # общее количество категорий
    unique_goods = set()  # все товары без повторений
    quantity_unique_goods = len(unique_goods)  # общее количество уникальных товаров

    def __init__(self, title, description, goods):
        self.title = title
        self.description = description
        self.goods = goods

        Category.unique_goods.update(goods)
        Category.quantity_unique_goods = len(Category.unique_goods)
        Category.quantity_category += 1


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




