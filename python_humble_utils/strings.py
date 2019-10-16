import re


def camel_or_pascal_case_to_snake_case(s: str) -> str:
    """Convert `camelCased` or `PascalCased` string to `snake_case`.

    Based on https://stackoverflow.com/a/1176023/1557013.

    :param s: string in `camelCase` or `PascalCase`.
    :return: string in `snake_case`.
    """
    snake_case = re.sub("([a-z0-9])([A-Z])", r"\1_\2", re.sub("(.)([A-Z][a-z]+)", r"\1_\2", s))
    snake_case = snake_case.lower()
    return snake_case


def camel_or_pascal_case_to_space_delimited(s: str) -> str:
    """Convert `camelCased` or `PascalCased` string to space-delimited.

    Based on https://stackoverflow.com/a/9283563/1557013.

    :param s: string in `camelCase` or `PascalCase`.
    :return: space-delimited string.
    """
    space_delimited = re.sub(r"((?<=[a-z])[A-Z]|(?<!\A)[A-Z](?=[a-z]))", r" \1", s)
    return space_delimited
