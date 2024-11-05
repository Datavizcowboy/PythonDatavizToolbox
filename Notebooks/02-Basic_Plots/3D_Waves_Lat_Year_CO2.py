# -*- coding: utf-8 -*-
"""
Patricia Cadule
IPSL Climate Center
"""
#from netCDF4 import Dataset, num2date
""" Libraries"""

from mpl_toolkits.mplot3d import Axes3D

import numpy as np
import pandas as pd
from netCDF4 import Dataset
import matplotlib.pyplot as pl
import matplotlib.ticker as ticker
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from matplotlib import cm
import calendar as cd
from scipy.interpolate import griddata

""" Paths """
root_begin='/Users/jorge/Documents/Projects/Topo/'
folder = '/Users/jorge/Desktop/'
    
""" CO2 PPM """
ncfile3 = Dataset(root_begin+'Experiment_CM62-ESMCO2-pi-06.3-spinup-prod_diag_CO2_cdo_monmean_1898-1907_zonmean.nc','r')
co2 = ncfile3.variables['CO2'][:,:,:]
lat = ncfile3.variables['lat'][:]
year = ncfile3.variables['time_counter'][:]

""" Make the data """

Xb = lat.data 
# X = Xpre[::-1]
# Y = year.data
Yb = np.arange(0,120,1)
Zpre = np.squeeze(co2.data, axis=(3,))
Zvor = Zpre[:,0,:]*1E6*29./44


Z =  np.ma.average(Zvor, axis=0) 
                   # weights=[1, 1], returned=True)

#number of data points per axis
# n = 20
# #upsample evenly along x and y axis
# x_up = np.linspace(np.min(Xb), np.max(Xb), n)
# y_up = np.linspace(np.min(Yb), np.max(Yb), n)

# x3d, y3d = np.meshgrid(x_up, y_up)

X, Y = np.meshgrid(Xb,Yb)

# z3d = griddata((Xb, Yb), Zpost, (x3d, y3d), method = "cubic")

""" Plot """
pl.rcParams['font.family'] = "Arial"
pl.rcParams['font.size'] = "10"
                
fig = pl.figure(figsize=pl.figaspect(0.5)*2.5)
ax = fig.add_subplot(111, projection='3d')

surf = ax.plot_surface(X,Y,Z, cmap=cm.rainbow, linewidth=1, antialiased=False)

ax.zaxis.set_major_locator(LinearLocator(0))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

ax.azim = -40
ax.elev = 65

x_scale=1.5
y_scale=3.0
z_scale=3.0

scale=np.diag([x_scale, y_scale, z_scale, 1.0])
scale=scale*(1.0/scale.max())
scale[3,3]=1.0

def short_proj():
  return np.dot(Axes3D.get_proj(ax), scale)

ax.get_proj=short_proj

ax.grid(False)
 
xLabel = ax.set_xlabel('\nLatitude', linespacing=2.2, fontsize="20")
yLabel = ax.set_ylabel('\nMonth ', linespacing=2.1, fontsize="20")
zLabel = ax.set_zlabel('\nCO2 (ppm)', linespacing=-3,rotation=90, fontsize="14")

ax.get_zaxis().set_visible(False)

ax.w_zaxis.pane.fill = False
ax.w_xaxis.pane.fill = False
ax.w_yaxis.pane.fill = False

ax.w_zaxis.set_pane_color((0.0, 0.0, 0.0, 0.0))
                
# ax.set_box_aspect((1, 2, 1)) 
# ax.pbaspect = [1.0, 1.0, 2.25] 
# ax.axhline(0, color='black',alpha=.5,linewidth=.75)
# ax.legend(fontsize=9,frameon=False,loc="upper left", bbox_to_anchor=(.01,.99))
# ax.minorticks_on()
# ax.xaxis.set_minor_locator(ticker.AutoMinorLocator(5))
# ax.grid(linestyle='dotted',linewidth=.2, alpha=0.8)    
# ax.set_xlabel('Year', fontsize=16,linespacing=4.2)
# ax.set_ylabel('GPP (PgC/yr)', fontsize=14)
# ax.set_xlim(1850,2015)
# ax.set_ylim(90,130)
fig.colorbar(surf, shrink=0.5, aspect=5)
ax.set_xlim3d(90, -90)
ax.set_ylim3d(0,120)
ax.set_zlim3d(278,290)

pl.savefig("/Users/jorge/Desktop/3D_plot_wave_v0.pdf", dpi=300, bbox_inches='tight')
pl.show()
