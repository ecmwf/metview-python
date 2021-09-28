
Changelog for Metview's Python interface
========================================

1.8.1
------------------
- fixed case where map_area_gallery() crashed
- fixed case where map_style_gallery() crashed
- fixed issue where plot_maps() could not plot wind data
- fixed issue where a style could not be updated when verb argument is specified


1.8.0
------------------
- new functions/methods on Fieldset to give an overview of contents:
  - fs.describe()
  - fs.describe("tp")
  - fs.ls()
  - see Jupyter notebook example at https://metview.readthedocs.io/en/latest/notebook_gallery.html
- new GRIB filtering function, select(), offers different filtering options from read() and is faster
  - see Jupyter notebook example at https://metview.readthedocs.io/en/latest/notebook_gallery.html
- new shorthand way to select parameters from Fieldsets, e.g.
  - g = fs["t"]
  - g = fs["t500"]
  - g = fs["t500hPa"]
- the Fieldset constructor can now take a list of paths to GRIB files or a wildcard:
  - e.g. a = mv.Fieldset(path=["/path1/to/data1.grib", "relpath/data2.grib"])
  - e.g. a = mv.Fieldset(path="data/*.grib")
- the result of a call to mcont() etc can now be modified, e.g.
  - c = mv.mcont() ; c["contour_line_colour"] = "green" ; mv.plot(data, c)
  - gv.update({"MAP_COASTLINE_land_SHADE_COLOUR": "green"}, sub="COASTlines")
- improved the output of print(Fieldset):
  - "Fieldset (6 fields)"


1.7.2
------------------
- new argument to setoutput(plot_widget=) - default True, set False to allow images to be saved into the notebook
- multi-page plots in Jupyter notebooks now contain the animation controls by default


1.7.1
------------------
- added automatic play and speed controls to animated plots in Jupyter notebooks


1.7.0
------------------
- added animate=True argument to plot() command for animated plots in Jupyter notebooks
- allowed cfgrib backend keyword arguments to be passed to Fieldset.to_dataset()
- Fieldset out-of-range indexing now raises an IndexError
- Fieldset merge() function now allows a single Fieldset as argument


1.6.1
------------------
- renamed function download_gallery_data() to metview.gallery.load_dataset()


1.6.0
------------------
- added new function download_gallery_data() to download Gallery example data files
- added write(filename) method for classes Fieldset, Geopoints, GeopointSet, Bufr and NetCDF
- added ability to construct a Fieldset from a list of Fieldsets: Fieldset([f1, f2, f3])
- added metzoom function (for the future)
- added keyword arguments to setoutput('jupyter') to control output size in notebooks
- added metview_python member to result of version_info() function


1.5.1
------------------
- temporarily removed tests that involve writing xarrays as GRIB 


1.5.0
------------------
- added support for int numpy arrays as input to functions and methods
- added support for bitwise and (&), or (|) and not (~) operators on Fieldsets
- added div() function (already available via the '/' operator)
- added mod() function
- improved timeout message by mentioning how to increase the timeout
- fixed error when updating an  mv.Request object


(No version update)
-------------------
- added new Jupyter notebook for data analysis
- added new Jupyter notebook for computing and plotting ensemble data
- fixed issue where Metview Request objects did not respect the input data type

1.4.2
------------------
- fixed issue when using a numpy array to index a Fieldset

1.4.1
------------------
- added travis ci and coveralls support
- added automatic upload to PyPi

1.4.0
------------------
- allow a geopoints column name to be used as index when assigning data to a column
- allow -, + and abs operators to work on Metview classes (e.g. a = -my_fieldset)
- added support for Metview's file object
- fixed issue where negative indexing did not work on a Fieldset
- fixed issue where concurrent iterators on a Fieldset did not work
- added experimental support for pickling Fieldsets
- automatically obtain list of Macro-based functions
- allow example notebooks to run in Binder

1.3.4 (2020-02-02)
------------------
- fixed issue when passing sliced numpy arrays to Metview
- added environment.yaml for running in Binder
- fixed issue when running example notebooks in Binder


1.3.3 (2020-01-13)
------------------
- fixed memory leak in Fieldset.append() method


1.3.2 (2019-12-06)
------------------
- added support for reflected operators on Fieldsets, e.g. "2 * Fieldset"
  - done for addition, subtraction, multiplication, division and power


1.3.1 (2019-10-11)
------------------
- added ml_to_hl() function


1.3.0 (2019-09-26)
------------------

- export the Request class
- fixed memory leak when returning a list of items
- allow bool-typed numpy arrays as input
- fixed issue where the Fieldset iterator could fail if used multiple times


1.2.0 (2019-07-11)
------------------

- Metview startup timeout configurable via environment variable METVIEW_PYTHON_START_TIMEOUT (in seconds)
- Metview startup timeout default set to 8 seconds in case of busy systems
- added integral() function
- fixed memory leak when exporting vectors as numpy arrays


1.1.0 (2019-03-04)
------------------

- added equality (``==``) and non-equality (``!=``) operators for Fieldset and Geopoints objects, e.g. ``same = (a == b)`` will produce a new Fieldset with 1s where the values are the same, and 0s elsewhere.
- added new thermodynamic, gradient and utility functions: 'thermo_data_info', 'thermo_parcel_path', 'thermo_parcel_area', 'xy_curve', 'potential_temperature', 'temperature_from_potential_temperature', 'saturation_mixing_ratio', 'mixing_ratio', 'vapour_pressure', 'saturation_vapour_pressure', 'lifted_condensation_level', 'divergence', 'vorticity', 'laplacian', 'geostrophic_wind_pl', 'geostrophic_wind_ml'
- improved conversion from geopoints to pandas dataframe to cope with new NCOLS subformat
- make conversion from Fieldset to xarray dataset compatible with latest versions of cfgrib


1.0.0 (2018-12-20)
------------------

- code cleanup so that tox and pyflakes pass the tests


0.9.1 (2018-11-24)
------------------

- fixed issue where creating ``Fieldset`` slices of more than 10 fields or so did not work
- allow the creation of a ``Fieldset`` object, either empty ``Fieldsest()`` or with a path to GRIB ``Fieldset('/path/to/grib')``
- added ``append()`` method to a ``Fieldset`` to append ``Fieldset``s to ``Fieldset``s
- the ``dataset_to_fieldset`` function that converts an xarray dataset to a Metview ``Fieldset`` now accepts the ``no_warn=True`` argument to suppress warnings while the xarray GRIB writer is pre-beta
- ignore errors on exit from a data examiner
- added more example Jupyter notebooks


0.9.0 (2018-10-29)
------------------

- Beta release.
