

Metview Python bindings
=======================

See documentation at https://software.ecmwf.int/metview/Metview%27s+Python+Interface


Requirements
------------

- A working Metview 5 installation, either from binaries or built from source.
  - See https://software.ecmwf.int/metview/Releases
- A Python 3 interpreter

The following section describes building Metview from the source bundle. This is not necessary
if you already have a Metview 5 installation.


Build Metview from source bundle 
---------------------------------

Procedure and needed files to install Metview's binaries from source::

    1) download and unpack the Metview source-bundle 
       from https://software.ecmwf.int/metview/The+Metview+Source+Bundle
    2) be sure your default Python interpreter is Python 2.7 when building
    3) configure the building in a separate directory by means of the
       cmake -DENABLE_ODB=ON -DENABLE_XXHASH=OFF <metview_source_path> command
    4) build by typing "make" or "make -j8"
    5) ensure that the command 'metview' will run this version by setting your PATH
       to include the 'bin' directory from where you built or installed it
    6) to start the tests type from <metview_build_path>/metview directory: ctest


Create a virtual environment
----------------------------

Create and activate a new virtualenv::

    python3 -m venv <folder>
    source <folder>/bin/activate


Install
-------

From the metview folder install with::

    pip install -e .


Test
----

Launch tests with::

    pytest -v tests

Run X on MacOS
--------------

    open -a XQuartz
    ip=$(ifconfig en0 | grep inet | awk '$1=="inet" {print $2}')
    xhost + $ip
    docker run --rm -it -e DISPLAY=$ip:0 -v `pwd`:/src metview
