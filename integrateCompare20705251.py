# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 13:11:04 2022

@author: Hardeep Kaur Gill - 20705251 (Python 3.9)

Description:
    This programme estimates the integral of the function sin(x) in the
    interval [a,b] using both the trapezoidal rule and the Simpson's 1/3 rule.
    The user should just input the limits. The programme will output the
    analytical answer and the numerical answer. The numerical answer is shown 
    in a table, where the number of intervals doubles in each row until an 
    error of 0 occurs.


"""
#Import Libraries 
import numpy as np #for the sin function and pi.

##-------------------------Colour Function--------------------------
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

#---------------------Handling Exceptions----------------------------
def lowerLimitCheck():
    
    #request user input
    a = input("Enter the lower limit a (e.g. 0.0): ")
    
    try:
        a = float(a) #try to parse as float
        return a #when everything is ok, return a
    
    except ValueError:
        print(ColorText("Please enter a valid number for the lower limit.", \
                        'red'))
        print(ColorText("For example, 0.", 'red'))
        print('\a') #added beeping sound
        return lowerLimitCheck() #repeat until the user inputs a valid number
    
def upperLimitCheck():
    
    #request user input
    b = input("Enter the upper limit b (e.g. 1.0): ")
    
    try: 
        b = float(b) #try to parse as float
        return b #when everything is ok, return b
    except ValueError:
        print(ColorText("Please enter a valid number for the upper limit.", \
                            'red'))
        print(ColorText("For example, 1.", 'red'))
        print('\a') #added beeping sound
        return upperLimitCheck() #repeat until the user inputs a valid number
#--------------------------End of Handling Exceptions------------------------
        

#-----------------------------User Defined Functions--------------------------
def f(x): #f(x) is the sin function for this code
    """
    Calculates the sin(x) function and returns it.
    
    Parameters
    ----------
    x : float
        x is inputted in rads. And it is used for sin(x).

    Returns
    -------
    result: float
        result hold the value of sin(x) and it is returned.

    """
    result = np.sin(x)
    return result

def my_trap(a, b, n):
    """
    Implements the algorithm for the trapezoidal rule on the function sin(x)
    
    Parameters
    ----------
    a : float 
    b : float 
    n : interval
    
    a and b are the limits of the integral and n is the number of intervals

    Returns
    -------
     : float
    The value of the Trapezoid Rule function which is (h/2)*(f1+ 2*f2+ 2*f3...
                                                             2*fn+ f(n+1))

    """
    #needed variables 
    h = (b - a)/n #step size
    sum = 0.0
    
    #loop through the repetitive part of the Rule till the end of the range
    for i in range(1, n):
        x = a + i*h #the different points for x on the x - axis 
        
        sum = sum + 2*f(x) #sum of all function results that are doubled
        
    return (h/2) * (sum + f(a) + f(b)) #add the limits and divide h by 2 to get
    #the average
    
def analytical(a, b):
    """
    This function returns the analytical result for the result of the 
    trapezoid rule

    Parameters
    ----------
    a : float
        a is the lower limit of the integral.
    b : float
        b is the upper limit of the integral.

    Returns
    -------
    float
    By integrating the function sin(x) - definite integral. we get 
    [cosx] for the limits a and b.

    """
    #this formula comes from the rules of integration for the sin(x) function
    #as we have the limits, the deinite integral can be calculated 
    return -np.cos(b) - ( - np.cos(a)) 

def integrate_simpson(a, b, n):
    """
    Implements the algorithm for the Simpson's Rule on the function sin(x)

    Parameters
    ----------
    Parameters
    ----------
    a : float 
    b : float 
    n : interval
    
    a and b are the limits of the integral and n is the number of intervals

    Returns
    -------
     : float
    The value of the Simpson's Rule function which is (h/3)*(f1+ 2*f2+ 4*f3
                                                    2*f4+ ... + 4*f(n-1)+ f(n))

    """
    #needed variables
    h = (b - a)/n #step size
    sumeven = 0.0
    sumodd = 0.0
    
    #loop through the repetitive part of the Rule till the end of the range
    for i in range(1, n):
        x = a + i*h #the different points for x on the x - axis 
        
        #from the simpson's Rule formula, it is clear if i is even then 2*f(x)
        #is used whilewhen i is odd then 4*f(x) is used
        if(i % 2 == 0):
            sumeven = sumeven + 2*f(x)
        elif(i % 2 == 1):
            sumodd = sumodd + 4*f(x)
            
     #return all added components        
    return (h/3) * (sumeven + sumodd + f(a) + f(b))

#----------------------End of User Defined Functions--------------------


#--------------------------Main Code Starts Here-------------------------

#inform the user of what is going on in this code
print("\nThis programme estimates the integral of the function sin(x) in the \
interval [a,b] using both the trapezoidal rule and the Simpson's 1/3 rule.\n")
print("\nThe user should just input the limits. The programme will output the \
      analytical answer and the numerical answer.")
print("\nThe numerical answer is shown in a table, where the number of \
      intervals doubles in each row until an error of 0 occurs.")

#request user inputs
a = lowerLimitCheck()
b = upperLimitCheck()


#print analytical results
print("\nThe analytical answer =", analytical(a, b))

#print formatted numerical results
print("\nThe estimated of the integral between the limits [", a,",", b, \
      "] are: ")

#define the titles    
title1 = "No. of intervals"
title2 = "Trap Estimate"
title3 = "Trap Error"
title4 = "Simp Estimate"
title5 = "Simp Error"

#print the titles
print(ColorText('\n{0:<18}'.format(title1), 'red'), \
ColorText('{0:<14}'.format(title2), 'red'), \
ColorText('{0:<14}'.format(title3), 'red'), \
ColorText('{0:<14}'.format(title4), 'red'), \
ColorText('{0:<12}'.format(title5), 'red'))
    
#declare needed variables for the loop
terror = 1
serror = -1
n = 2

while serror < -(1e-10): #loop till the serror gets bigger than -1E-10
    
    #to calculate the trapezoid error, subtract te analytical value from the 
    #numerical one, the same goes for the Simpson's Rule error
    terror = analytical(a,b) - my_trap(a, b, n)
    serror = analytical(a,b) - integrate_simpson(a, b, n)
    
    #print results row by row
    print('{0:<18}'.format(n), \
'{0:<14.10f}'.format(my_trap(a, b, n)), \
'{0:<14.10f}'.format(terror), \
'{0:<14.10f}'.format(integrate_simpson(a, b, n)), \
'{0:<12.10f}'.format(serror))
    
    n = 2*n #the interval doubles at every try
#----------------------Main Code Ends Here-----------------------------