""" Import Modules """

from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as pl
from bokeh.plotting import figure, output_file, show, HBox, VBox
import bokeh.server
import bokeh.server.start

""" Read NetCDF   """

#fh = Dataset('/Users/jorge/.spyder2/zoop/NATMIG_1m_20060101_20061231_grid_T_DFS5.compress.nc', 'r')
fh = Dataset('/Users/jorge/.spyder2/zoop/DRI_ptrc_2006.nc','r')
oxy=fh.variables['O2'][:,:,:,:]
fh.close()

""" Python Plot """

hist, bins = np.histogram(oxy*1E6, bins=np.linspace(0,400))
width = 0.7 * (bins[1] - bins[0])
center = (bins[:-1] + bins[1:]) / 2
pl.bar(center, hist, align='center', width=width)
pl.show()


""" Bokeh Plot  """

output_file("bo1_histo.html",title='ZOOP MIG')
#TOOLS = "resize,hover,save,pan,box_zoom,wheel_zoom"
TOOLS = "save"
p1 = figure(title="O2 histogram", x_axis_label='x', y_axis_label='y',plot_width=600, plot_height=400, \
   toolbar_location="left", tools=TOOLS, background_fill="white")
    
p1.quad(top=hist, bottom=0, left=bins[:-1], right=bins[1:],
     fill_color="#036564", line_color="#033649")
show(p1)