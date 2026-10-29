"""Tests for pizza pricing, order discounts, and delivery decisions."""

import pytest

from pizza_order import delivery_status, order_discount, pizza_price


@pytest.mark.parametrize("size,toppings,cheese,expected", [
    ("small", 0, False, 200),
    ("medium", 0, False, 350),
    ("large", 0, False, 500),
    ("small", 1, False, 240),
    ("medium", 3, False, 470),
    ("medium", 4, False, 500),
    ("large", 5, False, 680),
    ("medium", 0, True, 450),
    ("large", 3, True, 720),
    ("large", 4, True, 750),
])
def test_pizza_price(size, toppings, cheese, expected):
    assert pizza_price(size, toppings, cheese) == expected


@pytest.mark.parametrize("size,toppings,cheese,message", [
    ("extra large", 0, False, "unknown size"),
    ("medium", -1, False, "invalid toppings"),
    ("small", 0, True, "cheese burst not available for small"),
])
def test_invalid_pizza(size, toppings, cheese, message):
    with pytest.raises(ValueError, match=f"^{message}$"):
        pizza_price(size, toppings, cheese)


@pytest.mark.parametrize("total,day,student,expected", [
    (0, "monday", False, 0),
    (299, "tuesday", False, 0),
    (299, "tuesday", True, 0),
    (300, "tuesday", False, 150),
    (300, "tuesday", True, 200),
    (301, "tuesday", False, 150),
    (600, "saturday", False, 0),
    (600, "saturday", True, 50),
    (600, "sunday", False, 0),
    (600, "sunday", True, 50),
    (300, "monday", False, 30),
    (300, "monday", True, 80),
    (309, "friday", False, 30),
    (310, "friday", False, 31),
    (600, "wednesday", True, 110),
    (600, "thursday", False, 60),
])
def test_order_discount(total, day, student, expected):
    assert order_discount(total, day, student) == expected


@pytest.mark.parametrize("minutes,distance,expected", [
    (20, 3, "on time"),
    (30, 10, "on time"),
    (31, 10, "late"),
    (45, 10, "late"),
    (46, 10, "free pizza"),
    (20, 10.1, "not deliverable"),
    (40, 11, "not deliverable"),
    (60, 11, "not deliverable"),
])
def test_delivery_status(minutes, distance, expected):
    assert delivery_status(minutes, distance) == expected
