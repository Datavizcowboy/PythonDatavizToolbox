#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 12:31:04 2023

@author: jorge
"""

import xarray as xr 
import rioxarray as rio

""" Read the NetCDF """

folder ='/Users/jorge/Desktop/'

nc_file = xr.open_dataset('/Users/jorge/Documents/Projects/Mitiga/WIND/Windstorm_30y.nc')

print(nc_file)

bT = nc_file['Probability_ex']

# bTlon = nc_file['XLONG']
# bTlat = nc_file['XLAT']

bT = bT.rio.set_spatial_dims(x_dim='west_east', y_dim='south_north')

# bT.rio.write_crs("epsg:4326", inplace=True)

bT.rio.to_raster(r"/Users/jorge/Documents/Projects/Mitiga/WIND/TIFF/Windstorm_30y.tiff")

""" PLOT THE TIFF """

from osgeo import gdal
import matplotlib.pyplot as plt
import numpy as np

dataset = gdal.Open(r'/Users/jorge/Documents/Projects/Mitiga/WIND/TIFF/Windstorm_30y.tiff')

band2 = dataset.GetRasterBand(2) # Green channel
img1 = band2.ReadAsArray(0,0,dataset.RasterXSize, dataset.RasterYSize)

img = np.dstack(img1)

img_T = np.transpose(img[0])
img_T_flip = np.flipud(img_T)

f = plt.figure()
plt.imshow(img_T_flip)
# plt.savefig('/Users/jorge/Desktop/Tiff.png')
plt.show()

# loni = nc.variables['XLONG'][:]
# lati = nc.variables['XLAT'][:]
# oxy=nc.variables['Probability_ex'][:,:,:]
# nc.close()

# lons = loni.data[:]
# lats = lati.data[:]
# oxyy=oxy[1,:,:]

