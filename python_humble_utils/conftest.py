import os
from collections import namedtuple

import pytest


@pytest.fixture
def valid_file_meta():
    ValidFileMeta = namedtuple('ValidFileMeta', ['dir_path', 'file_name', 'file_extension',
                                                 'file_name_with_extension', 'file_path', 'file_content',
                                                 'file_content_encoding'])
    dir_path = os.path.join('path', 'to', 'dir', 'with')
    file_content = os.linesep.join(['Behold,', 'this', 'is', 'multiline', 'content!'])
    file_content_encoding = 'utf-8'
    file_name = 'file'
    file_extension = '.extension'
    file_name_with_extension = file_name + file_extension
    file_path = os.path.join(dir_path, file_name_with_extension)
    meta = ValidFileMeta(dir_path=dir_path, file_name=file_name, file_extension=file_extension,
                         file_name_with_extension=file_name_with_extension, file_path=file_path,
                         file_content=file_content, file_content_encoding=file_content_encoding)
    return meta
