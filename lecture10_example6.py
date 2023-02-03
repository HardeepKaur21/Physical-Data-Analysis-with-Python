# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 10:43:08 2022

@author: 20705251

Lecture 10 Example 6

"""
import numpy as np
import matplotlib.pylab as plt

N = 1000
MAXBINS = 200 #limit the number of historam bins to this number

#uniform
uniform_seq = np.random.uniform(-1.0, 3.0, N)
normal_seq = np.random.normal(1.0, 0.5, N)

plt.figure(dpi = 120)
plt.hist(uniform_seq, bins = min(int(np.sqrt(N)), MAXBINS))
plt.hist(normal_seq, bins = min(int(np.sqrt(N)), MAXBINS))

print(np.mean(uniform_seq))
print(np.mean(normal_seq), np.std(normal_seq))