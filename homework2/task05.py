"""
The solution of fifth task problem. There is an implementation
of a function that accept any iterable of unique value and then
it behaves as range function
"""


import string
from collections.abc import Iterable
from typing import Any, List


def custom_range(
    iterable_seq: Iterable, start: Any, end: Any = None, step: int = 1, /
) -> List[Any]:
    """
    Accept any iterable of unique value and then it behaves
    as range function

    :param iterable_seq: Initiale sequence of unique values
    :param start: start value
    :param end: end value
    :param step: step between elements of original sequance
    :return: list that consists elements from start to end
    with the step from initial seq
    """

    seq_list = list(iterable_seq)
    first_index = 0

    if end is None:
        last_index = seq_list.index(start)
    else:
        first_index = seq_list.index(start)
        last_index = seq_list.index(end)
        if step < 0:
            first_index, last_index = last_index, first_index
    return seq_list[first_index:last_index:step]


if __name__ == "__main__":
    print(custom_range(string.ascii_lowercase, "g"))
    print(custom_range(string.ascii_lowercase, "g", "p"))
    argv = ["g", "p", -2]
    print(custom_range(string.ascii_lowercase, *argv))
    print(custom_range("pure", "r"))
