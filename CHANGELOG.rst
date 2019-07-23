
Changelog for Metview's Python interface
========================================

1.3.0 (2019-??-??)
------------------

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
