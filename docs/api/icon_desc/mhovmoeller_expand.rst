Allows the production of Hovmoeller diagrams to be computed incrementally. This could be useful, for example, if the input data is too large or the Hovmoeller diagram needs to be updated periodically (e.g. to produce a diagram operationally during a certain period of time).

The resulting data can be plotted (using a default visualisation and with the plot area based on the range of data values) or saved as a NetCDF data file using :func:`write`.

If access to the computed values is not required, or for more control of the plotting, use :func:`mhovmoellerview`.