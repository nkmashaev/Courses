from collections import defaultdict
from itertools import zip_longest


def string_constructor(string: str) -> str:
    str_list = []
    for a in string:
        if a != "#":
            str_list.append(a)
        elif len(str_list) > 0:
            str_list.pop()
    return "".join(str_list)


def backspace_compare(first: str, second: str) -> True:
    return string_constructor(first) == string_constructor(second)
