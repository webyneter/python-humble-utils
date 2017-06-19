def get_class_name(cls: type) -> str:
    return cls.__class__.__name__


def get_class_qualname(cls: type) -> str:
    return cls.__qualname__
