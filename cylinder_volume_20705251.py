# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 13:25:23 2022

@author: Hardeep Kaur Gill - 20705251

Description: 
    Returns the volume of a cylinder given its radius and height.
"""
#This programme calculates the volume of a cylinder given the radius and the 
# length of the cylinder 

import numpy as np #needed for pi

#-------------------------------------------------
#define the function cylinder_vol()
def cylinder_vol(r_value, h_value):
    return(np.pi*r_value*r_value*h_value)
#--------------------------------------------------

#main program starts here 
print('\nThis programme calculates the volume of a cylinder of radius, r, \
and height, h. \
\nIt uses a USER DEFINED function.')

ans = 'Y' #use the programme at least once 
while ans == 'Y':
#prompt the user for the radius
    c_radius = float(input('\nEnter the radius of the cylinder in meters \
(e.g. 2.1): '))
    c_height =  float(input('Enter the height of the cylinder in meters \
(e.g. 3.4): '))

#call the function cylinder_vol
    c_volume = cylinder_vol(c_radius, c_height)

#output results
    print('\nThe volume of the cylinder is ' , \
       '{0:>10.3f}'.format(c_volume), ' meters\xb3')
        
    ans = input('\nDo you want to try another cylinder? (Y/N) ')