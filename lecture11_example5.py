# -*- coding: utf-8 -*-
"""
Created on Tue May  3 15:49:00 2022

@author: 20705251
"""

import numpy as np 
import matplotlib.pyplot as plt

#assumed model parameters
#(k cannot be fitted using a linear model)
a, phi, k = 2.5, np.pi/3.0, 1.5 #assumed

#independent variable 
x = np.linspace(0.0, 4*np.pi, 100)

#dependent variable (model data)
y0 = a* np.cos(k*x + phi) #is an array

sigma = 0.5
N = 10_000

#it is a general rule of thumb to take the sqrt of N for the bins of a hist
BINS = min(int(np.sqrt(N)), 100) #to make it look nice 

all_params = np.empty((N, 2)) #create an empty array to store all fitting results
#it has N rows and 2 columns


#build the model array (linear model)
#f1 = x^1, f0 = sin(x)
M = np.column_stack((np.cos(k*x, np.sin(k*x)))

for i in range(N):
    
    #y is y0 with the added random factor
    y = y0 + np.random.normal(0.0, sigma, size = y0.size)
    
    #perform the fit 
    params, res, rank, s = np.linalg.lstsq(M, y, rcond = None)
    ap, bp = params #in the same way from poly in previous examples
    #these are the parameters for the linearised model
    
    #below the parameters for the original model are calculated using the
    #estimated parameters for the linearised model above
    a = np.sqrt(ap**2 + bp**2)
    b = np.arctan2(-bp, ap)
    all_params[i, :] = a, b #store the model params in an array

#plot the results
plt.subplot(121)
plt.hist(all_params[:, 0], bins = BINS) #data for the a parameter

plt.subplot(122)
plt.hist(all_params[:,1], bins = BINS) #data for the b parameter

plt.tight_layout()