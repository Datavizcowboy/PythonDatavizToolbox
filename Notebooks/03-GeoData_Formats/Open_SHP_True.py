# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 11:56:22 2016
@author: jorge
"""
#from PIL import Image
#
#im = Image.open('/Users/jmartinez/Documents/Projects/MTQ/Temperature/Bio_Oracle_Present_Mean_Temp/Pres_Tas_Mean.tif')
#im.show()

#
#from osgeo import ogr
#import osgeo.ogr
#import matplotlib.pyplot as plt
#import shapefile

import shapefile as shp
import matplotlib.pyplot as plt

shape = shp.Reader(r'/Users/jmartinez/Documents/Projects/MTQ/Z_QGIS/COMMUNE/COMMUNE.shp')

# print 'number of shapes imported:',len(shape.shapes())
#
#file = ogr.Open('/Users/jmartinez/Documents/Projects/MTQ/Z_QGIS/COMMUNE.shp')
#shape = file.GetLayer(0)
##first feature of the shapefile
#feature = shape.GetFeature(0)
#first = feature.ExportToJson()
#print first # (GeoJSON format)

#shape = shapefile.Reader('/Users/jmartinez/Documents/Projects/MTQ/Z_QGIS/COMMUNE.shp')
##first feature of the shapefile
#feature = shape.shapeRecords()[0]
#first = feature.shape.__geo_interface__  
#print first # (GeoJSON format)
#
#
#first feature of the shapefile
feature = shape.shapeRecords()[0]
first = feature.shape.__geo_interface__  
# print first # (GeoJSON format)

plt.figure()
for shape in shape.shapeRecords():
    x = [i[0] for i in shape.shape.points[:]]
    y = [i[1] for i in shape.shape.points[:]]
    plt.plot(x,y)
plt.show()