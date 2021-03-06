# I decided to write a code that generates data filtering object from a list of keyword parameters:
from typing import Any, Callable


class Filter:
    """
    Helper filter class. Accepts a list of single-argument
    functions that return True if object in list conforms to some criteria
    """

    def __init__(self, functions: Callable[[Any], Any]):
        self.functions = functions

    def apply(self, data: Any):
        return [item for item in data if all(i(item) for i in self.functions)]


# example of usage:
# positive_even = Filter(lamba a: a % 2 == 0, lambda a: a > 0, lambda a: isinstance(int, a)))
# positive_even.apply(range(100)) should return only even numbers from 0 to 99


def make_filter(**keywords: Any):
    """
    Generate filter object for specified keywords

    :param keywords: key for filter creation
    """
    filter_funcs = []
    for key, value in keywords.items():
        # we need to storage global variables in local ones using assingment by default. Else
        # only last key and value will be storaged in filter function
        def keyword_filter_func(val, key=key, value=value):
            return val[key] == value

        filter_funcs.append(keyword_filter_func)
    return Filter(filter_funcs)


# make_filter(name='polly', type='bird').apply(sample_data) should return only second entry from the list

# There are multiple bugs in this code. Find them all and write tests for faulty cases.
