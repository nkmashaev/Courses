from functools import partial
from pathlib import Path

import pytest

import homework9.task01 as task01
import homework9.task02 as task02
import homework9.task03 as task03


# test task1
def test_get_data_path_file_not_exists_str_path():
    with pytest.raises(AttributeError, match="Error: Path not exists"):
        next(task01.get_data("not_exist"))
        next(task01.get_data(Path("not_exists")))


def test_get_data_path_not_file(tmpdir):
    with pytest.raises(AttributeError, match="Error: Expected file name"):
        next(task01.get_data(str(tmpdir)))
        next(task01.get_data(Path(str(tmpdir))))


def test_get_data_not_str_or_path_passed():
    with pytest.raises(AttributeError, match="Error: Expected str or Path"):
        next(task01.get_data(5))


@pytest.mark.parametrize(
    "files_data",
    [
        (("1", "3", "5"), ("2", "4", "6")),
        (("1", "3"), ("2", "4", "5", "6")),
        (("1", "3", "5", "6"), ("2", "4")),
        (("1", "2"), ("3", "4"), ("5", "6")),
    ],
)
def test_merge_sorted_files(tmpdir, files_data):
    for i, data in enumerate(files_data, 1):
        test = tmpdir.join(f"test{i}").write("\n".join(data))
    test_files = [str(f) for f in tmpdir.listdir()]
    assert list(task01.merge_sorted_files(test_files)) == [1, 2, 3, 4, 5, 6]


# test task2
def test_suppressor_class_suppress():
    with task02.Suppressor(IndexError):
        assert [0][1]


def test_suppressor_class_wrong_exception():
    with pytest.raises(IndexError):
        with task02.Suppressor(AttributeError):
            [0][1]


def test_suppressor_generator_suppress():
    with task02.suppressor(IndexError):
        assert [0][1]


def test_suppressor_generator_suppress():
    with pytest.raises(IndexError):
        with task02.Suppressor(AttributeError):
            [0][1]


# test task3
def test_universal_file_counter(tmpdir):
    tmpdir.join(f"test3_1.txt").write("1\n3\n5\n")
    tmpdir.join(f"test3_2.txt").write("2\n4\n6\n")
    tmpdir.join(f"test3_3.txt").write("5=2+3\n4=1+1+1+1")

    assert 8 == task03.universal_file_counter(Path(str(tmpdir)), "txt")
    assert 5 == task03.universal_file_counter(
        Path(str(tmpdir)), "txt", partial(str.split, sep="=")
    )
    assert 7 == task03.universal_file_counter(
        Path(str(tmpdir)), "txt", partial(str.split, sep="+")
    )
    assert 0 == task03.universal_file_counter(Path(str(tmpdir)), "none")
