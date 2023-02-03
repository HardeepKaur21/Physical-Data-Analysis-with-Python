# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 15:23:56 2022

Author: 20705251 - Hardeep Kaur Gill (Python 3.9)
Date: 10/02/2022

Description: 
        This code is designed to take in a value as the speed of an object
        in miles per hour and prints out a title, the value inputted and 
        the converted value in meters per second.
        
"""
# ---------- handling exceptions -------------
def speedchecker(prompt):
    num = input(prompt)

    #check if speed is negative
    try: 
        num = float(num) #passing the prompt as a float
        if num < 0: #speed is a magnitude so it cannot be negative 
            raise ValueError()
            
        return num
    
    #handling the exception
    except ValueError:
        print("Speed cannot be negative. Velocity can be negative.")
        print("Enter a valid value for the speed!")
        return speedchecker(prompt)
    
    

def is_letter(l):
    asci = ord(l)
    return (asci > 64 and asci < 91) or (asci > 96 and asci < 123)

print("is my output", is_letter("9"))
#Request the user to input a value for the speed in mph 
mph = speedchecker("Please enter a value for the speed in mph: ")



# --------- main program starts here ----------

#Convert mph to ms 
ms = (mph*1609.34)/3600

# Defining the titles
title1 = "Miles per hour"
title2 = "Meters per second"

#print the results formatted
#line 1
print('{0:<20}'.format(title1), 
      '{0:<6}'.format(':'), 
      '{0:>20}'.format(title2))

#line 2
print('{0:<20.3f}'.format(mph),
      '{0:<6}'.format('='),
      '{0:<20.3f}'.format(ms))

#line 3
print('{0:>25.5e}'.format(mph),
      '{0:<6}'.format('='),
      '{0:>25.5e}'.format(ms))