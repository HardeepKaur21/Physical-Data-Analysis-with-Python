# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 13:48:57 2022

@author: 20705251
"""

import numpy as np #needed to create arrays
import matplotlib.pyplot as plt #needed for plots

#some data 
x = np.array([0.3, 0.5, 0.7, 0.9])
y = np.array([1., 2., 2.5, 3.9])

#constant symmetric errors of +/- 0.05 on x-data
xerr = 0.05

#Assymetric, variable errors on y-data
yerr = np.array([[0.1, 0.25, 0.5, 0.4],
                [0.1, 0.15, 0.2, 0.4]])

fig = plt.figure()
ax = fig.add_subplot(111)
#ax.grid(False) #hide grid lines

ax.errorbar(x, y, yerr, xerr, fmt = 'ko', lw = 1, ls = '', capsize = 3)

ax.set_xlabel('x-axis (units)', fontsize = 12)

plt.ylabel('y-axis (units)', fontsize = 12)
plt.title('Graph title', fontsize = 20)
plt.show()
