grib_get
===========

.. py:function:: grib_get(fs, keys, [grouping])

   Extracts the values of a set of ecCodes keys from the GRIB headers of ``fs`` in an efficient way. 
   
   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :param list keys: the ecCodes keys
   :param str grouping: grouping mode ("field" or "key")
   :rtype: list of lists
 
   A single call to :func:`grib_get` can replace multiple calls to the other grib_get_* functions and is hence more efficient. 

   By default the keys will be retrieved as str, but their type can be specified by adding a modifier to their names, following the convention used by the ecCodes command line tool *grib_ls* where the key name is followed by a colon and then one or two characters which specify the type:
   
   * s=string
   * l=long
   * d=double
   * la=long array
   * da=double array. 
   
   For example, the key 'centre' can be retrieved as a str with 'centre' or 'centre:s', or as a number with 'centre:l'. 
   
   The result is always a list of lists:
   
   * if ``grouping`` is not specified or set to 'field', the result will be grouped by field, containing one list per field, each of these lists containing one element per key
   * if ``grouping`` is 'key', the result will be grouped by key, containing one list per key, each of these lists containing one element per field. 
   
   :Example:
   
      The following lines of code on a particular fieldset with 3 fields:
      
      .. code-block:: python

         print(mv.grib_get(f, 
               ['editionNumber', 'centre', 'level', 'step'], 'field'))
         print(mv.grib_get(f, 
               ['editionNumber', 'centre:l', 'level', 'step'], 'key'))

      produces this output:
      
      .. code-block:: python

         [['1', 'ecmf', '1000', '0'], ['1', 'ecmf', '925', '0'], ['1', 'ecmf', '850', '0']]
         [['1', '1', '1'], [98.0, 98.0, 98.0], ['1000', '925', '850'], ['0', '0', '0']]


.. py:function:: grib_get_long(fs, key)
.. py:function:: grib_get_double(fs, key)
.. py:function:: grib_get_string(fs, key)
.. py:function:: grib_get_long_array(fs, key)
.. py:function:: grib_get_double_array(fs, key)
.. py:function:: grib_get_string_array(fs, key)

   Extracts the value of an ecCode key from the GRIB headers of ``fs``. 
   
   :param fs: input fieldset
   :type fs: :class:`Fieldset`
   :param string key: the ecCodes key
   :rtype: number, str or list

   This group of functions is based on the similarly named ecCodes C API functions. The available ecCodes keys can be inspected in various ways:

   * in an interactive Metview session with the GRIB Examiner (right-click Examine or double-click on a GRIB icon)
   * with the ecCodes command line tool *grib_dump* 
   
   Fot further details about keys read `GRIB Keys - ecCodes GRIB FAQ 
   <https://confluence.ecmwf.int/display/UDOC/GRIB+Keys+-+ecCodes+GRIB+FAQ>`_.
   
   :func:`grib_get_long`, :func:`grib_get_double` and :func:`grib_get_string` return a value if ``fs`` has a single field, otherwise they return a list. 
   
   :func:`grib_get_long_array` and :func:`grib_get_double_array` return a 1d-ndarray if ``fs`` has a single field, otherwise they return a list 1d-ndarrays.
   
   :func:`grib_get_string` returns a list of strings if ``fs`` has a single field, otherwise it returns a list lists.

   .. note::
      :func:`grib_get_long` and :func:`grib_get_long_array` extract a C long value internally but it is cast into float on return.

   :Example:

      This code:

      .. code-block:: python

         import metview as mv
         print(mv.grib_get_long(data, "editionNumber"))
         print(mv.grib_get_long(data, "max"))
         print(mv.grib_get_double(data, "max"))
         print(mv.grib_get_string(data, "max"))
         print(mv.grib_get_string(data, "typeOfGrid"))

      can result in the following output for single-field GRIB file:

      .. code-block:: python

         1
         317
         317.278808594
         317.279
         regular_ll

   :Example:

      This code shows how to obtain the list of latitudes from a reduced Gaussian grid fieldset:

      .. code-block:: python
         
         import metview as mv
         g = mv.read('your_data_in_gg.grb')
         pl = mv.grib_get_long_array (g, 'pl')
         print(len(pl))
         print(pl)


.. mv-minigallery:: grib_get

.. mv-minigallery:: grib_get_double

.. mv-minigallery:: grib_get_long