# ==============================================================================
# Authors: ralf mueller, stephan siemen
#
#
# Plan is to create a plot similar to the scatter plot for co2 concentration and
# september minimum of sea ice extent
#
# reference:
#   https://www.mpg.de/10579957/W004_Environment_climate_062-069.pdf, p. 7
#
# ==============================================================================
import os
from ecmwfapi import ECMWFDataServer
from cdo import Cdo
from multiprocessing import Pool
from tarfile import TarFile
import matplotlib.pyplot as plt
import matplotlib.transforms as mtrans

# basic setup    {{{ ===========================================================
server = ECMWFDataServer()
cdo = Cdo()
cdo.debug = True
tasks = 4
startYear = 1980
endYear = 2014
# }}} ==========================================================================
# helper methods {{{ ===========================================================
def getDataFromTarfile(tarfile):
    tf = TarFile(tarfile)
    members = [m.name for m in tf.getmembers()]
    if list(set([os.path.exists(x) for x in members])) != [True]:
        tf.extractall()
    tf.close
    return members


def computeTimeSeries(file, varname, useCellArea=False):
    if useCellArea:
        ofile = cdo.mul(
            input="-fldmean -selname,%s %s -fldsum -gridarea %s"
            % (varname, file, file),
            options="-b F32",
            output="_" + os.path.basename(file),
            force=False,
        )
    else:
        ofile = cdo.fldmean(
            input="-selname,%s %s" % (varname, file),
            options="-b F32",
            output="_" + os.path.basename(file),
            force=False,
        )
    return ofile


def computeTimeSeriesOfFilelist(pool, files, varname, ofile, useCellArea=False):
    results = dict()
    for file in files:
        rfile = pool.apply_async(computeTimeSeries, (file, varname, False))
        results[file] = rfile
    pool.close()
    pool.join()

    for k, v in results.items():
        results[k] = v.get()

    cdo.yearmean(
        input="-cat %s" % (" ".join([results[x] for x in files])),
        output=ofile,
        force=False,
        options="-f nc",
    )
    return ofile


# }}} ==========================================================================
# Sea Ice Cover retrival + processing {{{
iceCover_file = "ci_interim_%s-%s-NH.grb" % (startYear, endYear)
if not os.path.exists(iceCover_file):
    server.retrieve(
        {
            "stream": "oper",
            "levtype": "sfc",
            "param": "31.128",
            "dataset": "interim",
            "step": "0",
            "grid": "0.5/0.5",
            "time": "12",
            "date": "%s-01-01/to/%s-01-01" % (startYear, endYear),
            "type": "an",
            "class": "ei",
            "area": "90/-180/0/180",
            "target": iceCover_file,
        }
    )
else:
    print("use existing file '%s'" % (iceCover_file))
# compute the nh ice extent: minimum usually happens in September
iceExtent = "ice_extent_%s-%s-daymean-SeptMin.nc" % (startYear, endYear)
cdo.setattribute(
    "sea_ice_extent@unit=m2,sea_ice_extent@standard_name=sea_ice_extent",
    input="-setname,sea_ice_extent -yearmin -fldsum -mul -selmon,9 %s -gridarea %s"
    % (iceCover_file, iceCover_file),
    output=iceExtent,
    force=False,
    options="-f nc",
)
iceExtent_ds = cdo.readXDataset(iceExtent)
# }}} ==========================================================================
# {{{ CO2 retrieval + processing ===========================================================
# cams return tarballs of netcdf files
co2_tarball = "co2_totalColumn_%s-%s.tar" % (startYear, endYear)
if not os.path.exists(co2_tarball):
    server.retrieve(
        {  # CO2
            "dataset": "cams_ghg_inversions",
            "datatype": "ra",
            "date": "%s-01-01/to/%s-01-01" % (startYear, endYear),
            "frequency": "3h",
            "param": "co2",
            "quantity": "total_column",
            "version": "v16r2",
            "target": co2_tarball,
        }
    )
else:
    print("use existing file '%s'" % (co2_tarball))
co2_files = getDataFromTarfile(co2_tarball)
co2_timeSeries = "co2_timeseries_%s-%s.nc" % (startYear, endYear)
computeTimeSeriesOfFilelist(Pool(tasks), co2_files, "XCO2", co2_timeSeries, False)
co2_ds = cdo.readXDataset(co2_timeSeries)

# }}} ==========================================================================
# scatter plot {{{ =============================================================
# some debugging output
iceExtent_ds.info()
co2_ds.info()
# shaping the data for plotting it
xSelection = co2_ds.sel(time=slice("%s-01-01" % (startYear), "%s-01-01" % (endYear)))
ySelection = iceExtent_ds.sel(
    time=slice("%s-01-01" % (startYear), "%s-01-01" % (endYear))
)
# create the final scatter plot
fig = plt.figure(figsize=(10, 7))
ax = plt.subplot(1, 1, 1)
trans_offset = mtrans.offset_copy(
    ax.transData, fig=fig, x=0.05, y=-0.20, units="inches"
)  # inches because we are in UK

x = xSelection.to_array()[1, :, 0, 0, 0]
y = ySelection.to_array()[1, :, 0, 0, 0]
plt.scatter(x, y)
# put years as labels
years = xSelection.time.dt.year
for _x, _y, _year in zip(x, y, years):
    plt.text(_x, _y, "%d" % (_year), transform=trans_offset)

plt.grid(True)
plt.ylabel("sea ice extent [m2]")
plt.xlabel("co2 concentration [ppm]")
plt.title("Correlation of NH Sea Ice extent minimum and CO2 emissions")
plt.savefig("seaIce_CO2_correlation.png")
# }}} ==========================================================================
# vim:fdm=marker
