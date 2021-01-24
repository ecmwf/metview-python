indexes
============


.. py:function:: indexes(fs, values)

   Finds the index of the values at each gridpoint of ``fs`` in the ``values`` array. 

   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :param ndarray values: the values to find the index for
   :rtype: :class:`Fieldset`

   Indexes are zero-based and will always have a minimum value of zero and a maximum value equal to the index of the last element of ``values``. A value lying between two values in ``values`` will use the index of the nearest value; if equidistant, then the higher value is used. ``values`` must be sorted in ascending order. 
 
   :Example: 
      
      Let us suppose that our input fieldset contains these values:

      .. code-block:: python

             10 10 30 40
         f = 15 25 35 45
             8  4 20 11

      then the following call:

      .. code-block:: python

         import metview as mv
         import numpy as np
         g = mv.indexes(f, np.array([5, 10, 15, 20, 25, 30]) 

      produces this GRIB, with values equal to the input values' positions in the input array:

      .. code-block:: python

             1 3 5 5
         g = 2 4 5 5
             1 0 3 1


.. mv-minigallery:: indexes
