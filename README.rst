
.. highlights:: console

Metview Python bindings
=======================

Python interface to Metview meteorological workstation and batch system.
See documentation at https://software.ecmwf.int/metview/Metview's+Python+Interface

.. warning::
    This is Alpha software.


Requirements
------------

- A working Metview 5 installation (at least version 5.0.3), either from binaries or built from source.
  See https://software.ecmwf.int/metview/Releases

  - An alternative is to build from the Metview Source Bundle.
    See https://software.ecmwf.int/metview/The+Metview+Source+Bundle

- Ensure that the command 'metview' will run this version by setting your PATH to include the 'bin' directory
  from where you built or installed it if it's not in a default location.

- A Python 3 interpreter (ideally version >= 3.5)


Install
-------

The package is installed from PyPI with::

    $ pip install metview


Test
----

To test that your system is properly setup open a Python 3 interpreter and try::

    >>> import metview as mv
    >>> mv.lowercase('Hello World!')
    'hello world!'


Build Metview from source bundle 
---------------------------------

If you don't have a Metview 5 installation on your machine you may build Metview from the
source bundle as follows:

 1. download and unpack the Metview source-bundle
    from https://software.ecmwf.int/metview/The+Metview+Source+Bundle
 2. be sure your default Python interpreter is Python 2.7 when building
 3. configure the building in a separate directory by means of the
    `cmake -DENABLE_ODB=ON -DENABLE_XXHASH=OFF <metview_source_path>` command
 4. build by typing `make` or `make -j8`
 5. install by `make install`
 6. to start the tests type from <metview_build_path>/metview directory: `ctest`


License
-------

Copyright 2017-2018 European Centre for Medium-Range Weather Forecasts (ECMWF).

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
