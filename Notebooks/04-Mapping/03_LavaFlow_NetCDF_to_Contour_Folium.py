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
from folium import plugins

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

d10_file = '/Users/datavizcowboy/Documents/Fuel/VOLCANOS/CATBOND/HawaiiBetter.nc'
ds        = xr.open_dataset(d10_file)

""" Extract the desired variable """

lats = ds.lat
lons = ds.lon
#var = ds.tephra_cloud_top[-1]
var = ds.myvar

var = np.where(var<0, np.nan, var)

import random 

#var = [i*100 for i in var]

#units = ds.tephra_cloud_top.long_name

#thedate = ds['time'][-1].values
#ts = pd.to_datetime(str(thedate)) 
## d = ts.strftime('%Y.%m.%d')
#d = ts.strftime('%c')

#var_name = ds.HM.description
#var_units = ds.HM.units
#title = var_name + ' ' + var_units 

""" BOUNDARIES """

#lat_list = [np.array(lats) for i in range(300)]   
#v_lat_list= np.vstack(lat_list) 

#vari = np.where(var>=1, 1, var)

#lon_list = [np.array(lons) for i in range(300)]   
#v_lon_list= np.vstack(lon_list) 

#clipped_lat = vari * v_lat_list
#clipped_lon = vari * v_lon_list


""" CONTOUR PLOT """

#colors=["gold", "goldenrod", "darkgoldenrod","darkorange","white"]
colors=['#ffffe5','#fff7bc','#fee391','#fec44f','#fe9929','#ec7014','#cc4c02','#8c2d04']
colors=['#fff7bc','#fee391','#fec44f','#fe9929','#ec7014','#cc4c02','#8c2d04']
cvals  = [0.001,0.02,0.04,0.06,0.08,0.17]
norm=plt.Normalize(min(cvals),max(cvals))
tuples = list(zip(map(norm,cvals), colors))
cmap = matplotlib.colors.LinearSegmentedColormap.from_list("", tuples)
#cmap = 'gist_heat'

contourf = plt.contourf(lons,lats,var,levels=cvals,vmin=0.0001, vmax=0.16,alpha=1, cmap=cmap,norm=norm);

""" CONVERT PLOT TO GEOJSON """

geojson = geojsoncontour.contourf_to_geojson(
    contourf=contourf,
    min_angle_deg=3.0,
    ndigits=4,
    # opacity=1,
    stroke_width=1,
    fill_opacity=1)

normed_data=var
cm = matplotlib.cm.get_cmap('RdYlBu')
colored_data = cm(var)

""" ADD THE GEOJSON TO FOLIUM MAP """

m = folium.Map(location=[lats.mean(), lons.mean()], zoom_start=7,tiles="cartodbdark_matter")

g = folium.GeoJson(
    geojson,
    style_function=lambda x: {
        'color':     x['properties']['stroke'],
        'weight':    x['properties']['stroke-width'],
#        'weight':0    ,
        'fillColor': x['properties']['fill'],
        'fillOpacity': .6,
        'opacity':   1,
    })
g.add_to(m)

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
from branca.colormap import ColorMap, LinearColormap, StepColormap
from branca.element import MacroElement
from branca.element import Figure, JavascriptLink
from branca.utilities import legend_scaler
from branca.element import Element

step = cmp.StepColormap(
 colors,
 index=[-1,-0.3,0,0.69897,1,1.69897,2],
 vmin=-1, vmax=2,
 )

e = Element("""
  var all = document.querySelectorAll('div.legend text')
  console.log(all)
  for(var i = 0; i < all.length; i++) {
   all[i].style.fill="white"
   all[i].style.fontSize=9
  }
  var ticks = document.querySelectorAll('div.legend g.tick text')
  console.log(ticks)
  for(var i = 0; i < ticks.length; i++) {
    var value = parseFloat(ticks[i].textContent.replace(',', ''))
    var newvalue = Math.pow(10.0, value).toFixed(1).toString()
    ticks[i].textContent = newvalue
    ticks[i].style.fill="white"
  }
""")

#step.add_to(m)

#html = step.get_root()
#html.script.get_root().render()
#html.script.add_child(e)



""" ADD CATBOND VOLCANOS """ 

list_names=["Popocatepetl","Nevado del Ruiz","Cotopaxi", "Tungurahua","Pichincha","Merapi","Raung","Villarica","Fuego","Mt.Cameroon"]

list_catbond = [[19.27361, -98.70222], [4.883333, -75.31667], [-0.6847222, -78.43167], [-1.466944, -78.44167]
			, [-0.1772222, -78.59889], [-7.541389, 110.4461], [8.125, 114.0417], [-39.42, -71.93917], [14.47444, -90.88028]
			, [4.216667, 9.1725]]

for point in range(0, len(list_catbond)):
    folium.Marker(list_catbond[point],popup=list_names[point],icon=folium.Icon(color='lightgray', icon='fa-caret-up', prefix='fa')).add_to(m)

""" ADD MINIMAP """ 
    
from folium import plugins
minimap = plugins.MiniMap()
m.add_child(minimap)

# svg_style = '<style>svg {background-color: white;opacity:1}</style>'
# m.get_root().header.add_child(folium.Element(svg_style))

""" SAVE AS HTML IN YETI """

#m.save('/Users/datavizcowboy/Dataviz-CubeProbe/views/Volcano_Ashload/index.html')
m.save('/Users/datavizcowboy/Sites/MITIGA/Volcanoes/VolcanoLava/index.html')
