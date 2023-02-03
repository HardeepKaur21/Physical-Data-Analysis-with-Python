# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 16:02:40 2022

@author: Hardeep Kaur Gill (Python 3.9)
Date: 16/02/2022

Description: 
    This program is designed to request an input from the user in degrees 
    centigrade and converts it to degreees Fahrenheit. In the end it prints
    out the result formatted for the user.
    
"""

##--------- Colour Function -------
def ColorText( text, color):
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
    
    
#--------main code starts here and handling exceptions at the same time-------

degreesc = 9 #declare this variable to be used in the while loop

#description of the purpose of the code to the user 
print("This program is designed to convert degrees C to degrees F.")
print("After performing the required calculations, this code will \
      print out both degrees C and degrees F in a specified format.")
print()
print("Also, this code will loop until the user inputs either a \
      negative value or a number greater than 100")
      

while((degreesc > 0) and (degreesc < 100)):
    
    #request the user to enter a valid input for the program
    degreesc = input("Please enter a value for the temperature in \
                           degrees celsius: ")
    try:
        degreesc = float(degreesc) #try passing the input as a float
        
        #in case the input is negative or greater than 100 raise a value error
        if degreesc > 100 or degreesc < 0:
            raise ValueError
        else: #if not then run the code normally 
        
        
            # to convert from degrees celcius to degrees fahrenheit
            # first divide by 5, and then multiply by 9, and then add 32
            degreesf = ((degreesc/5)*9)+32
            
            
            # print the formatted results
            print('{0:<1.2f}'.format(degreesc), \
                  '{0:<1}'.format('degrees centigrade = '), \
                  '{0:<1.3f}'.format(degreesf), \
                  '{0:>1}'.format('degrees Fahrenheit'))
            
                
            #check the intensity of the temperature
            if(degreesc > 32):
                print(ColorText("Temperature is rather warm", 'red'))
            elif(degreesf <= 59):
                print(ColorText("Temperature is quite cool", 'blue'))
            else:
                print(ColorText("Temperature is comfortable", 'green'))
                
    except ValueError: # handling the exception and end the loop 
    
        #print relative messages
        print("\nYour input should be a number between 0 and 100 to continue.")
        print("Bye :)")
        break

