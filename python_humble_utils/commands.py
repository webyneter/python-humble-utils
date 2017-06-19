import os
import re
import uuid
from ast import literal_eval
from typing import NamedTuple, Sequence

__all__ = [
    '',
]


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
    dir_path = os.path.split(file_path)[0]
    return dir_path


def parse_tuple_from_string(string_tuple: str) -> tuple:
    """
    Parse tuple from its literal string representation.

    :param string_tuple: tuple literal string representation e.g. '('this', 'is', 'a', 'tuple')'.
    :return: parsed tuple.
    """
    return literal_eval(string_tuple)


def generate_random_file_basename(file_extension: str) -> str:
    file_basename = '%s%s' % (str(uuid.uuid4().hex), file_extension)
    return file_basename


def generate_random_file_path(dir_path: str,
                              file_extension: str) -> str:
    file_basename = generate_random_file_basename(file_extension=file_extension)
    file_path = os.path.join(dir_path, file_basename)
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


# todo: test
# todo: resolve code duplication
def get_file_paths(dir_path: str,
                   allowed_file_extensions: Sequence[str] = None,
                   recursively: bool = False) -> Sequence[str]:
    """
    Get paths of files with extensions specified from the directory specified.

    :param dir_path: directory path.
    :param allowed_file_extensions: if not None, only files with these extensions will match.
    :param recursively: whether or not to traverse the directpry recursively.
    :return: a list of matching files.
    """
    file_paths = []
    if recursively:
        for root, _, file_basenames in os.walk(dir_path):
            for file_basename in file_basenames:
                file_path = os.path.join(root, file_basename)
                if allowed_file_extensions:
                    file_extension = extract_file_name_and_extension(file_path).extension
                    if file_extension not in allowed_file_extensions:
                        continue
                file_paths.append(file_path)
    else:
        for file_basename in os.listdir(dir_path):
            file_path = os.path.join(dir_path, file_basename)
            if allowed_file_extensions:
                file_extension = extract_file_name_and_extension(file_path).extension
                if file_extension not in allowed_file_extensions:
                    continue
            file_paths.append(file_path)
    return file_paths


# todo: test
def generate_tmp_file_path(tmpdir_factory,
                           file_name_with_extension: str,
                           tmp_file_dir_path: str = None) -> str:
    """
    Generate file path rooted in a temporary dir.

    :param tmpdir_factory: py.test's tmpdir_factory fixture.
    :param file_name_with_extension: e.g. 'file.ext'
    :param tmp_file_dir_path: generated tmp file directory path relative to base tmp dir,
    e.g. 'path/relative/to/basetemp'.
    :return: generated file path.
    """
    tmp_file_dir = tmpdir_factory.getbasetemp()

    if tmp_file_dir_path:
        if os.path.isabs(tmp_file_dir_path):
            raise ValueError('tmp_file_dir_path must be a relative path!')
        # http://stackoverflow.com/a/16595356/1557013
        for tmp_file_dir_path_part in os.path.normpath(tmp_file_dir_path).split(os.sep):
            # Accounting for possible path separator at the end.
            if tmp_file_dir_path_part:
                tmp_file_dir.mktemp(tmp_file_dir_path_part)

    file_path = str(tmp_file_dir.join(file_name_with_extension))
    return file_path


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
