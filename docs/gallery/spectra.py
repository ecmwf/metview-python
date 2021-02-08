"""
GRIB - Spherical Harmonics Spectrum
"""

# (C) Copyright 2017- ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
#
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
#

import metview as mv

# read grib file - contains only one
# spherical harmonic (spectral) field
filename = "z_for_spectra.grib"
if mv.exist(filename):
    f = mv.read(filename)
else:
    f = mv.gallery.load_dataset(filename)

# generate spectra plot definition
sp = mv.spec_graph(data=f, truncation=106, y_axis_type="logartihmic")

# define the output plot file
mv.setoutput(mv.pdf_output(output_name="spectra"))

# generate the plot
mv.plot(sp)
