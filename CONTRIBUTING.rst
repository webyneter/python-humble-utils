.. highlight:: shell

.. _contributing:

============
Contributing
============

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.



Ways to Contribute
------------------

Report Bugs
~~~~~~~~~~~

Report bugs at https://github.com/webyneter/python_humble_utils/issues complying with the project's issue template.


Fix Bugs via PRs
~~~~~~~~~~~~~~~~

Look through the GitHub issues: Anything tagged with `bug` and `help wanted` is open to whoever wants to implement it.

Make sure to submit clean, concise, well-tested PRs only, so it is easier for contributors to review it;
strive to deliver as short and atomic PRs as possible as this will dramatically increase the likelihood of it
being merged.


Implement Features
~~~~~~~~~~~~~~~~~~

Look through the GitHub issues for features. Anything tagged with `enhancement`
and `help wanted` is open to whoever wants to implement it.


Write Documentation
~~~~~~~~~~~~~~~~~~~

`python-humble-utils` could always use more documentation, whether as part of the
official docs, in docstrings, or even on the web in blog posts, articles, and such.


Submit Feedback
~~~~~~~~~~~~~~~

The best way to send feedback is to file an issue at https://github.com/webyneter/python_humble_utils/issues.

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions
  are welcome!



Get Started!
------------

Ready to contribute? Here's how to set up `python_humble_utils` for local development.

#. Fork us on GitHub.
#. Clone the fork locally::

    $ git clone git@github.com:<your username>/python_humble_utils.git

#. Install your local copy into a `virtualenv`_. Assuming you have `virtualenvwrapper`_ installed, this is how you set up the local development::

    $ mkvirtualenv python_humble_utils
    $ cd <fork root directory path>
    $ setvirtualenvproject
    $ python setup.py develop

#. Create a branch for local development::

    $ git checkout -b <issue id>-<issue title>

#. When you are done making changes to the local branch, ensure tests pass via `tox`::

    $ make tox

#. Commit the changes and push your branch to GitHub::

    $ git add .
    $ git commit -m "Your detailed description of your changes."
    $ git push origin <issue id>-<issue title>

#. Submit a pull request through the GitHub website or any git GUI tool you prefer.

.. _`virtualenv`: https://virtualenv.pypa.io/en/stable/
.. _`virtualenvwrapper`: https://virtualenvwrapper.readthedocs.io/en/stable/


Pull Request Guidelines
-----------------------

Upon submition, make sure the PR meets these guidelines:

#. the PR does not decrease code coverage (unless there is a very specific reason to);
#. the docs (both programmatic and manual) are updated, if needed.



Tips
----

To run a subset of tests::

    $ py.test python_humble_utils.tests.test_commands
