average_ew
=====================

.. py:function:: average_ew(fs, area, increment)
   
   Computes the zonal average for each field in ``fs`` for a set of latitude belts.

   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :param list area: area as [N,W,S,E] to perform the averaging 
   :param number increment: increment in degrees defining the size of the latitude belts
   :rtype: 1d-ndarray or 2d-ndarray

   If ``fs`` only contains one field a 1d-ndarray is returned otherwise the result is a 2d-ndarray. 
   
   The averaging is performed for each field individually within the latitude belts defined by ``area`` and ``increment``. Each grid point value is weighted by the cosine of its latitude. Missing values are ignored. If a latitude belt contains no grid point values Nan is returned for that belt. 

   :Example:
      
      .. code-block:: python

         ave = average_ew(fs, [60,-180,-60,180], 2.5)

      Here we compute the averages over full latitude circles starting from 60N, stepping by 2.5 degrees until 60S. If ``fs`` contains only one field the output will be a 1d-ndarray of 49 E-W average values, from North to South. If ``fs`` contains n fields then the output will be an array of n 1d-arrays each containing 49 values. Each value in the result represents the average at latitude Lat based on those grid points whose latitude coordinate is between Lat-1.25 and Lat+1.25 (1.25 is 2.5/2), i.e. within a latitude belt with width of 2.5 degrees, centered around Lat.

   .. note::
      See also :func:`average_ns`.

.. mv-minigallery:: average_ew
