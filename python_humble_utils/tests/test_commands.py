import os
from typing import Callable

import pytest

from .classes import Foo, Boo, Moo
from ..commands import extract_file_name_with_extension, extract_file_dir_path, extract_file_name_and_extension, \
    generate_random_file_path, generate_random_file_basename, parse_tuple_from_string, read_file, \
    create_or_update_file, camel_or_pascal_case_to_snake_case, get_all_subclasses, \
    camel_or_pascal_case_to_space_delimited
from ..conftest import ValidFileMeta
from ..pytest_commands import generate_tmp_file_path


def test_when_extracting_file_name_with_extension_given_valid_arguments_should_succeed(valid_file_meta: ValidFileMeta):
    actual = extract_file_name_with_extension(valid_file_meta.file_path)
    expected = valid_file_meta.file_name_with_extension
    assert actual == expected


def test_when_extracting_file_name_and_extension_given_valid_arguments_should_succeed(valid_file_meta: ValidFileMeta):
    name_and_extension = extract_file_name_and_extension(valid_file_meta.file_path)
    assert name_and_extension.name == valid_file_meta.file_name
    assert name_and_extension.extension == valid_file_meta.file_extension


def test_when_extracting_file_dir_path_given_valid_arguments_should_succeed(valid_file_meta: ValidFileMeta):
    file_path = valid_file_meta.file_path
    actual_file_dir_path = extract_file_dir_path(file_path=file_path)
    assert actual_file_dir_path == valid_file_meta.dir_path


@pytest.mark.parametrize('tup,verifier', [
    ("('text', 42)", lambda tup: isinstance(tup, tuple) and tup[0] == 'text' and tup[1] == 42),
    ('()', lambda tup: tup == ()),
])
def test_when_parsing_tuple_from_string_given_valid_arguments_should_succeed(tup: str,
                                                                             verifier: Callable[[str], bool]):
    parsed_tup = parse_tuple_from_string(tup)
    assert verifier(parsed_tup)


def test_when_generating_random_file_basename_given_valid_arguments_should_succeed(valid_file_meta: ValidFileMeta):
    file_extension = valid_file_meta.file_extension
    actual_file_basename = generate_random_file_basename(file_extension)
    assert extract_file_name_and_extension(actual_file_basename).extension == file_extension


def test_when_generating_random_file_path_given_valid_arguments_should_succeed(valid_file_meta: ValidFileMeta):
    dir_path = valid_file_meta.dir_path
    file_extension = valid_file_meta.file_extension
    actual_file_path = generate_random_file_path(dir_path=dir_path,
                                                 file_extension=file_extension)
    assert extract_file_dir_path(actual_file_path) == dir_path
    assert extract_file_name_and_extension(actual_file_path).extension == file_extension


@pytest.mark.parametrize('as_single_line,verifier', [
    (True, lambda file_content: os.linesep not in file_content),
    (False, lambda file_content: os.linesep in file_content),
])
def test_when_reading_file_given_valid_arguments_should_succeed(tmpdir_factory,
                                                                valid_file_meta: ValidFileMeta,
                                                                as_single_line: bool,
                                                                verifier: Callable[[str], bool]):
    tmp_file_path = generate_tmp_file_path(tmpdir_factory, valid_file_meta.file_name_with_extension)
    create_or_update_file(tmp_file_path, valid_file_meta.file_content, valid_file_meta.file_content_encoding)

    file_content = read_file(tmp_file_path, as_single_line)

    assert verifier(file_content)


def test_when_getting_file_paths_given_dir_with_files_without_subdirs_should_succeed():
    pass


def test_when_getting_file_paths_given_dir_with_files_and_subdirs_should_succeed():
    pass


def test_when_creating_or_updating_file_given_file_not_exists_should_create_file(tmpdir_factory,
                                                                                 valid_file_meta: ValidFileMeta):
    tmp_dir_path = os.path.join(str(tmpdir_factory.getbasetemp()), valid_file_meta.dir_path)
    tmp_file_path = os.path.join(tmp_dir_path, valid_file_meta.file_name_with_extension)

    os.makedirs(tmp_dir_path, exist_ok=True)
    create_or_update_file(tmp_file_path, valid_file_meta.file_content, valid_file_meta.file_content_encoding)

    with open(tmp_file_path, 'rb') as file:
        assert file.read().decode(valid_file_meta.file_content_encoding) == valid_file_meta.file_content


def test_when_creating_or_updating_file_given_file_exists_should_update_file(tmpdir_factory,
                                                                             valid_file_meta: ValidFileMeta):
    tmp_dir_path = os.path.join(str(tmpdir_factory.getbasetemp()), valid_file_meta.dir_path)
    tmp_file_path = os.path.join(tmp_dir_path, valid_file_meta.file_name_with_extension)

    os.makedirs(tmp_dir_path, exist_ok=True)
    with open(tmp_file_path, 'wb') as file:
        file.write(valid_file_meta.file_content.encode(valid_file_meta.file_content_encoding))

    updated_file_content = valid_file_meta.file_content + ' (+ this update)'
    create_or_update_file(tmp_file_path, updated_file_content, valid_file_meta.file_content_encoding)

    with open(tmp_file_path, 'rb') as file:
        assert file.read().decode(valid_file_meta.file_content_encoding) == updated_file_content


@pytest.mark.parametrize('s,expected', [
    ('IAmInCamelCase_but_i_am_not_AndHereAmIOnceAgain',
     'i_am_in_camel_case_but_i_am_not__and_here_am_i_once_again'),
    ('iAmInPascalCase_but_i_am_not_andHereAmIOnceAgain',
     'i_am_in_pascal_case_but_i_am_not_and_here_am_i_once_again'),
])
def test_when_converting_camel_or_pascal_case_to_snake_case_given_valid_arguments_should_succeed(s: str,
                                                                                                 expected: str):
    assert camel_or_pascal_case_to_snake_case(s) == expected


def test_when_getting_all_subclasses_given_no_subclasses_should_succeed():
    assert set(get_all_subclasses(Moo, False)) == set()
    assert set(get_all_subclasses(Moo, True)) == {Moo}


def test_when_getting_all_subclasses_given_self_included_should_succeed():
    assert set(get_all_subclasses(Foo, True)) == {Foo, Boo, Moo}


def test_when_getting_all_subclasses_given_self_excluded_should_succeed():
    assert set(get_all_subclasses(Foo, False)) == {Boo, Moo}


@pytest.mark.parametrize('s,expected', [
    ('iAmASTRANGECamelCase',
     'i Am ASTRANGE Camel Case'),
    ('YetAnotherOneBUTNOWWhilebeingastrangeOneIamStillAProperPascalCase',
     'Yet Another One BUTNOW Whilebeingastrange One Iam Still A Proper Pascal Case'),
])
def test_when_converting_camel_or_pascal_case_to_space_delimited_given_valid_arguments_should_succeed(s: str,
                                                                                                      expected: str):
    actual = camel_or_pascal_case_to_space_delimited(s)
    assert actual == expected
