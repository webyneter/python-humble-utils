import os
from pathlib import Path

from pytest import fixture


class FileMeta:
    """A container for file meta."""

    def __init__(
        self,
        dir_path: str,
        name: str,
        extension: str,
        name_with_extension: str,
        path: str,
        content: str,
        content_encoding: str,
    ):
        super().__init__()
        self.dir_path = dir_path
        self.name = name
        self.extension = extension
        self.name_with_extension = name_with_extension
        self.path = path
        self.content = content
        self.content_encoding = content_encoding


class Foo:
    class InsideFoo:
        pass


class BooFoo(Foo):
    pass


class MooBooFoo(BooFoo):
    pass


@fixture
def file_meta() -> FileMeta:
    dir_path = Path("path") / "to" / "dir" / "with"
    file_content = os.linesep.join(["Behold,", "this", "is", "multiline", "content!"])
    file_content_encoding = "utf-8"
    file_name = "name"
    file_extension = ".ext"
    file_name_with_extension = file_name + file_extension
    file_path = dir_path / file_name_with_extension
    return FileMeta(
        dir_path=dir_path,
        name=file_name,
        extension=file_extension,
        name_with_extension=file_name_with_extension,
        path=file_path,
        content=file_content,
        content_encoding=file_content_encoding,
    )
