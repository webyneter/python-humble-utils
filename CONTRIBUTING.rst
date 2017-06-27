.. highlight:: shell

.. _contributing:

Contributing
============

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.



Ways to Contribute
------------------

Report Bugs
~~~~~~~~~~~

`Create an issue`_ corresponding to the bug you have found complying with the project's issue template.

.. _`Create an issue`: https://github.com/webyneter/python-humble-utils/issues


Fix Bugs
~~~~~~~~

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

The best way to send feedback is to file an issue at https://github.com/webyneter/python-humble-utils/issues.

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions
  are welcome!



Workflow
--------

See :ref:`developing-locally` for detailed instructions on setting up
development environment.

Oncer you are all set up,

#. create a branch::

    $ git checkout -b <issue id>-<issue title>

#. make the contribution;

#. follow :ref:`developing-locally-tox` to run tests comprehensively;

#. commit changes to the branch::

    $ git add .
    $ git commit -m "<detailed description of your changes>"

#. push the branch to GitHub::

    $ git push origin <issue id>-<issue title>

#. submit a pull request via GitHub or any other git GUI tool you prefer.

.. _`virtualenv`: https://virtualenv.pypa.io/en/stable/
.. _`virtualenvwrapper`: https://virtualenvwrapper.readthedocs.io/en/stable/



Guidelines
----------

Upon submition, make sure the PR meets these guidelines:

#. the PR does not decrease code coverage (unless there is a very specific reason to);
#. the docs (both programmatic and manual) are updated, if needed.
