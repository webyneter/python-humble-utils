import gc
from typing import Optional, Callable, TypeVar

import pytest

from python_humble_utils.objects import flatten, get_all_instances
from tests.conftest import BooFoo, Foo, MooBooFoo

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


@pytest.mark.parametrize("num_instances", range(3))
@pytest.mark.parametrize("num_spoiler_instances", range(3))
def test_get_all_instances(num_instances: int, num_spoiler_instances: int):
    expected_foo_instances = [Foo() for __ in range(num_instances)]
    for i in range(num_spoiler_instances):
        if i % 2 == 0:
            BooFoo()
        else:
            MooBooFoo()

    actual_foo_instances = get_all_instances(Foo)

    assert len(actual_foo_instances) == num_instances
    assert all(fi in expected_foo_instances for fi in actual_foo_instances)
