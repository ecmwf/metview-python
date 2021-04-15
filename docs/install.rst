Binaries and Python Bindings
============================

Metview consists of two parts. The 'binaries' are the core of Metview, incorporating the
user interface, the majority of the data processing code and the Macro programming language.
The Python bindings sit on top of the binaries and provide a powerful Python interface to
Metview's functionality. The binaries can run standalone, and the Python bindings require
the binaries.


Metview on conda and PyPi
=========================

These packages are maintained by ECMWF and are generally up to date.

Metview's binaries are available on conda for both Linux and MacOS. From a conda environment, the following command will install Metview without any
need to compile from source:

.. code-block:: bash

    conda install -c conda-forge metview

Once installed, Metview can be updated with this command:

.. code-block:: bash

    conda update -c conda-forge metview


There is also a batch-only version of Metview's binaries on conda, called metview-batch. This does not include the graphical user interface and is therefore more lightweight and can be used in environments such as Binder. It does include the ability to produce graphical plots, and they must be generated as files (PNG, PDF, SVG, ...) or as inline plots in Jupyter notebooks.

.. code-block:: bash

    conda install -c conda-forge metview-batch

Metview's Python interface is installed separately via pip:

.. code-block:: bash

    pip install metview


Community-built Binary Packages
==================================

Community-built Metview binaries for a number of Linux distributions can be found here:
https://software.opensuse.org/download.html?project=home%3ASStepke&package=Metview

From Ubuntu 16.04, Metview is available from the standard repositories and can be installed like this:

.. code-block:: bash

    sudo apt-get install metview

These packages are not maintained by ECMWF, so any issues with installation should be reported to
their maintainers.

Metview Source Releases
============================

See the `Change History <https://confluence.ecmwf.int/display/METV/Change+History>`_ for details
of each release. The source of each Metview version can be found on the
`Releases <https://confluence.ecmwf.int/display/METV/Releases>`_ page.

To build Metview and its ECMWF dependencies in one go, try
`The Metview Source Bundle <https://confluence.ecmwf.int/display/METV/The+Metview+Source+Bundle>`_.

Metview's Python bindings are available on github:
https://github.com/ecmwf/metview-python