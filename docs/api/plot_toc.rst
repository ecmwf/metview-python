
Visualisation
===========================



Views
-------------------------------

.. list-table::
    :widths: 20 80
    :header-rows: 0


    * - :func:`annotationview`
      - Creates an annotation view

    * - :func:`cartesianview`
      - Creates a Cartesian view

    * - :func:`geoview`
      - Creates a map view

    * - :func:`maverageview`
      - Creates an average view

    * - :func:`mhovmoellerview`
      - Creates a Hovmoeller diagram view

    * - :func:`mvertprofview`
      - Creates a vertical profile view

    * - :func:`mxsectview`
      - Creates a cross section view

    * - :func:`thermoview`
      - Creates a thermodynamical diagram view


Visual definitions
-------------------------------

.. list-table::
    :widths: 20 80
    :header-rows: 0


    * - :func:`maxis`
      - Defines the axis plotting styles

    * - :func:`mcoast`
      - Defines the map plotting style

    * - :func:`mcont`
      - Defines the contouring style

    * - :func:`mgraph`
      - Defines the graph plotting style

    * - :func:`mlegend`
      - Defines the legend plotting style

    * - :func:`mobs`
      - Defines the BUFR observation plotting style

    * - :func:`msymb`
      - Defines the symbol plotting style

    * - :func:`mtaylor`
      - Defines the Taylor diagram style

    * - :func:`mtext`
      - Defines the title plotting style

    * - :func:`mthermo`
      - Defines the thermodynamical data plotting style

    * - :func:`mthermogrid`
      - Defines the thermodynamical diagram style

    * - :func:`mwind`
      - Defines the wind plotting style


Plotting
-------------------------------

.. list-table::
    :widths: 20 80
    :header-rows: 0


    * - :func:`binning`
      - Defines 1D or 2D binning for scatterplots

    * - :func:`eccharts`
      - Retrieves and plots ecCharts layers

    * - :func:`grib_vectors`
      - Combines GRIB scalar fields into vector data

    * - :func:`input_visualiser`
      - Defines visualisation for ndarray data

    * - :func:`met3d`
      - Visualises GRIB data in Met3D

    * - :func:`meteogram`
      - Generates a meteogram

    * - :func:`mimport`
      - Plots an image at the spcified position in a view

    * - :func:`mvl_geocircle`
      - Returns a curve for a circle/quadrants defined on the surface of the Earth

    * - :func:`mvl_geoline`
      - Returns a curve for a line sampled in lat-lon coordinates

    * - :func:`mvl_geopolyline`
      - Returns a curve with a polyline sampled in lat-lon coordinates

    * - :func:`netcdf_visualiser`
      - Defines visualisation for NetCDF data

    * - :func:`newpage`
      - Forces a new page on PostScript output

    * - :func:`odb_visualiser`
      - Defines visualisation for ODB data

    * - :func:`plot`
      - Generates a plot

    * - :func:`rttov_visualiser`
      - Defines visualisation for RTTOV model output

    * - :func:`scm_visualiser`
      - Defines visualisation for SCM output

    * - :func:`table_visualiser`
      - Defines visualisation for CSV data

    * - :func:`thermo_parcel_area`
      - returns a set of coloured areas from a thermo parcel path

    * - :func:`xs_build_curve`
      - Returns a curve for the given cross section data

    * - :func:`xs_build_orog`
      - Returns an orography area curve for the given cross section data

    * - :func:`xy_area`
      - Returns an xy area plot object with a given colour

    * - :func:`xy_curve`
      - Returns a curve with a given colour, style and thickness


Layout
-------------------------------

.. list-table::
    :widths: 20 80
    :header-rows: 0


    * - :func:`mvl_regular_layout`
      - Generates a regular grid of frames/subframes

    * - :func:`mxn_layout`
      - Generates a regular grid of plot pages

    * - :func:`plot_page`
      - Creates a page in a plot layout

    * - :func:`plot_subpage`
      - Creates a subpage in a plot layout

    * - :func:`plot_superpage`
      - Creates a top level plot layout


Graphical output
-------------------------------

.. list-table::
    :widths: 20 80
    :header-rows: 0


    * - :func:`eps_output`
      - Defines the EPS (Encapsulated PostScript) output format

    * - :func:`epscairo_output`
      - Defines the EPS output format using the Cairo driver

    * - :func:`kml_output`
      - Defines the KML output format

    * - :func:`pdf_output`
      - Defines the PDF output format

    * - :func:`png_output`
      - Defines the PNG output format

    * - :func:`ps_output`
      - Defines the PostScript output format

    * - :func:`pscairo_output`
      - Defines the PostScript output format using the Cairo driver

    * - :func:`svg_output`
      - Defines the SVG output format
