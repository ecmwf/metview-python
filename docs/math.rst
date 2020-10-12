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
