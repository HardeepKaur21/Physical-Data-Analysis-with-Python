# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 00:37:23 2022

Lecture 10 Example 4

@author: 20705251
"""

import matplotlib.pylab as plt
import random 

def print_bin_data(ns, bins):
    for i,n in enumerate(ns): #new 
        binmin = bins[i]
        binmax = bins[i+1]
        closing_par = ')' if i<len(ns) else ']' #new
        print(f'{n} counts in bin [{binmin:.5g}-{binmax:.5g}{closing_par}')

N = 5000

seq = [int(6.0*random.random()) +1 for _ in range(N)]

plt.figure(dpi = 120)
ns, _, _ = plt.hist(seq, bins = [ 0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5], 
                    align = 'mid', rwidth = 0.1)
#rwidth parameters narroes the bar for clarity

print(ns)