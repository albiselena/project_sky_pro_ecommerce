from src.utils import *
from config import ROOT_DIR
import os

def test_load_products():
    """Проверка работоспособности распаковки файла json"""
    operation_path = os.path.join(ROOT_DIR, "src", 'products.json')
    assert type(load_products(operation_path) == list and len(load_products(operation_path)) > 0)
    assert type(load_products(operation_path)[0]) == dict
    assert type(load_products(operation_path)[0]['name']) == str
    assert type(load_products(operation_path)[0]['products'][0]['price']) == float
    assert type(load_products(operation_path)[0]['products'][0]['quantity']) == int
