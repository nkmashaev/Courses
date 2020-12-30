from functools import partial
from pathlib import Path

import pytest

import homework9.task01 as task01
import homework9.task02 as task02
import homework9.task03 as task03


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
@pytest.fixture
def MyTestExp():
    class MyExp(ZeroDivisionError):
        pass

    return MyExp


def test_suppressor_class_suppress():
    with task02.Suppressor(IndexError):
        assert [0][1]


def test_suppressor_class_wrong_exception():
    with pytest.raises(IndexError):
        with task02.Suppressor(AttributeError):
            [0][1]


def test_suppressor_class_suppress_inheritance(MyTestExp):
    with task02.Suppressor(MyTestExp):
        assert 1 / 0


def test_suppressor_class_inheritance_wrong(MyTestExp):
    with pytest.raises(IndexError):
        with task02.Suppressor(MyTestExp):
            assert [0][1]


def test_suppressor_generator_suppress_inheritance(MyTestExp):
    with task02.suppressor(MyTestExp):
        assert 1 / 0


def test_suppressor_generator_inheritance_wrong(MyTestExp):
    with pytest.raises(IndexError):
        with task02.suppressor(MyTestExp):
            assert [0][1]


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
