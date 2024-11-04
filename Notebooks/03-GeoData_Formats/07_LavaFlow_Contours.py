#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 13:29:45 2023

@author: jorge
"""

""" Import useful libraries """

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import EngFormatter, StrMethodFormatter
import xarray as xr
import pandas as pd
import geopandas as gp
import datetime
from datetime import datetime
startTime = datetime.now()
import re

from geojson import Feature, LineString, FeatureCollection
import geojson

from cartopy.img_transform import warp_array
import cartopy.crs as ccrs
import matplotlib.cm
import geojsoncontour
# from geojson import Feature, LineString, FeatureCollection
# import geojson
from matplotlib.colors import rgb2hex
# import io
# from PIL import Image

""" Open File """
#d10_file = '/Users/datavizcowboy/Documents/Fuel/VOLCANOS/CATBOND/Cotopaxi-HM.nc'

#d10_file = '/Users/datavizcowboy/Documents/Fuel/VOLCANOS/CATBOND/MaunaLoa_reprojected.nc'
d10_file = '/Users/datavizcowboy/Documents/Fuel/VOLCANOS/CATBOND/HawaiiBetter.nc'
ds        = xr.open_dataset(d10_file)

""" Extract the desired variable """

lats = ds.lat
lons = ds.lon
#var = ds.tephra_cloud_top[-1]
var = ds.myvar

var = np.where(var<0, np.nan, var)
#var = [i*1000 for i in var]

""" CONVERT PLOT TO GEOJSON """

figure = plt.figure()
ax = figure.add_subplot(111)
contour = ax.contour(lons, lats, var, levels=np.linspace(start=0, stop=.25, num=10), cmap=plt.cm.Reds)

line_features = []
for collection in contour.collections:
    paths = collection.get_paths()
    color = collection.get_edgecolor()
    for path in paths:
        v = path.vertices
        coordinates = []
        for i in range(len(v)):
            lat = v[i][0]
            lon = v[i][1]
            coordinates.append((lat, lon))
        line = LineString(coordinates)
        properties = {
            "opacity": .5,
            "stroke-width": .5,
            "stroke": rgb2hex(color[0]),
        }
        line_features.append(Feature(geometry=line, properties=properties))

feature_collection = FeatureCollection(line_features)
geojson_dump = geojson.dumps(feature_collection, sort_keys=True)
with open('/Users/datavizcowboy/Sites/MITIGA/Volcanoes/VolcanoAshload/Leaflet/Hualalai_reprojected.geojson', 'w') as fileout:
    fileout.write(geojson_dump)

from pylab import *

cmap = cm.get_cmap('Reds', 10) 

for i in range(cmap.N):
    rgba = cmap(i)
    print(matplotlib.colors.rgb2hex(rgba))
