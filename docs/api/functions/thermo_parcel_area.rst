thermo_parcel_area
=======================

.. py:function:: thermo_parcel_area(parcel, [positive_colour, negative_colour])

   Convenience function to build positive and negative buoyancy areas from ``parcel`` to be plotted in a :func:`thermoview`.
   
   :param parcel: object describing the path of an ascending thermodynamic air parcel
   :type parcel: :func:`thermo_parcel_path`
   :param positive_colour: colour of the positive buoyancy areas, the default is "red"
   :type positive_colour: str
   :param negative_colour: colour of the negative buoyancy areas, the default is "blue"
   :type negative_colour: str
   :rtype: list of :func:`input_visualiser` and :func:`mgraph`
   
   Returns a list containing an :func:`input_visualiser` and an :func:`mgraph`, which can be directly used in :func:`plot`.
   

.. mv-minigallery:: thermo_parcel_area