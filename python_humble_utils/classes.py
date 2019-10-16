from typing import Collection, Type


def get_all_subclasses(cls: Type, including_self: bool = False) -> Collection[Type]:
    """Get all subclasses.

    :param cls: class to lookup subclasses of.
    :param including_self: whether or not the the :param cls: itself is to be accounted for.
    :return: :param cls: subclasses.
    """
    all_subclasses = [cls] if including_self else []
    for c in cls.__subclasses__():
        all_subclasses += get_all_subclasses(c, True)
    return all_subclasses
