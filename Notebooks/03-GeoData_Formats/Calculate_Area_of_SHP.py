# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 11:56:22 2016
@author: jorge
"""

import geopandas as gpd
import pandas as pd

folder = '/Users/jorge/Sites/MITIGA/Wildfires/Flames/'
years =[10,11,12,13,15,16,17,19,21,23,25]
areas = []
zeit =[]

for i in years:
    
    reader = r'/Users/jorge/Documents/Projects/Mitiga/MFS/Tech_Carles_SoMe/Fire_Perimter/2018-11-'+str(i)+'.shp' 
    
    data = gpd.read_file(reader)
    selection = data[:]
    
    counter = 0
    for index, row in selection.iterrows():
        poly_area = row['geometry'].area
        counter = counter + poly_area
        # print("Polygon area at index {0} is: {1:.3f}".format(index, poly_area)) 
    
    areas.append(counter)
    zeit.append(i)
    # print("Total Polygon area: {1:.3f}".format(index, counter)) 

hs2=pd.DataFrame({"areas":areas, "zeit": zeit})
hs2.reset_index().to_json(orient='records',path_or_buf=folder+'campfire_areas.json')     