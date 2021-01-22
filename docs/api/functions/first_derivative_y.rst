first_derivative_y
======================

.. py:function:: first_derivative_y(fs)

   Computes the meridional (from South to North) partial derivative of each field in the fieldset. 
   
   :param fs: input fieldset
   :type fs: :class:`Fieldset` 
   :rtype: :class:`Fieldset`
   
   The computations for a field f are based on the following formula:

   .. math::

      \frac {\partial f}{\partial y} = \frac{1}{R}\frac{\partial f}{\partial \phi} 
   
   where:
   
   * R is the radius of the Earth
   * :math:`\phi` is the latitude
   * :math:`\lambda` is the longitude.

   The derivatives are computed with a second order finite-difference approximation. The resulting fields contain missing values on the poles. 

   .. warning::
      :func:`first_derivative_y` is only implemented for regular latitude-longitude grids.


.. mv-minigallery:: first_derivative_y
