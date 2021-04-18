integrate
=============

.. py:function:: integrate(fs, [area_or_mask])

   Computes the average of each field in ``fs`` over an area. 
   
   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :param area_or_mask: list defining an area as [North, West, South, East] or fieldset defining a mask
   :type area_or_mask: list or :class:`Fieldset`
   :rtype: number or ndarray or None
   
   If ``fs`` contains only one field a number is returned. If there is more than one field a numpy array is returned. Missing values in the input fieldset are bypassed in this calculation. For each field for which there are no valid values None is returned.

   * If ``fs`` is the only argument the integration is done on all grid points.
   * If ``area_or_mask`` is a list it defines an **area** as [North, West, South, East] for the integration:

      .. code-block:: python

         import metview as mv
         europe = [75,-12.5,35,42.5]
         x = mv.integrate(field, europe) 

   * If ``area_or_mask`` is a fieldset it is used as a **mask** and the integration is performed only on the grid points where the mask values are non zero. ``area_or_mask`` should contain either one or as many fields as there are in ``fs``. If it has a single field then the mask is applied to all fields in ``fs``. If it has the same number of fields as ``fs``, then a different mask is applied to each input field. The example below shows how to use :func:`integrate` with a land-sea mask retrieved from MARS:
      
      .. code-block:: python

         import metview as mv
         
         # read grib data on a 1 degree by 1 degree grid
         f = mv.read("my_fs.grib") 

         # retrieve land-sea mask from MARS on the same grid
         lsm = mv.retrieve(
            type="an",
            date=-1,
            param="lsm",
            grid=[1,1],
            levtype="sfc"
         )

         # make sure values are either 0 or 1
         lsm = lsm > 0.5

         # compute the average value on land and on sea
         land = mv.integrate(f, lsm)
         sea = mv.integrate(f, not lsm) 


   .. note::
      The computations are based on the following approximation of the grid cell areas:

      .. math::

         A_{i} = 2 R^{2} cos\phi_{i} sin(\frac{\Delta\phi_{i}}{2}) \Delta\lambda_{i}
   
      where:

      * R is the radius of the Earth
      * :math:`\phi_{i}` is the latitude of the i-th grid cell
      * :math:`\Delta\phi_{i}` is the size of the grid cells in latitude
      * :math:`\Delta\lambda_{i}` is the size of the i-th grid cell in longitude.
   
      :func:`integrate` then supposes that :math:`\Delta\phi_{i}` is constant and the weighted average over the area is computed as:
   
      .. math::

         \frac {\sum_{i}f_{i} A_{i}}{\sum_{i}A_{i}} = \frac {\sum_{i}f_{i}cos\phi_{i}\Delta\lambda_{i}}{\sum_{i}cos\phi_{i}\Delta\lambda_{i}}

   The formula above is only used for reduced or regular **latitude-longitude and Gaussian grids**. For all other grid types :func:`integrate` simply returns the mathematical average of the values (just like :func:`average` does).

   .. warning:: 
   
      Please note that for **Gaussian grids** the formula can only be only regarded as an approximation since :math:`\Delta\phi_{i}` is not constant!

.. mv-minigallery:: integrate