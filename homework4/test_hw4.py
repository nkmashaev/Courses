import os
from unittest.mock import patch

import pytest

import homework4.task04 as task04
import homework4.task05 as task05
from homework4.task01 import read_magic_numb
from homework4.task02 import count_dots_on_i
from homework4.task03 import my_precios_logger

# task01 tests
test_task01_fname = os.path.join(".", "test_task01_data.txt")


@pytest.fixture
def prepare_test_dir():
    yield
    if os.path.exists(test_task01_fname):
        os.remove(test_task01_fname)


@pytest.mark.usefixtures("prepare_test_dir")
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
def test_read_magic_numb_true(numb):
    with open(test_task01_fname, "w") as in_file:
        in_file.write(f"{numb:.11E}")
    assert read_magic_numb(test_task01_fname) is True


@pytest.mark.usefixtures("prepare_test_dir")
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
def test_read_magic_numb_false(numb):
    with open(test_task01_fname, "w") as in_file:
        in_file.write(f"{numb:.11E}")
    assert read_magic_numb(test_task01_fname) is False


@pytest.mark.usefixtures("prepare_test_dir")
@pytest.mark.parametrize(
    "non_int",
    [
        "afkdf",
        "5 10",
        "",
    ],
)
def test_read_magic_numb_val_exception(non_int):
    with open(test_task01_fname, "w") as in_file:
        in_file.write(f"{non_int}")
    with pytest.raises(ValueError):
        read_magic_numb(test_task01_fname)


def test_read_magic_numb_file_not_exists():
    assert os.path.exists("file_not_exist") is False
    assert read_magic_numb("file_not_exist") is None


# task02 tests
class Dummy_html:
    def __init__(self, data: str, code: int):
        self.__code__ = code
        self.__data__ = data.encode()

    def getcode(self):
        return self.__code__

    def read(self):
        return self.__data__


@patch("urllib.request.urlopen")
def test_count_dots_on_i_data(mock_url):
    url = "https://example.com/"
    mock_url.return_value = Dummy_html("i" * 59, 200)
    ans = count_dots_on_i(url)
    assert ans == 59


@patch("urllib.request.urlopen")
def test_count_dots_on_i_not_connection(mock_url):
    url = "https://example.com/"
    mock_url.return_value = Dummy_html("error code", 500)
    with pytest.raises(ValueError) as execinfo:
        ans = count_dots_on_i("https://example.com/")
    assert str(execinfo.value) == f"Unreachable {url}"


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
    assert stderr == "error: log is empty\n"


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
