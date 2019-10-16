from pytest import raises

from python_humble_utils.vendor.pytest import generate_tmp_file_path
from tests.conftest import FileMeta


def test_relative_tmp_dir_path_given__generate_tmp_file_path_succeeds(
    tmpdir_factory, file_meta: FileMeta
):
    assert (
        generate_tmp_file_path(
            tmpdir_factory, file_meta.name_with_extension, tmp_dir_path=file_meta.dir_path
        )
        == tmpdir_factory.getbasetemp() / file_meta.dir_path / file_meta.name_with_extension
    )


def test_absolute_tmp_dir_path_given__generate_tmp_file_path_succeeds(
    tmpdir_factory, file_meta: FileMeta
):
    with raises(ValueError):
        generate_tmp_file_path(
            tmpdir_factory,
            file_meta.name_with_extension,
            tmp_dir_path=(tmpdir_factory.getbasetemp() / file_meta.dir_path),
        )


def test_no_tmp_dir_path_given__generate_tmp_file_path_succeeds(
    tmpdir_factory, file_meta: FileMeta
):
    assert (
        generate_tmp_file_path(tmpdir_factory, file_meta.name_with_extension)
        == tmpdir_factory.getbasetemp() / file_meta.name_with_extension
    )
