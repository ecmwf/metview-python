grib_cell_area
=================

.. py:function:: grid_cell_area(fs)

   Computes the area of each grid cell in ``fs`` with the grid points supposed to be at the centre of the grid cells. 
   
   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :rtype: :class:`Fieldset` 

   The grid cell area is returned in m\ :sup:`2` units. This function only works for regular latitude-longitude grids and Gaussian grids.

.. mv-minigallery:: grid_cell_area
