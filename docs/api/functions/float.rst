float
============

.. py:function:: float(fs, [number_of_bits])

   Returns a :class:`Fieldset` with integer data converted into floating point data for more accurate computations.
   
   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :param number number_of_bits: defines the number of bits used for packing the float values. If not given, the default value of 24 is used (unless :func:`gribsetbits` has been called to set it).  
   :rtype: :class:`Fieldset` 


.. mv-minigallery:: float
