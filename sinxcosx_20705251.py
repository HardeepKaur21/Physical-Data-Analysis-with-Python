# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 13:11:31 2022

@author: Hardeep Kaur Gill 20705251

Description: 
    for_loop_example_2

"""
# This program calculates values of the sine() and cosine() functions 
# in the range [0, 2*pi] in n euqually spaced steps 

# inform the user of what is going on 
print('\nThis program calculates values of the function sine() and cosine()')
print('functions in the range [0, 2*pi] in n equally spaced steps ')


#import the required libraries 
import numpy as np 

#decare and initialise constant end points
x0, x1 = 0.0, 2*np.pi #range

n = int(input("Please enter the number of intervals, n (e.g. 12): "))

deltaX = 2*np.pi/n

title1, title2, title3, title4 = "x(rad)", "x(degrees)", "sin(x)", "cos(x)"

print('{0:>8}'.format(title1), \
      '{0:>12}'.format(title2), \
      '{0:>16}'.format(title3), \
      '{0:>16}'.format(title4))
    
for i in range(0, n+1):
    x = x0 + i*deltaX
    
    print('{0:>8.3f}'.format(x), \
          '{0:>12.3f}'.format(x*(180/np.pi)), \
          '{0:>16.3f}'.format(np.sin(x)), \
          '{0:>16.3f}'.format(np.cos(x)))