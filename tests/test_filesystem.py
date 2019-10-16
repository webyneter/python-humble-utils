import os
from pathlib import Path
from typing import Optional, Callable, Sequence

import pytest
from hypothesis import given
from hypothesis._strategies import one_of, none, sampled_from, integers

from python_humble_utils.filesystem import (
    generate_random_dir_path,
    create_or_update_file,
    read_file,
    yield_file_paths,
)
from python_humble_utils.vendor.pytest import generate_tmp_file_path
from tests.conftest import FileMeta


@given(
    root_dir_path=one_of(none(), sampled_from((Path(".."), Path("..") / Path("test")))),
    subdir_count=integers(min_value=0, max_value=2),
)
def test_generate_random_dir_path(root_dir_path: Optional[Path], subdir_count: int):
    path = generate_random_dir_path(root_dir_path=root_dir_path, subdir_count=subdir_count)
    assert len(path.parts) == (len(root_dir_path.parts) if root_dir_path else 0) + 1 + subdir_count

    subdir_names = [str(i ** 2) for i in range(1 + subdir_count)]
    subdir_names_iter = iter(subdir_names)
    path = generate_random_dir_path(
        root_dir_path=root_dir_path,
        subdir_count=subdir_count,
        random_string_generator=lambda: next(subdir_names_iter),
    )
    assert len(path.parts) == (len(root_dir_path.parts) if root_dir_path else 0) + 1 + subdir_count
    assert path.parts[len(path.parts) - (1 + subdir_count) :] == tuple(subdir_names)


@pytest.mark.parametrize(
    "as_single_line,verifier",
    [
        (True, lambda file_content: os.linesep not in file_content),
        (False, lambda file_content: os.linesep in file_content),
    ],
)
def test_read_file(
    tmpdir_factory, file_meta: FileMeta, as_single_line: bool, verifier: Callable[[str], bool]
):
    tmp_file_path = generate_tmp_file_path(tmpdir_factory, file_meta.name_with_extension)
    create_or_update_file(tmp_file_path, file_meta.content, file_meta.content_encoding)

    file_content = read_file(tmp_file_path, as_single_line)

    assert verifier(file_content)


@pytest.mark.parametrize(
    "allowed_file_extensions,max_subdir_count",
    [
        ([], 0),
        ([".a"], 0),
        ([".a", ".b"], 0),
        ([], 1),
        ([], 2),
        ([".a"], 1),
        ([".a"], 2),
        ([".a", ".b"], 1),
        ([".a", ".b"], 2),
    ],
)
def test_yield_file_paths(
    tmpdir_factory, allowed_file_extensions: Sequence[str], max_subdir_count: int
):
    recursively = max_subdir_count > 0

    for subdir_count in range(max_subdir_count + 1):
        dir_path = Path(tmpdir_factory.getbasetemp()) / generate_random_dir_path(
            subdir_count=subdir_count
        )

        # Generate paths to files...
        # ...with a disallowed extension:
        file_extension_suffix = "z"
        if len(allowed_file_extensions) > 0:
            disallowed_file_extension = allowed_file_extensions[-1] + file_extension_suffix
        else:
            disallowed_file_extension = f".{file_extension_suffix}"
        disallowed_file_path = dir_path / Path(f"file{disallowed_file_extension}")
        # ...with allowed extensions:
        allowed_file_names_with_extension = [f"file{e}" for e in allowed_file_extensions]
        allowed_file_paths = [dir_path / Path(fne) for fne in allowed_file_names_with_extension]

        # Create files in respective dirs:
        os.makedirs(dir_path, exist_ok=True)
        open(disallowed_file_path, "w+").close()
        for p in allowed_file_paths:
            open(p, "w+").close()

        # Assert:
        assert set(yield_file_paths(dir_path, allowed_file_extensions, recursively)) == set(
            allowed_file_paths
        )


def test_file_not_exists__create_or_update_file_creates_file(tmpdir_factory, file_meta: FileMeta):
    tmp_dir_path = tmpdir_factory.getbasetemp() / file_meta.dir_path
    tmp_file_path = tmp_dir_path / file_meta.name_with_extension
    os.makedirs(tmp_dir_path, exist_ok=True)

    create_or_update_file(tmp_file_path, file_meta.content, file_meta.content_encoding)

    with open(tmp_file_path, "rb") as file:
        assert file.read().decode(file_meta.content_encoding) == file_meta.content


def test_file_exists__create_or_update_file_updates_file(tmpdir_factory, file_meta: FileMeta):
    tmp_dir_path = tmpdir_factory.getbasetemp() / file_meta.dir_path
    tmp_file_path = tmp_dir_path / file_meta.name_with_extension

    os.makedirs(tmp_dir_path, exist_ok=True)
    with open(tmp_file_path, "wb") as file:
        file.write(file_meta.content.encode(file_meta.content_encoding))

    updated_file_content = file_meta.content + " (+ this update)"
    create_or_update_file(tmp_file_path, updated_file_content, file_meta.content_encoding)

    with open(tmp_file_path, "rb") as file:
        assert file.read().decode(file_meta.content_encoding) == updated_file_content
