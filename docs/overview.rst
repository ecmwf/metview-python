Overview
===================

**Metview** is a meteorological workstation application designed to be a complete working environment
for both the operational and research meteorologist. Its capabilities include powerful data access,
processing and visualisation. It features both a powerful **icon-based user interface** for
interactive work and a **Python** interface for batch processing.

Metview can take input data from a variety of sources, including:

* :doc:`GRIB </data_types/fieldset>` files (editions 1 and 2)
* :doc:`BUFR </data_types/bufr>` files
* :doc:`MARS </gen_files/icon_functions/retrieve>` (ECMWF's meteorological archive)
* :doc:`ODB </data_types/odb>` (Observation Database)
* :doc:`ASCII data file </data_types/table>` (CSV, grids and scattered data)
* :doc:`Geopoints </data_types/geopoints>` (Metview's own format for handling scattered data)
* :doc:`NetCDF </data_types/netcdf>` files

Powerful data filtering and processing facilities are then available, and if graphics output is desired, then Metview can produce many plot types, including:

* map views with :ref:`scalar <gallery_group_map_scalar>`, :ref:`vector <gallery_group_map_vector>`, :ref:`point <gallery_group_map_point>` and :ref:`curve <gallery_group_map_curve>` data in various :ref:`projections <gallery_group_map_projections>` 
* :ref:`cross sections <gallery_group_sections>`
* vertical profiles
* :ref:`thermodynamic diagrams <gallery_group_map_thermo>`
* :ref:`x/y graph plots <gallery_group_xy>`
* intelligent overlay of data from various sources on the same map arrangement of multiple plots on the same page

Metview can also interface with external models and applications, such as `VAPOR <https://confluence.ecmwf.int/display/METV/3D+visualisation+with+VAPOR>`_, `Met3D  <https://confluence.ecmwf.int/display/METV/Met3D+Prepare>`_, `FLEXTRA <https://confluence.ecmwf.int/display/METV/The+FLEXTRA+interface>`_ and `FLEXPART <https://confluence.ecmwf.int/display/METV/The+FLEXPART+interface>`_.

