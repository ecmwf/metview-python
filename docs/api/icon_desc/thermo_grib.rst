Generates a thermodynamic diagram data unit from GRIB data (:class:`Fieldset`). In a thermodynamic diagram temperature, humidity (represented by the dew point) and wind values are displayed with respect to pressure. Metview supports the following diagram types: Tephigram, Skew-T and Emagram (see :func:`thermoview`).

The resulting data can be visualised with :func:`plot` or saved as a :class:`NetCDF` data file using :func:`write`.

If access to the output data values is not required, or for more control of the plotting, use :func:`thermoview`.