#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 10 12:51:11 2023

@author: jorge
"""

from osgeo import gdal

onefile = "/Users/jorge/Documents/Projects/Mitiga/UNDP/AVALANCHE/Natanebi/Blank.tif"
twofile = "/Users/jorge/Documents/Projects/Mitiga/UNDP/AVALANCHE/Natanebi/FinalPressure100y_Class.tif"
output = "/Users/jorge/Documents/Projects/Mitiga/UNDP/AVALANCHE/Natanebi/merged.tif"


files_to_mosaic = [onefile, twofile] # However many you want.
g = gdal.Warp(output, files_to_mosaic, format="GTiff",
              options=["COMPRESS=LZW", "TILED=YES"]) # if you want
g = None # Close file and flush to disk