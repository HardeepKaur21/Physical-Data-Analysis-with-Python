# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 11:13:26 2022

EP305 lecture 10 example 3

@author: 20705251
"""
import matplotlib.pylab as plt
import random

N = 1_000_000

seq1 = [random.random() for _ in range(N)]
seq2 = [22.0*random.random() -2.0 for _ in range(N)]

plt.figure(dpi = 120)
plt.subplot(121)
plt.hist(seq1, bins = [0, 0.25, 0.5, 0.75, 1.0])
plt.subplot(122)
res = plt.hist(seq2, bins = 11) #we can change the number of bins to a list etc
print(res)