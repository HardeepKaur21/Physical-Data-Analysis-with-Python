# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 11:06:54 2022

@author: 20705251

Lecture 10 Example 7 

"""

import numpy as np
import matplotlib.pylab as plt

N = 1_000_000
MAXBINS = 200 #limit the number of histogram bins to this value 

#input data
a_nominal, a_postol, a_negtol = 100.0, 0.2, 0.2
b_nominal, b_postol, b_negtol = 1.0, 0.05, 0.05

def print_nominal_tol(label, nominal, postol, negtol):
    #tolerance with 2 significant digits
    print(f'{label} = {nominal:g} +{postol:.2g}/-{negtol:.2g}')
    
def func(a, b):
    return a * b

def uniform_samples(N, nominal = 0.0, tol = 0.0, negtol = None):
    if negtol is None:
        negtol = tol
    return np.random.uniform(nominal - negtol, nominal + negtol, N)
    
#uniform sampling!
a_samples = uniform_samples(N, a_nominal, a_postol, a_negtol)
b_samples = uniform_samples(N, b_nominal, b_postol, b_negtol)

func_samples = func(a_samples, b_samples) #evaluate samples of the function
func_nominal = func(a_nominal, b_nominal) #nominal value of the function
func_postol = func_samples.max() - func_nominal #use max for postol approx.
func_negtol = func_nominal - func_samples.min() #use min for negtol approx.

print_nominal_tol('a', a_nominal, a_postol, a_negtol)
print_nominal_tol('b', b_nominal, b_postol, b_negtol)
print_nominal_tol('a*b', func_nominal, func_postol, func_negtol)

plt.hist(func_samples, bins=min(int(np.sqrt(N)),MAXBINS))