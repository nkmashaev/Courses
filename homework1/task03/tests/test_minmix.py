import os
from typing import Tuple

import pytest
from min_max.task03 import find_maximum_and_minimum


@pytest.mark.parametrize(
    ["file_name", "expected_result"],
    [
        (os.path.join("test_data_files", "test1"), (1, 7)),
        (os.path.join("test_data_files", "test2"), (1, 5)),
        (os.path.join("test_data_files", "test3"), (26, 59)),
        (os.path.join("test_data_files", "test4"), (1, 6)),
        (os.path.join("test_data_files", "test5"), (3, 57)),
    ],
)
def test_min_max(file_name: str, expected_result: Tuple[int, int]):
    actual_result = find_maximum_and_minimum(file_name)

    assert actual_result == expected_result
