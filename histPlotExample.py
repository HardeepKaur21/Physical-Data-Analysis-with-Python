# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 14:42:58 2022

@author: 20705251
"""

import numpy as np 
import matplotlib.pyplot as plt

samples = 10000
data1 = np.random.random(samples)

mu, sigma = 0.5, 0.1 #mean and standard deviation

data2 = np.random.normal(mu, sigma, samples)

Nbins = int(np.sqrt(samples)) #number of bins

plt.hist(data1, Nbins) #the random numbers
plt.hist(data2, Nbins) #the Gaussian Distribution

plt.show()