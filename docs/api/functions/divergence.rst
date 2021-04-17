divergence
==============

.. py:function:: divergence(fx, fy)

   Computes the horizontal divergence of 2-dimensional vector fields. 
   
   :param fx: zonal (west-east) vector component fieldset
   :type fx: :class:`Fieldset`
   :param fy: meridional (south-north) vector component fieldset
   :type fy: :class:`Fieldset`
   :rtype: :class:`Fieldset`  
   
   The computations for a vector field f=(fx , fy) are based on the following formula:

   .. math:: 
      
      div(f) = \frac{1}{R \ cos\phi}\frac{\partial f_x}{\partial \lambda} + \frac{1}{R}\frac{\partial f_y}{\partial \phi} - \frac{f_y}{R}tan\phi

   where:
   
   * R is the radius of the Earth (in m)
   * :math:`\phi` is the latitude
   * :math:`\lambda` is the longitude.

   The derivatives are computed with a second order finite-difference approximation. The resulting fields contain missing values on the poles. If ``fx`` and ``fy`` are horizontal wind components the ecCodes **paramId** of the resulting field is set to 155 (=divergence). 
   
   .. warning::
      :func:`divergence` is only implemented for regular latitude-longitude grids.



.. mv-minigallery:: divergence
