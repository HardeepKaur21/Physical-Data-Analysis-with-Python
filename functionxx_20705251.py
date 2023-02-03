# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 13:11:31 2022

@author: Hardeep Kaur Gill 20705251

Description: 
    for_loop_example

"""
# This porgram calculates values of the function y = x*x in the range [0, 1]
#in steps of size deltaX = 1/m where m is supplied by the user

# inform the user of what is going on 
print('\nThis program calculates values of the function y = x*x')
print('in the range [0,1] in steps of size deltaX = 1/m ')

#decare and initialise constant end points
x0, x1 = 0.0, 1.0

m = int(input("Please enter the number of intervals: "))

deltaX = (x1 - x0)/m

title1, title2 = "x", "x*x"

print('{0:>5}'.format(title1), \
      '{0:>10}'.format(title2))
    
for i in range(1, m+1):
    x = x0 + i*deltaX
    
    print('{0:>5.3f}'.format(x), \
          '{0:>10.3f}'.format(x*x))