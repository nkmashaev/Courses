"""
Module fibonacci is designed to check if the sequence is
a Fibonacci one.

According to wikipedia https://en.wikipedia.org/wiki/Fibonacci_number
the Fibonacci numbers form a sequence, called the Fibonacci sequence,
such that each number is the sum of the two preceding ones, starting from
0 and 1. It also can start with ones
"""
from collections import Sequence


def check_fibonacci(data: Sequence) -> bool:
    """
    Accepts a Sequence of integer, and return if the
    given sequence is a Fibonacci sequence

    :param data: sequence of integer is needed to be check
    :type data: Sequence[int]
    :return: if the given sequence is a Fibonacci sequence
    :rtype: bool
    """

    # get number of sequence elements
    numb_of_elements = len(data)

    # if the number of elements in data Sequence less then
    # two the condition F[n] = F[n-1] + F[n-2] can not be
    # satisfied, so that means that the considered sequence
    # is not the Fibonacci one
    if numb_of_elements <= 2:
        return False

    # Perform first two elements checking
    if not ((data[0] == 0 and data[1] == 1) or (data[0] == 1 and data[1] == 1)):
        return False

    # Perform condition checking
    for i in range(2, numb_of_elements, 1):
        if data[i] != data[i - 1] + data[i - 2]:
            return False

    # All condition are satisfied. The sequence is the
    # Fibonacci one
    return True
