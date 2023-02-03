# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 13:37:57 2022

@author: 20705251

Description: 
    This is the second exercise in the lab where we fill the arrays/lists with
    user inputted values.
"""

import numpy as np #used to create lists

#handling exceptions-----
def inputCheckerLength():
    n = input('Enter the length ' + str(i) + ' as a float: ')
    try:
        n = float(n)
        return n
    except ValueError:
        print("Please enter a number, not a letter. It can be any number:")
        return inputCheckerLength()
    
def inputCheckerPeriod():
    n = float(input('Enter the period ' + str(i) + ' as a float: '))

    try:
        n = float(n)
        return n
    except ValueError:
        print("Please enter a number, not a letter. It can be any number:")
        return inputCheckerLength()
    


n = 10

#create two 1-d arrays of zeroes, default type is float
sp_length = np.zeros(n)
sp_period = np.zeros(n)

#the quick method 
#create 2 lists (1-d arrays)
#sp_length = ([10., 20., 30., 40., 50., 60., 70., 80., 90., 100.])
#sp_period = ([0.61, 0.94, 1.09, 1.27, 1.37, 1.50, 1.66, 1.81, 1.85, 2.09])

#the long way
#read in individual values
for i in range(10):
    
    #print('Enter the length ', i, 'in cm:' )
    sp_length[i] = inputCheckerLength()
    
    #print('Enter the period ', i, 'in seconds: ')
    sp_period[i] = inputCheckerPeriod()

#print the header
print('\n{0:>15}'.format('index'), \
      '{0:>15}'.format('length (cm)'), \
    '{0:>15}'.format('period (s)'))
    
#print the contents of the lists
for i in range(len(sp_length)):
    print('{0:>15}'.format(i), \
          '{0:>15.3f}'.format(sp_length[i]), \
        '{0:>15.3f}'.format(sp_period[i]))