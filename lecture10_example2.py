# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 10:03:08 2022

@author: 20705251
"""

import random 

def random_sequence(N):
    '''
    Generate a sequence of random numbers.

    Parameters
    ----------
    N : INT
        Number of values needed.

    Returns
    -------
    seq: list
        list of N random values drawn from [0.0,1.0) interval.

    '''
    seq = [] #seq = [random.random() for _ in range(N)] can also work
    #what if we want to produce the list only if N >= 3
    #seq = [random.random() for i in range(N) if i>2]
    
    for _ in range(N):
        seq.append(random.random())
    return seq

rng_state = random.getstate() #store the current RNG state

seq1 = random_sequence(10) #first random sequence
seq2 = random_sequence(10) #second random sequence
print(f'1:\t{seq1}\n\n2:\t{seq2}')

print()
print()
print()

random.seed('my string seed') #re-seed the generator
seq3 = random_sequence(10)
seq4 = random_sequence(10)
print(f'3:\t{seq3}\n\n4:\t{seq4}')

print()
print()
print()

random.seed('my string seed') #re-seed the generator
seq3r = random_sequence(10)
seq4r = random_sequence(10)
print(f'3:\t{seq3r}\n\n4:\t{seq4r}') #these are the same 

print()
print()
print()

random.setstate(rng_state) #restore initial state
seq1r = random_sequence(10) #first random sequence again
seq2r = random_sequence(10) #second random sequence again
print(f'1:\t{seq1r}\n\n2:\t{seq2r}') 