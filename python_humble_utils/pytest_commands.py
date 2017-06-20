import os


def generate_tmp_file_path(tmpdir_factory,
                           file_name_with_extension: str,
                           tmp_dir_path: str = None) -> str:
    """
    Generate file path relative to a temporary directory.

    :param tmpdir_factory: py.test's `tmpdir_factory` fixture.
    :param file_name_with_extension: file name with extension e.g. `file_name.ext`.
    :param tmp_dir_path: path to directory (relative to the temporary one created by `tmpdir_factory`) where the generated file path should reside. # noqa
    :return: file path.
    """
    basetemp = tmpdir_factory.getbasetemp()

    if tmp_dir_path:
        if os.path.isabs(tmp_dir_path):
            raise ValueError('tmp_dir_path is not a relative path!')
        # http://stackoverflow.com/a/16595356/1557013
        for tmp_file_dir_path_part in os.path.normpath(tmp_dir_path).split(os.sep):
            # Accounting for possible path separator at the end.
            if tmp_file_dir_path_part:
                tmpdir_factory.mktemp(tmp_file_dir_path_part)
        tmp_file_path = os.path.join(str(basetemp), tmp_dir_path, file_name_with_extension)
    else:
        tmp_file_path = str(basetemp.join(file_name_with_extension))

    return tmp_file_path
