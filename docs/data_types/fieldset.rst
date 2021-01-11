Fieldset object
******************

.. py:class:: Fieldset

   Represents GRIB data. It is a list-like object with each list entry representing a GRIB message. 

   Fieldsets can be directly constructed either as empty, with a path to a GRIB file or using :func:`read`:

   .. code-block:: python

      import metview as mv

      f1 = mv.Fieldset()
      f2 = mv.Fieldset(path="test.grib")
      f3 = mv.read("my.grib")

   Indexing works in the standard way.
   
   .. code-block:: python

      f[1] # second field
      f[-1] # last field
      f[::2] # every second field
      
   Concatenation can be done with :py:meth:`append`:

   .. code-block:: python

      f = f.append(g)
   
      



