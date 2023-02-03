# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 11:06:54 2022

@author: 20705251

Assignment 10

Description:
    This code uses the Monte Carlo approach to determine the volume of a 
    box and its uncertainty. Given the width, depth, and height of the box.

"""

import numpy as np #used for the square root function
import matplotlib.pylab as plt #used to plot the histogram 

print('This code is designed to calculate the volume of a box given its width,\
      depth, height. Alonside with that the unceratainties are also \
          calculated.')

N = 1_000_000 #number of samples
MAXBINS = 200 #limit the number of histogram bins to this value 

#input data
w_nominal, w_postol, w_negtol = 50e-2, 0.5e-2, 0.5e-2 #width in meters
d_nominal, d_postol, d_negtol = 30e-2, 1e-3, 1e-3 #depth in meters
h_nominal, h_postol, h_negtol = 25e-2, 2e-3, 2e-3 #height in meters

#----------------------------User Defined Functions-------------------------

#this function is used to print the resultant values
def print_nominal_tol(label, nominal, postol, negtol):
    """
    This function is is used to print the resultant values.
    
    Parameters
    ----------
    label : String
        Used to show what is being calculated.
    nominal : float (1 decimal point)
        The result.
    postol : float (3 decimal places)
        positive value of the uncertainty.
    negtol : float (3 decimal places)
        negative value for the uncertainty.

    Returns
    -------
    None.

    """
    #tolerance with 2 significant digits
    print(f'{label} = {nominal:g} +{postol:.2g}/-{negtol:.2g}')

#this function is to calculate the volume
def func(a, b, c):
    """
    This function calculates the volume of the box given 3 measurements.

    Parameters
    ----------
    a : float
        first measurement (since they are gettin multiplied, it does not \
                               in what order the values are parsed in).
    b : float
        second measurement.
    c : float
        third measurement.

    Returns
    -------
    TYPE
        The result are the 3 measurements multipled with each other. Once this
        is the formula used to calclate the volume of a box. 
        Volume = width*height*depth.

    """
    return a * b * c #the volume is calculated as width*height*depth

def uniform_samples(N, nominal = 0.0, tol = 0.0, negtol = None):
    """
    Uniformly returns a list with random numbers between the range of an error
    interval.

    Parameters
    ----------
    N : integer
        Sample size.
    nominal : flot, optional
        The original measurement. The default is 0.0.
    tol : float, optional
        The uncertainty. The default is 0.0.
    negtol : float, optional
        If needed, the negative uncertainty, which is equal to the uncertainty
        most of the time, as well is parsed. The default is None.

    Returns
    -------
    Array
        An array of defined dimension, that has its lower boundary at
        nominal - negative tolerance and its upper boundary at nominal + 
        tolerance.

    """
    #if there is no negative tolerance, assume it to be the same as the 
    #tolerance
    if negtol is None: 
        negtol = tol
    return np.random.uniform(nominal - negtol, nominal + tol, N)
    
#get the samples for the physical measurements involved in [m]
w_samples = uniform_samples(N, w_nominal, w_postol, w_negtol)
d_samples = uniform_samples(N, d_nominal, d_postol, d_negtol)
h_samples = uniform_samples(N, h_nominal, h_postol, h_negtol)

#evaluate samples of the function
func_samples = func(w_samples, d_samples, h_samples)

#nominal value of the function
func_nominal = func(w_nominal, d_nominal, h_nominal)


#use max for postol approx. assume nominal to be the analytical value
#and the random values to be the numerical values
func_postol = func_samples.max() - func_nominal 

#same goes for the negative tolerance  #use min for negtol approx.
func_negtol = func_nominal - func_samples.min()

#use the defined function to print the values calculated
print_nominal_tol('w', w_nominal, w_postol, w_negtol)
print_nominal_tol('d', d_nominal, d_postol, d_negtol)
print_nominal_tol('h', h_nominal, h_postol, h_negtol)
print_nominal_tol('Volume (w*d*h)', func_nominal, func_postol, func_negtol)


#plot the histogram of all samples obtained.
plt.hist(func_samples, bins=min(int(np.sqrt(N)),MAXBINS))