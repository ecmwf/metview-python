
.. highlight:: console


Docker development environment
==============================

Setup
-----

You need docker working and up.

To create the development image run::

    $ make image

To create the wheelhouse cache of binary packages run::

    $ make wheelhouse


Development tasks
-----------------

Running unit tests on the target python version::

    $ make test

Running quality control::

    $ make qc

Running the full test suite on all python supported versions::

    $ make detox

To run a shell inside the container run::

    $ make shell

To update the requirements files to the latest versions::

    $ make update-test-req


Cleanup
-------

Light cleanup with::

    $ make clean

The wheelhouse is removed with::

    $ make distclean  # ARE YOU REALLY SURE?

