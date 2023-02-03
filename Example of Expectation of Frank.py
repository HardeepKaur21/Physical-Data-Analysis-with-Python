# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 13:54:55 2022

@author: 20705251
"""

# main program starts here 

# inform the user what is happening 

print('\nThis program requires the user to enter 2 numbers, a and b')
print('It performs the sum and prints the result')

#prompt the user to enter the numbers 

a = float(input('type in the first number: '))
b = float(input('type in the second number: '))

#input() reads a string 
#passing it to float() converts the string to a real number 

#do the addition
sum_ab = a + b

#print the results 
print('\n') #skip an extra line
print(a, ' plus ', b , ' = ', sum_ab)

