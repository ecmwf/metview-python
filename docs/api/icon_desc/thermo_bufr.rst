Derives (and returns) a Thermodynamic diagram data unit from :class:`Bufr` data. In such a diagram, temperature, humidity (represented by the dew point) and wind values are displayed with respect to pressure. All the three major thermodynamic diagrams types re supported in Metview: Tephigram, Skew-T and Emagram.

The resulting data can plotted (using a default visualisation and with the plot area based on the range of data values) or saved as a :class:`NetCDF` data file using :func:`write`.

If access to the output computed values is not required, or for more control of the plotting, use :func:`thermoview`.