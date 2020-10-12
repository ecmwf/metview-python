Mathematical functions
************************

.. py:function:: abs(data)
   
   Returns the absolute value of ``data``.

   :param data: input data
   :type data: :class:`Fieldset`, :class:`Geopoints`, nd-array or number 
   :rtype: same type as ``data``

   Missing values are retained, unaltered by the calculation.

.. py:function:: acos(fs)
   
   Returns the arc cosine of ``data`` in radians.
   
   :param data: input data
   :type data: :class:`Fieldset`, :class:`Geopoints`, nd-array or number
   :rtype: same type as ``data``

   Missing values are retained, unaltered by the calculation.

.. py:function:: asin(fs)
   
   Returns the arc sine of ``data`` in radians.
   
   :param data: input data
   :type data: :class:`Fieldset`, :class:`Geopoints`, nd-array or number
   :rtype: same type as ``data``

   Missing values are retained, unaltered by the calculation.

.. py:function:: atan(fs)
   
   Returns the arc tangent of ``data`` in radians.
   
   :param data: input data
   :type data: :class:`Fieldset`, :class:`Geopoints`, nd-array or number
   :rtype: same type as ``data``

   Missing values are retained, unaltered by the calculation.

.. py:function:: cos(fs)

   Returns the cosine of ``data``.
   
   :param data: input data
   :type data: :class:`Fieldset`, :class:`Geopoints`, nd-array or number
   :rtype: same type as ``data``

   Input values must be in radians. Missing values are retained, unaltered by the calculation.

.. py:function:: div(fs1, fs2):

   Returns a fieldset where values in each grid point are the integer part of the division of ``fs1`` by ``fs2`` (the function is operating field by field).

   :param fs1: first input fieldset
   :type fs1: :class:`Fieldset`
   :param fs2: second input fieldset
   :type fs2: :class:`Fieldset`
   :rtype: :class:`Fieldset` 

   A missing value in either ``fs1`` or ``fs2`` will result in a missing value in the corresponding place in the output fieldset.

.. py:function:: exp(data)
   
   Returns the exponential of ``data``.

   :param data: input data
   :type data: :class:`Fieldset`, :class:`Geopoints`, nd-array or number 
   :rtype: same type as ``data``

   Missing values are retained, unaltered by the calculation.

.. py:function:: int(gpt)

   Returns the integer part of ``data``. 
    
   :param data: input data
   :type data: :class:`Fieldset`, :class:`Geopoints`, nd-array or number 
   :rtype: same type as ``data``

   Missing values are retained, unaltered by the calculation.

.. py:function:: log(data)
   
   Returns the natural logarithm of ``data``.

   :param data: input data
   :type data: :class:`Fieldset`, :class:`Geopoints`, nd-array or number 
   :rtype: same type as ``data``

   Missing values are retained, unaltered by the calculation.

.. py:function:: log10(data)
   
   Returns the log base 10 of ``data``.

   :param data: input data
   :type data: :class:`Fieldset`, :class:`Geopoints`, nd-array or number 
   :rtype: same type as ``data``

   Missing values are retained, unaltered by the calculation.

.. py:function:: mod(data1, data2)

   Computes the remainder of dividing ``data1`` by ``data2``.
   
   :param data1: divident data
   :type data1: :class:`Fieldset` or :class:`NetCDF`
   :param data2: divisor data
   :type data2: :class:`Fieldset` or :class:`NetCDF`
   :rtype: same type as ``data1``
   
   Where the values of ``data2`` are larger than those of ``data1``, the output value is set to the integer part of ``data1``. A missing value in either ``data1`` or ``data2`` will result in a missing value in the corresponding place in the output. Note that only the integer parts of the inputs are considered in the calculation, meaning that a divisor of 0.5 would cause a division by zero.

.. py:function:: neg(fs)

   Returns the negative of ``data``.
   
   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :rtype: :class:`Fieldset`

   Missing values are retained, unaltered by the calculation.

   .. note::
      The following lines of codes are equivalent:

      .. code-block:: python

         import metview as mv
         fs = mv.neg(fs)
         fs = -fs 

.. py:function:: sgn(gpt)
    
   Returns the sign of ``data``:  -1 for negative , 1 for positive and 0 for 0 values.
    
   :param data: input data
   :type data: :class:`Fieldset`, :class:`Geopoints`, nd-array or number 
   :rtype: same type as ``data``

   Missing values are retained, unaltered by the calculation. 

.. py:function:: sin(fs)

   Returns the sine of ``data``.
   
   :param data: input data
   :type data: :class:`Fieldset`, :class:`Geopoints`, nd-array or number
   :rtype: same type as ``data``

   Input values must be in radians. Missing values are retained, unaltered by the calculation.

.. py:function:: sqrt(data)
   
   Returns the square root of ``data``.

   :param data: input data
   :type data: :class:`Fieldset`, :class:`Geopoints`, nd-array or number 
   :rtype: same type as ``data``

   Missing values are retained, unaltered by the calculation.

.. py:function:: tan(fs)

   Returns the tangent of ``data``.
   
   :param data: input data
   :type data: :class:`Fieldset`, :class:`Geopoints`, nd-array or number
   :rtype: same type as ``data``

   Input values must be in radians. Missing values are retained, unaltered by the calculation.
