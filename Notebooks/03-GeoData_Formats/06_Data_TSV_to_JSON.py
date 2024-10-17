# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 11:56:22 2016
@author: jorge
"""

import pandas as pd
import numpy as np
import csv

data = '/Users/datavizcowboy/Documents/Fuel/ANTICIPA/'
folder='/Users/datavizcowboy/Sites/MITIGA/Anticipa/'

fronts = data+'Anticipa_Data.tsv'

fp = open(fronts, 'r')  

lat=[]
lon=[]
resta24=[]
resta30=[]
street=[]
pobox=[]
town=[]

for g in fp.readlines()[1:]:

    model_name=g.strip()
    data=model_name.split('\t') 
    #dataf=[s.replace(',', '') for s in datas]
    #data=[s.replace('"', '') for s in dataf]
 
    lon.append(data[0])
    lat.append(data[1])
    resta24.append(data[11])
    resta30.append(data[12])
    street.append(data[2])
    pobox.append(data[3])
    town.append(data[4])
   
    resta24=[float(i) for i in resta24] 
    resta30=[float(i) for i in resta30] 
    
fp.close()

mypanda=pd.DataFrame({"lon":lon[:],"lat":lat[:],"street":street[:],"pobox":pobox[:],"town":town[:],"resta24":resta24[:],"resta30":resta30[:]})  
#mypanda=mypanda.iloc[::-1]
mypanda['per'] = (mypanda['resta30'] / mypanda['resta24'])*100-100
mypanda_per = mypanda.sort_values(by='per',ascending=False)
mypanda_per = mypanda_per.reset_index(drop=True)

mypanda_per = mypanda_per[mypanda_per.town != '"Rozas De Madrid, Las"']
mypanda_per = mypanda_per[mypanda_per.town != '"Boalo, El"']

mypanda_per_fuen=mypanda_per.loc[mypanda_per['town'] == 'Fuenlabrada']
mypanda_per.reset_index().to_json(orient='records',path_or_buf=folder+'DATA/Resta_data.json')
mypanda_per_fuen = mypanda_per_fuen.reset_index(drop=True)
mypanda_per_fuen.reset_index().to_json(orient='records',path_or_buf=folder+'DATA/Resta_data_fuen.json')
 
