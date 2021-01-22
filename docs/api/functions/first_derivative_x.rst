first_derivative_x
====================

.. py:function:: first_derivative_x(fs)
   
   Computes the zonal (from West to East) partial derivative of each field in ``fs``. 
   
   :param fs: input fieldset
   :type fs: :class:`Fieldset` 
   :rtype: :class:`Fieldset`
   
   The computations for a field f are based on the following formula:

   .. math::

      \frac {\partial f}{\partial x} = \frac{1}{R \ cos\phi}\frac{\partial f}{\partial \lambda} 

   where:
   
   * R is the radius of the Earth
   * :math:`\phi` is the latitude
   * :math:`\lambda` is the longitude.

   The derivatives are computed with a second order finite-difference approximation. The resulting fields contain missing values on the poles. 
   
   .. warning::
      :func:`first_derivative_x` is only implemented for regular latitude-longitude grids.



.. mv-minigallery:: first_derivative_x
