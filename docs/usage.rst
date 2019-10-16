Usage
=====

.. code-block:: python

    import os
    from pathlib import Path

    from python_humble_utils.filesystem import yield_file_paths
    from python_humble_utils.strings import camel_or_pascal_case_to_snake_case


    # ...

    file_paths = yield_file_paths(
        dir_path=Path("dir") / "with" / "scripts",
        allowed_file_extensions=(".sh", ".bash"),
        recursively=True
    )
    assert set(file_paths) == set(("s1.sh", "s2.bash", "s3.bash"))

    s = camel_or_pascal_case_to_snake_case("camelCasedString")
    assert s == "camel_cased_string"

    s = camel_or_pascal_case_to_snake_case("PascalCasedString")
    assert s == "pascal_cased_string"

    # ...
