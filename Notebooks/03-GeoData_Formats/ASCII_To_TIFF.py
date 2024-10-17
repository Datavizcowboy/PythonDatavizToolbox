s# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 11:56:22 2016
@author: jorge
"""

data = '/Users/jmartinez/Documents/Projects/MTQ/PRECIS/hadcm_cntrl_baseline_1970s_prec_20min_sa_eta_asc/prec_12.asc'

import os, subprocess

os.system("gdal_translate -of 'GTiff' /Users/jmartinez/Documents/Projects/MTQ/PRECIS/hadcm_cntrl_baseline_1970s_prec_20min_sa_eta_asc/prec_12.asc output.tiff")