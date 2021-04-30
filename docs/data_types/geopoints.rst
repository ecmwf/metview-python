Geopoints object
******************

.. py:class:: Geopoints

   Geopoints is the format used by Metview to handle spatially irregular data (e.g. observations)
   in an ASCII format. 


The Geopoints file formats
##########################

   A geopoints file is an ASCII file containing a header section and a data section consisting of
   several columns. There are some different 'flavours' of the format, described below.

   The data elements that can be present in a geopoints file are the point coordinates (latitude
   and longitude), the level, date, time and value of either one or two parameters. A two-parameter
   geopoints file is considered by the plotting engine to contain the components of a vector quantity
   such as wind.

   The format does not care about the alignment of columns, it just requires that there is at least one
   whitespace character between entries. The elements that must be present are an initial line tagged
   with the keyword `#GEO`, a line tagged with the keyword `#DATA` and the data points themselves.
   There can also be an optional section for meta-data, which must start with `#METADATA` - see section
   below for details. The lines in-between the header and the data sections are for human-readable
   information only and are not used in the interpretation of the file. All formats apart from the
   Standard format require an additional line in the header section to specify the format; this
   line must start with `#FORMAT` followed by the name of the format being used.

   Note that a time should be expressed as HHMM; a time of 12 will be interpreted as 0012 , ie 00:12.

Standard (6-column) geopoints
+++++++++++++++++++++++++++++

   This is the default format that Metview uses. This example shows a geopoints file containing dry bulb
   temperature at 2m (PARAMETER = 12004).

   .. code-block:: python

      #GEO
      PARAMETER = 12004
      lat        long    level  date       time    value
      #DATA
      36.15      -5.35     0   19970810    1200    300.9
      34.58      32.98     0   19970810    1200    301.6
      41.97      21.65     0   19970810    1200    299.4
      45.03       7.73     0   19970810    1200    294
      45.67       9.7      0   19970810    1200    302.2
      44.43       9.93     0   19970810    1200    293.4


Format XYV (Compact format)
++++++++++++++++++++++++++++

   This format allows data to be specified with just three columns: X (longitude), Y (latitude) and V (value).
   The start of an example file would look like the following:

   .. code-block:: python

      #GEO
      #FORMAT XYV
      PARAMETER = 12004
      x/long y/lat value
      #DATA
      -5.35  36.15  300.9
      32.98  34.58  301.6
      21.65  41.97  299.4


Format XY_VECTOR (XY Vector format)
++++++++++++++++++++++++++++++++++++

   This format allows two parameters to be stored as the components of a two-dimensional vector (for example
   uv wind components). The start of an example file would look like the following:

   .. code-block:: python

      #GEO
      #FORMAT XY_VECTOR
      # lat    lon   height   date       time      u       v
      #DATA
      80       0      0      20030617    1200   -4.9001  -8.3126
      80       5.5    0      20030617    1200   -5.6628  -7.7252
      80       11     0      20030617    1200   -6.4254  -7.13829


Format POLAR_VECTOR (Polar Vector format)
++++++++++++++++++++++++++++++++++++++++++

   This format allows two parameters to be stored as the speed and direction of a two-dimensional vector, the direction being specified in degrees where zero is due South and angles increase clockwise. The start of an example file would look like the following:

   .. code-block:: python

      #GEO
      #FORMAT POLAR_VECTOR
      # lat      lon     height     date       time   speed   direction
      #DATA
      50.97     6.05      0      20030614     1200     4       90
      41.97     21.65     0      20030614     1200     5       330
      35.85     14.48     0      20030614     1200     11      170


