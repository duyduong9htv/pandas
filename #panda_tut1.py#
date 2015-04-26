# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 15:59:07 2013

Author: DD Tran

On n'a pas tous les jours 20 ans. 
Ca nous arrive une fois seulement 
"""

import pandas as pd
import numpy as np 


#check out 10 minutes to pandas: 

#http://pandas.pydata.org/pandas-docs/stable/10min.html 


#==============================================================================
# creating a data frame using pandas 
#==============================================================================
data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
'year': [2000, 2001, 2002, 2001, 2002],
'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
frame = pd.DataFrame(data)


df = pd.DataFrame(data, columns = ['state', 'year', 'pop'])

print df.columns
print df.index
print df.values 

#accessing data 

values = df.values
print values[0, 0]
print values[0, 1]

#==============================================================================
# a frame column can be retrieved just like in a dict 
#==============================================================================
print "printing out columns retrieved by pandas:" 
print "populations: "
print frame['pop']

print "states:" 
print frame['state']


#==============================================================================
# Indexing into a data frame 
#==============================================================================


data = pd.DataFrame(np.arange(16).reshape((4, 4)),
                 index=['Ohio', 'Colorado', 'Utah', 'New York'],
                 columns=['one', 'two', 'three', 'four'])
                 

print data['one']

print data['two']

print data.index




#==============================================================================
# Arithmetic and data alignment 
#==============================================================================
                
#Series alignment                 
s1 = pd.Series([7.3, -2.5, 3.4, 1.5], index=['a', 'c', 'd', 'e'])
s2 = pd.Series([-2.1, 3.6, -1.5, 4, 3.1], index=['a', 'c', 'e', 'f', 'g'])

s = s1 + s2
print s 


#Data frame alignment 



                
                 

#==============================================================================
# INDEX OBJECTS 
#==============================================================================


obj = pd.Series(range(3), index = ['a', 'b', 'c'])
index = obj.index

#slicing: 

print index[1:]

print index[-3:] #last 3 indices 


#when extracting indices, the index object (what is extracted) is immutable 

index[1] = 'f' #not allowed 



#==============================================================================
# CORRELATION AND COVARIANCE 
#==============================================================================


import pandas.io.data as web 

all_data = {}
for ticker in ['AAPL', 'IBM', 'MSFT', 'GOOG']:
    all_data[ticker] = web.get_data_yahoo(ticker, '1/1/2000', '1/1/2010')

price = pd.DataFrame({tic: data['Adj Close']
                        for tic, data in all_data.iteritems()})

volume = pd.DataFrame({tic: data['Adj Close']
                        for tic, data in all_data.items()})          
                        

returns = price.pct_change()

                        