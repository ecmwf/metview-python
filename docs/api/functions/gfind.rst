gfind
=========

.. py:function:: gfind(fs, value, [eps])

   Returns a :class:`Geopoints` holding the grid points whose value is equal to ``value`` in the first field of ``fs``. 
   
   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :param number value: the value to match
   :param number eps: when specified data values are selected when :math:`abs(data - value) < eps`
   :rtype: :class:`Geopoints`  
  
   Missing values in ``fs`` are not returned.

.. mv-minigallery:: gfind
