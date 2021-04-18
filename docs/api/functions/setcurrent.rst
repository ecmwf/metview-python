setcurrent
==============

..  py:function::  setcurrent(nc, index_or_name)

    On a multi-variable :class:`NetCDF` sets the specified variable as the current variable. Functions and operators act on the current variable only.

    :param nc: input NetCDF
    :type nc: :class:`NetCDF`
    :param index_or_name: index or name of the NetCDF variable
    :type index_or_name: number or str
    :rtype: None

    A :class:`NetCDF` produced by the Metview applications are uni-variable, so in their case :func:`setcurrent` need not be used. For a multi-variable :class:`NetCDF` :func:`setcurrent` can be usefully combined with :func:`variables` as the example below illustrates it.

    :Example:

        .. code-block:: python

            import metview as mv 

            nc = mv.read("my_data.nc")

            for v in mv.variables(nc):
                mv.setcurrent(nc, v)
                # acts on current variable only
                nc = nc - 273.16


.. mv-minigallery:: setcurrent