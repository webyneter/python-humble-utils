import os
from typing import NamedTuple

from pytest import fixture

FileMeta = NamedTuple('FileMeta', [
    ('dir_path', str),
    ('file_name', str),
    ('file_extension', str),
    ('file_name_with_extension', str),
    ('file_path', str),
    ('file_content', str),
    ('file_content_encoding', str),
])


@fixture
def file_meta():
    dir_path = os.path.join('path', 'to', 'dir', 'with')
    file_content = os.linesep.join(['Behold,', 'this', 'is', 'multiline', 'content!'])
    file_content_encoding = 'utf-8'
    file_name = 'name'
    file_extension = '.ext'
    file_name_with_extension = file_name + file_extension
    file_path = os.path.join(dir_path, file_name_with_extension)
    return FileMeta(dir_path=dir_path,
                    file_name=file_name,
                    file_extension=file_extension,
                    file_name_with_extension=file_name_with_extension,
                    file_path=file_path,
                    file_content=file_content,
                    file_content_encoding=file_content_encoding)
