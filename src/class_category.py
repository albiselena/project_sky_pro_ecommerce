# Класс Category: категории товаров


class Category:
    category_name: str  # название категории
    category_description: str  # описание категории
    goods: []  # список товаров в категории

    quantity_category = 0  # общее количество категорий
    quantity_unique_goods = 0  # общее количество уникальных товаров

    def __init__(self, category_name, category_description, goods):
        self.category_name = category_name
        self.category_description = category_description
        self.__goods = goods
        Category.quantity_category += 1
        Category.quantity_unique_goods += len(self.__goods)

    def add_goods(self, product):
        self.__goods.append(product)

    @property
    def goods(self):
        result = (
            f'{product.name}, {product.price} руб. Остаток: {product.stock} шт.'
            for product in self.__goods
        )
        return '\n'.join(result)
