import os

import pytest

from ..conftest import ValidFileMeta
from ..pytest_commands import generate_tmp_file_path


def test_when_generating_tmp_file_path_given_relative_tmp_file_dir_path_should_succeed(tmpdir_factory,
                                                                                       valid_file_meta: ValidFileMeta):
    tmp_dir_path = os.path.join(str(tmpdir_factory.getbasetemp()), valid_file_meta.dir_path)
    tmp_file_path = os.path.join(tmp_dir_path, valid_file_meta.file_name_with_extension)
    expected = tmp_file_path

    actual = generate_tmp_file_path(tmpdir_factory, valid_file_meta.file_name_with_extension, valid_file_meta.dir_path)

    assert actual == expected


def test_when_generating_tmp_file_path_given_abs_tmp_file_dir_path_should_raise(tmpdir_factory,
                                                                                valid_file_meta: ValidFileMeta):
    with pytest.raises(ValueError):
        abs_tmp_dir_path = os.path.join(str(tmpdir_factory.getbasetemp()), valid_file_meta.dir_path)
        generate_tmp_file_path(tmpdir_factory, valid_file_meta.file_name_with_extension, abs_tmp_dir_path)


def test_when_generating_tmp_file_path_given_no_tmp_file_dir_path_should_succeed(tmpdir_factory,
                                                                                 valid_file_meta: ValidFileMeta):
    actual = generate_tmp_file_path(tmpdir_factory, valid_file_meta.file_name_with_extension)
    expected = os.path.join(str(tmpdir_factory.getbasetemp()), valid_file_meta.file_name_with_extension)
    assert actual == expected
