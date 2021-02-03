Derives (and returns) a vertical average cross section data unit of upper air fields in GRIB format. For each upper air field, this average is taken along the North-South or East-West direction over a specified rectangular area and then interpolated horizontally along the direction perpendicular to the averaging direction with a spacing consistent with the resolution of the input GRIB data.

The average cross section data can be plotted (using a default visualisation and with the plot area based on the range of data values) or saved as a NetCDF data file (:class:`NetCDF`) using :func:`write`. 

If access to the output computed values is not required, or for more control of the plotting, use  :func:`maverageview`. 
