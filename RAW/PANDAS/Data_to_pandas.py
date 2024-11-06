# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 11:56:22 2016
@author: jorge
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

folder='/Users/jmartinez/Sites/TrueKMeans/'
path = '/Users/jmartinez/Desktop/FarFetch/'

""" Variables """

WeekNumberbyYear =[]
TrafficSourceType=[]
VisitorType=[]
NonBounceVisit=[]
Device=[]
HomePageWasVisited =[]
ProductPageWasVisited	=[]
VisitToProductAfterListing	=[]
SiteSearchWasUsed	=[]
VisitWithAddtoBag	=[]
VisitWithAddtoWishlist	=[]
ShippingAddressWasVisited	=[]
PaymentPageWasVisited	=[]
ReviewOrderPageWasVisited	=[]
ConfirmationPageWasVisited	=[]
Visits=[]
Visits2016=[]
Visits2017=[]
Revenue=[]
Orders=[]
Quarter=[]
ToBag=[]
ToSee=[]
ToConfirm=[]
ToPay=[]

partial = pd.DataFrame()

""" Read the file """

fq=open(path+'farfetch.txt','r')
    
for g in fq.readlines():
        model_name=g.strip()
        data=model_name.split('\r')
        
fq.close()

for ii in range(0,len(data)):
        subdata=data[ii].split('\t')
        
        quarterind=np.float(subdata[0][-2:])
        yearind=np.float(subdata[0][:-3])
        
        if (yearind == 2016):
            
            if (quarterind < 5):
                Visits2016.append(np.float(subdata[-3]))
            
            if (quarterind < 13):
                Quarter.append(1)
            elif (quarterind > 12 and quarterind < 25):
                Quarter.append(2)
            elif (quarterind > 24 and quarterind < 37):
                Quarter.append(3)
            else: 
                Quarter.append(4)
                
            Visits.append(np.float(subdata[-3]))
            Revenue.append(np.float(subdata[-2]))
            Orders.append(np.float(subdata[-1]))
            
            if (subdata[3] == 'New'):
                VisitorType.append(np.float(0))
            else:
                VisitorType.append(np.float(1))
                
            if (subdata[10] == 'Yes'):
                VisitWithAddtoWishlist.append(np.float(1))
            else:
                VisitWithAddtoWishlist.append(np.float(0))
                
            if (subdata[2] == 'Mobile'):
                Device.append(np.float(1))
            else:
                Device.append(np.float(0))
                
            if (subdata[5] == 'Yes' and subdata[8] == 'Yes'):
                ToBag.append(np.float(1))
                ToSee.append(np.float(1))
            elif (subdata[5] == 'Yes' and subdata[8] == 'No'):
                ToBag.append(np.float(0))
                ToSee.append(np.float(1))   
            else:
                ToBag.append(np.float(0))
                ToSee.append(np.float(0))
                
                
            if (subdata[11] == 'Yes' and subdata[13] == 'Yes'):
                ToConfirm.append(np.float(1))
                ToPay.append(np.float(1))
            elif (subdata[11] == 'Yes' and subdata[13] == 'No'):
                ToConfirm.append(np.float(0))
                ToPay.append(np.float(1))   
            else:
                ToConfirm.append(np.float(0))
                ToPay.append(np.float(0))
        else: 
             Visits2017.append(np.float(subdata[-3]))
            
                
mypanda=pd.DataFrame({"vis":Visits,"rev":Revenue,"ord":Orders, "qua":Quarter,
                      "ret":VisitorType, "wish":VisitWithAddtoWishlist,
                      "tobag": ToBag, "tosee": ToSee, 
                      "toconf": ToConfirm, "topay": ToPay,
                      "dev": Device})  
#    mypanda.reset_index().to_json(orient='records',path_or_buf=folder+str(qdata)+'_dataset'+'.json')

""" REVENUE """
#total_revenue=mypanda['date_index'].loc[content['mention']=='Wagestream'].sum()
total_revenue=mypanda['rev'].sum()
total_revenue_q1=mypanda['rev'].loc[mypanda['qua']==1].sum()
total_revenue_q2=mypanda['rev'].loc[mypanda['qua']==2].sum()
total_revenue_q3=mypanda['rev'].loc[mypanda['qua']==3].sum()
total_revenue_q4=mypanda['rev'].loc[mypanda['qua']==4].sum()
total = total_revenue_q1 +total_revenue_q2+total_revenue_q3+total_revenue_q4

