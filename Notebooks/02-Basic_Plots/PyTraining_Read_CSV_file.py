#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 16:31:55 2023

@author: jorge
"""

import matplotlib.pyplot as plt
import numpy as np

# Path where the .csv file is storedy
path = '/Users/jorge/Documents/Projects/Cowboy/PyTraining/'

# Define empty arrays to store the data
day=[]
temperature=[]

# Name of the .csv file on the path
fronts = path + 'GlobalLandTemperaturesByMajorCity.csv'

# Open the .csv file
fp = open(fronts, 'r')  

# We now read every single line of the .csv
# The [1:] skips the first line with the variable names
for g in fp.readlines()[1:]:
    
    # We delete every space to keep only the values
    model_name=g.strip()
    
    # We split every line by the commas, generating an array of elements
    data=model_name.split(',')

    # We assign each element of the data array to our pre-defined arrays
    day.append(float(data[0]))
    temperature.append(float(data[1]))
    
fp.close()

""" CREATE THE PLOT """
fig, ax = plt.subplots(1,1)
ax.scatter(xco2,y)
# ax.grid(linestyle='dotted',linewidth=.2, alpha=0.8)    
# ax.set_xlabel('X values', fontsize=12,linespacing=4.2)
# ax.set_ylabel('Y values', fontsize=12)
# pl.title('Scatter Plot')
plt.show()