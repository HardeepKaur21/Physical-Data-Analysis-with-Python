# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 14:00:49 2022

@author: 20705251
"""

import numpy as np
import matplotlib.pyplot as plt 

x = np.arange(0, 2*np.pi, 0.1)
y = np.sin(x)

plt.figure()
plt.plot(x, y, 'mD', label = 'sin(t)') #plot y vs x. first
plt.legend()
plt.legend(loc = 'best', fontsize = 10)

plt.plot(x, y, 'k-', label = 'line')

plt.xlabel('x [radians]', fontsize = 10, color = 'k')
plt.ylabel('f(x) = sin(x)', fontsize = 10, color = 'k')

plt.text(4, 0.55, 'this is some text')

plt.show()