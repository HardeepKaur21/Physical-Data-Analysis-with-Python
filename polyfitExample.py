# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 10:36:57 2022

@author: 20705251
"""

import numpy as np
import matplotlib.pyplot as plt

#import all data. in the file the first column is x,
#the other columns are y data sets
data = np.loadtxt('EP305_lecture_11_data1.dat')

xcol, ycol = 0,1 #columns for x and y data
x, y = data[:, xcol], data[:, ycol]

#perform the fit
poly = np.polyfit(x, y, 2) #in order 1 (1ο βαθμο) 
#poly is an array of the coefficients of the polynomial
q, S, y0 = poly #unpack order 2 polynomial
print(f'Fitted model is y ={q:+0.3g} x^2 + {S:0.3g} x + {y0:.3g}.')

#plot the results 
plt.subplot(121)
plt.xlabel('x [l]')
plt.ylabel('y [l]')
plt.plot(x,y, 'kx') #data
plt.plot(x, np.polyval(poly, x), 'r-') #model

plt.subplot(122)
plt.xlabel('x [l]')
plt.ylabel('residuals [l]')
plt.plot(x, y - np.polyval(poly, x), 'k.') #data
plt.tight_layout()