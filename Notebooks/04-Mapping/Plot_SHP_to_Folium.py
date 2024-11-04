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
import folium
from cartopy.img_transform import warp_array
import cartopy.crs as ccrs
import matplotlib.cm
import geojsoncontour
# from geojson import Feature, LineString, FeatureCollection
# import geojson
from matplotlib.colors import rgb2hex
import json

import shapefile
from json import dumps

#reader = shapefile.Reader(r'../DATA/Final Flood Extent 5y.shp')  
reader = shapefile.Reader(r'/Users/datavizcowboy/Documents/Fuel/MFS/Tech_Carles_SoMe/Output_NoUrban/WindNinja/shape72_0_0_0_0_WF.shp')

fields = reader.fields[1:]
field_names = [field[0] for field in fields]
buffer = [] 

for sr in reader.shapeRecords():
       atr = dict(zip(field_names, sr.record))
       geom = sr.shape.__geo_interface__
       buffer.append(dict(type="Feature", \
        geometry=geom, properties=atr)) 

output = dumps({"type": "FeatureCollection","features": buffer},indent=2)


""" FOLIUM """

normed_data=var
cm = matplotlib.cm.get_cmap('gist_heat')
colored_data = cm(var)

m = folium.Map(location=[30,0], zoom_start=3,tiles="cartodbdark_matter")

folium.GeoJson(
    geojson,
    style_function=lambda x: {
        'color':     x['properties']['stroke'],
        'weight':    x['properties']['stroke-width'],
        'fillColor': x['properties']['fill'],
        'fillOpacity': .6,
        'opacity':   1,
    }).add_to(m)

col_neu = []

for i in range(cm.N):
    rgba = cm(i)
    # rgb2hex accepts rgb or rgba
    col_neu.append(matplotlib.colors.rgb2hex(rgba))

import branca.colormap as cmp
step = cmp.StepColormap(
 col_neu,
 vmin=np.nanmin(normed_data), vmax=np.nanmax(normed_data),
 caption='Probability')

step.add_to(m)

from folium import plugins
minimap = plugins.MiniMap()
m.add_child(minimap)

m.save('/Users/datavizcowboy/Dataviz-CubeProbe/views/Wildfires_BurntArea/index.html')

