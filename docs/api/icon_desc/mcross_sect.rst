Generates a vertical cross section data unit of upper air fields along a specified transect line. For each upper air field, point values are interpolated along the transect line, with a spacing consistent with the resolution of the input GRIB data.

The cross section data can be plotted (using a default visualisation based on the range of data values) or saved as a NetCDF data file (:class:`NetCDF`) using :func:`write`.

If an orography is plotted it can be customised by applying an :func:`mgraph` visual definition.

If access to the output computed values is not required, or for more control of the plotting, use :func:`mxsectview`.