# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 14:27:23 2022

@author: 20705251
"""

#Define the variables to be used in the code 
grade = 0

print("\nThis user is asked to enter two integers, x and y. The program \
      coninues asking for new values until the user enters 0 for both of them")

#Start a while loop that controls how long the code will run
while (grade < 100) or (grade > 0):
    
    #Request the user to enter a valur for the grade
    grade = int(input("Please enter an integer number for the grade: "))    
    
    #check what category the grade belongs to 
    if(grade >= 85):
        print("A mark of", grade, "% equals an A-grade")
        
    #check if x is greater than y
    elif(grade < 85 and grade >= 70):
        print("A mark of", grade, "% equals a B-grade")
        
    elif(grade < 70 and grade >= 55):
        print("A mark of", grade, "% equals a C-grade")
        
    elif(grade < 55 and grade >= 40):
        print("A mark of", grade, "% equals a D-grade")
    
    #last case is for the grade to be less than 40
    else:
        print("A mark of", grade, "% equals an E-grade")