Defines the visualisation for :class:`Odb` data using various plot types. Optionally it can perform an `ODB/SQL <https://confluence.ecmwf.int/display/ODBAPI/SQL>`_ query on the input ODB and visualises the resulting data. It works for both databases (ODB-1) and files (ODB-2 or ODC).

.. tip:: A tutorial about using ODB in Metview can be found `here <https://confluence.ecmwf.int/display/METV/ODB+Tutorial>`_.

**How can ODB/SQL queries be used in odb_visualiser?**

The queries cannot directly be used but have to be mapped for a specific set of arguments. We illustrate it with a simple example. Let us suppose we want to perform this ODB/SQL query on our data:

.. code-block:: sql

    SELECT
        lat@hdr,
        lon@hdr,
        fg_depar@body
    WHERE
        vertco_reference_1@body = 5
    ORDERBY
        obsvalue@body

and want to plot the results as points (symbols) on a map. To achieve this we need to use the following code:

.. code-block:: python

    import metview as mv

    db = mv.read("my_data.odb")

    vis = mv.odb_viusaliser(
        odb_data=db,
        odb_latitude_variable="lat@hdr",
        odb_longitude_variable="lon@hdr",
        odb_value_variable="fg_depar@body",
        odb_where="vertco_reference_1@body = 5",
        odb_orderby="obsvalue@body")
    
    mv.plot(vis)