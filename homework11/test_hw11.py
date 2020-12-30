from enum import Enum

import pytest

from homework11.task01 import SimplifiedEnum
from homework11.task02 import Order, flex_discount, morning_discount

# task1 test


@pytest.fixture
def metaClassEnumForTest():
    class testEnum(metaclass=SimplifiedEnum):
        __keys = ("TOP", "BOTTOM", "LEFT", "RIGHT")

    return testEnum


def test_simplifiedEnum(metaClassEnumForTest):
    assert metaClassEnumForTest.TOP == "TOP"
    assert metaClassEnumForTest.BOTTOM == "BOTTOM"
    assert metaClassEnumForTest.LEFT == "LEFT"
    assert metaClassEnumForTest.RIGHT == "RIGHT"


# task2 test
@pytest.mark.parametrize(
    ["pure_price", "expected"],
    [
        (100, 50.0),
        (200, 150.0),
    ],
)
def test_flex_dicount(pure_price, expected):
    order = Order(pure_price, flex_discount)
    assert order.final_price() == pytest.approx(expected)


@pytest.mark.parametrize(
    ["pure_price", "expected"],
    [
        (100, 50.0),
        (200, 100.0),
    ],
)
def test_morning_discount(pure_price, expected):
    order = Order(pure_price, morning_discount)
    assert order.final_price() == pytest.approx(expected)
