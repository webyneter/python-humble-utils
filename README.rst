Python Humble Utils
===================

.. image:: https://img.shields.io/pypi/v/python_humble_utils.svg
    :target: https://pypi.python.org/pypi/python_humble_utils
    :alt: PyPI

.. TODO .. image:: https://img.shields.io/pypi/status/python_humble_utils.svg
    :target:
    :alt:

.. TODO .. image:: https://img.shields.io/pypi/pyversions/python_humble_utils.svg
    :target:
    :alt:

.. image:: https://img.shields.io/travis/webyneter/python_humble_utils.svg
    :target: https://travis-ci.org/webyneter/python_humble_utils
    :alt: Travis CI

.. image:: https://codecov.io/gh/webyneter/python-humble-utils/branch/master/graph/badge.svg?token=NBiWMpI4Zt
    :target: https://codecov.io/gh/webyneter/python-humble-utils
    :alt: codecov

.. image:: https://pyup.io/repos/github/webyneter/python-humble-utils/shield.svg?token=7d438c38-7622-4513-83bc-003209eb3619
    :target: https://pyup.io/repos/github/webyneter/python-humble-utils/
    :alt: Updates

.. image:: https://readthedocs.org/projects/python-humble-utils/badge/?version=latest
    :target: https://python-humble-utils.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation

.. image:: https://img.shields.io/badge/License-MIT-green.svg
    :target: https://opensource.org/licenses/MIT
    :alt: License: MIT

.. TODO: gitter
.. TODO: codecov
.. TODO: https://github.com/probot/stale
.. TODO: https://github.com/danger/danger


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

Refer to :ref:`installation`.

.. _`documentation`: https://python-humble-utils.readthedocs.io/en/stable/


Usage
-----

.. code-block:: python

    import os

    from python_humble_utils.commands import (
        yield_file_paths,
        camel_or_pascal_case_to_snake_case
    )


    # ...


    file_paths = yield_file_paths(dir_path=os.path.join('path', 'to', 'dir'),
                                  allowed_file_extensions=['.sh', '.bash'],
                                  recursively=True)
    # assert file_paths == ['s1.sh', 's2.bash', 's3.bash']

    s = camel_or_pascal_case_to_snake_case('camelCasedString')
    # assert s == 'camel_cased_string'

    s = camel_or_pascal_case_to_snake_case('PascalCasedString')
    # assert s == 'pascal_cased_string'


    # ...



Contributing
------------

Your contributions are very much welcome! For detailed instructions, refer to :ref:`contributing`.



Code of Conduct
---------------

All those using `python-humble-utils`, including its codebase and project management ecosystem are expected to follow the `Python Community Code of Conduct`_.

.. _`Python Community Code of Conduct`: https://www.python.org/psf/codeofconduct/



Acknowledgements
----------------

This package was scaffolded via Cookiecutter_ with `audreyr/cookiecutter-pypackage`_ template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

