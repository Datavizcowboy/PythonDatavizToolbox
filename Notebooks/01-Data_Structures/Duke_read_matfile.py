#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 17:33:53 2017

@author: Jorge
"""

thefile = '/Users/jmartinez/Documents/Projects/DUKE/N2_FIX/N2_fixation_model_outputs.mat'

import numpy as np
import scipy.io
import pandas as pd
from netCDF4 import Dataset

mat = scipy.io.loadmat(thefile)
#data=np.array(mat)
data_0 = mat['CNRM_CM5']

container=[]

list_names=['CNRM_CM5','GFDL_ESM2M','CanESM2','MPI_ESM_LR','CESM1_BGC',
            'IPSL_CM5A_LR','Paulsen_2017','Landolfi_2015','Jickells_2017',
            'UvicESCM','Luo_2014']

for ll in range(0,len(list_names)):
    container.append(mat[list_names[ll]])


highsouth=[]
equator=[]
highnorth=[]

for ii in range(0,len(list_names)):
    highsouth.append(np.nansum(container[ii][0:30]))
    equator.append(np.nansum(container[ii][31:60]))
    highnorth.append(np.nansum(container[ii][61:90]))



""" Create de NetCDF File """

#root_grp = Dataset('/Users/jmartinez/Documents/Projects/DUKE/N2_FIX/py_netcdf4.nc', 'w', format='NETCDF4')
#root_grp.description = 'Example simulation data'
#
##ndim = 900 # Size of the matrix ndim*ndim
#xdimension = 0.75
#ydimension = 0.75
## dimensions
##root_grp.createDimension('time', None)
#root_grp.createDimension('x', 180)
#root_grp.createDimension('y', 90)
#
## variables
##time = root_grp.createVariable('time', 'f8', ('time',))
#x = root_grp.createVariable('x', 'f4', ('x',))
#y = root_grp.createVariable('y', 'f4', ('y',))
#field = root_grp.createVariable('field', 'f8', ('x', 'y',))
#
## data
#x_range =  np.linspace(89, -89, 90)
#y_range =  np.linspace(-179, 179, 180)
#
##y_range =  np.linspace(0, ydimension, ndim)
#
#x[:] = x_range
#y[:] = y_range
#for i in range(5):
##    time[i] = i*50.0
#    field[i,:,:] = np.random.uniform(size=(len(x_range), len(y_range)))
#
#root_grp.close()


