# -*- coding: utf-8 -*-
"""
MITIGA

Jorge Martinez-Rey 2022. 
"""
import geopandas as gp
import xarray as xr
import pandas as pd
import numpy as np

from wrf import (getvar, interplevel, to_np, latlon_coords, CoordPair, xy_to_ll, ll_to_xy)

# import geopandas as gp
import cartopy.crs as ccrs
import cartopy
import cartopy.feature as cfeature
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
from shapely.geometry import Polygon
from shapely.geometry import Point
from cartopy.io import shapereader
import cartopy.io.img_tiles as cimgt
# import regionmask
import rasterio

import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.colors as colors
from matplotlib.patches import Circle,RegularPolygon
from mpl_toolkits.axes_grid1 import make_axes_locatable
from geojson import Feature, LineString, FeatureCollection
import geojson
from matplotlib.colors import rgb2hex
import warnings
warnings.filterwarnings("ignore")
import shapefile
import geopandas as gp
pd.set_option('display.max_columns', 500)
import utm


results_path = '/Users/datavizcowboy/Documents/Cowboy/TRANSPARENC/'
output_path = '/Users/datavizcowboy/Documents/Cowboy/Desktop/'
folder='/Users/datavizcowboy/Sites/TRANSPARENC/DATA/'

hail_file = results_path+'Crop_2025_Alos.nc'
ds        = xr.open_dataset(hail_file) 
var = ds.myvar
edgar = ds.to_dataframe()
edgar = edgar.reset_index()
edgar_gdf = gp.GeoDataFrame(edgar, geometry=gp.points_from_xy(edgar.lon, edgar.lat))


df = gp.read_file('/Users/datavizcowboy/Documents/Cowboy/TRANSPARENC/Palm.shp')
df = df.to_crs(epsg=4326)

edgar_gdf.crs = df.crs

mask = gp.clip(edgar_gdf, df)

mypanda = pd.DataFrame(mask)
mypanda = mypanda.drop('geometry',axis=1)
mypanda.reset_index().to_json(orient='records',path_or_buf='/Users/datavizcowboy/Desktop/Crop_2025_masked_by_Palm.json')
