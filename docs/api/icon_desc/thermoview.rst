

Specifies the view for thermodynamic diagram plots from a suitable :class:`Fieldset` (GRIB), :class:`Bufr` and :func:`input_visualiser` data source. It can also take the output from :func:`thermo_data` as an input. In this case, a consistency check is performed between the parameters that are common to both functions.

In addition to the parameters required for the thermodynamic computation, :func:`thermoview` specifies the axis details as well as the plot positioning in the plot frame of the display window/paper sheet and the overlay of different data units in the same plot. 

When using :func:`thermoview` the generated profile data cannot be accessed. If you need to access this data use :func:`thermo_data` instead.

For further details on the role and usage of views in the visualisation process, please see `Anaylis Views <https://confluence.ecmwf.int/display/METV/Analysis+Views>`_.
