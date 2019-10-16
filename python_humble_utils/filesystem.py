import os
from pathlib import Path
from typing import Iterable, Optional, Callable, Collection
from uuid import uuid4


def generate_random_dir_path(
    root_dir_path: Optional[Path] = None,
    subdir_count: int = 0,
    random_string_generator: Optional[Callable[[], str]] = None,
) -> Path:
    """Generate a random directory path.

    :param root_dir_path: root dir path; by default, the current dir path is used
    :param subdir_count: a number of subdirectories to generate in the directory root.
    :param random_string_generator: random number generator; by default, the UUID4 hex is used
    :return: directory root path.
    """
    root_dir_path = root_dir_path or Path()
    random_string_generator = random_string_generator or (lambda: uuid4().hex)

    path = root_dir_path or Path()
    for __ in range(1 + subdir_count):
        path /= random_string_generator()
    return path


def read_file(file_path: str, as_single_line: bool = False) -> str:
    """Read file content.

    :param file_path: path to the file.
    :param as_single_line: whether or not the file is to be read as a single line.
    :return: file content.
    """
    with open(file_path, "r") as file:
        lines = []
        for line in file.readlines():
            if as_single_line:
                line = line.replace(os.linesep, "")
            lines.append(line)
        return "".join(lines)


def yield_file_paths(
    dir_path: Path, allowed_file_extensions: Collection[str], recursively: bool = False
) -> Iterable[Path]:
    """Yield file paths.

    :param dir_path: path to the containing directory.
    :param allowed_file_extensions: file extensions to match against e.g. `['.abc', '.def']`.
    :param recursively: whether or not the directory is to be recursively traversed.
    :return: file paths.
    """

    def filter_allowed_file_paths(
        dp: Path, fbns: Collection[str], afes: Collection[str]
    ) -> Iterable[Path]:
        for fbn in fbns:
            p = dp / Path(fbn)
            if p.suffix in afes:
                yield p

    if recursively:
        for root_dir_path, _, file_basenames in os.walk(dir_path):
            yield from filter_allowed_file_paths(dir_path, file_basenames, allowed_file_extensions)
    else:
        file_basenames = os.listdir(dir_path)
        yield from filter_allowed_file_paths(dir_path, file_basenames, allowed_file_extensions)


def create_or_update_file(
    file_path: str, file_content: str = "", file_content_encoding: str = "utf-8"
) -> None:
    """Create or update file.

    :param file_path: path to the file.
    :param file_content: file content.
    :param file_content_encoding: file content encoding e.g. `latin-1`.
    """
    with open(file_path, "wb+") as file:
        file.write(file_content.encode(file_content_encoding))
