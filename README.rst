Python Humble Utils
===================

.. image:: https://travis-ci.org/webyneter/python-humble-utils.svg?branch=master
    :target: https://travis-ci.org/webyneter/python-humble-utils
    :alt: Build Status

.. image:: https://badge.fury.io/py/python-humble-utils.svg
    :target: https://pypi.python.org/pypi/python-humble-utils
    :alt: Latest Version

.. image:: https://img.shields.io/pypi/pyversions/python-humble-utils.svg
    :target: https://pypi.python.org/pypi/python-humble-utils
    :alt: Supported Python Versions

.. image:: https://codecov.io/gh/webyneter/python-humble-utils/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/webyneter/python-humble-utils
    :alt: Coverage

.. image:: https://pyup.io/repos/github/webyneter/python-humble-utils/shield.svg
    :target: https://pyup.io/repos/github/webyneter/python-humble-utils/
    :alt: Updates

.. image:: https://readthedocs.org/projects/python-humble-utils/badge/?version=latest
    :target: http://python-humble-utils.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. image:: https://img.shields.io/badge/License-MIT-green.svg
    :target: https://opensource.org/licenses/MIT
    :alt: MIT License

Python utils for everyday use.

* `Documentation`_.
* Please, `open issues`_ before sending emails to the maintainers: You will get a much faster response!

.. _`open issues`: https://github.com/webyneter/python_humble_utils/issues/new
.. _`Documentation`: https://python-humble-utils.readthedocs.io/en/stable/



Feature Areas
-------------

* File operations.
* File/directory paths extraction.
* File/directory paths randomization.
* String case convertions.
* Python class convenience shortcuts.
* `py.test`_ fixtures and helpers.

.. _py.test: https://docs.pytest.org/en/stable/



Installation
------------

.. code-block:: console

    $ pip install python-humble-utils

or install from sources:

.. code-block:: console

    $ python setup.py install

Refer to Installation for detailed instructions.

.. TODO Refer to :ref:`installation`.


Usage
-----

.. code-block:: python

    import os

    from python_humble_utils.commands import (
        yield_file_paths,
        camel_or_pascal_case_to_snake_case
    )


    # ...


    file_paths = yield_file_paths(dir_path=os.path.join('dir', 'with', 'scripts'),
                                  allowed_file_extensions=['.sh', '.bash'],
                                  recursively=True)
    # assert set(file_paths) == set(['s1.sh', 's2.bash', 's3.bash'])

    s = camel_or_pascal_case_to_snake_case('camelCasedString')
    # assert s == 'camel_cased_string'

    s = camel_or_pascal_case_to_snake_case('PascalCasedString')
    # assert s == 'pascal_cased_string'


    # ...


Contributing
------------

Your contributions are very much welcome! Refer to :ref:`contributing` for more details.



Code of Conduct
---------------

All those using `python-humble-utils`, including its codebase and project management ecosystem are expected to follow the `Python Community Code of Conduct`_.

.. _`Python Community Code of Conduct`: https://www.python.org/psf/codeofconduct/



Acknowledgements
----------------

This package was scaffolded via Cookiecutter_ with `audreyr/cookiecutter-pypackage`_ template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

