# -*- coding: utf-8 -*-
"""
Spyder Editor

This program is designed to take in 2 positive integer values x,y and then 
calculates x squared and y cubed. After doing this, the code prints the 
results on the screen

Author - Hardeep Kaur Gill (20705251)
Version - 03/02/2022

"""

#program starts here 

#request user to input 2 positive integer numbers
x = int(input('Please enter a positive integer value for x: '))
y = int(input('Please enter a positive integer value for y: '))
#input() passes the user input as a string so int() is included
#to pass the string to an int


#calculate the square and cube of the user inputs
xsq = x**2    #xsq (x squared) stores the value of x squared
ycb = y**3    #ycb (y cubed) stores the value of y cubed


#print the results
print(x, 'squared =', xsq, 'and', y, 'cubed =', ycb)
#the comma is used to print together integer and strings in one line

