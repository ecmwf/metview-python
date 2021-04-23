mask
=========

.. py:function:: mask(fs, area)

   For each field in ``fs`` creates a field containing 0 or 1 values according to whether a grid point is inside (1) or outside (0) the ``area``.

   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :param list area: area as [N, W, S, E]
   :rtype: :class:`Fieldset`
   
   :Example:

      Non-rectangular masks, and even convex masks can be created by using the operators **and**, **or** and **not**. To create the following mask:

      .. image:: /_static/mask_1.png
         :width: 300px

      first decompose it into basic rectangles:

      .. image:: /_static/mask_2.png
         :width: 300px

      then create a mask for each of them and use **and** and **or** to compose the desired mask like this:

      .. code-block:: python
         
         import metview as mv

         # Define basic rectangles
         a = [50,-120,10,-30]
         b = [20,20,50,10]
         c = [50,50,40,100]
         d = [35,-60,-40,100]

         # The field defining the grids
         f = mv.read(path_to_your_grib_file)

         # First compute the union of a,c and d
         m = mv.mask(f,a) or mv.mask(f,d) or mv.mask(f,c)

         # Then remove b
         m = m and not mv.mask(f,b)

   
.. py:function:: mask(gpt, area)

    Creates a :class:`Geopoints` containing values of 0 or 1 according to whether they are inside (1) or outside (0) the ``area``.
    
    :param gpt: input geopoints
    :type gpt: :class:`Geopoints`
    :param list area: area as [N, W, S, E]
    :rtype: :class:`Geopoints`
   
    Points with missing latitudes or longitudes are considered to be outside any area. See the documentation for the fieldset version of this function to see how to compose more complex regions than a simple rectangular area.

.. mv-minigallery:: mask
