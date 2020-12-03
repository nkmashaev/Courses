from collections import defaultdict
from typing import Any

example_tree = {
    "first": ["RED", "BLUE"],
    "second": {
        "simple_key": ["simple", "list", "of", "RED", "valued"],
    },
    "third": {
        "abc": "BLUE",
        "jhl": "RED",
        "complex_key": {
            "key1": "value1",
            "key2": "RED",
            "key3": ["a", "lot", "of", "values", {"nested_key": "RED"}],
        },
    },
    "fourth": "RED",
}


def find_occurances(tree: dict, element: Any) -> int:
    elements_dict = defaultdict(int)

    def rec_counter(storage):
        if isinstance(storage, (int, str, bool)):
            elements_dict[storage] += 1
        elif isinstance(storage, dict):
            for i in storage.values():
                rec_counter(i)
        else:
            for i in storage:
                rec_counter(i)

    rec_counter(tree)
    return elements_dict[element]


if __name__ == "__main__":
    print(find_occurances(example_tree, "RED"))
