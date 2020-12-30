import os
from heapq import merge
from pathlib import Path
from typing import Iterator, List, Union


def get_data(file_path: Union[Path, str]) -> Iterator[int]:
    with open(file_path, "r") as in_file:
        for data in in_file:
            yield int(data)


def merge_sorted_files(file_list: List[Union[Path, str]]) -> Iterator:
    files_iterators = (get_data(in_file) for in_file in file_list)
    yield from merge(*files_iterators)
