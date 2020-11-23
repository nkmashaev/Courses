import functools
from typing import Any, Callable


def origfunc(orig_func):
    def decorator(func):
        class FuncSaver:
            def __init__(self, orig, wrapper):
                self.__original_func = orig
                self.__wrapper = wrapper
                functools.update_wrapper(self, orig)

            def __call__(self, *args, **kwargs):
                return self.__wrapper(*args, **kwargs)

            @property
            def original_func(self):
                return self.__original_func

        return FuncSaver(orig_func, func)

    return decorator


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
    without_print = custom_sum.original_func
    # the result returns without printing
    without_print(1, 2, 3, 4)
    without_print = custom_sum.__original_func
