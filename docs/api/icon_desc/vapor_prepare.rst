Converts GRIB data into the format required by the `VAPOR <https://confluence.ecmwf.int/display/METV/3D+visualisation+with+VAPOR>`_  3D visualisation system.

.. tip:: A tutorial for :func:`vapor_prepare` can be found `here <https://confluence.ecmwf.int/display/METV/VAPOR+Tutorial>`_.  Details about setting up the Metview VAPOR interface outside ECMWF can be accessed `here <https://confluence.ecmwf.int/display/METV/VAPOR+Setup>`_.

**VAPOR input files**

VAPOR input data is described by **.vdf** (VAPOR Data Format) files. These are XML files containing the name and dimension of all the variables and the path of the actual data files storing the data values.  VAPOR stores its data values in **.vdc** (VAPOR Data Collection) files. These are NetCDF files containing wavelet compressed 3D data. There is a separate file for each variable and timestep organized into a folder hierarchy.

**VAPOR grids**

VAPOR input data must be defined on a 3D grid,  which has to be regular horizontally (on a map projection). The vertical grid structures supported by the Metview VAPOR interface are as follows: 

* For **layered** grids VAPOR expects a parameter specifying the elevation of each 3D level in the input data. This is typically the case for pressure or ECMWF model level (:math:`\eta` levels) data with height or geopotential available (or it can be computed).
* For **regular** grids the 3D levels are supposed to be equidistant (in the user coordinate space). This type can be used when the data is available on equidistant height levels.

The situation when pressure or model level data is present without height information is somewhat special. The grid in this case is not layered but can be regarded as regular in its own coordinate space (pressure or model levels) letting z axis simply represent pressure or model levels in the 3D scene rendered in VAPOR.

VAPOR uses a right-handed coordinate system which means that:

* the horizontal grid has to start at the SW corner
* the vertical coordinates have to increase along the z axis (upwards)

**How does vaport_prepare work?**

First :func:`vapor_prepare` parses the GRIB data then generates the vdf and vdc files out of it. Internally it dumps GRIB data into a raw binary format then converts it into VAPOR format by using the **raw2vdf** VAPOR command line tool. :func:`vapor_prepare` implicitly rearranges the grid to make it VAPOR compliant.

**Which GRIBs are supported for the conversion?**

Only GRIB fields on a regular lat-lon grid are supported at the moment. However, please note that  GRIBs can be internally interpolated to a regular lat-lon grid by using the ``vapor_area_selection`` parameter. The parameters to be converted are supposed to have the same validity date and time and the same vertical levels. They also have to be valid on the same grid.