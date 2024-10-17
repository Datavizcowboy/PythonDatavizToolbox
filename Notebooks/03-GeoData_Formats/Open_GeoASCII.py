.# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 11:56:22 2016
@author: jorge
"""

import numpy as np


data = '/Users/jmartinez/Documents/Projects/MTQ/PRECIS/hadcm_cntrl_baseline_1970s_prec_20min_sa_eta_asc/prec_12.asc'

ascii_grid = np.loadtxt(data, skiprows=6)


import linecache
line1 = linecache.getline(data, 1)