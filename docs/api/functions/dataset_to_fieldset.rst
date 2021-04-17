dataset_to_fieldset
************************

.. py:function:: dataset_to_fieldset(xds)

   Converts an xarray Dataset to a :class:`Fieldset`.

   :param xds: the xarray Dataset
   :type xds: xarray.Dataset
   :rtype: :class:`Fieldset`

    The conversion is based on the Open Source `cfgrib <https://github.com/ecmwf/cfgrib>`_ package which
    is an xarray backend engine. Note that this uses an experimental feature of cfgrib and will only work for a small subset of xarray datasets.

   :Example:

    .. code-block:: python

        import metview as mv

        grib = mv.read('temperature_on_pl.grib')
        x = grib.to_dataset() # convert from Fieldset to dataset
        f = mv.dataset_to_fieldset(x) # convert back to Fieldset


.. mv-minigallery:: dataset_to_fieldset
