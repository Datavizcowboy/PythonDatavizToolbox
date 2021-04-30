""" Import Modules """

import numpy as np
import matplotlib.pyplot as pl
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

""" Data """

x= np.random.rand(10,1)
y= np.random.rand(10,1)

linear_regressor = LinearRegression()  # create object for the class
reg = linear_regressor.fit(x, y)  # perform linear regression
Y_pred = reg.predict(x)  # make predictions
r2_true = reg.score(x, y)

""" Plot """

pl.scatter(x,y)
pl.plot(x, Y_pred, color='red')
pl.show()
