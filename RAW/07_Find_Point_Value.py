# -*- coding: utf-8 -*-
"""
MITIGA

Jorge Martinez-Rey 2022.
"""

from netCDF4 import Dataset
import geopandas as gp
import xarray as xr
import pandas as pd
import numpy as np
from datetime import datetime
startTime = datetime.now()

#fh = Dataset('/Users/jorgemartinez/Documents/Fuel/ANTICIPA/CDD_avg.nc','r')

d10_file = '/Users/jorgemartinez/Documents/Fuel/ANTICIPA/CDD_avg.nc'
dsw        = xr.open_dataset(d10_file)
cdd = dsw.myvar

min_lat=40.4194408-0.001
max_lat=40.4194408+0.001
min_lon=-3.7020147-0.002
max_lon=-3.7020147+0.003

#cropw = cdd.where((cdd.lat > min_lat) & (cdd.lat < max_lat) & (cdd.lon > min_lon) & (cdd.lon < max_lon),drop=True)
cropped_ds = cdd.sel(lat=slice(min_lat,max_lat), lon=slice(min_lon,max_lon))

