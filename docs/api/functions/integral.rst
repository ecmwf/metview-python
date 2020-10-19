integral
============

.. py:function:: integral(fs)

   Computes the surface integral of each field in ``fs``. 
   
   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :rtype: float or ndarray

   The result is either a **number** (for one input field) or an **ndarray** (for multiple input fields). The computations are based on the cell area (in m\ :super:`2` units) returned by :func:`grid_cell_area`.
