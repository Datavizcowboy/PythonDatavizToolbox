""" Import Modules """

from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as pl
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

""" Read NetCDF   """

fh = Dataset('/Users/jorge/Documents/Projects/Topo/Experiment_CM62-ESMCO2-pi-06.3-spinup-prod_diag_CO2_cdo_monmean_1898-1907_zonmean.nc', 'r')
pp= fh.variables['CO2'][:,:,:,:]
fh.close()

""" Python Plot """

X=pp[1,2,:,0].reshape(-1, 1)
Y=pp[2,2,:,0].reshape(-1, 1)

linear_regressor = LinearRegression()  # create object for the class
linear_regressor.fit(X, Y)  # perform linear regression
Y_pred = linear_regressor.predict(X)  # make predictions
rtwo = r2_score(X,Y)

pl.plot(X, Y_pred, color='red')
pl.scatter(X,Y)

pl.title('r2 = '+str(rtwo))
pl.show()