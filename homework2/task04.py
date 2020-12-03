"""
Implementation of the fouth task. The task is to write
a function that accepts another function as an argument. Then
it should return such a function, so the every call to initial
one should be cached
"""
from typing import Any, Callable, List


def cache(func: Callable[[Any], Any]) -> Callable[[Any], Any]:
    """
    The function cache accepts another function as an
    argument and return such a function, so the every
    call to an initial one cached.

    :param func: function to cache
    :return: function that cached every call to initial one
    """
    func_res = []
    func_arg = []

    def action(*args: Any, **kwargs: Any) -> Any:
        """
        The implementation of function that save initial function
        and cache every call to it

        :param argv: arguments of the original function
        :return: cached result
        """
        given_arg = (args, kwargs)
        for curr_arg, res in zip(func_arg, func_res):
            if curr_arg == given_arg:
                return res

        res = func(*given_arg[0], **given_arg[1])
        func_res.append(res)
        func_arg.append(given_arg)
        return res

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
