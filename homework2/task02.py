"""
Given an array of size n, find the most common and the least common
elements. The most common element is the element that appears more than
n // 2 times. The least common element is the element that appears 
fewer than other

You may assume that the array is non-empty and the most common element
always exist in the array
"""


from typing import List, Tuple


def major_and_minor_elem(inp: List) -> Tuple[int, int]:
    """
    The implementation of the second task problem. Find the most and
    the least common elements and return tuple consist of them

    :param inp: array of elements
    :return: most and least common elements tuple
    """
    numbers_dict = {}

    for x in inp:
        if x in numbers_dict:
            numbers_dict[x] += 1
        else:
            numbers_dict.update({x: 0})

    min_numb = 0
    maj_numb = 0
    minor = 0
    major = 0
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


if __name__ == "__main__":
    print(major_and_minor_elem([3, 2, 3]))
    print(major_and_minor_elem([2, 2, 1, 1, 1, 2, 2]))
    print(major_and_minor_elem([3, 3, 3, 2, 1, 2, 3]))