""" ORDERS """

total_orders=mypanda['ord'].sum()
total_orders_q1=mypanda['ord'].loc[mypanda['qua']==1].sum()
total_orders_q2=mypanda['ord'].loc[mypanda['qua']==2].sum()
total_orders_q3=mypanda['ord'].loc[mypanda['qua']==3].sum()
total_orders_q4=mypanda['ord'].loc[mypanda['qua']==4].sum()

""" VISITORS """

total_visitors=mypanda['vis'].sum()
total_visitors_q1=mypanda['vis'].loc[mypanda['qua']==1].sum()
total_visitors_q2=mypanda['vis'].loc[mypanda['qua']==2].sum()
total_visitors_q3=mypanda['vis'].loc[mypanda['qua']==3].sum()
total_visitors_q4=mypanda['vis'].loc[mypanda['qua']==4].sum()

""" CONVERSION RATE """

conversion_rate = total_orders / total_visitors
conversion_rate_q1 = total_orders_q1 / total_visitors_q1
conversion_rate_q2 = total_orders_q2 / total_visitors_q2
conversion_rate_q3 = total_orders_q3 / total_visitors_q3
conversion_rate_q4 = total_orders_q4 / total_visitors_q4

""" AOV """

aov = total_revenue / total_orders
aov_q1 = total_revenue_q1 / total_orders_q1
aov_q2 = total_revenue_q2 / total_orders_q2
aov_q3 = total_revenue_q3 / total_orders_q3
aov_q4 = total_revenue_q4 / total_orders_q4

""" RETURNING """

ret_single = mypanda['ret'].sum()
ret_single_q1 = mypanda['ret'].loc[mypanda['qua']==1].sum()
ret_single_q2 = mypanda['ret'].loc[mypanda['qua']==2].sum()
ret_single_q3 = mypanda['ret'].loc[mypanda['qua']==3].sum()
ret_single_q4 = mypanda['ret'].loc[mypanda['qua']==4].sum()

returning = mypanda['vis'].loc[mypanda['ret']==1].sum()
returning_q1 = mypanda['vis'].loc[mypanda['ret']==1].loc[mypanda['qua']==1].sum()
returning_q2 = mypanda['vis'].loc[mypanda['ret']==1].loc[mypanda['qua']==2].sum()
returning_q3 = mypanda['vis'].loc[mypanda['ret']==1].loc[mypanda['qua']==3].sum()
returning_q4 = mypanda['vis'].loc[mypanda['ret']==1].loc[mypanda['qua']==4].sum()

returning_rate = returning / total_visitors
returning_rate_q1 = returning_q1 / total_visitors_q1
returning_rate_q2 = returning_q2 / total_visitors_q2
returning_rate_q3 = returning_q3 / total_visitors_q3
returning_rate_q4 = returning_q4 / total_visitors_q4

""" WISHLIST """

wish = mypanda['wish'].sum()
wish_q1 = mypanda['wish'].loc[mypanda['qua']==1].sum()
wish_q2 = mypanda['wish'].loc[mypanda['qua']==2].sum()
wish_q3 = mypanda['wish'].loc[mypanda['qua']==3].sum()
wish_q4 = mypanda['wish'].loc[mypanda['qua']==4].sum()

wish_rate = wish / ret_single
wish_rate_q1 = wish_q1 / ret_single_q1
wish_rate_q2 = wish_q2 / ret_single_q2
wish_rate_q3 = wish_q3 / ret_single_q3
wish_rate_q4 = wish_q4 / ret_single_q4

""" ToBag and ToSee """
fullbag = mypanda['tobag'].sum()
fullbag_q1 = mypanda['tobag'].loc[mypanda['qua']==1].sum()
fullbag_q2 = mypanda['tobag'].loc[mypanda['qua']==2].sum()
fullbag_q3 = mypanda['tobag'].loc[mypanda['qua']==3].sum()
fullbag_q4 = mypanda['tobag'].loc[mypanda['qua']==4].sum()

