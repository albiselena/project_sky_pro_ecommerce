# Класс Category: категории товаров


class Category:
    category_name: str  # название категории
    category_description: str  # описание категории
    goods: []  # список товаров в категории
    unique_category = set()  # множество для подсчёта категории, чтобы не повторялись категории
    quantity_category = 0  # общее количество категорий
    unique_goods = set()  # все товары без повторений
    quantity_unique_goods = len(unique_goods)  # общее количество уникальных товаров

    def __init__(self, category_name, category_description, goods):
        self.category_name = category_name
        self.category_description = category_description
        self.__goods = goods

        Category.unique_goods.add(self.__goods)  # добавляем продукты во множество, чтобы не допускать повторов
        Category.quantity_unique_goods = len(Category.unique_goods)

        Category.unique_category.add(category_name)  # добавляем категории во множество, чтобы не допускать повторов
        Category.quantity_category = len(Category.unique_category)

    def add_goods(self, product):
        self.__goods.append(product)

    @property
    def get_goods(self):
        products_str = ""
        for product in self.__goods:
            products_str += f'{product.name}, {product.price} руб. Осталось: {product.stock} шт.\n'
        return products_str

