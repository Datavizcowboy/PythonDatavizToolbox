#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 10:44:35 2023

@author: jorge
"""

import pandas as pd
import numpy as np

folder = '/Users/jorge/Sites/Chile/DATA/'
data = '/Users/jorge/Documents/Projects/Cowboy/OroraTech/chile_fire_cluster_sequence_v2.json'

df = pd.read_json(data)

""" Remove columns we won't use """

df.drop(['id',
       'mir_bt', 'tir_bt', 'normalized_frp',
       'landuse_class', 'product_id', 'algorithm', 'mir_bt_avg',
       'tir_bt_avg', 'mir_threshold', 'tir_threshold', 'delta_bt_avg',
       'delta_bt_thr', 'hotspot_class'], axis=1, inplace=True)

""" Pick every 20th row """

neu = df.iloc[::20, :]

neu_GOES = neu.loc[df['satellite'] == 'GOES-16']


""" Save as JSON file """

neu_GOES.to_json(date_format='iso',orient='records',path_or_buf=folder+'chile_events_v2.json')

""" Save as CSV file for the Bubble Dataviz"""

# neu.to_csv(folder+'chile_events_conf.csv')

""" Some interesting Stats """

print(np.max(neu['frp']))
print(np.mean(neu['frp']))
print(np.min(neu['frp']))

a = neu['satellite'].unique()
print(sorted(a))

""" Count the number of events per satellite """

list_satellites = ['AQUA', 'GOES-16', 'LANDSAT-8', 'MetOp-B', 'MetOp-C', 'NOAA-20', 'SENTINEL-2A', 'SENTINEL-2B', 'SENTINEL-3A', 'SENTINEL-3B', 'SUOMI-NPP', 'TERRA']

for i in range(0,12):
    elem = neu.loc[df['satellite'] == list_satellites[i]].size/9
    print(str(list_satellites[i])+' '+str(elem))