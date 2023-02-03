# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 07:22:45 2022

@author: Hardeep Kaur Gill - 20705251 (Python 3.9)

Description: 
    This code is designed to calculate the reactance of a 0.5 μF capacitor and 
    a 3 mH inductor at the frequency starting from the smallest value a in a 
    range defined by the user to the largest value which is b.  
"""
#---------------------Imported Libraries----------------------------
import numpy as np #used for pi

##---------------------Colour Function------------------------------
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

#----------------------User Defined Functions------------------------
def capacitiver(f):
    """
    Calculates the capacitive reactance of different values for the frequency
    using the formula: Xc = 1/(2πfC) and returns the result. The capacity is
    told to be C = 0.5F.
    
    Parameters
    ----------
    f : float
        The frequency. 

    Returns
    -------
    Xc : float
        The capacitive reactance.

    """
    C = 0.5 #Farads
    
    #calculate the capacitive reactance using the formula: Xc = 1/(2πfC)
    Xc = 1/(2*np.pi*f*C)
    return Xc

def inductiver(f):
    """
    Calculates the inductive reactance of different values for the frequency
    using the formula: Xl = 2πfL and returns the result. For this function
    the inductance is L = 3H.
    
    Parameters
    ----------
    f : float
        The frequency. 

    Returns
    -------
    Xl : float
        The inductive reactance.

    """
    L = 3 #Henries
    
    #calculate the inductive reactance using the formula: Xl = 2πfL
    Xl = 2*np.pi*f*L
    return Xl
    
#---------------------End of User Defined Functions------------------

#------------------------Handling Exceptions-------------------------
def checker():
    n = input("Please enter a number n, (0<n<=360) for the range (eg. 125): ")
   
    try:
        n = float(n)
        if(n > 360 or n <= 0):
            raise ValueError
        return n
    except ValueError:
        
        #inform user of the mistake
        print(ColorText("Your NUMBER should be between 0 and 360!",  \
                        'red'))
        print(ColorText("Remember: The capacitive reactance cannot be zero.", \
                        'red'))
        print(ColorText("Try again!", 'red'))
        print('\a') #added beeping sound
        return checker()
#------------------------End of Handling exceptions------------------
        
#------------------------Main code Starts Here-----------------------

#inform the user of what is happening
print("This program is here to help you calculate the inductive and \
capacitive reactance according to a differing frequency.")
print("The frequency is determined from the range you will input into the \
program. The range can be any 2 numbers from 0 (not including it) to 360 \
(they could be decimal numbers) and for each iteration f is increased by 30.")
print("In this code the capacity and the inductance are assumed to be 0.5F \
and 3H respectively.")

#get user inputs
a = checker()
b = checker()

#in case the user enters the numbers in the reverse order, the values of a, b 
#are exchanged 
if(a > b):
    temp = a
    a = b
    b = temp

#declare appropriate variables 
creactance = 0
lreactance = 0


#define titles
title1 = 'Frequency [Hz]'
title2 = 'C Reactance [Ω]'
title3 = 'L Reactance [Ω]'

#print the title in a way it looks different from the rest of the table 
#for aesthetic purposes 
print(ColorText('\n{0:f>20}'.format(title1), 'blue'), ColorText(' | ', 'blue'),\
      ColorText('{0:f>20}'.format(title2), 'blue'), ColorText(' | ', 'blue'), \
      ColorText('{0:f>20}'.format(title3), 'blue'))

f = a #define f as the smallest number in the range which is a 

#loop starts (we could have used a for loop but the frequency can be a decimal 
#number, so a while loop was preferred)
while(f < b+1): #to inclube b if necessary

    #call the capacitive reactance function
    creactance = capacitiver(f)
    
    #call the inductive reactance function
    lreactance = inductiver(f)
    
    #print formatted results
    print('{0:f>20}'.format(f), ' | ', \
          '{0:f>20.4e}'.format(creactance), ' | ', \
          '{0:f>20.4e}'.format(lreactance))
        
    f = f + 30 #increment f by 30 in each step
    
    
    
