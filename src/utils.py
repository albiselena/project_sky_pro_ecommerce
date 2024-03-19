import json
from config import ROOT_DIR
import os

products_file = os.path.join(ROOT_DIR, "src/products.json")


def load_products(products_file):
    """Распаковка файла json"""
    with open(products_file, "r") as f:
        return json.load(f)

#print(type(load_products(products_file)))



