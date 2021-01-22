integer
=============

.. py:function:: integer(fs)

   Returns the fieldset of the integer part of ``fs`` at each grid point or spectral coefficient.

   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :rtype: :class:`Fieldset` 

   This function modifies the resulting GRIB header to be of integer data type. Missing values are replaced with LONG_MAX. 
   
   .. note::
      :func:`integer` was used in Metview 3 to enable the plotting of certain types of satellite imagery.


.. mv-minigallery:: integer
