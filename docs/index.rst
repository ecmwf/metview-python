

Metview
====================================

.. warning::
   This documentation is work in progress. It is not yet ready.

.. image:: _static/metview-all-in-one.png
   :width: 300px

**Metview** is a meteorological workstation application designed to be a complete working environment for both the operational and research meteorologist. Its capabilities include powerful data access, processing and visualisation. It features both a powerful **icon-based user interface** for interactive work and a **Python** interface for batch processing.

.. Metview can take input data from a variety of sources, including:

.. * GRIB files (editions 1 and 2)
.. * BUFR files
.. * MARS (ECMWF's meteorological archive)
.. * ODB (Observation Database)
.. * Local databases
.. * ASCII data files (CSV, grids and scattered data)
.. * Geopoints (Metview's own format for handling scattered data)
.. * NetCDF

.. Powerful data filtering and processing facilities are then available, and if graphics output is desired, then Metview can produce many plot types, including:

.. * map views in various projections
.. * cross sections
.. * vertical profiles
.. * x/y graph plots
.. * intelligent overlay of data from various sources on the same map arrangement of multiple plots on the same page

.. Metview can also interface with external models and applications, such as VAPOR,  Met3D, FLEXTRA and FLEXPART.

Metview was developed as part of a cooperation between ECMWF and INPE (Brazilian National Institute for Space Research).

.. toctree::
   :maxdepth: 1
   :caption: Examples
   :titlesonly:

   gen_files/gallery/index
   notebook_gallery
   debug/advection
   gen_files/gallery/advection

.. toctree::
   :maxdepth: 1
   :caption: Documentation

   api/ref_guide 
   data_types/index
   

Indices and tables
==================

* :ref:`genindex`


.. * :ref:`modindex`
.. * :ref:`search`
