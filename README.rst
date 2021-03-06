Python Humble Utils
===================

.. image:: https://travis-ci.org/webyneter/python-humble-utils.svg?branch=master
    :target: https://travis-ci.org/webyneter/python-humble-utils
    :alt: Build Status

.. image:: https://badgen.net/dependabot/webyneter/python-humble-utils/?icon=dependabot
    :target: https://badgen.net/dependabot/webyneter/python-humble-utils/?icon=dependabot
    :alt: dependabot

.. image:: https://codecov.io/gh/webyneter/python-humble-utils/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/webyneter/python-humble-utils
    :alt: Coverage

.. image:: https://codeclimate.com/github/webyneter/python-humble-utils/badges/gpa.svg
    :target: https://codeclimate.com/github/webyneter/python-humble-utils
    :alt: Code Climate

.. image:: https://badge.fury.io/py/python-humble-utils.svg
    :target: https://pypi.python.org/pypi/python-humble-utils
    :alt: Latest Version

.. image:: https://img.shields.io/pypi/pyversions/python-humble-utils.svg
    :target: https://pypi.python.org/pypi/python-humble-utils
    :alt: Supported Python Versions

.. image:: https://readthedocs.org/projects/python-humble-utils/badge/?version=stable
    :target: http://python-humble-utils.readthedocs.io/en/stable/?badge=stable
    :alt: Documentation Status

.. image:: https://img.shields.io/badge/License-MIT-green.svg
    :target: https://opensource.org/licenses/MIT
    :alt: MIT License

.. image:: https://img.shields.io/gitter/room/webyneter/python-humble-utils.svg
    :target: https://gitter.im/webyneter/python-humble-utils?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge
    :alt: Join the chat at https://gitter.im/webyneter/python-humble-utils


Python utils for everyday use.

* `Documentation`_.
* Please, `open issues`_ before sending emails to the maintainers: You will get a much faster response!

.. _`open issues`: https://github.com/webyneter/python-humble-utils/issues/new
.. _`Documentation`: https://python-humble-utils.readthedocs.io/en/stable/installation.html



Feature Areas
-------------

* File operations.
* File/directory paths extraction.
* File/directory paths randomization.
* String case conversions.
* Python class convenience shortcuts.
* `py.test`_ fixtures and helpers.

.. _`py.test`: https://docs.pytest.org/en/stable/



Installation
------------

.. code-block:: console

    $ pip install python-humble-utils

or install from sources:

.. code-block:: console

    $ python setup.py install

Refer to `Installation`_ for detailed instructions.

.. _`Installation`: https://python-humble-utils.readthedocs.io/en/stable/installation.html


Usage
-----

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


Contributing
------------

Your contributions are very much welcome! Refer to `Contributing`_ for more details.

.. _`Contributing`: https://python-humble-utils.readthedocs.io/en/stable/contributing.html



Code of Conduct
---------------

All those using ``python-humble-utils``, including its codebase and project management ecosystem are expected to follow the `Python Community Code of Conduct`_.

.. _`Python Community Code of Conduct`: https://www.python.org/psf/codeofconduct/



Acknowledgements
----------------

This package was initially scaffolded via `Cookiecutter`_ with `audreyr/cookiecutter-pypackage`_ template.

.. _`Cookiecutter`: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

