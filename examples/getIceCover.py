import os
from ecmwfapi import ECMWFDataServer
from cdo import Cdo
from multiprocessing import Pool
from tarfile import TarFile
    
server = ECMWFDataServer()
cdo    = Cdo()
cdo.debug = True
pool   = Pool(4)
startYear = 1980
endYear   = 2014
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
        ofile = cdo.mul(input = '-fldmean -selname,%s %s -fldsum -selname,cell_area %s'%(varname,file,file))
    else:
        ofile = cdo.mul(input = '-fldmean -selname,%s %s -fldsum -gridarea %s'%(varname,file,file))
    return ofile


# }}} ==========================================================================
# data retrival {{{
iceCover_file = "ci_interim_%s-%s-NH.grb"%(startYear, endYear)
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

# cams return tarballs of netcdf files
# TODO co2 has problems
#co2_tarball = "co2_totalColumn.tar"
#if ( not os.path.exists(co2_tarball) ):
#    server.retrieve({ #CO2
#        "dataset"   : "cams_ghg_inversions",
#        "datatype"  : "ra",
#        "date"      : "2000-01-01/to/2000-02-01",
#        "frequency" : "3h",
#        "param"     : "co2",
#        "quantity"  : "total_column",
#        "version"   : "v16r2",
#        "target"    : co2_tarball
#    })
#else:
#    print("use existing file '%s'"%(co2_tarball))
#co2_files = getDataFromTarfile(co2_tarball)

meth_tarball = "meth_totalColumn.tar"
if ( not os.path.exists(meth_tarball) ):
    server.retrieve({ #Methane
        "dataset"   : "cams_ghg_inversions",
        "datatype"  : "ra",
        "date"      : "%s-01-01/to/%s-12-31"%(startYear,endYear),
        "frequency" : "6h",
        "param"     : "ch4",
        "quantity"  : "total_column",
        "version"   : "v16r1s",
        "target"    : meth_tarball
    })
else:
    print("use existing file '%s'"%(meth_tarball))
meth_files = getDataFromTarfile(meth_tarball)
exit()
# }}} ==========================================================================

# compute the nh ice extent and the other time series
iceExtent = 'ice_extent_1980-2014-daymean-Sept.nc'
cdo.setattribute('sea_ice_extent@unit=m2,sea_ice_extent@standard_name=sea_ice_extent',
         input = '-setname,sea_ice_extent -fldsum -mul -selmon,9 %s -gridarea %s'%(iceCover_file,iceCover_file),
         output=iceExtent,force=False,
         options = '-f nc')

# co2 removed because of data retrieval issues
#co2_timeSeries = cdo.mul(input = '-fldmean -yearsum %s -fldsum -gridarea %s'%(co2_file),
#        output = 'co2_emission.nc',
#        options = '-f nc',force=False)
meth_timeSeries = cdo.mul(input = '-fldmean -yearsum %s -fldsum -gridarea %s'%(meth_file),
        output = 'meth_emission.nc',
        options = '-f nc',force=False)
