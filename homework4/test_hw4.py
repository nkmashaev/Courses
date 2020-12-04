import os
import sys
import urllib.request
from unittest.mock import MagicMock, patch
from urllib.error import HTTPError

import pytest

import homework4.task04 as task04
import homework4.task05 as task05
from homework4.task01 import read_magic_numb
from homework4.task02 import count_dots_on_i
from homework4.task03 import my_precios_logger


@pytest.fixture
def temp_file_creation():
    test_file_name = ".test_file"
    yield test_file_name
    if os.path.exists(test_file_name):
        os.remove(test_file_name)


@pytest.mark.parametrize(
    "numb",
    [
        1,
        1.2,
        1.5,
        2.5,
        2.8,
        2.99,
    ],
)
def test_read_magic_numb_true(temp_file_creation, numb):
    with open(temp_file_creation, "w") as in_file:
        in_file.write(f"{numb:.11E}")
    assert read_magic_numb(temp_file_creation) is True


@pytest.mark.parametrize(
    "numb",
    [
        -1,
        0.0,
        0.5,
        0.99,
        3,
        3.5,
    ],
)
def test_read_magic_numb_false(temp_file_creation, numb):
    with open(temp_file_creation, "w") as in_file:
        in_file.write(f"{numb:.11E}")
    assert read_magic_numb(temp_file_creation) is False


@pytest.mark.parametrize(
    "non_int",
    [
        "afkdf",
        "5 10",
        "",
    ],
)
def test_read_magic_numb_val_exception(temp_file_creation, non_int):
    with open(temp_file_creation, "w") as in_file:
        in_file.write(f"{non_int}")
    with pytest.raises(ValueError, match="could not convert string to float: "):
        read_magic_numb(temp_file_creation)


def test_read_magic_numb_file_not_exists():
    assert os.path.exists("file_not_exist") is False
    assert read_magic_numb("file_not_exist") is None


# task02 tests
def test_count_dots_on_i_data(monkeypatch):
    monkeypatch.setattr(
        urllib.request,
        "urlopen",
        MagicMock(
            return_value=[
                b"<html>",
                b"<head>iii</head>",
                b"<body>qqq</body>",
                b"</html>",
            ]
        ),
    )
    assert count_dots_on_i("https://200") == 3


def test_count_dots_on_i_not_connection(monkeypatch):
    monkeypatch.setattr(
        urllib.request,
        "urlopen",
        MagicMock(side_effect=HTTPError(404, "NF", "", "", "")),
    )
    with pytest.raises(ValueError, match="Unreachable https://404"):
        count_dots_on_i("https://404")


# task03 tests
def test_my_precios_logger_stdout(capfd):
    my_precios_logger("OK")
    stdout, stderr = capfd.readouterr()
    assert stdout == "OK\n"
    assert stderr == ""


def test_my_precios_logger_stderr(capfd):
    my_precios_logger("error: log is empty")
    stdout, stderr = capfd.readouterr()
    assert stdout == ""
    assert stderr.endswith("error: log is empty\n")


# task04 tests
@pytest.mark.parametrize(
    ["numb", "expected"],
    [
        (5, ["1", "2", "Fizz", "4", "Buzz"]),
        (
            15,
            [
                "1",
                "2",
                "Fizz",
                "4",
                "Buzz",
                "Fizz",
                "7",
                "8",
                "Fizz",
                "Buzz",
                "11",
                "Fizz",
                "13",
                "14",
                "FizzBuzz",
            ],
        ),
    ],
)
def test_fizzbuzz_task4(numb, expected):
    actual = task04.fizzbuzz(numb)
    assert actual == expected


@pytest.mark.parametrize(
    "non_int",
    [
        "afkdf",
        "5 10",
        "",
    ],
)
def test_fizzbuzz_task4_exception(non_int):
    with pytest.raises(ValueError) as execinfo:
        task04.fizzbuzz(non_int)
    assert str(execinfo.value) == "Error: Expected integer number!"


# task05 tests
@pytest.mark.parametrize(
    ["numb", "expected"],
    [
        (5, ["1", "2", "Fizz", "4", "Buzz"]),
        (
            15,
            [
                "1",
                "2",
                "Fizz",
                "4",
                "Buzz",
                "Fizz",
                "7",
                "8",
                "Fizz",
                "Buzz",
                "11",
                "Fizz",
                "13",
                "14",
                "FizzBuzz",
            ],
        ),
    ],
)
def test_fizzbuzz_task5(numb, expected):
    actual = list(task05.fizzbuzz(numb))
    assert actual == expected


@pytest.mark.parametrize(
    "non_int",
    [
        "afkdf",
        "5 10",
        "",
    ],
)
def test_fizzbuzz_task5_exception(non_int):
    with pytest.raises(ValueError) as execinfo:
        list(task05.fizzbuzz(non_int))
    assert str(execinfo.value) == "Error: Expected integer number!"
