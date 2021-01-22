frequencies
=============

.. py:function:: frequencies(fs, bins, [area]) 

   Counts the number of grid points whose values fall within a set of specified ``bins``. 
   
   :param fs: input fieldset
   :type fs: :class:`Fieldset` 
   :param list bins: bins used for the computations
   :param list area: area as [North, West, South, East] used for the computations
   :rtype: list or list of lists

   ``bins`` is a list with numbers in ascending order defining the bins. The first and last bins are unbounded. E.g. if ``bins`` = [0, 10, 20] the following bins are defined:
   
   * first bin: (, 0)
   * second bin: [0, 10),
   * third bin: [10, 20),
   * fourth bin: [20, ),
   
   Missing values in ``fs`` are not included in the results.

   If ``fs`` has just one field the result is a list of n+1 elements where n is the number of elements in ``bins``. If ``fs`` has more than one field the result is a list of lists, one for each field. 
   
   .. warning::
      Note that this function accumulates its results between fields in ``fs``!


.. mv-minigallery:: frequencies
