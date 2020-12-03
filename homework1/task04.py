"""
Implemention of fourth task of hw1
Given four lists A, B, C, D of integer values,
    compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.
We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.
"""

from typing import List


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    """
    Function check_sum_of_four calculates ow many tuples (i, j, k, l) there are such
    that A[i] + B[j] + C[k] + D[l] is zero

    :param a: first list of integer values
    :param b: second list of integer values
    :param c: third list of integer values
    :param d: fourth list of integer values
    :return: number of tuples (i, j, k, l) for which A[i] + B[j] + C[k] + D[l] condition is true
    """
    counter = 0

    for a_i in a:
        for b_j in b:
            for c_k in c:
                for d_l in d:
                    if a_i + b_j + c_k + d_l == 0:
                        counter += 1
    return counter