Format NCOLS (Multi-column format)
+++++++++++++++++++++++++++++++++++

   This format allows any number of parameters to be stored in a geopoints file. The #COLUMNS section is
   used to understand the columns, as they can be put in any order. The following column names are reserved
   and are treated specially: longitude, level, date, time, stnid. A column with a different name will be
   treated as a value column. The data should all be numeric, apart from stnid, which is stored as a string.

   The start of an example file would look like the following:

   .. code-block:: python

      #GEO
      #FORMAT NCOLS
      #COLUMNS
      latitude longitude  time date       t2     o3    td    rh
      #DATA
      32.55   35.85  0600    20120218    273.9   35   280.3   75
      31.72   35.98  1800    20120218    274.9   24   290.4   68
      51.93   8.32   1200    20140218    278.9   28   300.5   34
      41.1    20.82  1200    20150218    279.9   83   310.6   42



Construction
############

   A geopoints file can be read from disk using :ref:`read() <read_fn>`:

   .. code-block:: python

      import metview as mv

      gpt = mv.read("obs.gpt") # create from geopoints file


   The :func:`create_geo` function can be used to construct a Geopoints object from scratch.


Indexing
########

   Indexing a single element of a Geopoints variable works in the standard Python way. The return
   value is a dict describing the nth point:

   .. code-block:: python

      g0 = gpt[0] # first element
      g7 = gpt[7] # eighth field
      print(g7.latitude, g7.longitude, g7.value)


Extracting and setting columns
##############################

   There are two ways to extract columns of data from a geopoints variable.

   1. Use the methods provided, e.g.

   .. code-block:: python

      lats = gpt.latitudes()
      vals = gpt.values()
      rh   = gpt.values('rh') # assuming NCOLS format with a value column of name 'rh'

   2. Use column indexing, e.g.

   .. code-block:: python

      lats = gpt['latitude']
      vals = gpt['value']
      rh   = gpt['rh'] # assuming NCOLS format with a value column of name 'rh'

   To assign values to a column, again there are 2 methods, but they have different behaviours:

   Use the set_ methods provided - these create new Geopoints variables and do not modify the originals, e.g.

   .. code-block:: python

      gpt_new = gpt.set_latitudes(lats) # lats is a numpy array

   Use column indexing - this modifies the original Geopoints variable and is therefore more efficient, e.g.

   .. code-block:: python

      gpt['latitude'] = lats # lats is a vector


Storing and retrieving meta-data
################################

   A geopoints file can have a section of meta-data key-value pairs in its header before the #DATA section,
   as illustrated here:

   .. code-block:: python

      #GEO
      PARAMETER = 12030
      #METADATA
      param=temperature
      date=20130804
      time=1200
      level=0.2
      #lat    long    level   date    time    value
      #DATA
      55.01   8.41    0.2     20130804  1200  294.4
      54.33   8.60    0.2     20130804  1200  296.9

   Here, four pieces of meta-data are stored. They can be set and queried in the Macro (or Python)
   language, like this:

   .. code-block:: python

      data = mv.read('geopoints_with_metadata.gpt')
      md = data.metadata()
      print(md)
      print(md['level'])

   Output:

   .. code-block:: python

      (date:20130804,level:0.2,param:temperature,time:1200)
      0.2

.. _geopoints_db_info:

Storing Data Origin Information in a Geopoints File
###################################################

   It is possible to store details of the origin of the geopoints data in its file. The following
   example shows the meta-information generated by an ODB query.

   .. code-block:: python

      #GEO
      lat long level date time value
      #DB_INFO
      DB_SYSTEM: ODB
      DB_COLUMN: lldegrees(lat@hdr);lldegrees(lon@hdr); ; ; ;obsvalue@body
      DB_COLUMN_ALIAS: lldegrees(lat);lldegrees(lon); ; ; ;obsvalue@body
      DB_PATH: /tmp/cgi/odb/ECMA.conv
      DB_QUERY_BEGIN select lldegrees(lat), lldegrees(lon), obsvalue from hdr, body where varno=$t2m and obsvalue is not null
      DB_QUERY_END
      #DATA
      36.150 -5.350 0.000 0 0000 295.10000000

   Currently, ODB is the only database system to generate this meta-information. It is not discussed in
   detail here because it is generated automatically. Functions exist to extract this information from
   a geopoints variable - see those whose names begin with "db_".


