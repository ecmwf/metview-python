import metview as mv
import numpy as np
from scipy import stats

t2m_grib = mv.read('./examples/t2m_grib.grib')

obs_3day = mv.read('./examples/obs_3day.bufr')

t2m_gpt = mv.obsfilter(
    parameter = '012004',
    output = 'geopoints',
    data = obs_3day
)

diff = t2m_grib - t2m_gpt

df = diff.to_dataframe()

print(df)

outliers = np.abs(stats.zscore(df)) > 1.5

print('# of outliers:', outliers.sum())
