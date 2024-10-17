""" Import Modules """

from netCDF4 import Dataset
import numpy as np
import pylab as pl
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt


# lon_0 is central longitude of projection.
# resolution = 'c' means use crude resolution coastlines.

""" Read the NetCDF """

fh = Dataset('/Users/jmartinez/Documents/Projects/OMZ/WOA_GRID/GF2G_o_h.nc','r')
pp=fh.variables['o2'][:,:,:,:]

fh.close()

""" Python Plot"""

m = Basemap(projection='robin',lon_0=0,resolution='c')
m.drawcoastlines()
m.fillcontinents(color='coral',lake_color='aqua')
# draw parallels and meridians.
m.drawparallels(np.arange(-90.,120.,30.))
m.drawmeridians(np.arange(0.,360.,60.))
m.drawmapboundary(fill_color='aqua')
plt.title("Robinson Projection")
plt.show()




#
#pl.clf()
#
#pl.figure()
##pl.contourf(pp[1,1,:,:])
#phy2d=pp[0,10,:,:]
#pl.pcolor(phy2d)
#maxx=len(pp[0][0][0])
#maxy=len(pp[0][0])
#pl.xlim((0,maxx))
#pl.ylim((0,maxy))
#pl.show()
#pl.colorbar()  

