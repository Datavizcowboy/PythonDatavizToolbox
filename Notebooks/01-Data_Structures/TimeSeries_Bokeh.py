""" Import Modules """

from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as pl
from bokeh.io import output_file, show
from bokeh.plotting import figure
#from bokeh.plotting import figure, output_file, show, HBox, VBox

""" Read NetCDF   """
fh = Dataset('/Users/jmartinez/Documents/Projects/MTQ/Temperature/TAS/MON/tas_Amon_IPSL-CM5B-LR_historical_r1i1p1_185001-200512.nc','r')

#fh = Dataset('/Users/jorge/.spyder2/zoop/NATMIG_1m_20060101_20061231_grid_T_DFS5.compress.nc', 'r')
lons = fh.variables['lon'][:]
lats = fh.variables['lat'][:]
#zdepmig = fh.variables['zdepmig'][:,:,:]
pp = fh.variables['tas'][:,:,:]
fh.close()

""" Monthly ticks  """

my_xticks = ['Jan','Feb','Mar','Apr','May','Jun','July','Aug','Sep','Oct','Nov','Dec']

""" Calculate the time series for total PP """

maxt=len(pp)
maxx=len(pp[0])
maxy=len(pp[0][0])

budget = []
months=maxt

for i in range(0,months,12):
    budget.append(np.mean(pp[i,:,:]))

x=range(0,months,12)
y=budget 

""" Python Plot   """

pl.plot(x,y)
#pl.xticks(x, my_xticks)
maxx=len(budget)
pl.xlim((1,maxx))
pl.show()

print (budget)

""" Bokeh Plot """

output_file("PP_Time_series.html",title='PP_time_series')
p1 = figure(title="Total PP", x_axis_label='month', x_range=list(my_xticks), y_axis_label='PP',plot_width=800, plot_height=400)
p1.line(x,y,size=12, color="red", alpha=0.5)
show(p1)