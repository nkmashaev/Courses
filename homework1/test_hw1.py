import os
from collections import Sequence
from typing import List, Tuple

import pytest

import homework1.task04 as task04
import homework1.task05 as task05
from homework1.task01 import check_power_of_2
from homework1.task02 import check_fibonacci
from homework1.task03 import find_maximum_and_minimum


# task1 tester
@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        (65536, True),
        (12, False),
        (0, False),
        (876251, False),
        (433836, False),
        (128, True),
        (1024, True),
        (-4, False),
    ],
)
def test_power_of_2(value: int, expected_result: bool):
    actual_result = check_power_of_2(value)

    assert actual_result == expected_result


# task2_tester
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
def test_check_fibonacci(data: Sequence, expected_result: bool):
    actual_result = check_fibonacci(data)

    assert actual_result == expected_result


# task_tester3
@pytest.fixture
def task03_file():
    test_file_name = os.path.join(".", ".test_task03")

    yield test_file_name

    if os.path.exists(test_file_name):
        os.remove(test_file_name)


@pytest.mark.parametrize(
    ["file_data", "expected_result"],
    [
        (["2", "4", "5", "7", "1", "2", "3", "6"], (1, 7)),
        (["1", "2", "3", "4", "5"], (1, 5)),
        (["31", "41", "59", "26", "41", "58"], (26, 59)),
        (["5", "2", "4", "6", "1", "3"], (1, 6)),
        (["3", "41", "52", "26", "38", "57", "9", "49"], (3, 57)),
    ],
)
def test_min_max(task03_file, file_data, expected_result):
    with open(task03_file, "w") as test_file:
        test_file.write("\n".join(file_data))
    actual_result = find_maximum_and_minimum(task03_file)
    assert actual_result == expected_result


# task4 tester
@pytest.mark.parametrize(
    ["a", "b", "c", "d", "expected_result"],
    [
        ([1, 2, 3], [0, 0, 0], [2, 1, 0], [-3, -3, -3], 27),
        ([41, 51, 49], [239, 30, 40], [54, 43, 12], [-4, 2, 0], 0),
        ([3, -5, -3], [5, -4, 0], [-5, 2, 1], [-2, -3, 5], 5),
    ],
)
def test_check_sum_of_four_enumeration(
    a: List[int], b: List[int], c: List[int], d: List[int], expected_result: int
):
    actual_result = task04.check_sum_of_enumeration(a, b, c, d)

    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["a", "b", "c", "d", "expected_result"],
    [
        ([1, 2, 3], [0, 0, 0], [2, 1, 0], [-3, -3, -3], 27),
        ([41, 51, 49], [239, 30, 40], [54, 43, 12], [-4, 2, 0], 0),
        ([3, -5, -3], [5, -4, 0], [-5, 2, 1], [-2, -3, 5], 5),
    ],
)
def test_check_sum_of_four_dict(
    a: List[int], b: List[int], c: List[int], d: List[int], expected_result: int
):
    actual_result = task04.check_sum_of_four_dict(a, b, c, d)

    assert actual_result == expected_result


# task5 tester
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
    actual_result = task05.find_maximal_subarray_sum(nums, k)

    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["nums", "k", "expected_result"],
    [
        ([1, 3, -1, -3, 5, 3, 6, 7], 3, 16),
        ([1, -17, 9, -17, 16, 14, 7, -13, 20], 2, 30),
        ([1, -17, 9, -17, 16, 14, 7, -13, 20], 1, 20),
        ([20, -15, -24, -1, 3], 3, 20),
    ],
)
def test_find_maximal_subarray_sum_deque(nums: List[int], k: int, expected_result: int):
    actual_result = task05.find_maximal_subarray_sum_deque(nums, k)

    assert actual_result == expected_result
