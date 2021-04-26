Generates a vertical profile data unit of upper air fields in GRIB format for a particular point location (or small area). For each upper air field, values are interpolated at the point location (or integrated over the small area).

The vertical profile data can be plotted using a default visualisation based on the range of data values. It can also be saved as a NetCDF data file (:class:`NetCDF`) using :func:`write`.

If access to the output computed values is not required, or for more control of the plotting, use  :func:`mvertprofview`. 
