set_values
=============

.. py:function:: set_values(fs, values, [mode])

   Creates a new fieldset with all the values in ``fs`` replaced by ``values``.

   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :param values: values to be written into ``fs``
   :type values: ndarray or list of ndarray
   :param str mode: resize mode. If specified must be set to "resize".
   :rtype: :class:`Fieldset`

   If ``values`` is an ndarray the same values are set in each field of ``fs``.

   If ``values`` is a list of ndarray the list size must be same as the number of fields in ``fs``. 
   
   The default behaviour is to produce an **error** if the number points in a field and the given ndarray are not the same. If, however, ``mode`` is specified and set to "resize" the resulting fieldset will be resized to have the same number of values as the ndarray. This can be a useful option when creating a new :class:`Fieldset` from a template. 
   
   Missing values in the ``values`` are retained as missing values in the fieldset.



..  py:function:: set_values(gpt, values)
..  py:function:: set_values(gpt, index_or_name, values)
    :noindex:

    Creates a new :class:`Geopoints` with the specified values column in ``gpt`` replaced by ``values``.

    :param gpt: input geopoints
    :type gpt: :class:`Geopoints`
    :param index_or_name: index or name of the values column to be replaced in ``gpt``
    :type index_or_name: number or str
    :param values: values to be written into ``gpt``
    :type values: number or list or ndarray
    :rtype: :class:`Geopoints`

    If ``index_or_name`` is specified and is a number it refers to the index of the column within the value columns (and not within all the columns in ``gpt``). E.g. 0 means the first value column. 
     
    ``index_or_name`` has to be used for :class:`Geopoints` of 'ncols' type. In all the other types the values column is uniquely identified.

    If ``values`` is a number all the values are replaced with it. If ``values`` is a list or ndarray and is shorter than the geopoints count then only the first values that have a corresponding value in ``values`` are changed.

    :Example:

        .. code-block:: python

            import metview as mv
             
            new_gpt_b = set_values(gpt_b, 
                        np.array([12.4, 13.3, 1.1]))

            # update the 4th value column
            new_gpt_c = set_values(gpt_c, 3, 
                        np.array([3.3, 4.4, 5.5]))
            
            # update the column labelled "precip" 
            new_gpt_d = set_values(gpt_d, "precip", 
                        np.array([0.3, 0.2, 0.1]))

    .. note::
        :func:`set_values` generates a new geopoints object, leaving the original one intact. If you wish to modify the original object, then a more efficient way is to directly access the columns using the following syntax, following the examples above:

        .. code-block:: python
            
            gpt['value'] = np.array([2.4, 13.3, 1.1])
            gpt[name_of_column_4] = np.array([3.3, 4.4, 5.5])
            gpt["precip"] = np.array([0.3, 0.2, 0.1])


.. mv-minigallery:: set_values
