import os
from pathlib import PurePath
from typing import Callable, Sequence
from uuid import UUID

from hypothesis import given
from hypothesis.strategies import integers
from pytest import mark, raises

from .classes import Foo, Boo, Moo
from ..commands import extract_file_name_with_extension, extract_file_dir_path, extract_file_name_and_extension, \
    generate_random_file_name_with_extension, parse_tuple_from_string, read_file, \
    create_or_update_file, camel_or_pascal_case_to_snake_case, get_all_subclasses, \
    camel_or_pascal_case_to_space_delimited, generate_random_dir_path, yield_file_paths, generate_hex_uuid_4, \
    get_class_name, get_class_qualname
from ..conftest import FileMeta
from ..pytest_commands import generate_tmp_file_path


def test_when_extracting_file_name_with_extension_given_valid_arguments_should_succeed(file_meta: FileMeta):
    actual = extract_file_name_with_extension(file_meta.file_path)
    expected = file_meta.file_name_with_extension
    assert actual == expected


def test_when_extracting_file_name_and_extension_given_valid_arguments_should_succeed(file_meta: FileMeta):
    name_and_extension = extract_file_name_and_extension(file_meta.file_path)
    assert name_and_extension.name == file_meta.file_name
    assert name_and_extension.extension == file_meta.file_extension


def test_when_extracting_file_dir_path_given_valid_arguments_should_succeed(file_meta: FileMeta):
    file_path = file_meta.file_path
    actual_file_dir_path = extract_file_dir_path(file_path=file_path)
    assert actual_file_dir_path == file_meta.dir_path


@mark.parametrize('tup,verifier', [
    ("('text', 42)", lambda tup: isinstance(tup, tuple) and tup[0] == 'text' and tup[1] == 42),
    ('()', lambda tup: tup == ()),
])
def test_when_parsing_tuple_from_string_given_valid_arguments_should_succeed(tup: str,
                                                                             verifier: Callable[[str], bool]):
    parsed_tup = parse_tuple_from_string(tup)
    assert verifier(parsed_tup)


def test_when_generating_hex_uuid_4_given_valid_arguments_should_succeed():
    retry_count = 128
    for i in range(retry_count):
        UUID(hex=generate_hex_uuid_4(), version=4)


@given(subdir_count=integers(min_value=0, max_value=2))
def test_when_generating_random_dir_path_given_valid_arguments_should_succeed(subdir_count: int):
    dir_path = generate_random_dir_path(subdir_count)
    subdirs = PurePath(dir_path).parts[1:]
    assert len(subdirs) == subdir_count
    # (Not testing the randomness of underlying UUIDs,
    # since that is the implementation detail we do not want
    # to rely upon.)


@given(subdir_count=integers(max_value=-1))
def test_when_generating_random_dir_path_given_invalid_arguments_should_raise(subdir_count: int):
    with raises(ValueError):
        generate_random_dir_path(subdir_count)


def test_when_generating_random_file_name_with_extension_given_valid_arguments_should_succeed(file_meta: FileMeta):
    file_extension = file_meta.file_extension
    actual_file_basename = generate_random_file_name_with_extension(file_extension)
    assert extract_file_name_and_extension(actual_file_basename).extension == file_extension


@mark.parametrize('as_single_line,verifier', [
    (True, lambda file_content: os.linesep not in file_content),
    (False, lambda file_content: os.linesep in file_content),
])
def test_when_reading_file_given_valid_arguments_should_succeed(tmpdir_factory,
                                                                file_meta: FileMeta,
                                                                as_single_line: bool,
                                                                verifier: Callable[[str], bool]):
    tmp_file_path = generate_tmp_file_path(tmpdir_factory, file_meta.file_name_with_extension)
    create_or_update_file(tmp_file_path, file_meta.file_content, file_meta.file_content_encoding)

    file_content = read_file(tmp_file_path, as_single_line)

    assert verifier(file_content)


