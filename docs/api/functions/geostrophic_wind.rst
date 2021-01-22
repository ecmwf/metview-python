geostrophic_wind
====================

.. py:function::  geostrophic_wind(z)

   Computes the geostrophic wind from geopotential fields defined on pressure levels. 
   
   :param z: input fieldset (geopotential on pressure levels)
   :type fs: :class:`Fieldset` 
   :rtype: :class:`Fieldset`
   
   For a given z geopotential field the computation of the geostrophic wind components is based on the following formulas:
   
   .. math::
   
      u_g = -\frac{1}{f} \frac{1}{R}\frac{\partial z}{\partial \phi}

      v_g = \frac{1}{f} \frac{1}{R \ cos\phi}\frac{\partial z}{\partial \lambda}

   where:
   
   * R is the radius of the Earth
   * :math:`\phi` is the latitude
   * :math:`\lambda` is the longitude.
   * :math:`f=2\Omega sin\phi` is the Coriolis parameter, where :math:`\Omega` is the Earth's angular velocity.

   The derivatives are computed with a second order finite-difference approximation. The resulting fieldset contains two fields for each input field: the u and v geostrophic wind components. In each output field the points close to the poles and the Equator are bitmapped (they contain missing values). 
   
   .. warning::
      :func:`geostrophic_wind` is only implemented for regular latitude-longitude grids.

.. mv-minigallery:: geostrophic_wind
