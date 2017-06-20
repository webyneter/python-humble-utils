.. highlight:: shell

.. _project-makefile:

Project Makefile
================

To facilitate smooth development worflow, we provide a `Makefile` defining a number of convenience commands.

* `clean` running
    #. `clean-build` (build artifact removal);
    #. `clean-pyc` (compilation artifact removal);
    #. `clean-test` (test and coverage artifact removal).

    Specifically::

        $ make clean
        $ make clean-build
        $ make clean-pyc
        $ make clean-test


* `lint` checking codebase compliance with `PEP8`_ via `flake8`_::

    $ make lint

* `test` running `py.test`_::

    $ make test

* `test-all` running `tox`_::

    $ make test-all

* `coverage` running `coverage`_::

    $ make coverage

* `docs` generating project docs via `Sphinx`_::

    $ make docs

* `servedocs` serving docs live via `watchdog`_::

    $ make servedocs

* `release` packaging and releasing the project to PyPI::

    $ make release

* `dist` builds source and wheel packages via `setuptools`_::

    $ make dist

* `install` installing the package to the current environment::

    $ make install

* `requirements` proxying the `./requirements/Makefile`::

    $ make requirements
    $ make requirements proxy=all
    $ make requirements proxy='check_pip_tools all'


.. _`PEP8`: https://www.python.org/dev/peps/pep-0008/
.. _`flake8`: http://flake8.pycqa.org/en/stable/
.. _`py.test`: https://docs.pytest.org/en/stable/
.. _`tox`: https://tox.readthedocs.io/en/stable/
.. _`coverage`: https://coverage.readthedocs.io/en/latest/
.. _`Sphinx`: http://www.sphinx-doc.org/en/stable/
.. _`watchdog`: https://github.com/gorakhargosh/watchdog
.. _`setuptools`: https://setuptools.readthedocs.io/en/stable/
