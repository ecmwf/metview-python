second_derivative_y
=====================

.. py:function:: second_derivative_y(fs)

   Computes the second meridional (from South to North) partial derivative of each field in ``fs``. 
   
   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :rtype: :class:`Fieldset`
   
   The computations for a field f are based on the following formula:

   .. math::
   
      \frac {\partial^2 f}{\partial y^2} = \frac{1}{R^2}\frac{\partial^2 f}{\partial \phi^2} 

   where:
   
   * R is the radius of the Earth in m
   * :math:`\phi` is the latitude

   The derivatives are computed with a second order finite-difference approximation. The resulting fields contain missing values on the poles. 
   
   .. warning::
      :func:`second_derivative_y` is only implemented for regular latitude-longitude grids.

.. mv-minigallery:: second_derivative_y
