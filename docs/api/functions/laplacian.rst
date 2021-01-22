laplacian
******************

.. py:function:: laplacian(fs)

   Computes the Laplacian of each field in ``fs``. 
   
   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :rtype: :class:`Fieldset`
   
   The computations for a field f are based on the following formula:

   .. math::
 
      \triangle f =\frac{1}{R^2 \ cos^2\phi}\frac{\partial^2 f}{\partial \lambda^2} + \frac{1}{R^2}\frac{\partial^2 f}{\partial \phi^2} - \frac{1}{R^2}tan\phi\frac{\partial f}{\partial \phi}

   where:

      * R: radius of the Earth
      * :math:`\phi`: latitude
      * :math:`\lambda`: longitude.

   The derivatives are computed with a second order finite-difference approximation. The resulting fields contain missing values on the poles. 

   .. warning::
      :func:`laplacian` is only implemented for regular latitude-longitude grids.

.. mv-minigallery:: laplacian
