from typing import Any


def is_integer(str_to_check: str) -> bool:
    try:
        float(str_to_check)
    except ValueError:
        return False
    else:
        return float(str_to_check).is_integer()


class KeyValueStorage:
    """
    KeyValueStorage is designed to read attributes from the file
    with name path_to_file and attach it to itself
    """

    def __init__(self, path_to_file: str):
        self.__storage = {}

        with open(path_to_file, "r") as in_file:
            for line in in_file:
                key, val = line.strip().split("=")
                if is_integer(val):
                    val = int(val)
                if not key.isidentifier():
                    raise ValueError("Error: Unacceptable attribute name is given!")
                if not key in KeyValueStorage.__dict__:
                    self.__storage[key] = val

    def __getitem__(self, key: Any) -> Any:
        return self.__storage[key]

    def __getattr__(self, key: str) -> Any:
        return self.__storage[key]
