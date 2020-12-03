"""
Given an array of size n, find the most common and the least common
elements. The most common element is the element that appears more than
n // 2 times. The least common element is the element that appears 
fewer than other

You may assume that the array is non-empty and the most common element
always exist in the array
"""


from collections import defaultdict
from typing import List, Tuple


def major_and_minor_elem(inp: List) -> Tuple[int, int]:
    """
    The implementation of the second task problem using defaultdict.
    Find the most and the least common elements and return tuple consist of them

    :param inp: array of elements
    :return: most and least common elements tuple
    """
    numbers_dict = defaultdict(int)

    for x in inp:
        numbers_dict[x] += 1

    is_first = True
    for key, val in numbers_dict.items():
        if is_first or min_numb > val:
            min_numb = val
            minor = key
        if is_first or maj_numb < val:
            maj_numb = val
            major = key
        is_first = False
    return major, minor


def major_and_minor_elem_2(inp: List) -> Tuple[int, int]:
    """
    The implementation of the second task problem using list sort.
    Find the most and the least common elements and return tuple consist of them

    :param inp: array of elements
    :return: most and least common elements tuple
    """

    sort_list = sorted(inp)
    min_numb = 1
    maj_numb = 1
    curr_el = sort_list[0]
    minor = curr_el
    major = curr_el
    curr_numb = 1

    for x in sort_list[1:]:
        if x != curr_el:
            if min_numb > curr_numb:
                min_numb = curr_numb
                minor = curr_el
            if maj_numb < curr_numb:
                max_numb = curr_numb
                major = curr_el
            curr_numb = 0
            curr_el = x
        curr_numb += 1

    if min_numb > curr_numb:
        min_numb = curr_numb
        minor = curr_el
    if maj_numb < curr_numb:
        max_numb = curr_numb
        major = curr_el
    return major, minor


if __name__ == "__main__":
    print(major_and_minor_elem([3, 2, 3]))
    print(major_and_minor_elem([2, 2, 1, 1, 1, 2, 2]))
    print(major_and_minor_elem([3, 3, 3, 2, 1, 2, 3]))
