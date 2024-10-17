# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 11:56:22 2016
@author: jorge
"""

import pandas as pd
import numpy as np
import csv
import json

data = '/Users/jorge/Documents/Projects/Cowboy/Argentina/'
folder='/Users/jorge/Sites/Argentina/'

p=1

ident=[]
lat=[]
lon=[]
unidad=[]
embarc=[]
pesc=[]
capt=[]

fronts = data+'UDP_Argentina.csv'

fp = open(fronts, 'r')  

for g in fp.readlines()[1:]:
    model_name=g.strip()
    data=model_name.split(';')

    ident.append(data[1])
    lat.append(data[2])
    lon.append(data[3])
    unidad.append(data[5])
    embarc.append(data[7])
    pesc.append(data[10])
    capt.append(data[12])
    
fp.close()

mypanda=pd.DataFrame({"id":ident,"lat":lat[:],"lon":lon[:],"uni":unidad[:],"emb":embarc[:],"pesc":pesc,"capt":capt})  

myboat= mypanda.drop(mypanda[mypanda.emb == 'NA'].index)
myboat= myboat.drop(myboat[myboat.emb == 'ND'].index)
mypesc=mypanda.drop(mypanda[mypanda.pesc == 'ND'].index)
mycapt=mypanda.drop(mypanda[mypanda.capt == 'ND'].index)

""" DICTIONARY """

mycapt["capt"] = pd.to_numeric(mycapt["capt"])
mycapt["pesc"] = pd.to_numeric(mycapt["pesc"])
mycapt["lat"] = pd.to_numeric(mycapt["lat"])
mycapt["lon"] = pd.to_numeric(mycapt["lon"])



capturas = mycapt[["capt"]].values
unidades = mycapt[["id"]].values
embarcaciones = mycapt[["emb"]].values

tuple_list = []
for i in range(0,len(capturas)):
    if (pesc[i][0] != 'N'):
        tuple_list.append([np.float(pesc[i]),unidades[i][0],capturas[i][0]])

my_dict = [dict(zip(("click_count", "name", "size"), x)) for x in tuple_list]

o_dict = {
 "name": "flare",
 "children": [
  {
   "name": "there",
   "children": [
    {
     "name": "industry",
        "children":my_dict
        }]}]}

with open(folder+"capt_dict.json", "w") as f:
    json.dump(o_dict, f)

# features = []
# features.append(
#     Feature(
#         geometry = MultiPolygon([[data]]),
#         properties = {
#             'weather': 0,
#             'temp': 0
#         }
#     )
# )

# mycapt = mycapt.sort_values("capt", ascending=False)
mycapt = mycapt.sort_values("lat", ascending=False)
# myboat.reset_index().to_json(orient='records',path_or_buf=folder+'arg_embarcaciones.json')
# mypesc.reset_index().to_json(orient='records',path_or_buf=folder+'arg_pescadores.json')
mycapt.to_json(orient='records',path_or_buf=folder+'arg_capturas_lat.json')
                
                
                
    

