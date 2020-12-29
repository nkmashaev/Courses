import pytest

from homework7.task01 import find_occurences
from homework7.task02 import backspace_compare, string_constructor
from homework7.task03 import tic_tac_toe_checker


# test task1
@pytest.fixture
def task1_test_tree():
    test_tree = {
        "first": ["RED", "BLUE"],
        "second": {
            "simple_key": ["simple", "list", "of", "RED", "valued"],
        },
        "third": {
            "abc": "BLUE",
            "jhl": "RED",
            "complex_key": {
                "key1": "third",
                "key2": "RED",
                "key3": ["a", "lot", "of", "values", {"nested_key": "RED"}],
            },
        },
        "fourth": "RED",
    }
    return test_tree


@pytest.mark.parametrize(
    ["arg", "occ_numb"],
    (("RED", 6), ("third", 2)),
)
def test_find_occurences(task1_test_tree, arg, occ_numb):
    assert find_occurences(task1_test_tree, arg) == occ_numb


# test task2
@pytest.mark.parametrize(
    ["str_with_backspace", "result"],
    [
        ("hello #!", "hello!"),
        ("hi####", ""),
        ("m#e#a#t#", ""),
    ],
)
def test_string_constructor(str_with_backspace, result):
    assert string_constructor(str_with_backspace) == result


@pytest.mark.parametrize(
    ["first", "second"],
    [
        ("asasv#####", ""),
        ("ab#c", "ad#c"),
        ("a##c", "#a#c"),
        ("###", ""),
    ],
)
def test_backspace_compare_return_True(first, second):
    assert backspace_compare(first, second) == True


@pytest.mark.parametrize(
    ["first", "second"],
    [
        ("sub", "###"),
        ("mesh", "m##e#sh"),
    ],
)
def test_backspace_compare_return_False(first, second):
    assert backspace_compare(first, second) == False


# test task3
def test_tic_tac_toe_x_wins():
    board = [["-", "-", "o"], ["-", "o", "o"], ["x", "x", "x"]]
    assert tic_tac_toe_checker(board) == "x wins!"


def test_tic_tac_toe_o_wins():
    board = [["-", "-", "o"], ["-", "o", "o"], ["o", "x", "x"]]
    assert tic_tac_toe_checker(board) == "o wins!"


def test_tic_tac_toe_unfinished():
    board = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
    assert tic_tac_toe_checker(board) == "unfinished"
