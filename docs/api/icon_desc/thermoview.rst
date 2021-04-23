

Specifies the view for a thermodynamic diagram. 

A suitable :class:`Fieldset` (GRIB), :class:`Bufr` or :func:`input_visualiser` data can be directly plotted into a :func:`thermoview`, the necessary profiles will be automatically extracted from the input data. On top of that :func:`thermo_bufr` and :func:`thermo_grib` objects can be also visualised in a :func:`thermoview`.

When using :func:`thermoview` the generated profile data cannot be accessed. If you need to access this data use :func:`thermo_bufr` or :func:`thermo_grib` instead.

For further details on the role and usage of views in the visualisation process, please see `Anaylis Views <https://confluence.ecmwf.int/display/METV/Analysis+Views>`_.
