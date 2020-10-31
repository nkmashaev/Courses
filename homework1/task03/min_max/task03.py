"""
Module min_max is designed to find minimum and maximum values from an integer
sequence that is given from file
"""
from typing import Tuple


def find_maximum_and_minimum(file_name: str) -> Tuple[int, int]:
    """
    The function, which reads input line-by-line, and find maximum and minimum values.
    Function should return a tuple with the max and min values

    :param file_name: Name of file with integer sequence
    :type file_name: str
    :return: min and max values of sequence
    :rtype: tuple
    """

    min_int = 0
    max_int = 0

    # open file with name file_name and attached it to in_file
    with open(file_name) as in_file:
        # Initializing min and max values with the first
        # number in the reading sequence
        first_numb = int(in_file.readline())
        min_int = first_numb
        max_int = first_numb
        for curr_line in in_file:
            curr_numb = int(curr_line)

            # Determine if current_number is maximum
            if curr_numb > max_int:
                max_int = curr_numb

            # Determine if current_number is minimum
            if curr_numb < min_int:
                min_int = curr_numb

    return min_int, max_int
