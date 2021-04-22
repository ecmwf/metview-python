netcdf_auto_translate_times
==============================

..  py:function::  netcdf_auto_translate_times(status)

    Sets whether Metview automatically translates time variables into dates when retrieving with the :func:`value` or :func:`values` functions. 
    
    :param status: enables/disables translation (0 or 1)
    :type status: number
    :rtype: None
    
    Setting ``status`` to 1 enables the translation (which is the default behaviour), setting it to 0 disables it. If disabled, :func:`value` and :func:`values` will instead return the raw numbers encoded in the NetCDF variable. This is a global option, not specific to a particular NetCDF file.



.. mv-minigallery:: netcdf_auto_translate_times
