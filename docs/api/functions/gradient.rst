gradient
===========

.. py:function:: gradient(fs)

   Computes the horizontal gradient of each field in a :class:`Fieldset`. 
   
   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :rtype: :class:`Fieldset`  
   
   The derivatives are computed with a second order finite-difference approximation. The resulting fieldset contains two fields for each input field: the zonal derivative followed by the meridional derivative. The output fields contain missing values at the poles.

   The computations for a field f are based on the following formula:

      .. math::

         \nabla f = (\frac {\partial f}{\partial x}, \frac {\partial f}{\partial y}) = (\frac{1}{R \ cos\phi}\frac{\partial f}{\partial \lambda}, \frac{1}{R}\frac{\partial f}{\partial \phi} )
   
   where:

   * R is the radius of the Earth (in m)
   * :math:`\phi` is the latitude
   * :math:`\lambda` is the longitude.

   .. warning::
      :func:`gradient` is only implemented for regular latitude-longitude grids.


.. mv-minigallery:: gradient
