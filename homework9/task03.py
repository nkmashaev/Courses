import os
from functools import partial
from itertools import chain
from pathlib import Path
from typing import Callable, Iterator, Optional, Union


def read_all_data(file_path: Path):
    with open(file_path) as in_file:
        yield in_file.read().rstrip()


def universal_file_counter(
    dir_path: Path, file_extension: str, tokenizer: Optional[Callable] = None
) -> int:
    if not dir_path.exists():
        raise AttributeError("Error: Could not find directory!")
    if not dir_path.is_dir():
        raise AttributeError("Error: Expected directory path!")
    file_names = (
        f
        for f in dir_path.iterdir()
        if f.is_file() and f.suffix.endswith(file_extension)
    )
    in_files = chain(*(read_all_data(f) for f in file_names))

    token_numb = 0
    if tokenizer is None:
        tokenizer = partial(str.split, sep="\n")
    for token in map(tokenizer, in_files):
        token_numb += len(token)
    return token_numb
