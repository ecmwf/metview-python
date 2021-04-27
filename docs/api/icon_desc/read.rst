Filters a :class:`Fieldset` (GRIB data) by selecting a set of messages according to the filter conditions. It also has post-processing options such as ``grid`` and ``area``, for regridding and sub-area extraction respectively; these use the same interpolation routines as the standard ECMWF MARS client.

.. note::
    
    :func:`read` is almost identical to :func:`retrieve` but it works with local GRIB data. 
    