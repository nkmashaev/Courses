"""
The implementation of the fifth task:
Given a list of integers numbers "nums".
You need to find a sub-array with length less equal to "k", with maximal sum.
The written function should return the sum of this sub-array.
Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    result = 16
"""

from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    """
    Function find_maximal_subarray_sum is designed to find a sub-array with length less
    equal k, with maximal sum. The written function should return the sum of this sub-array

    :param nums: a list of integers numbers
    :param k: max subarray size
    :return: the sum of found subarray
    """
    maximal_subarray_sum = nums[0]
    numb_of_elements = len(nums)

    for i in range(0, numb_of_elements - k + 1, 1):
        temp_max = nums[i]
        temp_sum = nums[i]
        for j in range(i + 1, i + k):
            temp_sum += nums[j]
            if temp_sum > temp_max:
                temp_max = temp_sum
        if temp_max > maximal_subarray_sum:
            maximal_subarray_sum = temp_max

    return maximal_subarray_sum
