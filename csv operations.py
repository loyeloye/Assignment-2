import numpy as np
import pandas as pd
from pandas import Series,DataFrame

dframe = pd.read_csv('sample.csv')
print(dframe)

dframe = pd.read_csv('sample.csv', header=None)
print(dframe)

#use readtable
dframe2 = pd.read_table('sample.csv', sep=',', header=None )
print(dframe2)

#partial rows importing
print(pd.read_csv('sample.csv',nrows=2,header= None))

#dump
dframe2.to_csv('outputCSV.csv', sep='!');

#select specific columns
dframe.to_csv('dataoutput.csv', columns=[0,1])