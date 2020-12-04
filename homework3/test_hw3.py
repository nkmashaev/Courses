from typing import List
from unittest import mock

import pytest

from homework3.task01 import cache
from homework3.task02 import perform_calculate
from homework3.task03 import make_filter
from homework3.task04 import is_armstrong


# task01 tests
def test_cache_only_cached():
    times_var = 3
    m = mock.Mock()
    n = m
    m = cache(times_var)(m)
    for i in range(times_var):
        m(1, 2, 3, [4, 5, 6], key=2)
    assert n.call_count == 1
    assert n.call_args_list == [((1, 2, 3, [4, 5, 6]), {"key": 2})]


def test_cache_recache():
    times_var = 3
    m = mock.Mock()
    n = m
    m = cache(times_var)(m)
    for i in range(times_var * 2):
        m(1, 2, 3, [4, 5, 6], key=2)
    assert n.call_count == 2
    assert n.call_args_list == [
        ((1, 2, 3, [4, 5, 6]), {"key": 2}),
        ((1, 2, 3, [4, 5, 6]), {"key": 2}),
    ]


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
        [9474],
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
        [2592],
        [929348],
        [99432842123],
    ],
)
def test_is_armstrong_false(not_armstrong):
    assert is_armstrong(not_armstrong) is False