fullsee = mypanda['tosee'].sum()
fullsee_q1 = mypanda['tosee'].loc[mypanda['qua']==1].sum()
fullsee_q2 = mypanda['tosee'].loc[mypanda['qua']==2].sum()
fullsee_q3 = mypanda['tosee'].loc[mypanda['qua']==3].sum()
fullsee_q4 = mypanda['tosee'].loc[mypanda['qua']==4].sum()

""" ToPay and ToConfirm """

fullconf = mypanda['toconf'].sum()
fullconf_q1 = mypanda['toconf'].loc[mypanda['qua']==1].sum()
fullconf_q2 = mypanda['toconf'].loc[mypanda['qua']==2].sum()
fullconf_q3 = mypanda['toconf'].loc[mypanda['qua']==3].sum()
fullconf_q4 = mypanda['toconf'].loc[mypanda['qua']==4].sum()

fullpay = mypanda['topay'].sum()
fullpay_q1 = mypanda['topay'].loc[mypanda['qua']==1].sum()
fullpay_q2 = mypanda['topay'].loc[mypanda['qua']==2].sum()
fullpay_q3 = mypanda['topay'].loc[mypanda['qua']==3].sum()
fullpay_q4 = mypanda['topay'].loc[mypanda['qua']==4].sum()

""" PLOT """

mypositive=mypanda.loc[mypanda['rev']>0]
#
hist, bins = np.histogram(mypositive['ord'], bins=160)
width = 0.9 * (bins[1] - bins[0])
center = (bins[:-1] + bins[1:]) / 2

fig, ax = plt.subplots(1,1)

plt.bar(center, hist, align='center', width=width)
plt.yscale('log')
#plt.xscale('log')

ax.set_title("Histogram - Orders",fontsize=16,loc='right')
ax.set_xlabel('Orders')
ax.set_ylabel('Number of occurrences (log scale)')
plt.show()

smallbuyers = mypanda['rev'].loc[mypanda['ord']<10].sum()
mediumbuyers = mypanda['rev'].loc[(mypanda['ord']>10) & (mypanda['ord']<100)].sum()

smallbuyersave = mypanda['rev'].loc[mypanda['ord']<10].mean()
mediumbuyersave = mypanda['rev'].loc[(mypanda['ord']>10) & (mypanda['ord']<100)].mean()

""" MOBILE ANALYSIS """

total_orders_mob=mypanda['ord'].loc[mypanda['dev']==1].sum()
total_visitors_mob=mypanda['vis'].loc[mypanda['dev']==1].sum()
conversion_rate_mob= total_orders_mob / total_visitors_mob

total_orders_other=mypanda['ord'].loc[mypanda['dev']==0].sum()
total_visitors_other=mypanda['vis'].loc[mypanda['dev']==0].sum()
conversion_rate_other= total_orders_other / total_visitors_other

fullbag_mob = mypanda['tobag'].loc[mypanda['dev']==1].sum()
fullsee_mob = mypanda['tosee'].loc[mypanda['dev']==1].sum()
fullconf_mob = mypanda['toconf'].loc[mypanda['dev']==1].sum()
fullpay_mob = mypanda['topay'].loc[mypanda['dev']==1].sum()

fullbag_other = mypanda['tobag'].loc[mypanda['dev']==0].sum()
fullsee_other = mypanda['tosee'].loc[mypanda['dev']==0].sum()
fullconf_other = mypanda['toconf'].loc[mypanda['dev']==0].sum()
fullpay_other = mypanda['topay'].loc[mypanda['dev']==0].sum()



#mypanda.plot.scatter(y='ord',x='vis', c='dev',colormap='viridis')


""" OUTPUT """
print("Total_Revenue: "+str(total_revenue))
print("Total_Revenue_Q1: "+str(total_revenue_q1))
print("Total_Revenue_Q2: "+str(total_revenue_q2))
print("Total_Revenue_Q3: "+str(total_revenue_q3))
print("Total_Revenue_Q4: "+str(total_revenue_q4))
print("Total_Orders: "+str(total_orders))