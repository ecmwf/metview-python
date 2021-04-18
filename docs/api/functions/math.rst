Mathematical functions
************************

.. py:function:: abs(data)
   
   Returns the absolute value of ``data``.

   :param data: input data
   :type data: :class:`Fieldset`, :class:`Geopoints`, :class:`NetCDF`, nd-array or number 
   :rtype: same type as ``data``

   Missing values are retained, unaltered by the calculation.

.. py:function:: acos(data)
   
   Returns the arc cosine of ``data`` in radians.
   
   :param data: input data
   :type data: :class:`Fieldset`, :class:`Geopoints`, :class:`NetCDF`, nd-array or number
   :rtype: same type as ``data``

   Missing values are retained, unaltered by the calculation.

.. py:function:: asin(data)
   
   Returns the arc sine of ``data`` in radians.
   
   :param data: input data
   :type data: :class:`Fieldset`, :class:`Geopoints`, :class:`NetCDF`, nd-array or number
   :rtype: same type as ``data``

   Missing values are retained, unaltered by the calculation.

.. py:function:: atan(data)
   
   Returns the arc tangent of ``data`` in radians.
   
   :param data: input data
   :type data: :class:`Fieldset`, :class:`Geopoints`, :class:`NetCDF`, nd-array or number
   :rtype: same type as ``data``

   Missing values are retained, unaltered by the calculation.

.. py:function:: atan2(data_y, data_x)
   
   Returns the arc tangent of ``data_y``/``data_x`` in radians.
   
   :param data_x: input 
   :type data_x: :class:`Fieldset`
   :param data_y: input 
   :type data_y: :class:`Fieldset`
   :rtype: :class:`Fieldset`

   Missing values are retained, unaltered by the calculation.

.. py:function:: cos(data)

   Returns the cosine of ``data``.
   
   :param data: input data
   :type data: :class:`Fieldset`, :class:`Geopoints`, :class:`NetCDF`, nd-array or number
   :rtype: same type as ``data``

   Input values must be in radians. Missing values are retained, unaltered by the calculation.

.. py:function:: exp(data)
   
   Returns the exponential of ``data``.

   :param data: input data
   :type data: :class:`Fieldset`, :class:`Geopoints`, :class:`NetCDF`, nd-array or number 
   :rtype: same type as ``data``

   Missing values are retained, unaltered by the calculation.


.. py:function:: div(data_1, data_2)

   Returns the integer part of the dividing ``data_1`` by ``data_2``.

   :param data_1: dividend data
   :type data_1:  :class:`Fieldset`, :class:`Geopoints`, :class:`NetCDF`, nd-array or number
   :param data_2: divisor data
   :type data_2: :class:`Fieldset`, :class:`Geopoints`, :class:`NetCDF`, nd-array or number
   :rtype: same type as ``data_1``

   A missing value in either ``data_1`` or ``data_2`` will result in a missing value in the corresponding place in the output.

.. py:function:: int(data)

   Returns the integer part of ``data``. 
    
   :param data: input data
   :type data: :class:`Fieldset`, :class:`Geopoints`, :class:`NetCDF`, nd-array or number 
   :rtype: same type as ``data``

   Missing values are retained, unaltered by the calculation.


