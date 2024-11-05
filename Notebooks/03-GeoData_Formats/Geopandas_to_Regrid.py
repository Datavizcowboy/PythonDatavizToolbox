# -*- coding: utf-8 -*-
"""
MITIGA

Jorge Martinez-Rey 2022. 
"""

import xarray as xr
import pandas as pd
import numpy as np
from wrf import (getvar, interplevel, to_np, latlon_coords, CoordPair, xy_to_ll, ll_to_xy)
import geopandas as gp
import cartopy.crs as ccrs
import cartopy
import cartopy.feature as cfeature
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
from shapely.geometry import Polygon
from shapely.geometry import Point
from cartopy.io import shapereader
import cartopy.io.img_tiles as cimgt
# import regionmask
import rioxarray
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.colors as colors
from matplotlib.patches import Circle,RegularPolygon
from mpl_toolkits.axes_grid1 import make_axes_locatable
import warnings
warnings.filterwarnings("ignore")
from pyresample.geometry import SwathDefinition
from pyresample.kd_tree import resample_nearest
import matplotlib.mlab as ml
import shapely

pd.set_option('display.max_columns', 500)

""" FOLDERS """

results_path = '/Users/jorge/Documents/Projects/Mitiga/UNDP/UNDP_GeorgAI_NetCDF/'
output_path = '/Users/jorge/Desktop/'
folder='/Users/Jorge/Sites/Mitiga/UNDP/UNDP_Georgia_Leaflet_Polygon/DATA/'

hail_file = results_path+'Annual_Bin/Wind_rt_cdf_binrange.nc'
ds        = xr.open_dataset(hail_file) 

''' Mask with Georgia boundaries'''

# resolution = '10m'
# category = 'cultural'
# name = 'admin_0_countries'

# shpfilename = shapereader.natural_earth(resolution, category, name)
# df = gp.read_file(shpfilename)

# # get geometry of a country
# poly = [df.loc[df['ADMIN'] == 'Georgia']['geometry'].values[0]]


''' Select bin to plot'''
intensity = 0

''' Select dataset to plot'''
bin_val = ds.intensities[intensity].values
var = ds.Probability.isel(intensities=intensity)*100
print(var.min().values, var.max().values)
# topo = ds.Topography
lats, lons = latlon_coords(var)

""" REGRID """

from scipy.interpolate import griddata

Yi = np.linspace(np.min(lats.data),float(np.max(lats.data)),6*len(lats))
Xi = np.linspace(np.min(lons.data),float(np.max(lons.data)),6*len(lons[0]))
X, Y = np.meshgrid(Xi,Yi)

""" Lambert to Regular"""

nvals = griddata((lons.values.ravel(),     
                                   lats.values.ravel()),    
                                   var.values.ravel(),          
                                   (X,Y),    
                                   method='linear')

""" OPEN FLOOD """

df = gp.read_file('/Users/jorge/Downloads/FLOODING/Flood_Natanebi/Final Flood Extent 5y.shp')
df = df.to_crs(epsg=4326)
x_min, y_min, x_max, y_max = df.total_bounds

""" GEOPANDAS ON THE NEW GRID """

# Cell Size

n_cells=100
cell_size = (x_max-x_min)/n_cells

# projection of the grid
# crs = "+proj=sinu +lon_0=0 +x_0=0 +y_0=0 +a=6371007.181 +b=6371007.181 +units=m +no_defs"

grid_cells = []

for x0 in np.arange(x_min, x_max+cell_size, cell_size ):
    for y0 in np.arange(y_min, y_max+cell_size, cell_size):
        # bounds
        x1 = x0-cell_size
        y1 = y0+cell_size
        grid_cells.append(shapely.geometry.box(x0, y0, x1, y1)  )

cell = gp.GeoDataFrame(grid_cells, columns=['geometry'])
cell['centroids'] = cell['geometry'].centroid


merged = gp.sjoin(df, cell)

merged['n_fires']=1
# Compute stats per grid cell -- aggregate fires to grid cells with dissolve
dissolve = merged.dissolve(by="index_right", aggfunc="count")
# put this into cell
cell.loc[dissolve.index, 'n_fires'] = dissolve.n_fires.values

""" GEOPANDAS ON X,Y """

# x = df['geometry'].x
# y = df['geometry'].y
# z = df['car_obs']

x = cell['centroids'].x
y = cell['centroids'].y
z = cell['n_fires']


points = (x,y)
values = z

river = griddata(points,
                    values,
                    (X,Y),
                    method='nearest')


""" CHECK OUTPUT """

# # # plt.plot(lons,lats, marker='.', color='k', linestyle='none')

fig,ax = plt.subplots(figsize=(3,2), dpi=144)

# fig, ax = plt.subplots(figsize=(15, 15))
# ax = cell.plot(column='n_fires', figsize=(12, 8), cmap='viridis', vmax=100, edgecolor="grey")
# ax = merged.plot(column='index_right', figsize=(12, 8), cmap='viridis', vmax=100, edgecolor="grey")

# cell.plot(ax=ax, facecolor="none", edgecolor='grey')

ax.pcolormesh(lons,lats,var)
# ax.pcolormesh(X,Y,nvals)
# ax.pcolormesh(X,Y,river,cmap='autumn')

# ax.colorbar()

df.plot(ax=ax, color='red')

ax.set_ylim(y_min,y_max)
ax.set_xlim(x_min,x_max)
# # # # ax.set_xlim(np.min(lons),np.min(lons)+1)

# # # # num = 25
# # # # ax.plot(lons[-num:],lats[-num:],marker='o', color='b', linestyle='none',ms=.2)
# # # # ax.plot(X[-num-5:],Y[-num-5:], marker='o', color='g', linestyle='none',ms=.2)

ax.plot(lons[:],lats[:],marker='o', color='b', linestyle='none',ms=1)
# ax.plot(X[:],Y[:], marker='+', color='black', linestyle='none',ms=1)

# # # # plt.scatter(lons,lats)

# plt.savefig("/Users/jorge/Desktop/fig.pdf",dpi=300, bbox_inches="tight")
# # # # plt.show()



















