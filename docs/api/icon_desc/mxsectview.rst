Specifies the view for cross section plots from a suitable GRIB data source . It can also take the output from :func:`mcross_sect` as an input. In this case, a consistency check is performed between the parameters that are common to both functions.

In addition to the parameters required for the cross section computation, :func:`mxsectview` specifies the axis details as well as the plot positioning in the plot frame of the display window/paper sheet and the overlay of different data units in the same plot.

When using :func:`mxsectview` the generated profile data cannot be accessed. If you need to access this data use :func:`mcross_sect` instead.

If an orography is plotted it can be customised by applying :func:`mgraph`.

For further details on the role and usage of views in the visualisation process, please see `Anaylis Views <https://confluence.ecmwf.int/display/METV/Analysis+Views>`_.
