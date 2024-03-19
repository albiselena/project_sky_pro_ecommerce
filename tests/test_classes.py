import pytest
from src.utils import load_products
from config import ROOT_DIR
import os
from src.classes import *

file = load_products(os.path.join(ROOT_DIR, "src", 'products.json'))

@pytest.fixture()
def category():
    return Category(
        file[0]['name'],
        file[0]['description'],
        file[0]['products'][0]['name']
    )


def test_category(category):
    assert category.title == "Смартфоны"
    assert category.description == "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни"
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
    assert product.title == "55\" QLED 4K"
    assert product.description == "Фоновая подсветка"
    assert product.price == 123000.0
    assert product.stock == 7
