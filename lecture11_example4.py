# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 12:05:31 2022

@author: H20705251
"""

import numpy as np
import matplotlib.pyplot as plt

#assumed model parametes
#(k cannot be fitted using a linear model)
a, phi, k = 2.5, np.pi/3.0, 1.5
#phi is like b in acos(kx+b)

#independent variable
x = np.linspace(0.0, 4*np.pi, 100)
#x is an array with 100 numbers from zero to 4π

#dependent variable (model data)
y0 = a *np.cos(k*x + phi)

#add random component
sigma = 0.5
y = y0 + np.random.normal(0.0, sigma, size = y0.size)
#y is an array of length 100

#build model array (linear model)
#fl = cos(kx), f0 = sin(kx)
M = np.column_stack((np.cos(k*x), np.sin(k*x)))

#perform the fit
params, res, rank, s = np.linalg.lstsq(M, y, rcond = None)
ap, bp = params #in the same way from poly in previous examples
#these are the parameters for the linearised model

#below the parameters for the original model are calculated using the
#estimated parameters for the linearised model above
a = np.sqrt(ap**2 + bp**2)
b = np.arctan2(-bp, ap)

print(f'Fitted y = {a:0.3g}cos(kx + {b:.3g}).')

#plot the results
plt.subplot(121)
plt.xlabel('x [l]')
plt.ylabel('y [l]')

plt.plot(x, y, 'kx') #data
plt.plot(x, a*np.cos(k*x+b), 'r-') #our model

plt.subplot(122)
plt.xlabel('x [l]')
plt.ylabel('residuals [l]')

plt.plot(x, y - a*np.cos(k*x+b), 'k.') #data

plt.tight_layout()