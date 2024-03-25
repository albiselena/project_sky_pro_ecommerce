from typing import List, Dict

import pytest
from src.utils import load_products
from config import ROOT_DIR
import os
from src.class_category import *
from src.class_product import *

file = load_products(os.path.join(ROOT_DIR, "src", 'products.json'))


# Тесты для класса Category
@pytest.fixture()
def category():
    return Category(
        file[0]['name'],
        file[0]['description'],
        file[0]['products']
    )


def test_init_category(category):
    assert category.category_name == "Смартфоны"
    assert category.category_description == ("Смартфоны, как средство не только коммуникации, но и получение "
                                             "дополнительных функций для удобства жизни")
    assert category.quantity_category == 1
    assert category.quantity_unique_goods == 3


@pytest.fixture()
def dictionary_category():
    return Category('Телефоны',
                    'Разные',
                    [Product('Samsung', '256GB', '180000.0', 3),
                     Product('Iphone 15', '512GB', 210000.0, 7)])


def test_goods_category(dictionary_category):
    """Тест на геттер goods класса Category, тест len, тест str"""
    assert dictionary_category.goods == ['Samsung, 180000.0 руб. Остаток: 3 шт.',
                                         'Iphone 15, 210000.0 руб. Остаток: 7 шт.']
    assert len(dictionary_category) == 10
    assert str(dictionary_category) == "Телефоны, количество продуктов: 10 шт."


# Тесты для класса Product
@pytest.fixture()
def product():
    return Product(
        file[1]['products'][0]['name'],
        file[1]['products'][0]['description'],
        file[1]['products'][0]['price'],
        file[1]['products'][0]['quantity']
    )


def test_init_product(product):
    assert product.name == "55\" QLED 4K"
    assert product.description == "Фоновая подсветка"
    assert product.price == 123000.0
    assert product.quantity == 7


@pytest.fixture()
def dictionary():
    return Product.from_dict(file[0]['products'][0])


def test_class_product(dictionary):
    """Тест на класс-метод в классе Product """
    assert dictionary.name == "Samsung Galaxy C23 Ultra"
    assert dictionary.description == "256GB, Серый цвет, 200MP камера"
    assert dictionary.price == 180000.0
    assert dictionary.quantity == 5


def test_product_price():
    """Тест на сеттер price класса Product"""
    product = Product('телевизор', 'плазма', 10, 3)
    product.price = 0
    assert product.price == 10
    product.price = 27000
    assert product.price == 27000


def test_str_product(dictionary):
    """Тест на метод __str__ класса Product"""
    assert str(dictionary) == "Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_add_product(product):
    """Тест на метод __add__ класса Product, в файле json цена = 123000, кол-во 7"""
    product_other = Product('телевизор', 'плазма', 123000.0, 3)
    assert product + product_other == 1230000.0


# Тест класс IterCategory

def test_iter_category():
    """Тест на итератор класса IterCategory"""
    itercategory = IterCategory(['Телефоны', 'DVD', 'Телевизоры'])
    assert itercategory.category == ['Телефоны', 'DVD', 'Телевизоры']
    cat_list = [i for i in itercategory]
    assert cat_list == ['Телефоны', 'DVD', 'Телевизоры']
