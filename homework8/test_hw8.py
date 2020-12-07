import os
import sqlite3

import pytest

from homework8.task01 import KeyValueStorage, is_integer
from homework8.task02 import TableData


# test1 test
@pytest.fixture
def temp_file():
    test_file_name = os.path.join(os.path.dirname(__file__), ".test.dat")

    yield test_file_name

    if os.path.exists(test_file_name):
        os.remove(test_file_name)


@pytest.mark.parametrize(
    "integer_str",
    [
        "1",
        "5",
        "-1",
    ],
)
def test_is_integer_true(integer_str):
    assert is_integer(integer_str) == True


@pytest.mark.parametrize(
    "not_integer_str",
    [
        "1.0e-1",
        "5.1",
        "string",
    ],
)
def test_is_integer_false(not_integer_str):
    assert is_integer(not_integer_str) == False


@pytest.mark.parametrize(
    ["key", "value"],
    [
        ("name", "kek"),
        ("last_name", "top"),
        ("song", "shaliday"),
    ],
)
def test_KeyValueStorage_has_attribute(temp_file, key, value):
    with open(temp_file, "w") as test_file:
        test_file.write(f"{key}={value}\n")
    storage = KeyValueStorage(temp_file)
    assert hasattr(storage, key)


@pytest.mark.parametrize(
    ["key", "value"],
    [
        ("name", "kek"),
        ("last_name", "top"),
        ("song", "shaliday"),
    ],
)
def test_KeyValueStorage_has_item(temp_file, key, value):
    with open(temp_file, "w") as test_file:
        test_file.write(f"{key}={value}\n")
    storage = KeyValueStorage(temp_file)
    assert not storage[key] is None


@pytest.mark.parametrize(
    ["key", "value"],
    [
        ("name", "kek"),
        ("last_name", "top"),
        ("song", "shaliday"),
    ],
)
def test_KeyValueStorage_val_is_str(temp_file, key, value):
    with open(temp_file, "w") as test_file:
        test_file.write(f"{key}={value}\n")
    storage = KeyValueStorage(temp_file)
    assert isinstance(storage[key], str)
    assert isinstance(getattr(storage, f"{key}"), str)


@pytest.mark.parametrize(
    ["key", "value"],
    [
        ("Re", 100),
        ("Pr", 1),
        ("Ta", 20),
    ],
)
def test_KeyValueStorage_val_is_int(temp_file, key, value):
    with open(temp_file, "w") as test_file:
        test_file.write(f"{key}={value}\n")
    storage = KeyValueStorage(temp_file)
    assert isinstance(storage[key], int)
    assert isinstance(getattr(storage, f"{key}"), int)


@pytest.mark.parametrize(
    "bad_key",
    [
        "1",
        "1.51",
        "1x",
        "@mail",
    ],
)
def test_KeyValueStorage_bad_key_raise_valerr(temp_file, bad_key):
    with open(temp_file, "w") as test_file:
        test_file.write(f"{bad_key}=some_val\n")
    with pytest.raises(
        ValueError, match="Error: Unacceptable attribute name is given!"
    ):
        storage = KeyValueStorage(temp_file)


def test_KeyValueStorage_builtin_key(temp_file):
    with open(temp_file, "w") as test_file:
        test_file.write(f"__doc__=5\n")
    doc = KeyValueStorage.__doc__
    storage = KeyValueStorage(temp_file)
    assert storage.__doc__ == doc
    assert getattr(storage, "__doc__") == doc


# task2 test
@pytest.fixture
def table_for_test():
    temp_table_name = os.path.join(os.path.dirname(__file__), ".temp_table.db")
    con = sqlite3.connect(temp_table_name)
    cursorObj = con.cursor()
    cursorObj.execute("CREATE TABLE presidents(name text, id integer, country text)")
    con.commit()

    yield temp_table_name

    if os.path.exists(temp_table_name):
        os.remove(temp_table_name)


def test_len(table_for_test):
    data = ("Yeltsin", 1, "Russia")
    con = sqlite3.connect(table_for_test)
    cursorObj = con.cursor()
    cursorObj.execute("INSERT INTO presidents(name, id, country) VALUES(?, ?, ?)", data)
    con.commit()
    presidents = TableData(database_name=table_for_test, table_name="presidents")
    assert len(presidents) == 1

    data = ("Trump", 2, "USA")
    cursorObj.execute("INSERT INTO presidents(name, id, country) VALUES(?, ?, ?)", data)
    con.commit()
    assert len(presidents) == 2


@pytest.mark.parametrize(
    "president",
    [
        ("Yeltsin", 1, "Russia"),
        ("Trump", 2, "USA"),
    ],
)
def test_contains(table_for_test, president):
    con = sqlite3.connect(table_for_test)
    cursorObj = con.cursor()
    cursorObj.execute(
        "INSERT INTO presidents(name, id, country) VALUES(?, ?, ?)", president
    )
    con.commit()

    presidents = TableData(database_name=table_for_test, table_name="presidents")
    assert president[0] in presidents


def test_not_in_table(table_for_test):
    presidents = TableData(database_name=table_for_test, table_name="presidents")
    assert not "not in table" in presidents


def test_contains_if_table_changed(table_for_test):
    con = sqlite3.connect(table_for_test)
    cursorObj = con.cursor()
    cursorObj.execute(
        "INSERT INTO presidents(name, id, country) VALUES(?, ?, ?)",
        ("someone", 0, "test"),
    )
    con.commit()

    presidents = TableData(database_name=table_for_test, table_name="presidents")
    assert "someone" in presidents

    cursorObj.execute("UPDATE presidents SET name = 'anyone' where id = '0'")
    con.commit()
    assert not "someone" in presidents
    assert "anyone" in presidents


def test_key_access(table_for_test):
    presidents = TableData(database_name=table_for_test, table_name="presidents")
    con = sqlite3.connect(table_for_test)
    cursorObj = con.cursor()
    data = ("Yeltsin", 1, "Russia")
    cursorObj.execute("INSERT INTO presidents(name, id, country) VALUES(?, ?, ?)", data)
    con.commit()
    assert presidents["Yeltsin"] == ("Yeltsin", 1, "Russia")


def test_iterator_possibilities(table_for_test):
    presidents = TableData(database_name=table_for_test, table_name="presidents")
    con = sqlite3.connect(table_for_test)
    cursorObj = con.cursor()
    data = ("Yeltsin", 1, "Russia")
    cursorObj.execute("INSERT INTO presidents(name, id, country) VALUES(?, ?, ?)", data)
    con.commit()

    data = ("Trump", 2, "USA")
    cursorObj.execute("INSERT INTO presidents(name, id, country) VALUES(?, ?, ?)", data)
    con.commit()

    for president in presidents:
        assert president["name"] in ("Yeltsin", "Trump")
