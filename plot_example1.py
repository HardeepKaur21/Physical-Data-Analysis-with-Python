# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 13:15:05 2022

@author: Hardeep Kaur Gill - 20705251
"""

import numpy as np #needed for many standard function  
import matplotlib.pyplot as plt #needed for plotting

x = np.arange(11)
y=x**2


#plt.ion() #toggles interactive mode
plt.figure()
plt.plot(x, y)
plt.show()