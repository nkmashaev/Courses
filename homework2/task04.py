"""
Implementation of the fouth task. The task is to write
a function that accepts another function as an argument. Then
it should return such a function, so the every call to initial
one should be cached
"""
from collections import Callable
from typing import Any, List


def cache(func: Callable) -> Callable:
    """
    The function cache accepts another function as an
    argument and return such a function, so the every
    call to an initial one cached.

    :param func: function to cache
    :return: function that cached every call to initial one
    """
    func_result = {}

    def action(*argv: List[Any]) -> Any:
        """
        The implementation of function that save initial function
        and cache every call to it

        :param argv: arguments of the original function
        :return: cached result
        """
        key = tuple(argv)
        if key not in func_result:
            func_result[key] = func(*key)
        return func_result[key]

    return action


def func(a, b):
    return (a ** b) ** 2


if __name__ == "__main__":
    cache_func = cache(func)
    some = 100, 200
    val_1 = cache_func(*some)
    val_2 = cache_func(*some)
    print(id(val_1), id(val_2))

    assert val_1 is val_2
