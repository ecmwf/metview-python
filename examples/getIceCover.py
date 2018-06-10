# ==============================================================================
# Author: ralf mueller, stephan siemen
#
#
# Plan is to create a plot similar to the scatter plot for co2 concentration and
# september minimum of sea ice extend
#
# doc: https://www.mpg.de/10579957/W004_Environment_climate_062-069.pdf
# page 7
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
cdo    = Cdo()
cdo.debug = True
tasks     = 4
startYear = 1980
endYear   = 2014
# }}} ==========================================================================
# helper methods {{{ ===========================================================
def getDataFromTarfile(tarfile):
    tf = TarFile(tarfile)
    members = [ m.name for m in tf.getmembers()]   
    if (list(set([os.path.exists(x) for x in members])) != [True]):
        tf.extractall()
    tf.close
    return members

def computeTimeSeries(file,varname,useCellArea=False):
    if (useCellArea):
        ofile = cdo.mul(input = '-fldmean -selname,%s %s -fldsum -selname,cell_area %s'%(varname,file,file),
                options = '-b F32')
    else:
        ofile = cdo.mul(input = '-fldmean -selname,%s %s -fldsum -gridarea %s'%(varname,file,file),
                options = '-b F32')
    return ofile

def computeTimeSeriesOfFilelist(pool,files,varname,ofile,useCellArea=False):
    results = dict()
    for file in files:
        rfile = pool.apply_async(computeTimeSeries,(file,varname,False))
        results[file] = rfile
    pool.close()
    pool.join()

    for k,v in results.items():
        results[k] = v.get()

    cdo.yearmean(input = '-cat %s'%(' '.join([results[x] for x in files])),
            output = ofile, force=False,
            options = '-f nc')
    return ofile

# }}} ==========================================================================
# data retrival {{{
iceCover_file = "ci_interim_%s-%s-NH.grb"%(startYear, endYear)
iceCover_file = "ci_interim_%s-%s-NH.grb"%(1980, 2014)
if ( not os.path.exists(iceCover_file) ):
    server.retrieve({
        'stream'    : "oper",
        'levtype'   : "sfc",
        'param'     : "31.128",
        'dataset'   : "interim",
        'step'      : "0",
        'grid'      : "0.5/0.5",
        'time'      : "12",
        'date'      : "%s-01-01/to/%s-01-01"%(startYear,endYear),
        'type'      : "an",
        'class'     : "ei",
        'area'      : "90/-180/0/180",
        'target'    : iceCover_file
     })
else:
    print("use existing file '%s'"%(iceCover_file))
# compute the nh ice extent and the other time series
iceExtent = 'ice_extent_%s-%s-daymean-SeptMin.nc'%(startYear,endYear)
cdo.setattribute('sea_ice_extent@unit=m2,sea_ice_extent@standard_name=sea_ice_extent',
         input  = '-setname,sea_ice_extent -yearmin -fldsum -mul -selmon,9 %s -gridarea %s'%(iceCover_file,iceCover_file),
         output = iceExtent,force=False,
         options = '-f nc')
iceExtent_ds = cdo.readXDataset(iceExtent)

# cams return tarballs of netcdf files
co2_tarball = "co2_totalColumn_%s-%s.tar"%(startYear, endYear)
if ( not os.path.exists(co2_tarball) ):
    server.retrieve({ #CO2
        "dataset"   : "cams_ghg_inversions",
        "datatype"  : "ra",
        "date"      : "%s-01-01/to/%s-01-01"%(startYear,endYear),
        "frequency" : "3h",
        "param"     : "co2",
        "quantity"  : "total_column",
#       "quantity"  : "concentration",
        "version"   : "v16r2",
        "target"    : co2_tarball
    })
else:
    print("use existing file '%s'"%(co2_tarball))
co2_files = getDataFromTarfile(co2_tarball)
#co2_results = dict()
#pool   = Pool(4)
#for file in co2_files:
#    ofile = pool.apply_async(computeTimeSeries,(file,'XCO2',False))
#    co2_results[file] = ofile
#pool.close()
#pool.join()
#for k,v in co2_results.items():
#    co2_results[k] = v.get()
co2_timeSeries = 'co2_timeseries_%s-%s.nc'%(startYear,endYear)
#cdo.yearmean(input = '-cat %s'%(' '.join([co2_results[x] for x in co2_files])),
#        output = co2_timeSeries, force=False,
#        options = '-f nc')
computeTimeSeriesOfFilelist(Pool(4),co2_files,'XCO2',co2_timeSeries,False)
co2_ds = cdo.readXDataset(co2_timeSeries)

# }}} ==========================================================================
# scatter plot {{{ =============================================================
iceExtent_ds.info()
co2_ds.info()
plt.scatter( co2_ds.sel(time=slice('%s-01-01'%(startYear), '%s-01-01'%(endYear))).to_array()[1,:,0,0,0],
        iceExtent_ds.sel(time=slice('%s-01-01'%(startYear), '%s-01-01'%(endYear))).to_array()[1,:,0,0,0])
plt.grid(True)
plt.show()
# }}} ==========================================================================
