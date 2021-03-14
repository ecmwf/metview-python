Fieldset object
******************

.. py:class:: Fieldset

   Represents GRIB data. It is a list-like object with each list entry representing a GRIB message. 

Construction
############
  

   Fieldsets can be directly constructed either as empty, with a path to a GRIB file or using :func:`read`:

   .. code-block:: python

      import metview as mv

      f1 = mv.Fieldset() # empty Fieldset
      f2 = mv.Fieldset(path="test.grib") # create from GRIB file
      f3 = mv.read("my.grib") # create from GRIB file

Concatenation
#############

   Concatenation can be performed in these ways:

   .. code-block:: python

      f4 = mv.Fieldset(fields=[f1, f2, f3]) # create from list of Fieldsets
      f4.append(f2) # append f2 onto the end of f4
      f5 = mv.merge(f2, f3)


Indexing
############

   Indexing and slicing works in the standard Python way. There is no such thing as a single
   field object in Metview, only a Fieldset with a single field.
   
   .. code-block:: python

      f[0] # first field
      f[1] # second field
      f[-1] # last field
      f[0:6] # the first 5 fields
      f[::2] # every second field

Iteration
############

   A Fieldset is iterable, with each iteration returning a single-field Fieldset, e.g.

      .. code-block:: python

         fs = mv.Fieldset(path="test.grib")
         field_maxes = [f.maxvalue() for f in fs]

   `len(fs)` and `fs.count()` both return the number of fields in the Fieldset.


Functions vs methods
####################

   Functions that work with Fieldsets can also be used as methods, provided that their first argument
   is a Fieldset. For example, the following two operations are shown in two equivalent ways:

      .. code-block:: python

         a = mv.abs(fs)
         a = fs.abs()
         b = mv.bitmap(fs, 0)
         b = fs.bitmap(0)


Per-point methods
###################

   Unary functions and methods on Fieldsets act on each grid point of each field. For example, the
   :py:meth:`abs` method will return a new Fieldset where all the grid values of all the fields have
   the absolute of their original value.

   Operations between Fieldsets act on corresponding grid points in the corresponding fields in each
   Fieldset. Both Fieldsets must have the same number of fields and the same number of points in their
   corresponding fields. For example, if we have one Fieldset containing analysis data for 99
   vertical levels, and another with forecast data for the same 99 levels (stored in the same order) then
   we can easily compute the difference Fieldset like this:

      .. code-block:: python

         diff = forecast_fs - analysis_fs # contains 99 fields of differences

   The following list of operators are valid when acting between two Fieldsets and also when acting between
   a Fieldset and a number:
   `+`, `-`, `*`, `/`, `**`, `&`, `|`, `~`, `>`, `>=`, `<`, `<=`, `==`, `!=`.

   Of these, the logical operators, such as `>` and `==` return a Fieldset containing values of
   1 where they pass the test, or 0 where they fail.


Data extraction
################

A Fieldset can return an xarray by calling its :py:meth:`to_dataset` method.

A Fieldset can return a numpy array of values by calling its :py:meth:`values` method.

A Fieldset can return a :py:class:`Geopoints` object by calling the :py:meth:`grib_to_geo` function.






.. include:: /gen_files/toc/grib_obj.rst
   
      



