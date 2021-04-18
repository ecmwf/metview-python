netcdf_preserve_missing_values
================================

..  py:function::  netcdf_preserve_missing_values(status)

    Sets whether Metview correctly handles missing values by not including them in computations. 
    
    :param status: enables/disables missing value inclusion (0 or 1)
    :type status: number
    :rtype: None

    Set ``status`` to 1 to ensure the correct treatment of missing values, or set it to 0 to revert to Metview 4's behaviour of considering them to be normal numbers. This is a global option, not specific to a particular NetCDF file.


.. mv-minigallery:: netcdf_preserve_missing_values
