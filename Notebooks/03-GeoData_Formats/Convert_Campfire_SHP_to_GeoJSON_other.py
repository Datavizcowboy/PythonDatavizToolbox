# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 11:56:22 2016
@author: jorge
"""

import json
from osgeo import ogr
from io import open

driver = ogr.GetDriverByName('ESRI Shapefile')
# shp_path = './geo_admbnda_adm0_geostat_20191018.shp' 

years =[10,11,12,13,15,16,17,19,21,23,25]


# shp_path = '/Users/jorge/Documents/Projects/Mitiga/Tech_Carles_SoMe/Fire_Perimter/2018-11-25.shp'
shp_path = '/Users/jorge/Documents/Projects/Mitiga/Tech_Carles_SoMe/Output_NoUrban/WindNinja/shape72_0_0_0_0_WF.shp'

data_source = driver.Open(shp_path, 0)

fc = {
    'type': 'FeatureCollection',
    'features': []
    }

lyr = data_source.GetLayer(0)
for feature in lyr:    
    fc['features'].append(feature.ExportToJson(as_object=True))

str1 = str(fc) 
str2 = str(str1.encode('utf-8'), errors='ignore')

with open('model_campfire_0.json', 'w') as f:
    json.dump(str2, f)
    
#import shapefile
#   # read the shapefile
#reader = shapefile.Reader('/Users/jmartinez/Documents/Projects/MTQ/Z_QGIS/COMMUNE/COMMUNE.shp')
#fields = reader.fields[1:]
#field_names = [field[0] for field in fields]
#buffer = []
#for sr in reader.shapeRecords():
#       atr = dict(zip(field_names, sr.record))
#       geom = sr.shape.__geo_interface__
#       buffer.append(dict(type="Feature", \
#        geometry=geom, properties=atr)) 
#   
#   # write the GeoJSON file
#from json import dumps
#geojson = open("pyshp-demo.json", "w")
#geojson.write(dumps({"type": "FeatureCollection",\
# "features": buffer}, indent=2) + "\n")
#geojson.close()