import os
import re
import uuid
from ast import literal_eval
from typing import NamedTuple, Sequence


def extract_file_name_with_extension(file_path: str) -> str:
    return os.path.basename(file_path)


NameAndExtension = NamedTuple('NameAndExtension', [
    ('name', str),
    ('extension', str)
])


def extract_file_name_and_extension(file_path: str) -> NameAndExtension:
    name_with_extension = extract_file_name_with_extension(file_path)
    name, extension = os.path.splitext(name_with_extension)
    return NameAndExtension(name, extension)


def extract_file_dir_path(file_path: str) -> str:
    return os.path.split(file_path)[0]


def parse_tuple_from_string(string_tuple: str) -> tuple:
    """
    Parse tuple from its literal string representation.

    :param string_tuple: tuple literal string representation e.g. '('this', 'is', 'a', 'tuple')'.
    :return: parsed tuple.
    """
    return literal_eval(string_tuple)


def generate_hex_uuid_4() -> str:
    return str(uuid.uuid4().hex)


def generate_random_dir_path(subdir_count: int = 0) -> str:
    if subdir_count < 0:
        raise ValueError("'subdir_count' must not be negative!")

    dir_path = os.path.join(generate_hex_uuid_4(), '')
    if subdir_count > 0:
        for l in range(subdir_count):
            dir_path = os.path.join(dir_path, generate_hex_uuid_4())

    return dir_path


def generate_random_file_name_with_extension(file_extension: str) -> str:
    return "{}{}".format(generate_hex_uuid_4(), file_extension)


# todo: get rid of, combining the above two instead
def generate_random_file_path(dir_path: str,
                              file_extension: str) -> str:
    file_name_with_extension = generate_random_file_name_with_extension(file_extension)
    file_path = os.path.join(dir_path, file_name_with_extension)
    return file_path


def read_file(file_path: str,
              as_single_line: bool = False) -> str:
    with open(file_path, 'r') as file:
        lines = []
        for line in file.readlines():
            if as_single_line:
                line = line.replace(os.linesep, '')
            lines.append(line)
        return ''.join(lines)


def get_file_paths(dir_path: str,
                   allowed_file_extensions: Sequence[str],
                   recursively: bool = False) -> Sequence[str]:
    """
    Get paths of files with extensions specified from the directory specified.

    :param dir_path: directory path.
    :param allowed_file_extensions: if not None, only files with these extensions will match.
    :param recursively: whether or not to traverse the directpry recursively.
    :return: a list of matching files.
    """

    def filter_allowed_file_paths(dp: str, fbs: Sequence[str], afe: Sequence[str]) -> Sequence[str]:
        ps = []
        for fb in fbs:
            p = os.path.join(dp, fb)
            if extract_file_name_and_extension(p).extension in afe:
                ps.append(p)
        return ps

    file_paths = []

    if recursively:
        for root_dir_path, _, file_basenames in os.walk(dir_path):
            file_paths = filter_allowed_file_paths(dir_path, file_basenames, allowed_file_extensions)
    else:
        file_basenames = os.listdir(dir_path)
        file_paths = filter_allowed_file_paths(dir_path, file_basenames, allowed_file_extensions)

    return file_paths


def create_or_update_file(file_path: str,
                          file_content: str = '',
                          file_content_encoding: str = 'utf-8') -> None:
    with open(file_path, 'wb+') as file:
        file.write(file_content.encode(file_content_encoding))


def camel_or_pascal_case_to_snake_case(s: str) -> str:
    """
    https://stackoverflow.com/a/1176023/1557013
    :param s:
    :return:
    """
    snake_case = re.sub('([a-z0-9])([A-Z])', r'\1_\2', re.sub('(.)([A-Z][a-z]+)', r'\1_\2', s))
    snake_case = snake_case.lower()
    return snake_case


def get_all_subclasses(cls: type,
                       including_self: bool = False) -> Sequence[type]:
    """
    Get all subclasses of the class specified.

    :param cls: class to lookup subclasses of.
    :param including_self: whether or not to include the :param cls: itself into the result.
    :return: a list of :param cls: subclasses, with or without the :param cls: depending on the :param including_self:.
    """
    all_subclasses = [cls] if including_self else []
    for c in cls.__subclasses__():
        all_subclasses += get_all_subclasses(c, True)
    return all_subclasses


def camel_or_pascal_case_to_space_delimited(s: str) -> str:
    space_delimited = re.sub(r'((?<=[a-z])[A-Z]|(?<!\A)[A-Z](?=[a-z]))', r' \1', s)
    return space_delimited
