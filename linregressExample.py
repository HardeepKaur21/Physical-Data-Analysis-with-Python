# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 09:52:28 2022

@author: 20705251
"""

from scipy.stats import linregress
import numpy as np
import matplotlib.pyplot as plt

#import all data. In the file in the first column is x, 
#the other coumns are y data sets
data = np.loadtxt('EP305_lecture_11_data1.dat')

xcol, ycol = 0, 4 #columns for x and y data
x, y = data[:, xcol], data[:, ycol] #: means all rows 

#perform the fit
S, y0, r, _, sigmaS = linregress(x,y)
#r is the correlation coefficient
#_ is the p-test value
#sigmaS is the standard error on the slope 

print(f'Fitted model is y = {S:0.3g} x + {y0:.3g}.')
print(f'Uncertainty of slope is {sigmaS: .3g}.')

#plot the results 
plt.subplot(121)
plt.xlabel('x [l]')
plt.ylabel('y [l]')
plt.plot(x,y, 'kx') #data
plt.plot(x, S*x + y0, 'r-')

plt.subplot(122)
plt.xlabel('x [l]')
plt.ylabel('residuals [l]')
plt.plot(x, y-(S*x + y0), 'k.') #data

plt.tight_layout() #type of laying of the subplots
