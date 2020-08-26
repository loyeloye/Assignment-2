from typing import List

import pandas as pd
from pandas import Series
import numpy as np
object = Series ([5,10,15,25])
print (object)

print(object.values) #brings out the values, when doing
print(object.index) #stops before zero stops at 4  with increments of 1

#using numpy arrays to create series
data_array = np.array(['a','b','c'])
s = Series(data_array)
print(s)

#using custom indexs
s = Series(data_array, index=[100,101,102]) #this changes the index
print(s)
s = Series(data_array, index=['cars','boats','houses']) #strings can be used to replace integers
print(s)

#using real life examples

revenue = Series([20,80,40,35], index=['ola', 'uber', 'grab', 'gojek'])
print(revenue ['ola'])
print(revenue[revenue>=35]) #to get revenues greater than or equal to 35

#using boolean conditions
print ('lyft' in revenue) #in tells us in true or false if the string is in the revenue or not

revenue_dict = revenue.to_dict()# this shows this {'ola': 20, 'uber': 80, 'grab': 40, 'gojek': 35} its converting revenue to dict
#print(revenue_dict)

#nan values
index_2 = ['ola', 'uber', 'grab', 'gojek', 'lyft']
revenue2 = Series (revenue, index_2)
print(revenue2)

print(pd.isnull(revenue2)) #it shows that value that are not true

print(pd.notnull(revenue2))

#addition of series
print(revenue + revenue2)

#assigning names

revenue2.name="company revenues"
revenue.index.name="company name"
print(revenue2)