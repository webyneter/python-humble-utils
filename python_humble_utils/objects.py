import gc
from typing import TypeVar, Any, Optional, Callable, Iterable, Type, Sequence

T = TypeVar("T")
M = TypeVar("M")


def flatten(
    obj: Any, flatten_dicts_by_values: bool = True, coerce: Optional[Callable[[T], M]] = None
) -> Iterable[M]:
    """Flatten an arbitrarily complex object.

    :param obj: an obj to flatten.
    :param flatten_dicts_by_values: if True, mapping will be flattened by values, otherwise by keys.
    :param coerce: a callable used to coerce items of the resulting iterable to
    :return: a recursively-constructed iterable of the object's constituents.
    """
    if isinstance(obj, dict):
        if flatten_dicts_by_values:
            items = obj.values()
        else:
            items = obj.keys()
        items = list(items)
        yield from flatten(items, flatten_dicts_by_values=flatten_dicts_by_values, coerce=coerce)
    elif isinstance(obj, list):
        for item in obj:
            yield from flatten(item, flatten_dicts_by_values=flatten_dicts_by_values, coerce=coerce)
    else:
        if coerce is not None:
            yield coerce(obj)
        else:
            yield obj


def get_all_instances(cls: Type[T]) -> Sequence[T]:
    """Get all class instances.

    :type cls: class whose instances need to be looked up.
    """
    all_instances = []

    all_objects = gc.get_objects()
    for obj in all_objects:
        if isinstance(obj, cls):
            all_instances.append(obj)

    return all_instances
