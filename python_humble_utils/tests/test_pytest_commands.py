import os

from pytest import raises

from ..conftest import FileMeta
from ..pytest_commands import generate_tmp_file_path


def test_when_generating_tmp_file_path_given_relative_tmp_dir_path_should_succeed(tmpdir_factory,
                                                                                  file_meta: FileMeta):
    tmp_dir_path = os.path.join(str(tmpdir_factory.getbasetemp()), file_meta.dir_path)
    tmp_file_path = os.path.join(tmp_dir_path, file_meta.file_name_with_extension)
    expected = tmp_file_path

    actual = generate_tmp_file_path(tmpdir_factory, file_meta.file_name_with_extension, file_meta.dir_path)

    assert actual == expected


def test_when_generating_tmp_file_path_given_abs_tmp_dir_path_should_raise(tmpdir_factory,
                                                                           file_meta: FileMeta):
    with raises(ValueError):
        abs_tmp_dir_path = os.path.join(str(tmpdir_factory.getbasetemp()), file_meta.dir_path)
        generate_tmp_file_path(tmpdir_factory, file_meta.file_name_with_extension, abs_tmp_dir_path)


def test_when_generating_tmp_file_path_given_no_tmp_dir_path_should_succeed(tmpdir_factory,
                                                                            file_meta: FileMeta):
    actual = generate_tmp_file_path(tmpdir_factory, file_meta.file_name_with_extension)
    expected = os.path.join(str(tmpdir_factory.getbasetemp()), file_meta.file_name_with_extension)
    assert actual == expected
