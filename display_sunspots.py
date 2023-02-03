# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 14:35:36 2022

@author: 20705251
"""

import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("sunspots.txt", float)
x = data[:, 0]
y = data[:, 1]

xyr = 1749 + (x/12)

plt.scatter(xyr, y, s=10, marker=2, linewidths=1)
plt.xlabel("year")
plt.ylabel("sunspot number")
plt.xlim(1950, max(xyr))
plt.ylim(-5, max(y))



plt.show()
