import os
from functools import partial
from itertools import chain
from pathlib import Path
from typing import Callable, Iterator, Optional, Union


def read_all_data(file_path: Path):
    with open(file_path) as in_file:
        yield in_file.read().rstrip()


def universal_file_counter(
    dir_path: Path, file_extension: str, tokenizer: Callable = str.split
) -> int:

    in_files = chain(*(read_all_data(f) for f in dir_path.rglob(f"*.{file_extension}")))
    token_numb = 0
    for token in map(tokenizer, in_files):
        token_numb += len(token)
    return token_numb
