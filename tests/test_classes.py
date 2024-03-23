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
        file[0]['products']
    )


def test_init_category(category):
    assert category.category_name == "Смартфоны"
    assert category.category_description == "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни"
    assert category.quantity_category == 1
    assert category.quantity_unique_goods == 3



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




