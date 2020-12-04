"""
Implemenation of the first task of homework4. 
"""
import os


def read_magic_numb(path: str) -> bool:
    """
    Function read_magic_numb gets file path as an argument and read the
    first line of the file. If first line is a number return true if number
    in an interval [1, 3) and false otherwise.

    In case of any error, a ValueError should be thrown

    :param path: file path
    :return: true if number from file an interal [1, 3) and false otherwise
    :raise: ValueError
    """
    if os.path.exists(path):
        with open(path, "r") as in_file:
            numb = float(in_file.readline().strip())
        return 1.0 <= numb < 3.0
