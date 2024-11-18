""" Import Modules """


import numpy as np
import matplotlib.pyplot as pl
from bokeh.io import output_file, show
from bokeh.plotting import figure
import pandas as pd
from bokeh.palettes import Spectral11
#from bokeh.plotting import figure, output_file, show, HBox, VBox

""" Read DAta   """

sdata=[]
counter=[]
alldata=[]

path = '/Users/jmartinez/Documents/Projects/MTQ/DAILY/STA/'
folder='/Users/jmartinez/Sites/MGClimDeX/Dev_1/'
 
fronts=path+'All_Stations_short.txt'

fq = open(fronts, 'r')  
for g in fq.readlines():
    model_name=g.strip()

    station = path+str(model_name)
 
    fp = open(station, 'r')  
    k=0
    for g in fp.readlines():
        model_name=g.strip()
        data=model_name.split('\t')
        if (data[1] != '-999'):
            sdata.append(data[1])
        else:
            sdata.append(float('nan'))
        counter.append(k)
        k=k+1
    fp.close()
    
    alldata.append(sdata)
    sdata=[]
    counter=[]

fq.close()

toy_df=pd.DataFrame(data={"tas":alldata[0][::20],"tas1":alldata[1][::20]})  

toy_df2 = pd.DataFrame(data=np.random.rand(5,3), columns = ('a', 'b' ,'c'), index = pd.DatetimeIndex(start='01-01-2015',periods=5, freq='d'))   

#ssdata=np.ma.masked_where(sdata == '-999', sdata)

""" Bokeh Plot """

numlines=len(toy_df.columns)
mypalette=Spectral11[0:numlines]
#
##p = figure(width=500, height=300, x_axis_type="datetime") 
p = figure(width=1000, height=600) 

p.multi_line(xs=[toy_df.index.values],
                ys=[toy_df[name].values for name in toy_df],
                line_color=mypalette,
                line_width=5)
show(p)

#output_file("TAS_Time_series.html",title='TAS_time_series')
#p1 = figure(title="TAS",plot_width=800, plot_height=400)
#p1.line(toy_df.index.values,toy_df['tas'].values)
#p2.line(toy_df.index.values,toy_df['tas1'].values)
#show(p1,p2)