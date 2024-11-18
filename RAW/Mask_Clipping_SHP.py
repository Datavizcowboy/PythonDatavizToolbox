# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 11:56:22 2016
@author: jorge
"""

import pandas as pd
import numpy as np
import csv
import json
import matplotlib.pyplot as plt
from geojson import Feature, LineString, FeatureCollection, Polygon
import geojson
import matplotlib.cm
import geojsoncontour
import geopandas as gpd
from matplotlib.colors import rgb2hex
from shapely.geometry import Polygon
from shapely.geometry import Point

data = '/Users/jorgemartinez/Documents/Fuel/NATIONWIDE/'
folder='/Users/jorgemartinez/Sites/Yeti/public/data/'

lat=[]
lon=[]
obs=[]
datum=[]
diff=[]

fronts = data+'CDD_CONUS_aggregated_1994_2003.csv'

""" CSV TO JSON """

fp = open(fronts, 'r')  

for g in fp.readlines()[1:]:
    model_name=g.strip()
    data=model_name.split(',')

    lat.append(float(data[0]))
    lon.append(float(data[1]))
    obs.append(float(data[2]))
    datum.append(float(data[3]))
    diff.append(float(data[3])-float(data[2])) 

fp.close()

mypanda=pd.DataFrame({"lat":lat[:],"lon":lon[:],"obs":obs[:],"datum":datum[:],"diff":diff[:]})  
#mypanda.to_json(orient='records',path_or_buf=folder+'CONUS_HDD.json')

""" MESHGRID FROM CSV """

loni = np.unique(lon)
lati = np.unique(lat)
count = 0

xs,ys = np.meshgrid(loni,lati)
#xs, ys = np.meshgrid(lon, lat)

dataMesh = np.empty_like(xs)

count=0
for j in range(0,len(lati)):
  for i in range(0,len(loni)):
     dataMesh[j,i]=datum[count]
     count = count+1

#for i, j, d in zip(loni, lati, datum):
#    dataMesh[list(loni).index(i), list(lati).index(j)] = d
#    #print(d)


mask = gpd.read_file('/Users/jorgemartinez/Documents/Fuel/cb_2018_us_nation_20m/cb_2018_us_nation_20m.shp')

""" FLORIDA MASK """

maskFlo = gpd.read_file('/Users/jorgemartinez/Documents/Fuel/cb_2018_us_nation_20m/cb_2018_us_state_20m.shp')

maskFlo = maskFlo.drop(index=24)


""" FILTER ALL POINTS BY US EXTENSION """

lati=[]
loni=[]
lati2=[]
loni2=[]
lati3=[]
loni3=[]
lati4=[]
loni4=[]
tau=[]


index_list = list(maskFlo.index.values)

for k in index_list: 

 for j in range(0,len(xs),1):
   for i in range(0,len(xs[0]),1):
      
              point = Point(float(xs[j][i]),float(ys[j][i]))
              cut = maskFlo.loc[[k],'geometry']
              thecheck = cut.contains(point)
              # print(thecheck)
              
              if(thecheck.values[0] == True):
           
                 # Shift in longitudes
                 lati.append(float(ys[j][i]))
                 loni.append(float(xs[j][i]))
                 lati2.append(float(ys[j+1][i]))
                 loni2.append(float(xs[j+1][i]))
                 lati3.append(float(ys[j][i+1]))
                 loni3.append(float(xs[j][i+1]))
                 lati4.append(float(ys[j+1][i+1]))
                 loni4.append(float(xs[j+1][i+1]))
                
                 # Store wind speeds
                 tau.append(float(dataMesh[j][i]))

mypanda_US=pd.DataFrame({"lat":lati,"lon":loni,
                          "lat2":lati2,"lon2":loni2,
                          "lat3":lati3,"lon3":loni3,
                          "lat4":lati4,"lon4":loni4,"windx":tau[:]})  
mypanda_US.to_json(orient='records',path_or_buf=folder+'CONUS_CDD_US_FLO_1994_2003.json')


