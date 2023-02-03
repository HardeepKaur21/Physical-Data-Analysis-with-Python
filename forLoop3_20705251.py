# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 11:03:44 2022

@author: Hardeep Kaur Gill - 20705251 (Python 3.9)

Description:
    This programme is designed to take in an integer number n from the user
    and print out 5 columns. The first contains the values from 1 to n and the
    rest contain the sum of n, exponential n, factorial n, and the natural 
    log of n.

"""

import numpy as np #need this library for the functions of the columns
import math as mt #need this for the factorial function

#inform the user of the purpose of this code and how it works 
print("\nHello! This code is written to output 5 columns. Each contains:")
print("1. The numbers 0 to n (you will be defining n) \
      \n2. The sum of n \
      \n3. The exponential of n \
      \n4. The factorial of n \
      \n5. The natural log of n")
print("n should be an integer from 0 to 10000")

#--------------------------handling exceptions-----------------------
def nChecker():
    n = input("Please enter an int number for n [0-10000] (e.g. 15): ")
    try:
        n = int(n) #attempt to pass n as an integer 
        if(n < 0 or n > 10000): # n has to be in the defined range
            raise ValueError()
        return n 
    except ValueError: #if n is not in the range
        print("You did not enter an integer. Try again!")
        return nChecker()

#-------------------------main code starts here-----------------------

#request the user to enter n 
n = nChecker();
    
#format the titles
print('{0:<8}'.format("n"), \
      '{0:<10}'.format("Sum Of n"), \
      '{0:<18}'.format("Exponential Of n"), \
      '{0:<20}'.format("Factorial Of n"), \
      '{0:<10}'.format("Natural log Of n"))

#declare other variables to be used in for loop to keep n fixed
x = 0
sumx = 0

#implement the for loop 
for i in range(1, n+1):
    x = x+1 #increment 
    sumx = sumx + x # for the sum function 
    print('{0:<8}'.format(x), \
          '{0:<10}'.format(sumx), \
          '{0:<18.3f}'.format(np.exp(x)), \
          '{0:<20}'.format(mt.factorial(x)), \
          '{0:<10.3f}'.format(np.log(x)))
    
    if i % 10 == 0:
        print("Reached i =", i, "already")