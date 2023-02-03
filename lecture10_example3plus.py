# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 14:31:34 2022

Lecture 10 example 3 plus

@author: 20705251
"""

import numpy as np
import matplotlib.pylab as plt
import random

N = 1_000_000

def print_bin_data(ns, bins):
    for i,n in enumerate(ns): #new 
        binmin = bins[i]
        binmax = bins[i+1]
        closing_par = ')' if i<len(ns) else ']' #new
        print(f'{n} counts in bin [{binmin:.5g}-{binmax:.5g}{closing_par}')

seq1 = [random.random() for _ in range(N)]
seq2 = [20.0*random.random() - 10.0 for _ in range(N)]

plt.figure(dpi=120) #new
plt.subplot(121)
ns1, bins1, _ = plt.hist(seq1, bins = np.linspace(0.0, 1.0, 10+1)) #new

plt.subplot(122)
ns2, bins2, _ = plt.hist(seq2, bins = np.linspace(-10.0, 10.0, 10+1)) #new

print('Unscaled Distribution')
print_bin_data(ns1, bins1)

print('Scaled Distribution')
print_bin_data(ns2, bins2)