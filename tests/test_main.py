import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from main import Product, Category

# Тесты для класса Product
def test_product_str():
    product = Product("Test Product", "Test Description", 100.0, 10)
    assert str(product) == "Test Product, 100.0 руб. Остаток: 10 шт."

def test_product_add():
    product_a = Product("Product A", "A", 100.0, 10) # 100 * 10 = 1000
    product_b = Product("Product B", "B", 200.0, 2)  # 200 * 2 = 400
    assert (product_a + product_b) == 1400.0

# Тесты для класса Category
def test_category_str():
    p1 = Product("P1", "D1", 10.0, 3)
    p2 = Product("P2", "D2", 20.0, 7)
    category = Category("Test Category", "Test Cat Desc", [p1, p2])
    assert str(category) == "Test Category, количество продуктов: 10 шт."

    p3 = Product("P3", "D3", 1.0, 5)
    category_another = Category("Another Category", "Another Cat Desc", [p1, p2, p3])
    assert str(category_another) == "Another Category, количество продуктов: 15 шт."

    empty_category = Category("Empty Category", "Empty Cat Desc", [])
    assert str(empty_category) == "Empty Category, количество продуктов: 0 шт." 