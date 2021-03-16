BUFR object
******************

.. py:class:: Bufr

   Metview's Fieldset object represents BUFR data. As this format is very complicated to work with,
   its only method is :py:meth:`write`.

   Some Bufr objects can also be plotted directly if they conform to certain standards.

   Bufr objects can also be passed to the :py:meth:`thermo_bufr` function in order to compute
   a thermodynamic diagram.

   To work directly with the values of BUFR data in Metview, you must filter it using one of Metview's filters.

   See the complete list of BUFR functions here.