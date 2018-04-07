

Metview Python bindings
=======================


Build Metview from source bundle and branch repository "METV-1649-python-prototype"
-----------------------------------------------------------------------------------

Procedure and needed files::

    1) download and unpack the Metview source-bundle "MetviewBundle-2017.10.90-Source.tar"
       from https://drive.google.com/open?id=0B_YlV_l0V0y7RTlWUzlERmFZMFU
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
