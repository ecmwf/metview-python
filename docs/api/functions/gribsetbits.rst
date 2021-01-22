gribsetbits
=================

.. py:function:: gribsetbits(number_of_bits)

   Sets the number of GRIB packing bits to ``number_of_bits`` (e.g. 8, 10, 16), and returns the previously used internal value. 

   :param int number_of_bits: number of bits
   :rtype: float 

   This function is particularly useful when dealing with 10-bit satellite images as these require GRIB packing to be set to 10 bits.

.. mv-minigallery:: gribsetbits
