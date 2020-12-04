"""
Modification of decorator cache from previous homework:
current implemention would give out cached value up to times number only
"""

from typing import Any, Callable, List


def cache(times: int) -> Callable[[Any], Any]:
    """
    The function cache accepts another function as an
    argument and return such a function, so the every
    call to an initial one cached for times times

    :param func: function to cache
    :return: function that cached every call to initial one
    """

    def decorator(func: Callable[[Any], Any]) -> Callable[[Any], Any]:

        func_res = []
        func_arg = []
        func_num = []

        def wrapper(*args: Any, **kwargs: Any) -> Any:
            given_arg = (args, kwargs)
            for i, (curr_arg, res) in enumerate(zip(func_arg, func_res)):
                if curr_arg == given_arg:
                    func_num[i] -= 1
                    if func_num[i] == 0:
                        del func_num[i]
                        del func_res[i]
                        del func_arg[i]
                    return res

            res = func(*given_arg[0], **given_arg[1])
            func_res.append(res)
            func_arg.append(given_arg)
            func_num.append(times)
            return res

        return wrapper

    return decorator


@cache(times=2)
def f():
    return input("? ")
