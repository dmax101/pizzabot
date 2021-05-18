import pytest
import os
import pprint as pp

from model.order import Order

@pytest.fixture(scope="function", autouse=True)
def order():
    order = Order("Danilo")

    return order

def test_name_is_ok(order):
    pp.pprint(order.client)
    assert "Danilo" == order.client, "Has to be Danilo"

def test_add_item_sc(order):
    item = {
        "name": "pepperoni",
        "value": 46.50
    }

    order.add_item_sc(item)

    for item_sc in order.shopping_cart:
        pp.pprint(item_sc)

    assert len(order.shopping_cart) == 1

    order.remove_item_sc("pepperoni")

def test_remove_item_sc(order):
    pp.pprint(order.shopping_cart)

    order.add_item_sc({
        "name": "pepperoni",
        "value": 46.50
    })
    order.add_item_sc({
        "name": "calabresa",
        "value": 30.50
    })

    order.remove_item_sc("pepperoni")

    assert len(order.shopping_cart) == 1, "Has to be equal 1"
    assert "pepperoni" not in order.shopping_cart, "Can't have Pepperoni"

    order.remove_item_sc("calabresa")

def test_calculate_total(order):
    order.add_item_sc({
        "name": "pepperoni",
        "value": 46.50
    })
    order.add_item_sc({
        "name": "calabresa",
        "value": 30.50
    })

    total = order.calculate_total()

    assert total == 77.00, "Has to be 77.00"
    