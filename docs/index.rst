

Metview
====================================

.. image:: _static/metview-all-in-one.png
   :width: 300px

**Metview** is a meteorological workstation application designed to be a complete working environment
for both the operational and research meteorologist. Its capabilities include powerful data access,
processing and visualisation. It features both a powerful **icon-based user interface** for
interactive work and a **Python** interface for batch processing.

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


.. note::
   These pages concentrate on the Python interface. The full documentation will appear here over time,
   but for now the rest of the Metview documentation (the user interface and the Macro language) and
   supplemental resources such as training courses and FAQs can be found at
   https://confluence.ecmwf.int/metview.

Metview was developed as part of a cooperation between ECMWF and INPE (Brazilian National Institute for Space Research).

.. toctree::
   :maxdepth: 1
   :caption: Examples
   :titlesonly:

   gen_files/gallery/index
   notebook_gallery

.. toctree::
   :maxdepth: 1
   :caption: Documentation

   data_types/index
   api/ref_guide 

.. toctree::
   :maxdepth: 1
   :caption: Installation  
   
   install

Indices and tables
==================

* :ref:`genindex`


.. * :ref:`modindex`
.. * :ref:`search`
