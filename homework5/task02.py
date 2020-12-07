import functools
from typing import Any, Callable


def origfunc(orig_func):
    def save_func(func):
        setattr(func, "__original_func", orig_func)
        functools.update_wrapper(wrapper=func, wrapped=orig_func)
        return func

    return save_func


def print_result(func):
    @origfunc(func)
    def wrapper(*args, **kwargs):
        """
        Function-wrapper which print
        result of an original function
        """

        result = func(*args, **kwargs)
        print(result)
        return result

    return wrapper


@print_result
def custom_sum(*args):
    """
    This function can sum any objects
    which have __add__
    """
    return functools.reduce(lambda x, y: x + y, args)


if __name__ == "__main__":
    custom_sum([1, 2, 3], [4, 5])
    custom_sum(1, 2, 3, 4)
    print(custom_sum.__doc__)
    print(custom_sum.__name__)
    # the result returns without printing
    without_print = custom_sum.__original_func
    without_print(1, 2, 3, 4)