.. py:function:: intbits(data, bit, [number_of_bits])

    Takes the numbereger part of the values of ``data`` and extracts a specified ``bit`` (or bits).

    :param data: input data
    :type data: :class:`Geopoints` or int
    :param number bit: the bit to extract (1 is the least significant bit!)
    :param number number_of_bits: the number of bits to extract (starting at ``bit``)
    :rtype: :class:`Geopoints` or number

    If only ``bit`` is specified it will always be returned as 1 or 0, regardless of its position in the integer.
    
    With ``number_of_bits`` a group of bits can be extracted. The result will be treated as if the first bit was the least significant bit of the result. 
    
    :Example:
    
        These examples show how intbits work on individual numbers:

        .. code-block:: python

            import metview as mv

            # To extract the 1st, 2nd and 3rd bits from
            # an int separately:
            
            # in bit-form, this is 00000110 with the least significant
            # bit at the right
            n = 6 

            flag = mv.intbits (n, 1) # flag is now 0
            flag = mv.intbits (n, 2) # flag is now 1
            flag = mv.intbits (n, 3) # flag is now 1

            # To extract the 1st and 2nd bits together 
            # to make a single int:
            flag = mv.intbits (n, 1, 2) # flag is now 2

            # To extract the 2nd and 3rd bits together 
            # to make a single int:
            flag = mv.intbits (n, 2, 2) # flag is now 3

            # To extract the 3rd and 4th bits together 
            # to make a single int:
            flag = mv.intbits (n, 3, 2) # flag is now 1

    The number of bits available depends on the machine architecture and Metview's compilation options, but at the time of writing it should be 32. This function does not treat missing values differently from any other values (for efficiency with large datasets).

.. py:function:: log(data)
   
   Returns the natural logarithm of ``data``.

   :param data: input data
   :type data: :class:`Fieldset`, :class:`Geopoints`, :class:`NetCDF`, nd-array or number 
   :rtype: same type as ``data``

   Missing values are retained, unaltered by the calculation.

.. py:function:: log10(data)
   
   Returns the log base 10 of ``data``.

   :param data: input data
   :type data: :class:`Fieldset`, :class:`Geopoints`, :class:`NetCDF`, nd-array or number 
   :rtype: same type as ``data``

   Missing values are retained, unaltered by the calculation.


.. py:function:: mod(data_1, data_2)

   Returns the integer remainder of dividing ``data_1`` by ``data_2``.
   
   :param data_1: divident data
   :type data_1: :class:`Fieldset`, :class:`Geopoints`, :class:`NetCDF`, nd-array or number 
   :param data_2: divisor data
   :type data_2: :class:`Fieldset`, :class:`Geopoints`, :class:`NetCDF`, nd-array or number
   :rtype: same type as ``data_1``
   
   Where the values of ``data_2`` are larger than those of ``data_1``, the output value is set to the integer part of ``data_1``. A missing value in either ``data_1`` or ``data_2`` will result in a missing value in the corresponding place in the output. Note that only the integer parts of the inputs are considered in the calculation, meaning that a divisor of 0.5 would cause a division by zero.

.. py:function:: neg(data)

   Returns the negative of ``data``.
   
   :param data: input fieldset
   :type data: :class:`Fieldset`
   :rtype: :class:`Fieldset`

   Missing values are retained, unaltered by the calculation.

   .. note::
      The following lines of codes are equivalent:

      .. code-block:: python

         import metview as mv
         fs = mv.neg(fs)
         fs = -fs 

.. py:function:: sgn(data)
    
   Returns the sign of ``data``:  -1 for negative , 1 for positive and 0 for 0 values.
    
   :param data: input data
   :type data: :class:`Fieldset`, :class:`Geopoints`, :class:`NetCDF`, nd-array or number 
   :rtype: same type as ``data``

   Missing values are retained, unaltered by the calculation. 

.. py:function:: sin(data)

   Returns the sine of ``data``.
   
   :param data: input data
   :type data: :class:`Fieldset`, :class:`Geopoints`, :class:`NetCDF`, nd-array or number
   :rtype: same type as ``data``

   Input values must be in radians. Missing values are retained, unaltered by the calculation.

.. py:function:: sqrt(data)
   
   Returns the square root of ``data``.

   :param data: input data
   :type data: :class:`Fieldset`, :class:`Geopoints`, :class:`NetCDF`, nd-array or number 
   :rtype: same type as ``data``

   Missing values are retained, unaltered by the calculation.

.. py:function:: tan(data)

   Returns the tangent of ``data``.
   
   :param data: input data
   :type data: :class:`Fieldset`, :class:`Geopoints`, :class:`NetCDF`, nd-array or number
   :rtype: same type as ``data``

   Input values must be in radians. Missing values are retained, unaltered by the calculation.


.. mv-minigallery:: abs
.. mv-minigallery:: sqrt

