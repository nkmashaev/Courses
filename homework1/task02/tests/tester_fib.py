from collections import Sequence

import pytest
from fibonacci.fibonacci_sequance import check_fibonacci


@pytest.mark.parametrize(
    ["data", "expected_result"],
    [
        ((0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377), True),
        ((0, 2, 2, 4, 6, 10, 16, 26, 42), False),
        ((1, 3, 5, 7, 10, 12, 16, 20, 21, 23), False),
        ((1, 1, 10, 11, 21), False),
        ((1, 1, 2, 3, 5, 8), True),
    ],
)
def test_power_of_2(data: Sequence, expected_result: bool):
    actual_result = check_fibonacci(data)

    assert actual_result == expected_result
