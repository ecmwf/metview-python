
import xarray as xr

from . import metview


class Fieldset:
    def __init__(self, path: str):
        self.grib_handle =  metview.read(path)

    def to_dataset(self):
        # create a dataset from a self.grib_handle
        return xr.Dataset()