Exporting as a pandas dataframe
###############################

   The Geopoints data type has an additional function, :py:meth:`to_dataframe`, which can be used
   to produce a Pandas Dataframe object as shown. Note that the date and time columns are combined
   into a single datetime column.

   .. code-block:: python

      import metview as mv
      import pandas as pd
 
      gpt = mv.read("gpts.gpt") # returns a Geopoints
      df = gpt.to_dataframe()   # returns a Pandas Dataframe
      print(df.head())

   Output:

   .. code-block:: python

                     date  latitude   level  longitude    value
      0 2018-01-14 12:00:00      30.0  1000.0      -24.0  288.736
      1 2018-01-14 12:00:00      30.0  1000.0      -18.0  288.736
      2 2018-01-14 12:00:00      30.0  1000.0      -12.0  286.736
      3 2018-01-14 12:00:00      30.0  1000.0       -6.0      NaN
      4 2018-01-14 12:00:00      30.0  1000.0        0.0      NaN


Per-point methods
###################

   Numeric operations typically operate on just the value column of a Geopoints object;
   latitudes and longitudes for example are untouched unless otherwise stated. For the format
   XY_VECTOR, both value columns are used in calculations. For the NCOLS format, all value
   columns are manipulated during operations. Currently the level, date and time can only be used
   for filtering (or can be extracted into  Vector variables for other uses). They must be
   present in the file but you can specify any dummy value if you do not intend to use them.


   Unary functions and methods on Geopoints act on each point. For example, the
   :py:meth:`abs` method will return a new Geopoints where all the values have
   the absolute of their original value.

   Operations between Geopoints act on corresponding points in each
   Geopoints. Both Geopoints must have the same number of points. For example, if we have one
   Geopoints containing observation data for one time step, and another containing
   observations for the same points at another time step, then we can easily compute the
   difference Geopoints like this:

      .. code-block:: python

         diff = gpt1 - gpt2

   Similarly, operations work between Geopoints and numbers, for example:

      .. code-block:: python

         temperature_in_K = mv.read("temp.gpt")
         temperature_in_C = temperature_in_K - 273.15


   The following list of operators are valid when acting between two Geopoints and also when acting between
   a Geopoints and a number. Of these, the logical operators return a Geopoints containing values of
   1 where they pass the test, or 0 where they fail.

.. csv-table:: Table Title
   :file: operators.csv
   :header-rows: 1

Operations between geopoints and fieldsets
##########################################

   When you carry out an operation between geopoints and fieldset (or images) variables the result
   is another geopoints variable:

   * When operating with fieldsets, the values of the field(s) at the geopoints locations are calculated
     by interpolation and the resulting field values undergo the operation with the geopoints values
   * When combining with an image no interpolation takes place; the pixel values where the geopoints are
     located are extracted and these undergo the operation with the geopoints values
   * Unless otherwise stated in the operator or function description, only the first value of a two-valued
     geopoint is considered during a calculation
   * Combinations include algebraic operations, boolean operations and a number of functions.


Missing values in geopoints
###########################

   When you combine fieldset data with geopoints, you may end up with some missing values in your
   Geopoints variable. These will have the value `numpy.nan`. Any operation on a geopoints variable
   will bypass missing values (e.g. :func:`mean`) or retain them unaltered (e.g. :func:`max`); see individual
   function descriptions for more details.

   In order to remove missing values from a geopoints variable, use the function :func:`remove_missing_values`
   as illustrated below:

   .. code-block:: python

      geo_clean = geo_source.remove_missing_values()


Missing coordinates in geopoints
################################

   It is possible to include missing values in the latitude or longitude columns (or both). A point with
   either coordinate missing will be excluded from any operation that requires location information.

Plotting
########

   Geopoints objects can be plotted with :func:`plot` command and customised
   using :func:`msymb`.


Methods and functions
#####################

.. include:: /gen_files/toc/geopoints_obj.rst