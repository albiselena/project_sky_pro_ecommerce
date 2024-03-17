import pytest

from src.classes import *


@pytest.fixture()
def category():
    return Category(
        "фрукты",
        "сладкие",
        ["инжир", "финики", "банан", "инжир", "хурма", "банан", "папайя"]
    )


def test_category(category):
    assert category.title == "фрукты"
    assert category.description == "сладкие"
    assert category.goods == ["инжир", "финики", "банан", "инжир", "хурма", "банан", "папайя"]
    assert category.quantity_category == 1
    assert len(category.unique_goods) == 5
    assert category.quantity_unique_goods == 5


@pytest.fixture()
def product():
    return Product(
        "инжир",
        "улучшает настроение",
        485.30,
        35
    )


def test_product(product):
    assert product.title == "инжир"
    assert product.description == "улучшает настроение"
    assert product.price == 485.30
    assert product.stock == 35
