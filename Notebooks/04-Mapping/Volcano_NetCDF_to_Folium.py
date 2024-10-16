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
import folium
from cartopy.img_transform import warp_array
import cartopy.crs as ccrs
import matplotlib.cm
import geojsoncontour
# from geojson import Feature, LineString, FeatureCollection
# import geojson
from matplotlib.colors import rgb2hex
# import io
# from PIL import Image

""" Title and Units to be plotted """

title = 'tephra_grn_load'

""" Open File """

d10_file = '/Users/datavizcowboy/Documents/Fuel/MFS/StandardOutput/example.nc'
ds        = xr.open_dataset(d10_file)

""" Extract the desired variable """

lats = ds.lat
lons = ds.lon
#var = ds.tephra_cloud_top[-1]
var = ds.tephra_grn_load[1]

var = np.where(var==0, np.nan, var)
var = [i*1000000000000000 for i in var]

units = ds.tephra_cloud_top.long_name

thedate = ds['time'][-1].values
ts = pd.to_datetime(str(thedate)) 
# d = ts.strftime('%Y.%m.%d')
d = ts.strftime('%c')

""" BOUNDARIES """

y_min=np.min(lats)
y_max=np.max(lats)
x_min=np.min(lons)
x_max=np.max(lons)

""" CONTOUR PLOT """

cmap = plt.cm.plasma
contourf = plt.contourf(lons,lats,var,levels=[0.1,1,10,100],vmin=np.nanmin(var), vmax=np.nanmax(var),alpha=1, cmap=cmap);

""" CONVERT PLOT TO GEOJSON """

geojson = geojsoncontour.contourf_to_geojson(
    contourf=contourf,
    min_angle_deg=3.0,
    ndigits=100,
    # opacity=1,
    stroke_width=1,
    fill_opacity=1)

normed_data=var
cm = matplotlib.cm.get_cmap('plasma')
colored_data = cm(var)

""" ADD THE GEOJSON TO FOLIUM MAP """

m = folium.Map(location=[lats.mean(), lons.mean()], zoom_start=6,tiles="cartodbpositron")

folium.GeoJson(
    geojson,
    style_function=lambda x: {
        'color':     x['properties']['stroke'],
        'weight':    x['properties']['stroke-width'],
        'fillColor': x['properties']['fill'],
        'fillOpacity': .8,
        'opacity':   1,
    }).add_to(m)

# folium.raster_layers.ImageOverlay(mesh,
#                       [[lats.min(), lons.min()], [lats.max(), lons.max()]],
#                       mercator_project=True,
#                       opacity=1).add_to(m)

""" CREATE A COLORBAR """ 

col_neu = []

for i in range(cm.N):
    rgba = cm(i)
    # rgb2hex accepts rgb or rgba
    col_neu.append(matplotlib.colors.rgb2hex(rgba))

import branca.colormap as cmp
step = cmp.StepColormap(
 col_neu,
 vmin=np.nanmin(normed_data), vmax=np.nanmax(normed_data),
 caption=title)

step.add_to(m)

""" ADD CATBOND VOLCANOS """ 

list_names=["Popocatepetl","Nevado del Ruiz","Cotopaxi", "Tungurahua","Pichincha","Merapi","Raung","Villarica","Fuego","Mt.Cameroon"]

list_catbond = [[19.27361, -98.70222], [4.883333, -75.31667], [-0.6847222, -78.43167], [-1.466944, -78.44167]
			, [-0.1772222, -78.59889], [-7.541389, 110.4461], [8.125, 114.0417], [-39.42, -71.93917], [14.47444, -90.88028]
			, [4.216667, 9.1725]]

for point in range(0, len(list_catbond)):
    folium.Marker(list_catbond[point],popup=list_names[point]).add_to(m)

""" ADD MINIMAP """ 
    
from folium import plugins
minimap = plugins.MiniMap()
m.add_child(minimap)

# svg_style = '<style>svg {background-color: white;opacity:1}</style>'
# m.get_root().header.add_child(folium.Element(svg_style))

""" SAVE AS HTML IN YETI """

m.save('/Users/datavizcowboy/Dataviz-CubeProbe/views/Catbond_Map/index.html')

