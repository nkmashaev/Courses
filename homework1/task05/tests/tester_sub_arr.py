from typing import List

import pytest
from task05 import find_maximal_subarray_sum


@pytest.mark.parametrize(
    ["nums", "k", "expected_result"],
    [
        ([1, 3, -1, -3, 5, 3, 6, 7], 3, 16),
        ([1, -17, 9, -17, 16, 14, 7, -13, 20], 2, 30),
        ([1, -17, 9, -17, 16, 14, 7, -13, 20], 1, 20),
        ([20, -15, -24, -1, 3], 3, 20),
    ],
)
def test_find_maximal_subarray_sum(nums: List[int], k: int, expected_result: int):
    actual_result = find_maximal_subarray_sum(nums, k)

    assert actual_result == expected_result
