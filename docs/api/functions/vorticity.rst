vorticity
============

.. py:function:: vorticity(fx, fy)

   Computes the vertical component of the curl differential operator for 2-dimensional vector fields.
   
   :param fx: zonal (west-east) vector component fieldset
   :type fx: :class:`Fieldset`
   :param fy: meridional (south-north) vector component fieldset
   :type fy: :class:`Fieldset`
   :rtype: :class:`Fieldset`  
   
   For wind fields (i.e. when the input fieldsets are u and v wind components) this computes the relative vorticity (:math:`\zeta`). The computations for a vector field f=(fx ,fy ) are based on the following formula:

   .. math::
      
      \zeta =\frac{1}{R \ cos\phi}\frac{\partial f_y}{\partial \lambda} - \frac{1}{R}\frac{\partial f_x}{\partial \phi} + \frac{f_x}{R}tan\phi

   where:
   
   * R is the radius of the Earth (in m)
   * :math:`\phi` is the latitude
   * :math:`\lambda` is the longitude

   The derivatives are computed with a second order finite-difference approximation. The resulting fields contain missing values on the poles. If the input fields are horizontal wind components the ecCodes paramId of the resulting field is set to 138 (relative vorticity).

   .. warning::
      :func:`vorticity` is only implemented for regular latitude-longitude grids. 

.. mv-minigallery:: vorticity
