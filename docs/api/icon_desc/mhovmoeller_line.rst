Generates a Hovmoeller diagram data unit for a given transect line for GRIB (:class:`Fieldset`) input. The generated data can be used to display a two-dimensional graph with latitude or longitude as one axis and time as the other. The point values for each field are interpolated along the transect line, with a spacing consistent with the resolution of the input GRIB data.

The resulting data can be plotted (using a default visualisation and with the plot area based on the range of data values) or saved as a NetCDF data file using :func:`write`.

If access to the computed values is not required, or for more control of the plotting, use :func:`mhovmoellerview`.