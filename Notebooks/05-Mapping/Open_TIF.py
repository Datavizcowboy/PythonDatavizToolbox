# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 11:56:22 2016
@author: jorge
"""
#from PIL import Image
#
#im = Image.open('/Users/jmartinez/Documents/Projects/MTQ/Temperature/Bio_Oracle_Present_Mean_Temp/Pres_Tas_Mean.tif')
#im.show()

from osgeo import gdal
import numpy as np
import matplotlib.pyplot as plt

#dataset = gdal.Open("/Users/jmartinez/Documents/Projects/MTQ/BioOracle_Present.Surface.Cloud.cover.Mean.tif", gdal.GA_ReadOnly)
#dataset = gdal.Open("/Users/jmartinez/Documents/Projects/MTQ/Cariwig_Precip_Gridded_GeoTiff/Gridded_precip_1.tiff", gdal.GA_ReadOnly)
#dataset = gdal.Open("/Users/jmartinez/Documents/Projects/MTQ/Change_Factors/echam5_2071-2101-1971-2001_mean_precip_1.tiff", gdal.GA_ReadOnly)
#dataset = gdal.Open("/Users/jmartinez/Documents/Projects/MTQ/GRIDDED_HIST/Gridded_precip_1.tiff", gdal.GA_ReadOnly)

dataset = gdal.Open("/Users/jmartinez/Documents/Projects/MTQ/output.tiff", gdal.GA_ReadOnly)


data = dataset.GetRasterBand(1).ReadAsArray()
data[data==-999.0] = np.nan
datat=np.transpose(data)
plt.pcolormesh(data)    
plt.colorbar()
plt.show()
