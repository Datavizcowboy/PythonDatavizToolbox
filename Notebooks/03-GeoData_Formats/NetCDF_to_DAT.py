# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 11:56:22 2016

@author: jorge
"""

import pandas as pd
import netCDF4
import numpy as np

folder='/Users/Jorge/Sites/zoo_flat/'
nc = netCDF4.Dataset('/Users/Jorge/Documents/Projects/DUKE/Duke_Export/eppley_export.nc')
lons = nc.variables['ETOPO60X'][:]
lats = nc.variables['ETOPO60Y'][:]
oxygen = nc.variables['EXP'][:,:]

lati=[]
loni=[]
oxy=[]
k=1

cat=['lat','lon','oxy']

for j in range(0,len(oxygen),2):
    for i in range(0,len(oxygen[0]),2):
         lati.append(float(lats[j]))
         if lons[i] > 180:
             loni.append(float(lons[i])-360)
         else: 
             loni.append(float(lons[i]))
         meano2=round(float(np.mean(oxygen[1,10:15,j,i]*1E-3)),2)    
         oxy.append(meano2)
         
#hs=pd.Series(oxygen[1,:,:],index=lons[10])
hs2=pd.DataFrame({"lat":lati[:],"lon":loni[:],"o2":oxy[:]})
hs2=hs2.fillna(999)
#hs2.reset_index().to_json(orient='records',path_or_buf=folder+'bia_o2.json')
#hs2.to_csv(folder+'woa2005_surface_oxygen_full.csv')        
np.savetxt(r'/Users/Jorge/Sites/exp_eppley.dat', hs2.values, fmt='%d')

