#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 14:56:43 2023

@author: jorge
"""
import matplotlib.pyplot as plt
import numpy as np
import re

# Path where the .csv file is stored
path = '/Users/jorge/Documents/Projects/Cowboy/Argentina/'

# Define empty arrays to store the data
xco2=[]
y=[]

# Name of the .csv file on the path
fronts = path + 'co2_brw_surface_1980_2005_replace.txt'

# Open the .csv file
fp = open(fronts, 'r')  

# We now read every single line of the .csv
# The [1:] skips the first line with the variable names
for g in fp.readlines():
    
    # We delete every space to keep only the values
    model_name=g.strip()
    
    model_replaced = re.sub('[^A-Za-z0-9 .]+', "", model_name)
    # We split every line by the commas, generating an array of elements
    data=model_replaced.split(' ')

    # We assign each element of the data array to our pre-defined arrays
    xco2.append(float(data[7]))
    y.append(float(data[8]))
    
fp.close()

""" CREATE THE PLOT """
fig, ax = plt.subplots(1,1)
ax.scatter(xco2,y)
# ax.grid(linestyle='dotted',linewidth=.2, alpha=0.8)    
# ax.set_xlabel('X values', fontsize=12,linespacing=4.2)
# ax.set_ylabel('Y values', fontsize=12)
# pl.title('Scatter Plot')
plt.show() 
