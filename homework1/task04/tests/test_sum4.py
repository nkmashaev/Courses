from typing import List

import pytest
from task04 import check_sum_of_four


@pytest.mark.parametrize(
    ["a", "b", "c", "d", "expected_result"],
    [
        ([1, 2, 3], [0, 0, 0], [2, 1, 0], [-3, -3, -3], 27),
        ([41, 51, 49], [239, 30, 40], [54, 43, 12], [-4, 2, 0], 0),
        ([3, -5, -3], [5, -4, 0], [-5, 2, 1], [-2, -3, 5], 5),
    ],
)
def test_check_sum_of_four(
    a: List[int], b: List[int], c: List[int], d: List[int], expected_result: int
):
    actual_result = check_sum_of_four(a, b, c, d)

    assert actual_result == expected_result
