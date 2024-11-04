""" Import Modules """

from netCDF4 import Dataset
import numpy as np
import pylab as pl
from bokeh.plotting import figure, output_file, show, HBox, VBox

""" Read NetCDF   """

fh = Dataset('/Users/jorge/.spyder2/zoop/NATMIG_1m_20060101_20061231_grid_T_DFS5.compress.nc', 'r')
lons = fh.variables['nav_lon'][:]
lats = fh.variables['nav_lat'][:]
zdepmig = fh.variables['zdepmig'][:,:,:]
pp= fh.variables['PPPHY'][:,:,:,:]
fh.close()


""" Python Plot """

pl.clf()
phy1=pp[1,:,300,:]

pl.figure()
pl.pcolor(phy1)
maxx=len(pp[0][0][0])
maxy=len(pp[0])
pl.xlim((0,maxx))
pl.ylim((maxy,0))
pl.show()
pl.colorbar()

""" Bokeh Plot """

output_file("bo1_lines.html",title='ZOOP MIG')

p1 = figure(title="Cross Section", x_axis_label='x', y_axis_label='y',plot_width=400, plot_height=400, \
    x_range=[1,maxx], y_range=[maxy, 0])

p1.image(image=[phy1],x=[0], y=[maxy], dw=[maxx], dh=[maxy], palette='Spectral11')

show(p1)