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
        """Геттер складывающий продукты из класса Product в атрибут goods класса Category,
        и возвращающий это всё строкой класса Product"""
        list_goods = []
        for product in self.__goods:
            list_goods.append(str(product))
        return list_goods

    def __len__(self):
        """Метод для подсчёта количества товаров в категории для вывода в __str__"""
        stock = 0
        for product in self.__goods:
            stock += product.quantity
        return stock


    def __str__(self):
        return f'{self.category_name}, количество продуктов: {len(self)} шт.'


class IterCategory:
    def __init__(self, category):
        self.category = category

    def __iter__(self):
        self.current_value = -1
        return self

    def __next__(self):
        self.current_value += 1
        if self.current_value < len(self.category):
            return self.category[self.current_value]
        else:
            raise StopIteration
