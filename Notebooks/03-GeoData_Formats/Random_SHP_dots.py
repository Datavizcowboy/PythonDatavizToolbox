#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 14:17:34 2022

@author: jorge
"""

from osgeo import gdal
from osgeo import ogr
from osgeo import osr
import geopandas as gpd
import numpy as np

import shapefile as shp
# import matplotlib as plt
import geoplot
import geoplot.crs as gcrs

import matplotlib.ticker as mticker
import matplotlib.colors as colors
from matplotlib.patches import Circle,RegularPolygon
from mpl_toolkits.axes_grid1 import make_axes_locatable

reader = r'/Users/jorge/Documents/Projects/Cowboy/OroraTech/chile_fire_shape.shp' 

gdf_polys = gpd.read_file(reader)
# generate random data within the bounds
x_min, y_min, x_max, y_max = gdf_polys.total_bounds
# set sample size
n = 2000
# generate random data within the bounds
x = np.random.uniform(x_min, x_max, n)
y = np.random.uniform(y_min, y_max, n)
# convert them to a points GeoSeries
gdf_points = gpd.GeoSeries(gpd.points_from_xy(x, y))
# only keep those points within polygons
gdf_points = gdf_points[gdf_points.within(gdf_polys.unary_union)]
print(gdf_points)

# gdf_points.to_json() 
# gdf_points.to_file('/Users/jorge/Sites/Chile/DATA/random_seed.geojson', driver='GeoJSON')  
# gdf_points.crs

import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(15, 15))
gdf_polys.plot(ax=ax)
gdf_points.plot(ax=ax,color='r', markersize=80)
# gdf_points.plot(ax=ax,color='r',markersize=gdf_points['values'])


# geoplot.polyplot(gdf_polys, projection=gcrs.AlbersEqualArea(), edgecolor='darkgrey', facecolor='lightgrey', linewidth=.3,
#     figsize=(12, 8))