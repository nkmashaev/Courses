"""
The implementation of the third task. The function combinations takes K
lists as arguments and returns all possible lists of K items where the 
first element is from the first list, the second is from the
second one and so one.
"""

from itertools import product
from typing import Any, List


def combinations(*args: List[Any]) -> List[List]:
    """
    Takes K lists as arguments and returns all possible lists of K
    items where the first element is from the first list,
    the second is from the second and so one.

    :param args: list containing K lists
    :return: list of lists
    """
    combo = []
    accumulation = [None] * len(args)
    recursive_combine(*args, accumulation=accumulation, rec_depth=0, comb_storage=combo)
    return combo


def recursive_combine(
    *args: List[Any], accumulation: List[Any], rec_depth: int, comb_storage: List[List]
):
    """
    The list combination recursive builder. Takes initial list of lists,
    current list for construction accumulation, current element in accumulation
    to construct which is defined by recursive depth(rec_depth), combinations storage
    comb_storage.

    :param args: initial list of lists
    :param accumulation: current combination list for construction
    :param rec_depth: current recursive depth
    :param comb_storage: storage of combinations
    """
    is_last = len(args) == 1
    for x in args[0]:
        accumulation[rec_depth] = x
        if is_last:
            curr_accum = [y for y in accumulation]
            comb_storage.append(curr_accum)
        else:
            recursive_combine(
                *args[1:],
                accumulation=accumulation,
                rec_depth=rec_depth + 1,
                comb_storage=comb_storage
            )


def combine_with_itertools(*args: List[Any]) -> List[List]:
    """
    Takes K lists as arguments and returns all possible lists of K
    items where the first element is from the first list,
    the second is from the second and so one.

    The base of that implemetation is itertools.product function

    :param args: list containing K lists
    :return: list of lists
    """
    return [list(x) for x in product(*args)]


if __name__ == "__main__":
    print(combinations([1, 2], [3, 4]))
    print(combinations([1, 2, 3], [4, 5, 6], [7, 8, 9, 10]))
    print(combine_with_itertools([1, 2], [3, 4]))
