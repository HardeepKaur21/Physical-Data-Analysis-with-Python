# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 13:23:53 2022

@author: 20705251

Description:
    This is the first practice exercise during the lab on arrays.
"""

#import numpy as np #used to create lists

print("Programme to print simple pendulum data.")
print("Total number of data pairs is 10.")

#create 2 lists (1-d arrays)
sp_length = ([10., 20., 30., 40., 50., 60., 70., 80., 90., 100.])
sp_period = ([0.61, 0.94, 1.09, 1.27, 1.37, 1.50, 1.66, 1.81, 1.85, 2.09])

#print the header
print('\n{0:>15}'.format('index'), \
      '{0:>15}'.format('length (cm)'), \
    '{0:>15}'.format('period (s)'))
    
for i in range(len(sp_length)):
    print('{0:>15}'.format(i), \
          '{0:>15.3f}'.format(sp_length[i]), \
        '{0:>15.3f}'.format(sp_period[i]))