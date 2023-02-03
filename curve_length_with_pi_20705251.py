# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 12:22:10 2022

@author: Hardeep Kaur Gill - 20705251 (Python 3.9)

Description: 
    This program computes the length of a semicircle by considering it as a 
    number of straight sections joined together. 
"""
#Libraries Imported--------------------------------------------------
import numpy as np # used for pi and sqrt function

##--------- Colour Function-------------------
def ColorText(text, color):
    CEND = '\033[0m'
    CBOLD = '\033[1m'
    CRED = '\033[31m'
    CGREEN = '\033[32m'
    CYELLOW = '\033[33m'
    CBLUE = '\033[34m'
    CVIOLET = '\033[35m'
    CBEIGE = '033[36m'
    
    if color == 'red':
        return CRED + CBOLD + text + CEND
    elif color == 'green':
        return CGREEN + CBOLD + text + CEND
    elif color == 'yellow':
        return CYELLOW + CBOLD + text + CEND 
    elif color == 'blue':
        return CBLUE + CBOLD + text + CEND
    elif color == 'violet':
        return CVIOLET + CBOLD + text + CEND
    elif color == 'beige':
        return CBEIGE + CBOLD + text + CEND
#---------------------End of Colour Function-------------------------

#---------------------User Defined Functions-------------------------
def f(x): #to calculate y of the semi-circle
    """
    Gives the value of y for a section of a semi-circle

    Parameters
    ----------
    x : float
        Length of the diameter divided by n.

    Returns
    -------
    np.sqrt(1-x*x).

    """
    #the function returns the result of x^2 + y^2 = 1 but solved for y
    return(np.sqrt(1-(x*x))) 

def new_length(x, dx): #calculates the distance between the points (x,f(x)) 
    # and (x+dx, f(x+dx)) 
    """
    Gives the distance between the two points containing x and dx

    Parameters
    ----------
    x : float
        Starting point.
    dx : float
        Next point.

    Returns
    -------
    np.sqrt(dx*dx+(f(x+dx)-f(x))*(f(x+dx)-f(x))).

    """
    #this function returns the result of the equation of distance which is:
        # dist = sqrt((x2 - x1)^2 - (y2 - y1)^2) where x2 = x+dx 
        # and y2 = f(x+dx)
    return(np.sqrt(dx*dx+(f(x+dx)-f(x))*(f(x+dx)-f(x))))
#-------------------End Of User Defined Functions----------------------

#---------------------main code starts here--------------------
#these are determined by the radius of the cyrcle which in this case is 1 
x_max = 1 
x_min = -1

title1 = 'n'
title2 = 'length'
title3 = 'error'

print(ColorText('\n{0:>18}'.format(title1), 'red'), ColorText(' | ', 'red'), \
      ColorText('{0:>18}'.format(title2), 'red'), ColorText(' | ', 'red'), \
      ColorText('{0:>18}'.format(title3), 'red'))

#declaring variables 
c_error = 1 
c_length = 0 
n = 1


#loop till the error gets smaller than 1E-6
while c_error > 1e-6:
    
    #dx is the small length to be added each time 
    dx = (x_max-x_min)/n
    
    #the inner loop will run for all dx
    for i in range(0,n):
        
        #x increses by dx each time
        x = x_min+i*dx
        
        #calculate the length
        c_length = c_length+new_length(x, dx)
        
    #it is known that the length of the semi-circle is pi, so to calculate
    #the error we subtract the measured value from the original one
    c_error = np.pi-c_length
    
    
    #print out the results
    print('{0:>18}'.format(n), ' | ', \
          '{0:>18.7f}'.format(c_length), ' | ', \
          '{0:>18.7f}'.format(c_error))
        
        
    n = n*2 #double n to see how the length and the error change
    c_length = 0  #reset the length 
