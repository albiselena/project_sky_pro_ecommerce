from typing import List, Dict

import pytest
from src.utils import load_products
from config import ROOT_DIR
import os
from src.class_category import *
from src.class_product import *

file = load_products(os.path.join(ROOT_DIR, "src", 'products.json'))


@pytest.fixture()
def category():
    return Category(
        file[0]['name'],
        file[0]['description'],
        file[0]['products'][0]['name']
    )


def test_category(category):
    assert category.category_name == "Смартфоны"
    assert category.category_description == "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни"
    assert category.goods == "Samsung Galaxy C23 Ultra"
    assert category.quantity_category == 1
    assert category.unique_goods == {"Samsung Galaxy C23 Ultra"}
    assert category.quantity_unique_goods == 1
    assert category.unique_category == {"Смартфоны"}


@pytest.fixture()
def product():
    return Product(
        file[1]['products'][0]['name'],
        file[1]['products'][0]['description'],
        file[1]['products'][0]['price'],
        file[1]['products'][0]['quantity']
    )


def test_product(product):
    assert product.name == "55\" QLED 4K"
    assert product.description == "Фоновая подсветка"
    assert product.price == 123000.0
    assert product.stock == 7


def test_from_dict():
    """Тест на создание объекта класса Product из словаря с данными о товаре"""
    expected = {"name": "Смартфоны", "description": "средство", "price": 12000.0, "stock": 1}
    assert Product.from_dict("Смартфоны", "средство", 12000.0, 1) == expected
    assert type(Product.from_dict("Смартфоны", "средство", 12000.0, 1)) == dict



