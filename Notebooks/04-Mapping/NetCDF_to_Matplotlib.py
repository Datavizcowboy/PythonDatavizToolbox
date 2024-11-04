#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 13:29:45 2023

@author: jorge
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import EngFormatter, StrMethodFormatter
import xarray as xr
import pandas as pd
import geopandas as gp
from datetime import datetime
startTime = datetime.now()

""" OPEN FILE """

d10_time = '/Users/jorge/Documents/Projects/Mitiga/MFS/StandardOutput/PortugalTestv0_IgnitionRiskMap_2017_41_9_10_2017-16_10_2017.nc'
dt        = xr.open_dataset(d10_time)

thedate = dt['time'][0].values
ts = pd.to_datetime(str(thedate)) 
d = ts.strftime('%Y.%m.%d')

d10_file = '/Users/jorge/Documents/Projects/Mitiga/MFS/StandardOutput/Portugal_3035.nc'
ds        = xr.open_dataset(d10_file)

lats = ds.lat
lons = ds.lon
var = ds.Band1/9999

""" BOUNDARIES """

y_min=np.min(lats)
y_max=np.max(lats)
x_min=np.min(lons)
x_max=np.max(lons)

df = gp.read_file('/Users/jorge/Documents/Projects/Mitiga/MFS/StandardOutput/gadm41_PRT_1.shp')
df = df.to_crs(epsg=4326)

""" IF TIF """

# dataset = gdal.Open(r'/Users/jorge/Documents/Projects/Mitiga/MFS/UniformStyle/i483/index_20120725000000_ec58dd63.tif')
# band2 = dataset.GetRasterBand(1)
# img1 = band2.ReadAsArray(0,0,dataset.RasterXSize, dataset.RasterYSize)
# img = np.dstack(img1)

""" PLOT """

plt.style.use('dark_background')

fig,ax = plt.subplots(1,1)

ax.set_ylim(y_min,y_max)
ax.set_xlim(x_min,x_max)

# ax.set_title('Ignition Points Probability', fontsize=10,linespacing=4.2)
ax.set_xlabel('Longitude', fontsize=6,linespacing=1, color='grey')
ax.set_ylabel('Latitude', fontsize=6, color='grey')

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_color('grey')
ax.spines['left'].set_color('grey')

# ax.legend(fontsize=8,frameon=False,loc="upper left", bbox_to_anchor=(0.1,0.2))

ax.text(0.05,0.98,'Ignition Points',fontsize=7,weight='bold',transform=ax.transAxes, bbox=dict(facecolor='none',edgecolor='none',boxstyle='square')) 
ax.text(0.05,0.95,'Probability',fontsize=6,transform=ax.transAxes, bbox=dict(facecolor='none',edgecolor='none',boxstyle='square')) 
ax.text(0.05,0.93,d,fontsize=4,transform=ax.transAxes, bbox=dict(facecolor='none',edgecolor='none',boxstyle='square')) 

ax.minorticks_on()
ax.tick_params(axis='both', which='major', labelsize=4, colors='grey')
ax.tick_params(axis='both', which='minor', labelsize=4, colors='grey')

ax.yaxis.set_major_formatter(EngFormatter(unit=u"°N"))

ax.xaxis.set_ticks(np.arange(-10, -4, 1))

ax.set_xticklabels(['10°W','9°W','8°W','7°W','6°W','5°W'])

# ax.xaxis.set_major_formatter(EngFormatter(unit=u"°W"))


df.plot(ax=ax, color='white', edgecolor='black',linewidth=.2,aspect=1)

cmap = plt.get_cmap('gist_heat')
mesh = ax.pcolormesh(lons,lats,var,vmin=np.nanmin(var), vmax=np.nanmax(var),alpha=0.7, cmap=cmap);

cbax = ax.inset_axes([1.1, 0, 0.02, 0.2], transform=ax.transAxes)
cbar = plt.colorbar(mesh, ax=ax, cax=cbax, shrink=.3, pad=.2, aspect=20)
cbar.ax.tick_params(labelsize=4, width=0.01) 
# plt.imshow(var)
ax.grid(linestyle='dotted',linewidth=.2, alpha=0.8)  

plt.savefig("/Users/jorge/Desktop/Portugal2.png", dpi=300)
plt.show()

""" ALTERNATIVE PLOT """
print(datetime.now() - startTime)