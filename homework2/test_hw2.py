import os
import string

import pytest

import homework2.task01 as task01
from homework2.task02 import major_and_minor_elem
from homework2.task03 import combinations
from homework2.task04 import cache
from homework2.task05 import custom_range


# task01 get_longest_diverse_words tester
@pytest.mark.parametrize(
    ["file_path", "expected_range"],
    [
        (
            os.path.join("test_data_files", "data.txt"),
            [
                "Bevölkerungsabschub,",
                "Kollektivschuldiger,",
                "résistance-Bewegungen,",
                "unmißverständliche",
                "Schicksalsfiguren;",
                "politisch-strategischen",
                "Entscheidungsschlacht.",
                "Werkstättenlandschaft",
                "Gewissenserforschung,",
                "Werkstättenlandschaft",
            ],
        ),
    ],
)
def test_get_longest_diverse_words(file_path, expected_range):
    if not os.path.exists(file_path):
        file_path = os.path.join("homework2", file_path)
    actual_result = task01.get_longest_diverse_words(file_path)
    assert actual_result == expected_range


# task01 get_rarest_char
@pytest.mark.parametrize(
    ["file_path", "expected_range"],
    [
        (
            os.path.join("test_data_files", "data.txt"),
            [
                "›",
                "‹",
                "7",
                "8",
                "0",
                "Ä",
                "Y",
                "Ö",
                "'",
                "é",
                "î",
                "’",
                "X",
                "(",
                ")",
                "›",
            ],
        ),
    ],
)
def test_get_rarest_char(file_path, expected_range):
    if not os.path.exists(file_path):
        file_path = os.path.join("homework2", file_path)
    actual_result = task01.get_rarest_char(file_path)
    assert actual_result in expected_range


# task01 count_punctuation_char
@pytest.mark.parametrize(
    ["file_path", "expected_range"],
    [
        (os.path.join("test_data_files", "data.txt"), 5305),
    ],
)
def test_count_punctuation_char(file_path, expected_range):
    if not os.path.exists(file_path):
        file_path = os.path.join("homework2", file_path)
    actual_result = task01.count_punctuation_char(file_path)
    assert actual_result == expected_range


# task01 count_non_ascii_chars
@pytest.mark.parametrize(
    ["file_path", "expected_range"],
    [
        (os.path.join("test_data_files", "data.txt"), 2972),
    ],
)
def test_count_non_ascii_chars(file_path, expected_range):
    if not os.path.exists(file_path):
        file_path = os.path.join("homework2", file_path)
    actual_result = task01.count_non_ascii_chars(file_path)
    assert actual_result == expected_range


# task01 get_most_common_non_ascii_char
@pytest.mark.parametrize(
    ["file_path", "expected_range"],
    [
        (os.path.join("test_data_files", "data.txt"), ["ä"]),
    ],
)
def test_get_most_common_non_ascii_char(file_path, expected_range):
    if not os.path.exists(file_path):
        file_path = os.path.join("homework2", file_path)
    actual_result = task01.get_most_common_non_ascii_char(file_path)
    assert actual_result in expected_range


# task02 tester
@pytest.mark.parametrize(
    ["input", "expected_range"],
    [
        ([3, 2, 3], (3, 2)),
        ([2, 2, 1, 1, 1, 2, 2], (2, 1)),
        ([3, 3, 3, 2, 1, 2, 3], (3, 1)),
    ],
)
def test_major_and_minor_elem(input, expected_range):
    actual_result = major_and_minor_elem(input)
    assert actual_result == expected_range


# task03 tester
@pytest.mark.parametrize(
    ["input", "expected_range"],
    [
        ([[1, 2], [3, 4]], [[1, 3], [1, 4], [2, 3], [2, 4]]),
        (
            [["a", "b"], ["c"], ["d", "e"]],
            [["a", "c", "d"], ["a", "c", "e"], ["b", "c", "d"], ["b", "c", "e"]],
        ),
    ],
)
def test_combinations(input, expected_range):
    actual_result = combinations(*input)
    assert actual_result == expected_range


# task04 tester
def test_cache():
    some = 100, 200

    def test_func1(a, b):
        return a ** b ** 2

    cache_func1 = cache(test_func1)
    val_1 = cache_func1(*some)
    val_2 = cache_func1(*some)
    assert val_1 is val_2

    cache_func2 = cache(range)
    val_1 = cache_func2(*some)
    val_2 = cache_func2(*some)
    assert val_1 is val_2


# task05 tester
@pytest.mark.parametrize(
    ["iterable_seq", "values", "expected_range"],
    [
        (string.ascii_lowercase, ["g"], ["a", "b", "c", "d", "e", "f"]),
        (
            string.ascii_lowercase,
            ["g", "p"],
            ["g", "h", "i", "j", "k", "l", "m", "n", "o"],
        ),
        (string.ascii_lowercase, ["g", "p", 2], ["g", "i", "k", "m", "o"]),
        (string.ascii_lowercase, ["g", "p", -2], ["p", "n", "l", "j", "h"]),
        ("pure", ["r"], ["p", "u"]),
    ],
)
def test_custom_range(iterable_seq, values, expected_range):
    actual_result = custom_range(iterable_seq, *values)
    assert actual_result == expected_range
