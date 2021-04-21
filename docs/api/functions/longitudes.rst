longitudes
============

.. py:function:: longitudes(fs)

   Returns the longitudes of the grid points on ``fs`` as an ndarray. 
   
   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :rtype: 1D-ndarray or list of 1D-ndarrays

   If ``fs`` contains more than one field a list of ndarrays is returned. Each of these ndarrays contains one value per gridpoint in each field.

.. py:function:: longitudes(gpt)

    Returns the longitudes column of ``gpt`` as an ndarray.
    
    :param gpt: input geopoints
    :type gpt: :class:`Geopoints`
    :rtype: ndarray

.. mv-minigallery:: longitudes
