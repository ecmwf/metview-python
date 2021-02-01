
NetCDF functions
==================
This is the list of all functions related to :class:`NetCDF` data.

.. list-table::
    :widths: 20 80
    :header-rows: 0


    * - :func:`attributes`
      - Returns the attributes of the current NetCDF variable

    * - :func:`dimension_names`
      - Returns a list of the netcdf's dimension names.

    * - :func:`dimensions`
      - Returns a list of the netcdf's dimensions.

    * - :func:`global_attributes`
      - Returns a definition variable holding the netcdf's global metadata.

    * - :func:`max`
      - Maximum

    * - :func:`min`
      - Minimum

    * - :func:`netcdf_auto_rescale_values_to_fit_packed_type`
      - Sets the behaviour of netcdf value handling: 1=on, 0=off

    * - :func:`netcdf_auto_scale_values`
      - Sets the behaviour of netcdf value handling: 1=on, 0=off

    * - :func:`netcdf_auto_translate_times`
      - Sets the behaviour of netcdf value handling: 1=on, 0=off

    * - :func:`netcdf_preserve_missing_values`
      - Sets the behaviour of netcdf value handling: 1=on, 0=off

    * - :func:`netcdf_visualiser`
      - Defines visualisation for NetCDF data

    * - :func:`setcurrent`
      - Sets the variable number on which netcdf functions will operate.

    * - :func:`value`
      - Returns the n:th value from the current netcdf variable.

    * - :func:`values`
      - Returns the values from a data object

    * - :func:`variables`
      - Returns a list of the names of the given netcdf file's variables.
