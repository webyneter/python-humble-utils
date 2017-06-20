import os
import re
import uuid
from ast import literal_eval
from typing import NamedTuple, Sequence, Iterable


def extract_file_name_with_extension(file_path: str) -> str:
    """
    Extract file name with extension.

    :param file_path: path to the file.
    :return: file name with extension.
    """
    return os.path.basename(file_path)


NameAndExtension = NamedTuple('NameAndExtension', [
    ('name', str),
    ('extension', str)
])


def extract_file_name_and_extension(file_path: str) -> NameAndExtension:
    """
    Extract file name and extension as named tuple.

    :param file_path: path to the file.
    :return: named tuple of file name and extension.
    """
    name_with_extension = extract_file_name_with_extension(file_path)
    name, extension = os.path.splitext(name_with_extension)
    return NameAndExtension(name, extension)


def extract_file_dir_path(file_path: str) -> str:
    """
    Extract directory path.

    :param file_path: path to the file.
    :return: directory path.
    """
    return os.path.split(file_path)[0]


def parse_tuple_from_string(string_tuple: str) -> tuple:
    """
    Parse tuple from its literal string representation.

    :param string_tuple: tuple literal string representation e.g. `'('this', 'is', 'a', 'tuple')'`.
    :return: parsed tuple.
    """
    return literal_eval(string_tuple)


def generate_hex_uuid_4() -> str:
    """
    Generate UUID (version 4) in hexadecimal representation.

    :return: hexadecimal representation of version 4 UUID.
    """
    return str(uuid.uuid4().hex)


def generate_random_dir_path(subdir_count: int = 0) -> str:
    """
    Generate randomly-named directory.

    :param subdir_count: a number of subdirectories to generate in the directory root.
    :return: directory root path.
    """
    if subdir_count < 0:
        raise ValueError("'subdir_count' must not be negative!")

    dir_path = os.path.join(generate_hex_uuid_4(), '')
    if subdir_count > 0:
        for l in range(subdir_count):
            dir_path = os.path.join(dir_path, generate_hex_uuid_4())

    return dir_path


def generate_random_file_name_with_extension(file_extension: str) -> str:
    """
    Generate random file name with the extension specified.

    :param file_extension: file name extensionm e.g. `.ext`.
    :return: file name with the extension.
    """
    return "{}{}".format(generate_hex_uuid_4(), file_extension)


def read_file(file_path: str,
              as_single_line: bool = False) -> str:
    """
    Read file content.

    :param file_path: path to the file.
    :param as_single_line: whether or not the file is to be read as a single line.
    :return: file content.
    """
    with open(file_path, 'r') as file:
        lines = []
        for line in file.readlines():
            if as_single_line:
                line = line.replace(os.linesep, '')
            lines.append(line)
        return ''.join(lines)


def yield_file_paths(dir_path: str,
                     allowed_file_extensions: Sequence[str],
                     recursively: bool = False) -> Iterable[str]:
    """
    Yield file paths.

    :param dir_path: path to the containing directory.
    :param allowed_file_extensions: file extensions to match against e.g. `['.abc', '.def']`.
    :param recursively: whether or not the directory is to be recursively traversed.
    :return: file paths.
    """

    def filter_allowed_file_paths(dp: str, fbs: Sequence[str], afe: Sequence[str]) -> Iterable[str]:
        for fb in fbs:
            p = os.path.join(dp, fb)
            if extract_file_name_and_extension(p).extension in afe:
                yield p

    if recursively:
        for root_dir_path, _, file_basenames in os.walk(dir_path):
            yield from filter_allowed_file_paths(dir_path, file_basenames, allowed_file_extensions)
    else:
        file_basenames = os.listdir(dir_path)
        yield from filter_allowed_file_paths(dir_path, file_basenames, allowed_file_extensions)


def create_or_update_file(file_path: str,
                          file_content: str = '',
                          file_content_encoding: str = 'utf-8') -> None:
    """
    Create or update file.

    :param file_path: path to the file.
    :param file_content: file content.
    :param file_content_encoding: file content encoding e.g. `latin-1`.
    """
    with open(file_path, 'wb+') as file:
        file.write(file_content.encode(file_content_encoding))


def camel_or_pascal_case_to_snake_case(s: str) -> str:
    """
    Convert `camelCased` or `PascalCased` string to `snake_case`.

    Based on https://stackoverflow.com/a/1176023/1557013.

    :param s: string in `camelCase` or `PascalCase`.
    :return: string in `snake_case`.
    """
    snake_case = re.sub('([a-z0-9])([A-Z])', r'\1_\2', re.sub('(.)([A-Z][a-z]+)', r'\1_\2', s))
    snake_case = snake_case.lower()
    return snake_case


def camel_or_pascal_case_to_space_delimited(s: str) -> str:
    """
    Convert `camelCased` or `PascalCased` string to space-delimited.

    Based on https://stackoverflow.com/a/9283563/1557013.

    :param s: string in `camelCase` or `PascalCase`.
    :return: space-delimited string.
    """
    space_delimited = re.sub(r'((?<=[a-z])[A-Z]|(?<!\A)[A-Z](?=[a-z]))', r' \1', s)
    return space_delimited


def get_all_subclasses(cls: type,
                       including_self: bool = False) -> Sequence[type]:
    """
    Get all subclasses.

    :param cls: class to lookup subclasses of.
    :param including_self: whether or not the the :param cls: itself is to be accounted for.
    :return: :param cls: subclasses.
    """
    all_subclasses = [cls] if including_self else []
    for c in cls.__subclasses__():
        all_subclasses += get_all_subclasses(c, True)
    return all_subclasses


def get_class_name(cls: type) -> str:
    """
    Get class name.

    :param cls: class.
    :return: :param cls: name.
    """
    return cls.__class__.__name__


def get_class_qualname(cls: type) -> str:
    """
    Get fully-qualified class name.

    :param cls: class.
    :return: fully-qualified :param cls: name.
    """
    return cls.__qualname__
