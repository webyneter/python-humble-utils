from typing import Optional, Callable, TypeVar

import pytest

from python_humble_utils.objects import flatten

T = TypeVar("T")
M = TypeVar("M")


@pytest.mark.parametrize("flatten_dicts_by_values", [False, True])
@pytest.mark.parametrize("coerce", [None, str])
def test_flatten(flatten_dicts_by_values: bool, coerce: Optional[Callable[[T], M]]):
    obj = [
        "something",
        1,
        [2, bytes(range(3))],
        4,
        ["5", {"6": 7, 7: [8], "9": [10, "11", 12, ["13", "14", 15]]}],
    ]

    flattened_obj = list(
        flatten(obj, flatten_dicts_by_values=flatten_dicts_by_values, coerce=coerce)
    )

    if flatten_dicts_by_values:
        expected = ["something", 1, 2, bytes(range(3)), 4, "5", 7, 8, 10, "11", 12, "13", "14", 15]
    else:
        expected = ["something", 1, 2, bytes(range(3)), 4, "5", "6", 7, "9"]
    if coerce is not None:
        expected = [coerce(e) for e in expected]
    assert flattened_obj == expected
