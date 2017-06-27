.. highlight:: shell

.. _developing-locally:

Developing Locally
==================


Environment Setup
-----------------

#. Fork us on `GitHub`_.

#. Clone your fork locally::

    $ git clone git@github.com:<your username>/python-humble-utils.git

#. Create a `virtualenv`_; assuming you have `virtualenvwrapper`_ installed, this is how you do it::

    $ mkvirtualenv python_humble_utils
    $ cd <cloned project root>
    $ setvirtualenvproject

#. Initialize environment::

    $ python setup.py develop


.. _`GitHub`: https://github.com/webyneter/python-humble-utils/
.. _`virtualenv`: https://virtualenv.pypa.io/en/stable/
.. _`virtualenvwrapper`: https://virtualenvwrapper.readthedocs.io/en/stable/



Scenarios
---------


Updating Requirements
~~~~~~~~~~~~~~~~~~~~~

To keep your environment in sync with project requirements, `pip-tools`_ is utilized.

Project requirements must be declared and pinned in the appropriate `./requirements/*.in` files.
They are then compiled to `./requirements/*.txt` files on command.
Note that the requirement hierarchy is maintained through relative imports of `./requirements/*.txt` files
into `./requirements/*.in` files.

#. When adding/upgrading/removing a dependency to/in/from the specific `*.in` file, the respective `*.txt` file must be updated as well::

    $ make requirements

#. To install/upgrade/uninstall dependencies into/in/from the environment::

    $ make requirements proxy=sync_development


.. _`pip-tools`: https://github.com/jazzband/pip-tools


.. _developing-locally-tox:

Running `tox` with Multiple Python Distributions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Running `tox` locally requires a number of Python distributions to be available,
which is a challenge, to say the least. `pyenv`_ helps overcome this major obstacle.

#. Follow `pyenv installation instructions`_ to install `pyenv` system-wide.

#. Install all versions of Python the project is tested against by `tox` (see `./tox.ini`).

#. Run `tox`::

    $ make test-all


.. _`pyenv`: https://github.com/pyenv/pyenv
.. _`pyenv installation instructions`: https://github.com/pyenv/pyenv#installation
