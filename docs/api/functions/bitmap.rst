bitmap
========

.. py:function:: bitmap(fs, value)
.. py:function:: bitmap(fs, field)
   :noindex:

   Returns a copy of ``fs`` with none or more of its values replaced with the GRIB missing value indicator. 
   
   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :param value: bitmap value
   :type value: number
   :param field: bitmap fieldset
   :type field: :class:`Fieldset`
   :rtype: :class:`Fieldset`
   
   The behaviour of :func:`bitmap` depends on the arguments:

   * if ``value`` is specified, any value in ``fs`` being equal to it is replaced with the missing value indicator. 
   * if ``field`` is specified with the same number of fields as ``fs``, the result takes the arrangement of missing values from ``field``. 
   * if ``field`` contains only one field, the arrangement of missing values from that field are copied into all fields of the output fieldset. 
   
   See also :func:`nobitmap`.


.. mv-minigallery:: bitmap
