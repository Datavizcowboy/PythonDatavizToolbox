#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 23:22:30 2021
@author: jorge
"""

import pandas as pd
import re
import numpy as np
# import nltk
# from nltk import everygrams
# nltk.download('punkt')
# from nltk import ngrams, FreqDist
from sklearn.feature_extraction.text import CountVectorizer
import warnings
warnings.filterwarnings("ignore")

folder='/Users/datavizcowboy/Sites/TRANSPARENC/DATA/'

""" ______________________________________ READ THE CSV FILE and STORE IDs """

therank = []
thefreq = []
theyear = []
themonth = []
theday = []
thearticles = []

keyword = 'satellites'

df = pd.read_csv('/Users/datavizcowboy/Documents/Fuel/TRANSPARENC/posts.csv')

# cleaning the data
df["content"] = df["content"].str.replace("\\n", " ")
df['content'].replace('', np.nan, inplace=True)
df['content'].replace(' ', np.nan, inplace=True)
df['content'].replace('       ', np.nan, inplace=True)
df.drop(['author', 'title'], axis = 1, inplace =True)
# df.dropna(subset=['authors'], inplace=True)
# df['bref']=df['date'].apply(lambda x: x[0:4])

for nn in range(2005,2023):
  for mm in range(1,13):
    dsliced = df.loc[df['year'] == nn]
    dslicer = dsliced.loc[df['month'] == mm]
    print(str(nn)+"_"+str(mm)) 
    # a = dslice['content'].str.lower().str.cat(sep=' ')
    if (dslicer.content.any() == True):
        
        word_vectorizer = CountVectorizer(ngram_range=(1,2), analyzer='word')
        sparse_matrix = word_vectorizer.fit_transform(dslicer['content'].values.astype('U'))
        frequencies = sum(sparse_matrix).toarray()[0]
        
        output = pd.DataFrame(frequencies, index=word_vectorizer.get_feature_names(), columns=['frequency'])
        output = output.sort_values('frequency', ascending=False)
        output['rank'] = range(1, len(output) + 1)
        output['body'] = output.index
        output.index = output['rank'] 
        
        thenumber = output[output['body'].str.contains(r'(?:\s|^)'+keyword+'(?:\s|$)',flags=re.IGNORECASE)]
    
        if (len(thenumber)>0):
            position = thenumber.iloc[[0]]    
            therank.append(thenumber.iloc[[0]].index[0].tolist())
            thefreq.append(thenumber['frequency'].values[0].tolist())
            theyear.append(nn)
            themonth.append(mm)
            thearticles.append(dslicer.size)
        else:
            therank.append(0)
            thefreq.append(0)
            theyear.append(nn)
            themonth.append(mm)
            thearticles.append(dsliced.size)
        
mypanda=pd.DataFrame({"year":theyear,"month":themonth, "rank":therank, "freq":thefreq, "articles":thearticles})  
mypanda['allfreq'] = mypanda['freq'].cumsum()
mypanda.reset_index().to_json(orient='records',path_or_buf=folder+'TechCrunch2years_Satellites.json')
