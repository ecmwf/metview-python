
Metview Python bindings
=======================

Python interface to Metview, a meteorological workstation and batch system for accessing, examining, manipulating and visualising meteorological data.
See documentation at https://metview.readthedocs.io/en/latest/index.html


Try the example notebooks on Binder!
------------------------------------
Click the link below to start a Binder session to try the examples online now:

.. image:: https://mybinder.org/badge_logo.svg
 :target: https://mybinder.org/v2/gh/ecmwf/metview-python/master?filepath=examples


Requirements
------------

- A working Metview 5 installation (at least version 5.0.3, ideally 5.3.0 or above), either from binaries or built from source.
  Conda packages are available for Linux, and native packages are available for many Linux distributions.
  See https://metview.readthedocs.io/en/latest/install.html

  - An alternative is to build from the Metview Source Bundle.
    See https://confluence.ecmwf.int/metview/The+Metview+Source+Bundle

- Ensure that the command 'metview' will run this version by setting your PATH to include the 'bin' directory
  from where you built or installed it if it's not in a default location.

- A Python 3 interpreter (ideally version >= 3.5) 


Install
-------

The package is installed from PyPI with::

    $ pip install metview


or from conda-forge with::

    $ conda install metview-python -c conda-forge


Test
----

You may run a simple selfcheck command to ensure that your system is set up correctly::

    $ python -m metview selfcheck
    Hello world - printed from Metview!
    Trying to connect to a Metview installation...
    Metview version 5.2.0 found
    Your system is ready.


To manually test that your system is properly setup open a Python 3 interpreter and try::

    >>> import metview as mv
    >>> mv.lowercase('Hello World!')
    'hello world!'


Examples
--------

The [examples](examples) folder contains some Jupyter notebooks and some standalone examples for you to try out!


Project resources
-----------------

============= =========================================================
Development   https://github.com/ecmwf/metview-python
Download      https://pypi.org/project/metview
Code quality  .. image:: https://travis-ci.com/ecmwf/metview-python.svg?branch=master
                :target: https://travis-ci.com/ecmwf/metview-python
                :alt: Build Status on Travis CI
              .. image:: https://coveralls.io/repos/ecmwf/metview-python/badge.svg?branch=master&service=github
                :target: https://coveralls.io/github/ecmwf/metview-python
                :alt: Coverage Status on Coveralls
============= =========================================================


License
-------

Copyright 2017-2021 European Centre for Medium-Range Weather Forecasts (ECMWF).

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at: http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
