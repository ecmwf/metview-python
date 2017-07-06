

Metview Python bindings
=======================


Build Metview from source bundle and branch repository "METV-1649-python-prototype"
-----------------------------------------------------------------------------------

Procedure and needed files::

    1) download and unpack the Metview source-bundle "MetviewBundle-2017.05.0-Source.tar"
       from https://software.ecmwf.int/wiki/display/METV/The+Metview+Source+Bundle
    2) delete or rename the "metview" directory. It will be replace by the branch repository
    3) clone metview from feature/METV-1649-python-prototype
    4) edit libemos/gribex/CMakeLists.txt and comment out emoscyc.F from the list
       of files to be compiled
    5) edit libemos/libemos-dp/CMakeLists.txt and change "TYPE STATIC" into "TYPE SHARED"
    6) edit the CMakeLists.txt file in the root directory of the bundle source to change
       TAG 4.8.6 into BRANCH feature/METV-1649-python-prototype
    6) replace all files into <metview_source_path>/mars-client/src with files
       contained in the mars-src.zip archive (https://software.ecmwf.int/issues/secure/attachment/34940/34940_mars-src.zip)
    7) configure the building in a separate directory by means of the
       cmake -DENABLE_ODB=ON -DENABLE_XXHASH=OFF <metview_source_path> command
    8) build by typing "make" or "make -j8"
    9) to start the tests type from <metview_source_path>/metview directory: ctest 


Create a virtual environment
----------------------------

Create and activate a new virtualenv::

    python3 -m venv <folder>
    source <folder>/bin/activate


Export LD_LIBRARY_PATH variable
-------------------------------

Add these paths to the LD_LIBRARY_PATH variable typing the following command line::

    export LD_LIBRARY_PATH=\
        <build_dir>/metview/src/Macro:\
        <build_dir>/metview/src/libMetview:\
        <build_dir>/metview/src/libFTimeUtil:\
        <build_dir>/metview/src/libUtil:<build_dir>/lib:\
        <source_bundle_dir>/metview/src/Macro/include


Install
-------

From the mpy folder install with::

    pip install -e .


Test
----

Launch tests with::

    pytest -v tests
