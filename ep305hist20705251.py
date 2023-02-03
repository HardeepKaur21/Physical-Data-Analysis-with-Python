# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 17:25:12 2022

@author: Hardeep Kaur Gill - 20705251

Description:
    This code is written to read the data from the file sunspots.txt, 
    calculate the mean, median, mode and standard deviation of the sunspot 
    data and plot a histogram of the number of sunspots/month distributed 
    over 40 bins.
"""


#Import the libraries---------------------------------
import numpy as np #needed for arrays and other related functions
import matplotlib.pyplot as plt #needed to plot the historgram 


#------------User Defined Functions-------------------
def mode(a):
    """

    Parameters
    ----------
    a : array
        To find the most occuring value in this array.

    Returns
    -------
    integer
        The most reoccuring value.

    """
    #this function returns 2 arrays one that holds all of the unique values
    #in the array and the other holds the amount of time each number appears 
    vals,counts = np.unique(a, return_counts=True)
    
    #this function takes in the array with the count of each value in the 
    #original array, and returns the index of the maximum value
    index = np.argmax(counts)
    
    return vals[index] #now we just need to return the value in that index


#-------------------Main code starts here----------------
#Load the data
data = np.loadtxt("sunspots.txt", float)
#x = data[:, 0] #read every row in the first column 
y = data[:,1] #read every row in the second column, we need this column


#Convert to arrays
b = np.array(y) 

#Calculate the mean
bmean = np.mean(b)

#Calculate the median
bmedian = np.median(b)

#Calculate the mode
bmode = mode(b)

#Calculate the standard deviation
bstd = np.std(b)

#Define the bins
bins = 40

#plot the histogram
plt.hist(y, bins, color = 'm')
plt.grid(False) #I wanted to put a grid on but it does not look good

#customize the histogram
plt.title('Number of sunspots/month over 40 bins', color='c', fontsize = 14)
plt.xlabel("Bins")
plt.ylabel("Sunspot Number/Month")

#Include the statistcal data on the histogram

plt.text(70, 350, 'Average No Sunspots/Month: {0:<9.3f}'.format(bmean))
plt.text(70, 320, 'Median of No Sunspots/Month: {0:<9.3f}'.format(bmedian))
plt.text(70, 290, 'Mode of No Sunspots/Month: {0:<9.3f}'.format(bmode))
plt.text(70, 260,'Standard Dev of No Sunspots/Month: {0:<5.3f}'.format(bstd))

plt.show()