

Metview Python bindings
=======================

See documentation at https://software.ecmwf.int/metview/Metview%27s+Python+Interface


Requirements
------------

- A working Metview 5 installation (at least version 5.0.3), either from binaries or built from source.
  - See https://software.ecmwf.int/metview/Releases
  - An alternative is to build from the Metview Source Bundle - see https://software.ecmwf.int/metview/The+Metview+Source+Bundle
  - Ensure that the command 'metview' will run this version by setting your PATH to include the 'bin' directory from where you built or installed it if it's not in a default location
- A Python 3 interpreter (ideally version >= 3.5)


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
