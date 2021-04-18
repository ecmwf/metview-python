netcdf_auto_rescale_values_to_fit_packed_type
===============================================

..  py:function:: netcdf_auto_rescale_values_to_fit_packed_type(status)

    Sets whether Metview automatically rescales values if they overflow the packed data type of the current NetCDF variable. 
    
    :param status: enables/disables rescaling (0 or 1)
    :type status: number
    :rtype: None
    
    Setting ``status`` to 1 enables the rescaling (which is the default behaviour), setting it to 0 disables it. If disabled, and the computed values overflow the data type, the script will fail.


.. mv-minigallery:: netcdf_auto_rescale_values_to_fit_packed_type
