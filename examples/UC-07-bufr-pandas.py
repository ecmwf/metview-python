# (C) Copyright 2017- ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
#
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.

"""
Metview Python use case

UC-07-pandas. The Analyst compute simple differences between observations and analysis
and use pandas to perform further computations

BUFR version - BUFR is not tabular or gridded, but we can use Metview Python
framework to extract a particular parameter to a tabular format (geopoints)

--------------------------------------------------------------------------------
1. Analyst retrieves the analysis from a gridded data file
--------------------------------------------------------------------------------

--------------------------------------------------------------------------------
2. Analyst retrieves an observational parameter from a tabular or a gridded file
--------------------------------------------------------------------------------

--------------------------------------------------------------------------------
3. Analyst calculates the difference between the observational data and the
   analysis
--------------------------------------------------------------------------------

--------------------------------------------------------------------------------
4. Analyst converts this data to a pandas dataframe and computes the number
   of outliers based on the zscore
--------------------------------------------------------------------------------
"""

import metview as mv
import numpy as np
from scipy import stats

t2m_grib = mv.read("./t2m_grib.grib")

obs_3day = mv.read("./obs_3day.bufr")

t2m_gpt = mv.obsfilter(parameter="012004", output="geopoints", data=obs_3day)

diff = t2m_grib - t2m_gpt

df = diff.to_dataframe()

print(df)

outliers = np.abs(stats.zscore(df["value"])) > 1.5

print("# of outliers:", outliers.sum())
