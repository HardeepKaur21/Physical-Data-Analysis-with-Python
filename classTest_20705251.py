# -*- coding: utf-8 -*-
"""
Created on Tue May  3 13:02:10 2022

@author: Hardeep Kaur Gill 20705251

Description:
    This code is designed to (i) read the data from the file, 
    
    (ii) plot a graph of the data using a red ‘+’ symbol as the marker 
    (no line) ( x and y-range 0-105), 
    
    (iii) calculate the covariance (xy) and coefficient of linear 
    correlation (r) using the formulae below, and 
    
    (iv) print the results.

"""
#------------Needed Libraries---------------
import matplotlib.pyplot as plt
import numpy as np

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
#-----------User Defined Functions-------------

def file_read(file_name): 
    """
    This function reads in data from a file. 

    Parameters
    ----------
    file_name : string
        file_name is the name of the file from where the data is gonna be read 
        from.

    Returns
    -------
    x_coordinates : array
        The array with the data from the first column.
    y_coordinates : array
       The array with the data from the second column of the text file.

    """
    #open a file for reading
    in_file = open(file_name, 'r')
    
    #create 2 lists. Lists because I want to use the append function 
    x_coordinates = []
    y_coordinates = []

    header = in_file.readline() #read in the header separately
    #print(header)

    for line in in_file:
        values = line.split() #read data from each line in list
        x_coordinates.append(float(values[0])) #column 1 convert to float
        y_coordinates.append(float(values[1])) #column 2 convert to float
          
    in_file.close()
    
    x_coordinates = np.array(x_coordinates)
    y_coordinates = np.array(y_coordinates)
    
    return x_coordinates, y_coordinates

def graph_data(x, y):
    """
    This function plots a graph of the x and y coodinates.
    
    Parameters
    ----------
    x: list
        x coordinates, the data.
    y: list
        y coordinates, the data

    Returns
    -------
    None.

    """
    plt.plot(x, y, 'r+')
    plt.title('Y vs X', fontsize = 20)
    plt.xlabel('X - Coordinates')
    plt.ylabel('Y - Coordinates')
    plt.xlim(0,105)
    plt.ylim(0,105)
    plt.grid(True)
 
        
#The following 2 functions are used in the covar and correl functions only
#they include the for loops for the sums required in the formulas for the 
#covariance and the correlation
def sum2StDev(x, y): #the observation minus the mean is the standard dev(!sure)
    sumxy = 0
    #to calculate the sum of the data minus the mean 
    for i in range(len(x)-1):
        sumxy = sumxy +(x[i] - np.mean(x)*(y[i] - np.mean(y)))
    return sumxy
def sum1sqStDev(x): #1 means 1 array sq means squared
    sumx= 0
    for i in range(len(x)-1):
        sumx = sumx + ((x[i] - np.mean(x))**2)
    return sumx
        
        
#Covariance and Correlation functions and Table function
def covar(x, y):
    cov = (1/len(x))*sum2StDev(x, y)
    return cov
    
def correl(x, y):
    r = sum2StDev(x, y)/np.sqrt(sum1sqStDev(x)*sum1sqStDev(y))
    return r

def table(x, y, cov, r):
    #print the header
    title1 = ColorText('X - Coords', 'blue')
    title2 = ColorText('Y - Coords', 'blue')
    title3 = ColorText('Covariance, σxy', 'blue')
    title4 = ColorText('Correlation, r', 'blue')
    print('\n{0:>32}'.format(title1), \
          '{0:>31}'.format(title2), \
          '{0:>31}'.format(title3), \
             '{0:>30}'.format(title4))
        
    for i in range(len(x)):
        print('{0:>18.1f}'.format(x[i]), \
              '{0:>18.1f}'.format(y[i]), \
            '{0:>18.3g}'.format(cov), \
                '{0:>18.3g}'.format(r))
        
#-----------------------Main Method Starts Here------------------------
#read file
x, y = file_read('EP305_test_data.txt')

#call the graph function to plot graph
graph_data(x, y)

#calculate covarince and correlaiton
cov = covar(x, y)
r = correl(x, y)

#plot the table
table(x, y, cov, r)