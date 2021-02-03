Defines the **view** for Hovmoeller diagram plots from a suitable GRIB data source. It can also take the output from a hovmoeller data object as an input. In this case, a consistency check is performed between the parameters that are common to both functions.

In addition to the parameters required for the Hovmoeller diagram computation, :func:`mhovmoellerview` specifies the axis details as well as the plot positioning in the plot frame of the display window/paper sheet and the overlay of different data units in the same plot.

To access the computed output values use a hovmoeller data object.

For further details on the role and usage of views in the visualisation process, please see `Anaylis Views <https://confluence.ecmwf.int/display/METV/Analysis+Views>`_.
  