"""
The implementation of the first task. The first task consists of next problems^
1) Find of 10 longest words consisting from largest amount of unique symbols
2) Find rarest symbol for document
3) Count every punctuation char
4) Count every non ascii char
5) Find most common non ascii char for document
"""


import os
import string
from functools import cmp_to_key
from typing import List


def compare(word1: str, word2: str) -> int:
    """
    Comparator for the first step solution. Accepts two words and
    compare it according to properties which is described in the first
    point of the assingment

    :param word1: first word to compare
    :param word2: second word to compare
    :return: the result of comparison
    """
    uniq_char_numb1 = len(set(word1))
    uniq_char_numb2 = len(set(word2))
    if uniq_char_numb1 > uniq_char_numb2:
        return -1
    elif uniq_char_numb1 < uniq_char_numb2:
        return 1
    else:
        if len(word1) > len(word2):
            return -1
        elif len(word1) < len(word2):
            return 1
        else:
            return 0


def get_longest_diverse_words(file_path: str) -> List[str]:
    """
    This function is designed to search ten longest words
    consisting from largest amount of unique symbols

    :param file_path: Data file name
    :return: list of words
    """
    word_list = []
    with open(file_path, "r") as in_file:
        for line in in_file:
            word_list = word_list + [
                bytes(word, "utf-8").decode("unicode_escape") for word in line.split()
            ]
    word_list.sort(key=cmp_to_key(compare))
    return word_list[:10]


def get_rarest_char(file_path: str) -> str:
    """
    Find rarest symbol for document

    :param file_path: Data file name
    :return: rarest symbol
    """
    freq_dict = {}
    buff = ""
    with open(file_path, "r") as in_file:
        for line in in_file:
            for char in line:
                buff = buff + char
                if buff.startswith("\\"):
                    if len(buff) == 6:
                        buff = bytes(buff, "utf-8").decode("unicode_escape")
                        if buff in freq_dict:
                            freq_dict[buff] += 1
                        else:
                            freq_dict[buff] = 1
                        buff = ""
                else:
                    if buff in freq_dict:
                        freq_dict[buff] += 1
                    else:
                        freq_dict[buff] = 1
                    buff = ""
    rarest, freq = None, 0
    for key, val in freq_dict.items():
        if rarest is None or freq > val:
            freq = val
            rarest = key
            is_first = False
    return rarest


def count_punctuation_char(file_path: str) -> int:
    """
    Count number of punctuation chars

    :param file_path: Data file name
    :return: number of punctuation chars
    """
    numb = 0
    buff = ""
    with open(file_path, "r") as in_file:
        for line in in_file:
            for char in line:
                buff = buff + char
                if buff.startswith("\\"):
                    if len(buff) == 6:
                        buff = bytes(buff, "utf-8").decode("unicode_escape")
                        if buff in string.punctuation:
                            numb += 1
                        buff = ""
                else:
                    if buff in string.punctuation:
                        numb += 1
                    buff = ""
    return numb


def count_non_ascii_chars(file_path: str) -> int:
    """
    Count every non ascii char

    :param file_path: Data file name
    :return: number of non ascii char
    """
    non_ascii_numb = 0
    buff = ""
    with open(file_path, "r") as in_file:
        for line in in_file:
            for char in line:
                buff = buff + char
                if buff.startswith("\\"):
                    if len(buff) == 6:
                        buff = bytes(buff, "utf-8").decode("unicode_escape")
                        if buff not in string.printable:
                            non_ascii_numb += 1
                        buff = ""
                else:
                    if buff not in string.printable:
                        non_ascii_numb += 1
                    buff = ""
    return non_ascii_numb


def get_most_common_non_ascii_char(file_path: str) -> str:
    """
    Find most common non ascii char for document

    :param file_path: Data file name
    :return: non ascii char
    """
    freq_dict = {}
    buff = ""
    with open(file_path, "r") as in_file:
        for line in in_file:
            for char in line:
                buff = buff + char
                if buff.startswith("\\"):
                    if len(buff) == 6:
                        buff = bytes(buff, "utf-8").decode("unicode_escape")
                        if buff not in string.printable:
                            if buff in freq_dict:
                                freq_dict[buff] += 1
                            else:
                                freq_dict[buff] = 1
                        buff = ""
                else:
                    if buff not in string.printable:
                        if buff in freq_dict:
                            freq_dict[buff] += 1
                        else:
                            freq_dict[buff] = 1
                    buff = ""
    # print(freq_dict)
    common, freq = None, 0
    for key, val in freq_dict.items():
        if freq < val:
            freq, common = val, key
    return common


if __name__ == "__main__":
    file_path = os.path.join("test_data_files", "data.txt")
    print(get_longest_diverse_words(file_path))
    print(get_rarest_char(file_path))
    print(count_punctuation_char(file_path))
    print(count_non_ascii_chars(file_path))
    print(get_most_common_non_ascii_char(file_path))
