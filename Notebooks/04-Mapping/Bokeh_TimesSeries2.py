""" Import Modules """

from netCDF4 import Dataset
import numpy as np
import pylab as pl
import matplotlib.pyplot as plt
from bokeh.plotting import figure, output_file, show

#HBox, VBox

""" Read the NetCDF """

#fh = Dataset('/Users/jorge/.spyder2/zoop/NATMIG_1m_20060101_20061231_grid_T_DFS5.compress.nc', 'r')
#lons = fh.variables['nav_lon'][:]
#lats = fh.variables['nav_lat'][:]
#zdepmig = fh.variables['zdepmig'][:,:,:]
#pp= fh.variables['PPPHY'][:,:,:,:]

fh = Dataset('/Users/jmartinez/Documents/Projects/OMZ/WOA_GRID/bianchi.nc','r')

lons = fh.variables['LONGITUDE'][:]
lats = fh.variables['LATITUDE'][:]
pp=fh.variables['O2_LINEAR'][:,:,:,:]
fh.close()

""" Python Plot """

#figure = plt.figure()
#ax = figure.add_subplot(111)
#contour = ax.contour(lonrange, latrange, Z, levels=numpy.linspace(start=0, stop=100, num=10), cmap=plt.cm.jet)


plt.clf()
plt.figure()
#pl.contourf(pp[1,1,:,:])
phy2d=pp[0,10,:,:]

plt.pcolor(phy2d)

maxx=len(pp[0][0][0])
maxy=len(pp[0][0])

#plt.set_xticks(np.arange(0,360), minor=False)
#plt.set_yticks(np.arange(-90,90), minor=False)

plt.xticks(np.arange(0,360,40))
plt.yticks(np.arange(-90,90,30))


plt.xlim((0,maxx))
plt.ylim((0,maxy))
plt.show()
#pl.colorbar()  

""" Bokeh Plot"""

output_file("bo1_lines.html",title='ZOOP MIG')

p1 = figure(title="MIG Fields", x_axis_label='x', y_axis_label='y',plot_width=400, plot_height=400, \
    x_range=[1,maxx], y_range=[0, maxy], tools = "pan,wheel_zoom,box_zoom,reset")

p1.image(image=[phy2d],x=[0], y=[0], dw=[maxx], dh=[maxy],palette="RdYlBu11")

show(p1)