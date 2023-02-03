# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 13:37:09 2022

@author: 20705251
"""
#Define the variables to be used in the code 
x = 5
y = 5

print("\nThis user is asked to enter two integers, x and y. The program \
      coninues asking for new values until the user enters 0 for both of them")

#Start a while loop that controls how long the code will run
while (x != 0) and (y != 0):
    
    #Request the user to enter two numbers to be compared
    x = int(input("Please enter a value for the variable x: "))
    y = int(input("Please enter a value for the variable y: "))
    
    
    #check if x is less than y
    if(x < y):
        print("x (", x, ") is less than y(", y, ")")
        
    #check if x is greater than y
    elif(x > y):
        print("x (", x, ") is greater than y (", y, ")")
    
    #check if the numbers are equal
    else:
        print("x (", x, ") equals y (", y, ")")