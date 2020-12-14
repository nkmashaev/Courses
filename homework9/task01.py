import os
from heapq import merge
from pathlib import Path
from typing import Iterator, List, Union


def get_data(file_path: Union[Path, str]) -> Iterator[int]:
    if isinstance(file_path, Path):
        if not file_path.exists():
            raise AttributeError("Error: Path not exists")
        if not file_path.is_file():
            raise AttributeError("Error: Expected file name")
    if isinstance(file_path, str):
        if not os.path.exists(file_path):
            raise AttributeError("Error: Path not exists")
        if not os.path.isfile(file_path):
            raise AttributeError("Error: Expected file name")
    else:
        raise AttributeError("Error: Expected str or Path")
    with open(file_path, "r") as in_file:
        while True:
            data = in_file.readline()
            if not data:
                break
            yield int(data)


def merge_sorted_files(file_list: List[Union[Path, str]]) -> Iterator:
    files_iterators = (get_data(in_file) for in_file in file_list)
    yield from merge(*files_iterators)
