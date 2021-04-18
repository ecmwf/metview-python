netcdf_auto_scale_values
============================

..  py:function:: netcdf_auto_scale_values(status)

    Sets whether Metview automatically applies scale_factor and add_set attributes if they are present. 
    
    :param status: enables/disables auto scaling (0 or 1)
    :type status: number
    :rtype: None
    
    Setting ``status`` to 1 enables the scaling (which is the default behaviour), setting it to 0 disables it. If disabled, the the raw numbers encoded in the NetCDF variable will be used in any calculations. This is a global option, not specific to a particular NetCDF file.

.. mv-minigallery:: netcdf_auto_scale_values
