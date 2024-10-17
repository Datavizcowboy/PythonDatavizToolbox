# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 11:56:22 2016

@author: jorge
"""

import netCDF4
import numpy as np

#nc = netCDF4.Dataset('/Users/jmartinez/Documents/Projects/Acidoscope/pH/pH_Omon_CESM1-BGC_historical_r1i1p1_1850-2005a.nc')

nc = netCDF4.Dataset('/Users/jmartinez/Documents/Projects/Acidoscope/pH/all_together.nc')

lons = nc.variables['longitude'][:]
lats = nc.variables['latitude'][:]
oxygen = nc.variables['pH'][:,:,:]

lati=[]
loni=[]
oxy=[]
k=1

cat=['lat','lon','oxy']
#for i in range(0,len(oxygen[0][0][0]),1):
for j in range(len(oxygen[0])-1,0,-1):
    #for j in range(len(oxygen[0][0]),0,1):
    for i in range(212,len(oxygen[0][0]),1):
         oxy.append(oxygen[150,j,i])
   
#for j in range(len(oxygen[0][0])-1,0,-1):       
    for i in range(0,212,1):
         oxy.append(oxygen[150,j,i])
   
oxy[-1]=9
    
preoxy=np.log(oxy)      
foxy=np.array(oxy)
doxy=foxy.astype(np.float32).tobytes()
#np.save('/Users/jmartinez/Sites/Acidoscope/DATA_2/Data_Proto/ALL_PH.dat', doxy)