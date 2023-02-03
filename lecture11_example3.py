# -*- coding: utf-8 -*-
"""
Created on Mon May  2 15:24:07 2022

@author: 20705251
"""

import numpy as np 
import matplotlib.pyplot as plt

#import the data
data = np.loadtxt('EP305_lecture_11_data1.dat')

xcol, ycol = 0, 2 #columns (indexes) to read in as x and y datasets

x, y = data[:, xcol], data[:,ycol] #import appropriate columns to the variables

#build the model array (linear model) f1 = x, f0 = 1
M = np.column_stack((x**2, x, np.ones_like(x)))

#perform the fit
poly, res, rank, s = np.linalg.lstsq(M, y, rcond = None)
#poly is the array of fitted model coefficients
#res are the residuals
#rank is the rank of the coefficient matrix
#s are the singular values of the coefficient matrix
print(poly)
q, S, y0 = poly #unpack order 1 polynomial
print(f'Fitted model is y = {q:.3g} x\xb2 + {S:.3g} x + {y0:.3g}.') 
#g removes insignificant zeroes
#.3 sets the precision to 3

#plot the results
plt.subplot(121) #to plot data and compare it with our model
plt.xlabel('x [l]')
plt.ylabel('y [l]')

plt.plot(x, y, 'kx') #plot the data
plt.plot(x, np.polyval(poly, x), 'r-') #our model

plt.subplot(122) #to view the residuals
plt.xlabel('x [l]')
plt.ylabel('residuals [l]')

plt.plot(x, y - np.polyval(poly, x), 'k.') #residuals are the difference the
# observed value and the predicted value

plt.tight_layout() #has to do with the layout of the subplots