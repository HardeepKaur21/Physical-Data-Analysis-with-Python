# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 09:26:39 2022

@author: 20705251

Lecture 10 example 5
"""
import numpy as np 
import matplotlib.pylab as plt
from scipy.special import erfinv
import random

N = 100

uniform_seq = [random.random() for _ in range (N)]
#transform to normal distribution using inverse CDF 
normal_seq = erfinv(np.asarray(uniform_seq)*2.0 - 1.0) * np.sqrt(2.0)

plt.figure(dpi = 120)
plt.subplot(121)
plt.hist(uniform_seq, bins = min(int(np.sqrt(N)), 100)) #new

plt.subplot(122)
plt.hist(normal_seq, bins = min(int(np.sqrt(N)), 100))

print(np.mean(normal_seq), np.std(normal_seq))
