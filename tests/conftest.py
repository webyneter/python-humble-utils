import os

from pytest import fixture


class FileMeta:
    """A container for file meta."""

    def __init__(self, dir_path: str,
                 file_name: str,
                 file_extension: str,
                 file_name_with_extension: str,
                 file_path: str,
                 file_content: str,
                 file_content_encoding: str):
        super().__init__()
        self.dir_path = dir_path
        self.file_name = file_name
        self.file_extension = file_extension
        self.file_name_with_extension = file_name_with_extension
        self.file_path = file_path
        self.file_content = file_content
        self.file_content_encoding = file_content_encoding


@fixture
def file_meta() -> FileMeta:
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
