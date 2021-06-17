""" Import Modules """

import numpy as np
import matplotlib.pyplot as pl

""" Generate random numbers """

x= np.random.rand(10,1)
y= np.random.rand(10,1)

""" Plot """

pl.scatter(x,y)

pl.title('Scatter Plot')
pl.show()