@mark.parametrize('allowed_file_extensions,max_subdir_count', [
    ([], 0),
    (['.a'], 0),
    (['.a', '.b'], 0),
    ([], 1),
    ([], 2),
    (['.a'], 1),
    (['.a'], 2),
    (['.a', '.b'], 1),
    (['.a', '.b'], 2),
])
def test_when_getting_file_paths_given_valid_arguments_should_succeed(tmpdir_factory,
                                                                      allowed_file_extensions: Sequence[str],
                                                                      max_subdir_count: int):
    recursively = max_subdir_count > 0

    for subdir_count in range(max_subdir_count + 1):
        dir_path = generate_random_dir_path(subdir_count)
        dir_path = os.path.join(str(tmpdir_factory.getbasetemp()), dir_path)

        # Generate paths to files...
        # ...with a disallowed extension:
        file_extension_suffix = 'z'
        if len(allowed_file_extensions) > 0:
            disallowed_file_extension = allowed_file_extensions[-1] + file_extension_suffix
        else:
            disallowed_file_extension = '.{}'.format(file_extension_suffix)
        disallowed_file_name_with_extension = generate_random_file_name_with_extension(disallowed_file_extension)
        disallowed_file_path = os.path.join(dir_path, disallowed_file_name_with_extension)
        # ...with allowed extensions:
        allowed_file_names_with_extension = [generate_random_file_name_with_extension(e)
                                             for e in allowed_file_extensions]
        allowed_file_paths = [os.path.join(dir_path, fne)
                              for fne in allowed_file_names_with_extension]

        # Create files in respective dirs.
        os.makedirs(dir_path, exist_ok=True)
        open(disallowed_file_path, 'w+').close()
        for p in allowed_file_paths:
            open(p, 'w+').close()

        # Assert.
        actual = set(yield_file_paths(dir_path, allowed_file_extensions, recursively))
        expected = set(allowed_file_paths)
        assert actual == expected


def test_when_creating_or_updating_file_given_file_not_exists_should_create_file(tmpdir_factory,
                                                                                 file_meta: FileMeta):
    tmp_dir_path = os.path.join(str(tmpdir_factory.getbasetemp()), file_meta.dir_path)
    tmp_file_path = os.path.join(tmp_dir_path, file_meta.file_name_with_extension)

    os.makedirs(tmp_dir_path, exist_ok=True)
    create_or_update_file(tmp_file_path, file_meta.file_content, file_meta.file_content_encoding)

    with open(tmp_file_path, 'rb') as file:
        assert file.read().decode(file_meta.file_content_encoding) == file_meta.file_content


def test_when_creating_or_updating_file_given_file_exists_should_update_file(tmpdir_factory,
                                                                             file_meta: FileMeta):
    tmp_dir_path = os.path.join(str(tmpdir_factory.getbasetemp()), file_meta.dir_path)
    tmp_file_path = os.path.join(tmp_dir_path, file_meta.file_name_with_extension)

    os.makedirs(tmp_dir_path, exist_ok=True)
    with open(tmp_file_path, 'wb') as file:
        file.write(file_meta.file_content.encode(file_meta.file_content_encoding))

    updated_file_content = file_meta.file_content + ' (+ this update)'
    create_or_update_file(tmp_file_path, updated_file_content, file_meta.file_content_encoding)

    with open(tmp_file_path, 'rb') as file:
        assert file.read().decode(file_meta.file_content_encoding) == updated_file_content


@mark.parametrize('s,expected', [
    ('IAmInCamelCase_but_i_am_not_AndHereAmIOnceAgain',
     'i_am_in_camel_case_but_i_am_not__and_here_am_i_once_again'),
    ('iAmInPascalCase_but_i_am_not_andHereAmIOnceAgain',
     'i_am_in_pascal_case_but_i_am_not_and_here_am_i_once_again'),
])
def test_when_converting_camel_or_pascal_case_to_snake_case_given_valid_arguments_should_succeed(s: str,
                                                                                                 expected: str):
    assert camel_or_pascal_case_to_snake_case(s) == expected


@mark.parametrize('s,expected', [
    ('iAmASTRANGECamelCase',
     'i Am ASTRANGE Camel Case'),
    ('YetAnotherOneBUTNOWWhilebeingastrangeOneIamStillAProperPascalCase',
     'Yet Another One BUTNOW Whilebeingastrange One Iam Still A Proper Pascal Case'),
])
def test_when_converting_camel_or_pascal_case_to_space_delimited_given_valid_arguments_should_succeed(s: str,
                                                                                                      expected: str):
    actual = camel_or_pascal_case_to_space_delimited(s)
    assert actual == expected


def test_when_getting_all_subclasses_given_no_subclasses_should_succeed():
    assert set(get_all_subclasses(Moo, False)) == set()
    assert set(get_all_subclasses(Moo, True)) == {Moo}


def test_when_getting_all_subclasses_given_self_included_should_succeed():
    assert set(get_all_subclasses(Foo, True)) == {Foo, Boo, Moo}


def test_when_getting_all_subclasses_given_self_excluded_should_succeed():
    assert set(get_all_subclasses(Foo, False)) == {Boo, Moo}


def test_when_getting_class_name_given_valid_arguments_should_succeed():
    assert get_class_name(Foo) == Foo.__class__.__name__
    assert get_class_name(Foo.InsideFoo) == Foo.InsideFoo.__class__.__name__


def test_when_getting_class_qualname_given_valid_arguments_should_succeed():
    assert get_class_qualname(Foo) == Foo.__qualname__
    assert get_class_qualname(Foo.InsideFoo) == Foo.InsideFoo.__qualname__
