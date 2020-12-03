import pytest

from homework7.task01 import find_occurances
from homework7.task02 import backspace_compare
from homework7.task03 import tic_tac_toe_checker


# test task1
def test_find_occurances():
    test_tree = {
        "first": ["RED", "BLUE"],
        "second": {
            "simple_key": ["simple", "list", "of", "RED", "valued"],
        },
        "third": {
            "abc": "BLUE",
            "jhl": "RED",
            "complex_key": {
                "key1": "value1",
                "key2": "RED",
                "key3": ["a", "lot", "of", "values", {"nested_key": "RED"}],
            },
        },
        "fourth": "RED",
    }
    assert find_occurances(test_tree, "RED") == 6


# test task2
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
