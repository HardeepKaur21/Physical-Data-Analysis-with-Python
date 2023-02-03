# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 14:28:27 2022

@author: Hardeep Kaur Gill 20705251
"""
#inform the user of the program purpose
print('This program counts the number of prime numbers')
print('in the range 1 - n where n is a user entrered constant')

#enter the search range 
n = int(input('Enter the max value of the search range: '))

p = 1
print(p, ' is a prime a number')

for i in range(0 , n+1, 1):
    x = 0
    for j in range(2, i , 1): # end point is omitted
        if i % j == 0:
            x= x+1
    if x == 0:
        print(i , ' is a prime number')
        p = p + 1
    
    if i % 1000 == 0:
        print("Reached i =", i, "already")
        
print("\nThere are", p, "primes in", n)