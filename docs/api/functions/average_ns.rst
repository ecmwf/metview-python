average_ns
=======================

.. py:function:: average_ns(fs, area, increment)
   
   Computes the meridional average for each field in ``fs`` for a set of longitude strips.

   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :param list area: area as [N,W,S,E] to perform the averaging 
   :param number increment: increment in degrees defining the size of the longitude strips
   :rtype: 1d-ndarray or 2d-ndarray
   
   The averaging is performed for each field individually within the longitude strips defined by ``area`` and ``increment``. Each grid point value is weighted by the cosine of its latitude. Missing values are ignored. If a longitude strip contains no grid point values Nan is returned for that strip. 

   :Example:
      
      .. code-block:: python

         ave = average_ns(fs, [30,0,-30,360], 5)

      Here we compute the averages over longitude strips bounded by 30N and 30S, in 5 degree intervals around the globe. The result for each field in ``fs`` is vector of 73 values (in this case values for 0 and 360 are duplicated values). Each value returned (representing the average at longitude Lon) is the average of non-missing values in those grid points whose longitude coordinate is between Lon-2.5 and Lon+2.5 (2.5 is 5/2), in the strip between 30N and 30S.


.. mv-minigallery:: average_ns
