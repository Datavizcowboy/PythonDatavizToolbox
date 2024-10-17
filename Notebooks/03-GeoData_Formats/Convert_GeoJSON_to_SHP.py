#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 17:30:33 2023

@author: jorge
"""

import geopandas as gpd

gdf = gpd.read_file('/Users/jorge/Documents/Projects/Cowboy/OroraTech/chile_fire_cluster_perimeter.json')
gdf.to_file('/Users/jorge/Documents/Projects/Cowboy/OroraTech/chile_fire_shape.shp')

reader = r'/Users/jorge/Documents/Projects/Cowboy/OroraTech/chile_fire_shape.shp' 
data = gpd.read_file(reader)
selection = data[:]

areas = []
lengths = []

for index, row in selection.iterrows():
    
    poly_area = row['geometry'].area
    poly_length = row['geometry'].length
    
    areas.append(poly_area)
    lengths.append(poly_length)
    
print(sum(areas))
print(sum(lengths))