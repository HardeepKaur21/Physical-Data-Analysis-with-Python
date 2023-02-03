# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 09:03:29 2022

@author: Hardeep Kaur Gill - 20705251 (Python 3.9)

Description: 
    This programme is designed to find the quasratic roots of a quadratic 
    equation of the form Ax\xb2 + Bx + C. The user inputs the variables A,B,C.
    At the end of the code the user is asked a question whether to continue
    with another equation.
"""
#Libraries Imported
import numpy as np #needed for the sqrt function
import cmath as cm #needed for negative sqrt

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

#-----------------------Exception Handler----------------------------
#I wanted this porgram to deal with each varable separately
#start with A
def AChecker():
    A = input("Please enter a value for A (e.g. 1, but not zero!): ")
    try:
        A = float(A) #try to parse as a float
        if(A == 0): #in case A is zero, print message and raise ValueError
            warning = ColorText('A cannot be zero! If it is, then you have \
a linear function. Not a quadratic one. Try again!', 'red')
            print(warning)
            raise ValueError
        return A #when A is ok return it
    except ValueError: #deal with ValueError
        print(ColorText("Please enter a valid number for A.", 'red'))
        print('\a') #added beeping sound
        return AChecker() #repeat until A is valid

#then check B
def BChecker():
    B = input("Please enter a value for B (e.g. -8): ")
    try: 
        B = float(B) #try to parse as a float
        return B #when B is ok return it
    except ValueError: #deal with ValueError
        print(ColorText("Please enter a valid number for B.", 'red'))
        print('\a') #added beeping sound
        return BChecker() #repeat until B is valid


#then check C
def CChecker():
    C = input("Please enter a value for C (e.g. 12): ")
    try: 
        C = float(C) #try to parse as a float
        return C #when C is ok return it
    except ValueError: #deal with ValueError
        print(ColorText("Please enter a valid number for C.", 'red'))
        print('\a') #added beeping sound
        return CChecker() #repeat until C is valid
#------------------End of Handling Exceptions-----------------------

#-------------------Quadratic Roots Functions-----------------------
#first root
def root1(A, B, C):
    """
    Calculates the first root of the quadratic equation (Ax\xb2 + Bx + C)
    
    Parameters
    -----------
    A: float
    B: float
    C: float
    These values are used for the quadratic formula.
    
    Returns
    --------
    x1: float 
    """
    x1 = 0.0 #x1 is the first root of the equation which will be returned 
    d = B*B - 4*A*C
    if(d<0): #we are expecting complex numbers
        #to calculate the first root we use the formula -B + square root of
        #B\xb2 - 4 times A times C all of this divided by 2 times A
        x1 = complex(((-B) + cm.sqrt(d))/(2*A))
        print("complex: ", x1)
        return x1
    
    elif(d>=0):
        #to calculate the first root we use the formula -B + square root of
        #B\xb2 - 4 times A times C all of this divided by 2 times A
        x1 = ((-B) + np.sqrt(d))/(2*A)
        return x1

#second root
def root2(A, B, C):
    """
    Calculates the first root of the quadratic equation (Ax\xb2 + Bx + C)
    
    Parameters
    -----------
    A: float
    B: float
    C: float
    These values are used for the quadratic formula.
    
    Returns
    --------
    x2: float 
    """
    x2 = 0.0 #x2 is the second root of the equation which will be returned 
    d = B**2 - 4*A*C
    if(d<0): #we are expecting complex numbers
        #to calculate the first root we use the formula -B + square root of
        #B\xb2 - 4 times A times C all of this divided by 2 times A
        x2 = complex(((-B) - cm.sqrt((B*B) - 4*A*C))/(2*A))
        return x2
    
    elif(d>0):
        #to calculate the first root we use the formula -B + square root of
        #B\xb2 - 4 times A times C all of this divided by 2 times A
        x2 = ((-B) - np.sqrt((B*B) - 4*A*C))/(2*A)
        return x2
#------------------End of Quadratic Roots Functions---------------------

#----------------------Main Code Starts Here-----------------------------
#Inform the user of the purpoe of the program
print("\nThis programme can solve a quadratic formula of the form \
Ax\xb2 + Bx + C. You just have to enter the values for A, B, C.")
print("The code will continue asking you if you want to continue with \
different equations. Just type Y for 'yes' and N for 'no'.")

ans = 'Y' #control while loop
while ans == 'Y':
    #call the input checker
    A = AChecker()
    B = BChecker()
    C = CChecker()
    d = B*B - 4*A*C #discriminant
    
    #call the root functions and print results accordingly
    if(d > 0): #if d> 0 the equation has 2 solutions
        #print results
        r1 = root1(A,B,C)
        r2 = root2(A,B,C)
        
        #print results
        print("\nThe equation",A,"x\xb2 + ",B,"x +",C,"has roots at:")
        print(ColorText("x1 = ",'blue'),r1,"      ", \
ColorText("x2 = ",'blue'),r2)
    
    elif(d == 0): #if d = 0, then the equations has only 1 solution
        #call functions 
        r1 = root1(A,B,C)
        
        #print results
        print("\nThe equation",A,"x\xb2 + ",B,"x +",C,"has 1 root at:")
        print(ColorText("x1 = ",'blue'), r1)
    
    elif(d<0): #if d<0, then we are expecting complex numbers
        #call functions
        r1 = complex(root1(A,B,C)) 
        r2 = complex(root2(A,B,C)) 
        
        #print results
        print("\nThe equation",A,"x\xb2 + ",B,"x +",C,"has 2 complex \
roots at:")
        print(ColorText("x1 = ",'blue'),r1,"      ", \
ColorText("x2 = ",'blue'),r2)
    
    #give the user the power to either continue, or exit the code.
    ans = input(ColorText('\nDo you want to try another equation? \
(Y/N) ', 'green'))

#-------------main code ends here-----------------