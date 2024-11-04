# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 17:27:29 2015
@author: GraphicPrototype
Jorge Martinez Rey

"""

from netCDF4 import Dataset, num2date
import time, calendar, datetime, numpy
import numpy as np
import numpy.ma as ma
import matplotlib.pyplot as pl
#from mpl_toolkits.basemap import Basemap
import urllib, os
import json
import random
import pandas as pd


name=[]
multikeys=[]
multinames=[]
multiall=[]
dummy=[]
k=1

""" Read .TXT file   """
dictionary={}
nom=['indi']
cat=['lat','lon','area']
m=1
     
fp = open('/Users/Jorge/Documents/Projects/ICEBERGS/icebergs_python.txt','r') 
for i in fp.readlines():
    ipdata = i.split()
    name=[m]    
    dn=dict(zip(nom,name))
    multinames.append(dn)
    m=m+1
fp.close()   
     
fp = open('/Users/Jorge/Documents/Projects/ICEBERGS/icebergs_python.txt','r') 
for i in fp.readlines():
    sdata = i.strip()
    ndata = sdata.split()
    for s in range(0,len(ndata)):
       ndata[s]=float(ndata[s])
    dictionary = dict(zip(cat,ndata))
#    dictionary = dn.update(pictionary)    
    multikeys.append(dictionary)
    k=k+1    
    if k == 6913 :
        break
fp.close()

for k in range(0,6912):
    multikeys[k].update(multinames[k])
    dummy=multikeys[k]    
    multiall.append(dummy)

    
#hs2=pd.DataFrame({"lat":lati[:],"lon":loni[:],"o2":oxy[:]})
#hs2=hs2.fillna(999)
#hs2.reset_index().to_json(orient='records',path_or_buf=folder+'bia_o2.json')    
    
    
j=json.dumps(multiall, indent=4)
f=open("data_iceberg_sonntag.json","w")
f.write(j)
f.close()












































