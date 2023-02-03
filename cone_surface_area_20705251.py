# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 14:12:43 2022

@author: Hardeep Kaur Gill - 20705251

Description:   
    Returns the area of a ccone given its radius and height.
"""
#This programme calculates the area of a cone given the radius and the 
# length of the cone

#Libraries
import numpy as np #needed for pi and square root function

#-------------------------------------------------
#define the function cone_area()
def cone_area(r_value, h_value):
    l = np.sqrt((r_value*r_value) + (h_value*h_value))
    area = np.pi*r_value*l + np.pi*(r_value*r_value)
    return(area)
#----------------------------------------------------- 


#----------------handling exceptions------------------
def valueChecker():
    r = input('\nEnter the radius of the cone in meters (e.g. 2.1): ')
    h = input('Enter the height of the cone in meters (e.g. 3.4): ')
    try:
        r = float(r)
        h = float(h)
        if(r < 0 and h < 0):
            print("The radius and the height cannot be negative! Please \
try again.")
            raise ValueError
        elif(r < 0):
            print("The radius of the cone cannot be negative! Please \
try again.")
            raise ValueError
        elif(r > 0):
            print("The height of the cone cannot be negative! Please \
try again.")
            raise ValueError
        else:
            return r,h
    except ValueError:
        return valueChecker()
        
#----------------main program starts here------------- 
print('\nThis programme calculates the area of a cone of radius, r, \
and height, h. \
\nIt uses a USER DEFINED function.')

ans = 'Y' #use the programme at least once 
while ans == 'Y':
#prompt the user for the radius
    c_radius, c_height = valueChecker()

#call the function cylinder_vol
    c_area = cone_area(c_radius, c_height)

#output results
    print('\nThe volume of the cylinder is ' , \
       '{0:>10.2f}'.format(c_area), ' meters\xb2')
        
    ans = input('\nDo you want to try another cone? (Y/N) ')