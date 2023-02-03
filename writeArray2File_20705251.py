# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 14:07:08 2022

@author: Hardeep Kaur Gill - 20705251 - Python 3.9

Description:
    This code has 4 different functions:
        One for gettting the data
        One for printing them out
        One to create a file
        One to read the file in
"""
#Imported Libraries
import numpy as np #needed for the arrays

##-------------------------Colour Function--------------------------
def ColorText(text, color):
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
    elif color == 'purple':
        return CVIOLET + CBOLD + text + CEND
    elif color == 'beige':
        return CBEIGE + CBOLD + text + CEND
#---------------------End of Colour Function-------------------------

#--------------------Handling Exceptions-----------------------------
def inputCheckerLength(i): #i is parsed to keep the same format as in the lab
    n = input('Enter the length ' + str(i) + ' as a float: ')
    try:
        n = float(n)
        return n
    except ValueError:
        print("Please enter a number, not a letter. It can be any number:")
        return inputCheckerLength(i)
    
def inputCheckerPeriod(i): #i is parsed to keep the same format as in the lab
    n = input('Enter the period ' + str(i) + ' as a float: ')

    try:
        n = float(n) #try parsing n as float
        return n #is successful then return it
    except ValueError: #is error raised then allow the user to try again
        print("Please enter a number, not a letter. It can be any number:")
        return inputCheckerLength(i)
    
#--------------------End of exceptions handling---------------------
#---------------------User Defined Functions------------------------
def get_data(): #function one:
    """
    This function gets data from the keyboard and adds it in a list

    Returns
    -------
    sp_length : list
        This list is used to input the data for the length of the pendulum.
    sp_period : list
        This list is used to input the data for the period of the pendulum.

    """
    n = 10

    #create two 1-d arrays of zeroes, default type is float
    sp_length = np.zeros(n)
    sp_period = np.zeros(n)
    
    for i in range(n):
        
        #fill in the length array with user-inputted values, these values are
        #checked in the handling exceptions part of the code
        sp_length[i] = inputCheckerLength(i)
        
        #fill in the length array with user-inputted values, these values are
        #checked in the handling exceptions part of the code
        sp_period[i] = inputCheckerPeriod(i)
    
    return sp_length, sp_period

def print_data(sp_length, sp_period): #function 2:
    """
    Parameters
    ----------
    sp_length : TYPE
        Used to print the list.
    sp_period : TYPE
        Used to print it.

    Returns
    -------
    None.

    """

    #print the header
    print('\n{0:>15}'.format('Index'), \
          '{0:>15}'.format('Length (cm)'), \
          '{0:>15}'.format('Period (s)'))
        
    #I wanted the index column of the table to go from 1-10 instead of 0-9
    n = 1
    
    #print the contents of the lists
    for i in range(len(sp_length)):
        print('{0:>15}'.format(n), \
              '{0:>15.3f}'.format(sp_length[i]), \
            '{0:>15.3f}'.format(sp_period[i]))
        n = n+1

def file_write(sp_length, sp_period, file_name): #function three:
    """
    This function creates a file with the name "file_name" and inputs data 
    from the lists sp_length and sp_period

    Parameters
    ----------
    sp_length : list
        used to input data from it.
    sp_period : list
        used to input data from it.
    file_name : string
        The file to be created

    Returns
    -------
    None.

    """
    
    #open a file for writing
    out_file = open(file_name, 'w')

    #put header on file
    print('{0:>15}'.format('index'), \
          '{0:>15}'.format('length (cm)'), \
        '{0:>15}'.format('period (s)'), file = out_file)
        
    #write the values to the file
    for i in range(len(sp_length)):
        print('{0:>15}'.format(i), \
              '{0:>15.3f}'.format(sp_length[i]), \
            '{0:>15.3f}'.format(sp_period[i]), file = out_file)

    #close the file
    out_file.close()


def file_read(file_name): #function four
    """
    This function reads in data from a file. 

    Parameters
    ----------
    file_name : string
        file_name is the name of the file from where the data is gonna be read 
        from.

    Returns
    -------
    sp_length_v3 : array
        The array with the data from the text file that contains data on the 
        length of the pendulum.
    sp_length_v3 : array
       The array with the data from the text file that contains data on the 
       length of the pendulum.

    """
    #open a file for reading
    in_file = open(file_name, 'r')
    
    #create 2 lists. Lists because I want to use the append function 
    sp_length_v3 = []
    sp_period_v3 = []

    header = in_file.readline() #read in the header separately
    #print(header)

    for line in in_file:
        values = line.split() #read data from each line in list
        sp_length_v3.append(float(values[1])) #column 2 convert to float
        sp_period_v3.append(float(values[2])) #column 3 convert to float
          

    in_file.close()
    return sp_length_v3, sp_length_v3
#-----------------------Main Code Starts Here-----------------------
print("\nThis programme is written to take in data from a pendulum experiment \
      in 2 ways, one way is by inputting values from the user. And the other \
          is by reading the data from a text file.")
print("The programme then outputs the 2 tables created from each method of \
      inputting data in they array or list.")


#Acquire the data from the keyboard
sp_length, sp_period = get_data()

#Display the data
print('\nOriginal Data', ColorText('read from the keyboard','red'), \
      'shown below')
print_data(sp_length, sp_period)

file_write(sp_length, sp_period, 'pendulum.txt')

#Retrieve the data from the file
sp_length_v2, sp_period_v2 = file_read('pendulum.txt')

sp_length_v2 = np.array(sp_length_v2) #to convert the returned lists
sp_period_v2 = np.array(sp_period_v2) #to arrays

#Display the retrieved data
print('\nData', ColorText('retrieved from file', 'purple'), 'shown below')
print_data(sp_length_v2, sp_period_v2)
