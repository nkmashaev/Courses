from typing import List

import pytest

from homework3.task01 import cache
from homework3.task02 import perform_calculate
from homework3.task03 import make_filter
from homework3.task04 import is_armstrong


# task01 tests
def test_cache_true():
    times_var = 3

    @cache(times=times_var)
    def func_for_test(a: int, b: int) -> List[int]:
        return a ** b ** 2

    res = func_for_test(100, 200)
    assert all([func_for_test(100, 200) is res for i in range(times_var)]) is True


@pytest.mark.parametrize(
    ["times", "val"],
    [[1, 3], [2, 5], [3, 10]],
)
def test_cache_false(times, val):
    times_var = 3

    @cache(times=times_var)
    def func_for_test(a: int, b: int) -> List[int]:
        return a ** b ** 2

    res = func_for_test(100, 200)
    assert all([func_for_test(100, 200) is res for i in range(2 * times_var)]) is False


# task02 tests
def test_perform_calculate_result():
    assert 1024259 == perform_calculate()[1]


def test_perform_calculate_exec_time():
    assert 60.0 > perform_calculate()[0]


# task03 tests
sample_data = [
    {
        "name": "Bill",
        "last_name": "Gilbert",
        "occupation": "was here",
        "type": "person",
    },
    {
        "is_dead": True,
        "kind": "parrot",
        "type": "bird",
        "name": "polly",
        "mame": "no",
        "lame": "ok",
    },
    {"type": "person", "name": "polly", "status": "student"},
    {"name": "victor", "type": "bird", "home": "Peppe's"},
    {"type": "bird", "name": "Kesha"},
]


@pytest.mark.parametrize(
    ["kwargs", "data", "expected"],
    [
        [{"name": "polly", "type": "bird"}, sample_data, [sample_data[1]]],
        [{"type": "polly", "name": "bird"}, sample_data, [sample_data[1]]],
        [{"type": "person"}, sample_data, [sample_data[0], sample_data[2]]],
    ],
)
def test_make_filter(kwargs, data, expected):
    res = make_filter(**kwargs).apply(data)
    assert all([i in expected for i in res]) is True


# test for is_armstrong(int) func of task04. Tests for armstrong numbs
@pytest.mark.parametrize(
    ["armstrong_numb"],
    [
        [1],
        [2],
        [3],
        [4],
        [5],
        [6],
        [7],
        [8],
        [9],
        [153],
        [370],
        [371],
        [407],
        [1634],
        [8208],
        [9474],
        [54748],
        [92727],
        [93084],
        [548834],
        [1741725],
        [4210818],
        [9800817],
        [9926315],
    ],
)
def test_is_armstrong_true(armstrong_numb):
    assert is_armstrong(armstrong_numb) is True


# tests for not armstrong numb
@pytest.mark.parametrize(
    ["not_armstrong"],
    [
        [15],
        [35],
        [936],
        [34],
        [18],
        [2592],
        [800],
        [900],
        [990],
        [501],
        [341],
        [999],
        [253],
        [807],
        [42925],
        [2395932],
        [243249223],
        [32939492],
        [8943247],
        [23592034283],
        [2482384],
        [75462],
        [929348],
        [99432842123],
    ],
)
def test_is_armstrong_false(not_armstrong):
    assert is_armstrong(not_armstrong) is False
