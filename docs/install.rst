Installing
==================================


Metview on conda and PyPi
=========================

Metview is available on conda for both Linux and MacOS. From a conda environment, the following command will install Metview without any need to compile from source:

.. code-block:: bash

    conda install -c conda-forge metview

Once installed, Metview can be updated with this command:

.. code-block:: bash

    conda update -c conda-forge metview


There is also a batch-only version of Metview on conda, called metview-batch. This does not include the graphical user interface and is therefore more lightweight and can be used in environments such as Binder. It does include the ability to produce graphical plots, and they must be generated as files (PNG, PDF, SVG, ...) or as inline plots in Jupyter notebooks.

.. code-block:: bash

    conda install -c conda-forge metview-batch

Metview's Python interface is installed separately via pip:

.. code-block:: bash

    pip install metview


Community-built Binary Packages
==================================

The following link provides binary installations for many Linux platforms:

    https://software.opensuse.org/download.html?project=home%3ASStepke&package=Metview

From Ubuntu 16.04, Metview is available from the standard repositories and can be installed like this:
sudo apt-get install metview


Metview Source Releases
============================

See the `Change History <https://confluence.ecmwf.int/display/METV/Change+History>`_ for details of each release.

The source of each Metview version can be found on the
`Releases <https://confluence.ecmwf.int/display/METV/Releases>`_ page.

To build Metview and its ECMWF dependencies in one go, try
`The Metview Source Bundle <https://confluence.ecmwf.int/display/METV/The+Metview+Source+Bundle>`_.
