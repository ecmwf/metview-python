NetCDF functions
******************

..  py:function:: attributes(nc)

    Returns the attributes of the current NetCDF variable in ``nc``.

    :param nc: input nectdf
    :type nc: :class:`NetCDF`
    :rtype: dict


..  py:function:: dimensions(nc)

    Returns the dimension values of the current NetCDF variable in ``nc``. 

    :param nc: input nectdf
    :type nc: :class:`NetCDF`
    :rtype: ndarray


..  py:function:: dimension_names(nc)

    Returns the list of the dimension names of the current NetCDF variable in ``nc``.

    :param nc: input nectdf
    :type nc: :class:`NetCDF`
    :rtype: list

..  py:function:: global_attributes(nc)

    Returns the global attributes of ``nc``.

    :param nc: input nectdf
    :type nc: :class:`NetCDF`
    :rtype: dict


..  py:function:: max(nc, nc_other)
..  py:function:: max(nc, value)

    Returns the :class:`NetCDF` of the maximum value of ``nc`` and ``nc_other`` or ``value``.

    :param nc: input nectdf
    :type nc: :class:`NetCDF`
    :param nc_other: another input nectdf
    :type nc_other: :class:`NetCDF`
    :param value: value
    :type value: float
    :rtype:  :class:`NetCDF`

..  py:function:: min(nc, nc_other)
..  py:function:: min(nc, value)

    Returns the :class:`NetCDF` of the minumum value of ``nc`` and ``nc_other`` or ``value``.

    :param nc: input nectdf
    :type nc: :class:`NetCDF`
    :param nc_other: another input nectdf
    :type nc_other: :class:`NetCDF`
    :param value: value
    :type value: float
    :rtype:  :class:`NetCDF`


..  py:function:: netcdf_auto_rescale_values_to_fit_packed_type(status)

    Sets whether Metview automatically rescales values if they overflow the packed data type of the current NetCDF variable. 
    
    :param status: enables/disables rescaling (0 or 1)
    :type status: int
    :rtype: None
    
    Setting ``status`` to 1 enables the rescaling (which is the default behaviour), setting it to 0 disables it. If disabled, and the computed values overflow the data type, the script will fail.


..  py:function::  netcdf_auto_translate_times(status)

    Sets whether Metview automatically translates time variables into dates when retrieving with the :func:`value` or :func:`values` functions. 
    
    :param status: enables/disables translation (0 or 1)
    :type status: int
    :rtype: None
    
    Setting ``status`` to 1 enables the translation (which is the default behaviour), setting it to 0 disables it. If disabled, :func:`value` and :func:`values` will instead return the raw numbers encoded in the NetCDF variable. This is a global option, not specific to a particular NetCDF file.


..  py:function::  netcdf_preserve_missing_values(status)

    Sets whether Metview correctly handles missing values by not including them in computations. 
    
    :param status: enables/disables missing value inclusion (0 or 1)
    :type status: int
    :rtype: None

    Set ``status`` to 1 to ensure the correct treatment of missing values, or set it to 0 to revert to Metview 4's behaviour of considering them to be normal numbers. This is a global option, not specific to a particular NetCDF file.


..  py:function:: netcdf_auto_scale_values(status)

    Sets whether Metview automatically applies scale_factor and add_set attributes if they are present. 
    
    :param status: enables/disables auto scaling (0 or 1)
    :type status: int
    :rtype: None
    
    Setting ``status`` to 1 enables the scaling (which is the default behaviour), setting it to 0 disables it. If disabled, the the raw numbers encoded in the NetCDF variable will be used in any calculations. This is a global option, not specific to a particular NetCDF file.


..  py:function::  setcurrent(nc, index_or_name)

    On a multi-variable :class:`NetCDF` sets the specified variable as the current variable. Functions and operators act on the current variable only.

    :param nc: input NetCDF
    :type nc: :class:`NetCDF`
    :param index_or_name: index or name of the NetCDF variable
    :type index_or_name: int or str
    :rtype: None

    A :class:`NetCDF` produced by the Metview applications are uni-variable, so in their case :func:`setcurrent` need not be used. For a multi-variable :class:`NetCDF` :func:`setcurrent` can be usefully combined with :func:`variables` as the example below illustrates it.

    :Example:

        .. code-block:: python

            import metview as mv 

            nc = mv.read("my_data.nc")

            for v in mv.variables(nc):
                mv.setcurrent(nc, v)
                # acts on current variable only
                nc = nc - 273.16


..  py:function::  value(nc, index)

    Returns the value at position ``index`` of the current NetCDF variable from ``nc``.
   
    :param nc: input NetCDF
    :type nc: :class:`NetCDF`
    :param index: value index (zero-based)
    :type index: int
    :rtype: float, str or datetime.datetime

..  py:function::  values(nc, [index])

    Returns all the values of the current NetCDF variable in ``nc``.

    :param nc: input NetCDF
    :type nc: :class:`NetCDF`
    :param index: value index (zero-based)
    :type index: list
    :rtype: ndarray or list of str or list of datetime.datetime

    To define a hypercube for the value extraction ``index`` has to be specified as a list with the same number of elements as the number of dimensions of the current NetCDF variable. The elements (except one) should be numbers, specifying the indexes (0-based) into the respective dimensions from where the value(s) are to be taken. If all elements are numbers, then they simply specify the coordinates for a single value (returned as a single-value array). Optionally, one of the elements can be set to the string 'all'; in this case, all the values from that dimension are returned. 
    
    :Example:
    
        If the current NetCDF variable is defined with 3 dimensions: Q(time, region, exp) then we can obtain the values for all times, for the second region and the fifth exp with this syntax:

        .. code-block:: python

            v = mv.values(nc, ['all', 1, 4])


..  py:function:: variables(nc)

    Returns the variable names from ``nc``.

    :param nc: input NetCDF
    :type nc: :class:`NetCDF`
    :rtype: list of str
