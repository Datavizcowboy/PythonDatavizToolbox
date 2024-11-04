#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 16:32:19 2023

@author: jorge
"""

# from PIL import Image
# im = Image.open('/Users/jorge/Documents/Projects/Mitiga/MFS/UniformStyle/i576/index_20120723000000_b1ef04e6.tif')
# im.show()

from osgeo import gdal
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
startTime = datetime.now()

dataset = gdal.Open(r'/Users/jorge/Documents/Projects/Mitiga/MFS/UniformStyle/i483/index_20120725000000_ec58dd63.tif')

band2 = dataset.GetRasterBand(1) # Green channel

img1 = band2.ReadAsArray(0,0,dataset.RasterXSize, dataset.RasterYSize)

img = np.dstack(img1)

f = plt.figure()
plt.imshow(img[0])
plt.savefig('/Users/jorge/Desktop/Tiff.png')
plt.show()

print('size is '+str(len(img[0]))+' by '+str(len(img[0][0])))
print(datetime.now() - startTime)