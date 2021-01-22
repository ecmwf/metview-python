second_derivative_x
========================


.. py:function:: second_derivative_x(fs)

   Computes the second zonal (from West to East) partial derivative of each field in ``fs``. 
   
   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :rtype: :class:`Fieldset`

   The computations for a field f are based on the following formula:
   
   .. math::

      \frac {\partial^2 f}{\partial x^2} = \frac{1}{R^2 \ cos^2\phi}\frac{\partial^2 f}{\partial \lambda^2} 

   where:

   * R is the radius of the Earth in m
   * :math:`\phi` is the latitude
   * :math:`\lambda` is the longitude.    

   The derivatives are computed with a second order finite-difference approximation. The resulting fields contain missing values on the poles. 
   
   .. warning::
      :func:`second_derivative_x` is only implemented for regular latitude-longitude grids.


.. mv-minigallery:: second_derivative_x
