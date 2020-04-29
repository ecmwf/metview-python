
.. highlight:: console


============
Contributing
============

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given. Note that contributors must
agree to ECMWF's Contribution License Agreement (CLA) before their contribution
can be accepted.

You can contribute in many ways:

Types of Contributions
----------------------

Report Bugs
~~~~~~~~~~~

Report bugs at https://github.com/ecmwf/metview-python/issues

If you are reporting a bug, please include:

* Your operating system name and version.
* Installation method and version of all dependencies.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug, including a (small) sample file.

Fix Bugs
~~~~~~~~

Look through the GitHub issues for bugs. Anything tagged with "bug"
and "help wanted" is open to whoever wants to implement a fix for it.

Implement Features
~~~~~~~~~~~~~~~~~~

Look through the GitHub issues for features. Anything tagged with "enhancement"
and "help wanted" is open to whoever wants to implement it.

Code Cleanup
~~~~~~~~~~~~

Look through the GitHub issues for code cleanliness issues. These are not likely to
affect the behaviour of the software, but are more related to style, e.g. PEP8.
Anything tagged with "code cleanliness" and "help wanted" is open to whoever wants to do it.


Get Started!
------------

Ready to contribute? Here's how to set up `metview-python` for local development. Please note this documentation assumes
you already have `virtualenv` and `Git` installed and ready to go.

1. Fork the `metview-python` repo on GitHub.
2. Clone your fork locally::

    $ cd path_for_the_repo
    $ git clone https://github.com/ecmwf/metview-python.git
    $ cd metview-python

3. Assuming you have virtualenv installed (If you have Python3.5 this should already be there), you can create a new environment for your local development by typing::

    $ python3 -m venv ../metview-python-env
    $ source ../metview-python-env/bin/activate

    This should change the shell to look something like
    (metview-python-env) $

4. Install system dependencies as described in the README.rst file, then install the python dependencies into your local environment with::

    $ pip install -r requirements/requirements-tests.txt
    $ pip install -e .

5. Create a branch for local development::

    $ git checkout -b name-of-your-bugfix-or-feature

   Now you can make your changes locally.

6. The next step would be to run the test cases. `metview-python` uses py.test, you can run PyTest. Before you run pytest you should ensure all dependancies are installed::

    $ pip install -r requirements/requirements-dev.txt
    $ pytest -v --flakes

7. Before raising a pull request you should also run tox. This will run the tests across different versions of Python::

    $ tox

8. If your contribution is a bug fix or new feature, you should add a test to the existing test suite.

9. Commit your changes and push your branch to GitHub::

    $ git add .
    $ git commit -m "Description of your changes (#issue-number)"
    $ git push origin name-of-your-bugfix-or-feature

10. Submit a pull request through the GitHub website.

Pull Request Guidelines
-----------------------

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests. Any data files should be a small as possible.

2. If the pull request adds functionality, the docs should be updated. Put
   your new functionality into a function with a docstring, and add the
   feature to the list in README.rst.

3. The pull request should work for Python 3.5, 3.6 and 3.7, and for Pypy3. Check
   the tox results and make sure that the tests pass for all supported Python versions.






Docker development environment
------------------------------

This provides an alternative way to run and test Metview's Python interface, installing
the binary dependencies into a Docker image with several 'make' commands to interact with it.

Setup
~~~~~

You need docker working and up.

To create the development image run::

    $ make image

To create the wheelhouse cache of binary packages run::

    $ make wheelhouse


Development tasks
~~~~~~~~~~~~~~~~~

Running unit tests on the target python version::

    $ make test

Running quality control::

    $ make qc

Running the full test suite on all python supported versions::

    $ make detox

To run a shell inside the container run::

    $ make shell

To start a Jupyter notebook inside the container run::

    $ make notebook

To update the requirements files to the latest versions::

    $ make update-req

All tasks can be run locally by adding `RUN=` to the command line, for example::

    $ make qc RUN=


Cleanup
~~~~~~~

Light cleanup with::

    $ make clean

Complete cleanup with::

    $ make distclean

