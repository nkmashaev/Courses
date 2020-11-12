from typing import Any, Callable, List


def cache(times: int) -> Callable:
    def decorator(func: Callable) -> Callable:

        cached_dict = {}

        def wrapper(*args: List[Any]) -> Any:
            key = tuple(args)
            if key in cached_dict:
                cached_dict[key][0] -= 1
                val = cached_dict[key][1]
                if cached_dict[key][0] == 0:
                    del cached_dict[key]
            else:
                val = func(*args)
                cached_dict[key] = [times, val]
            return val

        return wrapper

    return decorator


@cache(times=2)
def f():
    return input("? ")
