# -*- coding: utf-8 -*-
"""
Created on Sat May  7 14:03:52 2022

@author: 20705251 - Hardeep Kaur Gill (Python 3.9)

Description:
    This program is designed to input data from a text file called 
    EP305Formal2.txt and print out a statistical summary of a subset of the
    data.That data is also plotted on a graph where the mean, 
    median, mode and standard deviation are displayed as well. 
"""
#---------------------------Needed Libraries-------------------------
import numpy as np
import matplotlib.pyplot as plt

#-------------------------Colour Function--------------------------
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

#----------------------------User Defined Functions-------------------
def mode(a):
    """
    Calculates the mode in a list.
    
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
    header = in_file.readline() #read in the header separately
    #there should be an easier way to define a 2D array but this i found easier
    months = [[], [], [], [], [], [], [], [], [], [], [], [], []]
    
    for line in in_file:
        values = line.split() #read data from each line in list
        
        #to make the appedning process easier 
        for j in range(13):
            months[j].append(float(values[j]))
             
    in_file.close()
    return months

def subset_creator(months, index1, index2):
    """
    This function is used to create a subset of data from the data read from
    the file.

    Parameters
    ----------
    months : 2D array
        The array from which the subset is created.
    index1 : int
        Used to define the starting point of the subset.
    index2 : int
        Used to define the ending point of the subset.

    Returns
    -------
    sub : list
        A list of all data points needed .

    """
    sub  = []
    r = index2 - index1 #7
    ind = months[0].index(index1) #1
    for i in range(ind+1, r+2): #row  #the months array has its rows as the columns
    #of the text file this is why the numbers in range are a bit weird
        for j in range(1, 13): #columns #include 13th column
            sub.append(months[j][i])
    return sub

def minFinder(months, sub):
    '''
    Returns the month (1 means Jan, 2 Feb etc...) and year of the smallest 
    value in the subset.

    Parameters
    ----------
    months : 2D array
        Used because it has all of the values organised and connected by 
        indices.
    sub : list
        The subset of which to calculate the minimum.

    Returns
    -------
    year : int 
        The year at which the min occurs.
    month : int
        The month at which the min occurs.
    minSub : int
        The value of the minimum occurance.

    '''
    minSub = min(sub)
    ind = 0
    
    #to find in which month the minimum value is contained
    for i in range(12):
        if minSub in months[i]:
            month = i
   #month is a 2D array and it has the columns of the text file as rows
   #to find the year in which the min occurs we need to find in which column
   #the min is contained and index zero of that column holds the year.
    for j in range(len(months[i])):
        if (minSub == months[i][j]):
            ind = j
            
    year = months[0][ind] #months[0] holds the years
    
    return year, month, minSub

def maxFinder(months, sub):
    '''
    Returns the month (1 means Jan, 2 Feb etc...) and year of the smallest 
    value in the subset.

    Parameters
    ----------
    months : 2D array
        Used because it has all of the values organised and connected by 
        indices.
    sub : list
        The subset of which to calculate the maximum.

    Returns
    -------
    year : int 
        The year at which the max occurs.
    month : int
        The month at which the max occurs.
    maxSub : int
        The value of the maximum occurance.

    '''
    maxSub = max(sub)
    ind = 0
    
    #to find in which month the minimum value is contained
    for i in range(12):
        if maxSub in months[i]:
            month = i
            
   #month is a 2D array and it has the columns of the text file as rows
   #to find the year in which the max occurs we need to find in which column
   #the max is contained and index zero of that column holds the year.
    for j in range(len(months[month])):
        if (maxSub == months[month][j]):
            ind = j
    year = months[0][ind] #months[0] holds the years
    
    return year, month, maxSub

def graph(subset, mean, median, mode, stDev):
    '''
    This function plots a graph of the data versus its index and includes the
    statistical information as well.

    Parameters
    ----------
    subset : list
        This is the list from wher he data is pulled.
    mean : float
        To include on the graph.
    median : float
        To include on the graph.
    mode : float
        To include on the graph.
    stDev : float
        To include on the graph.

    Returns
    -------
    None.

    '''
    #plot the points
    plt.plot(subset)
    
    #modify the appearance of the graph (blue is favorite :) )
    plt.grid(True)
    plt.xlabel('Index of the Value in the Subset')
    plt.ylabel('Value in the Subset')
    plt.title('Value vs Index', fontsize = 24, color = 'b')
    
    #add the statistical information about the data
    plt.text(90, -15,'Mean: {0:>32.4g}'.format(mean))
    plt.text(90, -17, 'Median: {0:>29.4g}'.format(median))
    plt.text(90, -19, 'Mode: {0:>32.4g}'.format(mode))
    plt.text(90, -21,'Standard Deviation: {0:>10.4g}'.format(stDev))
    
def table(minValue, minYear, minMonth, maxValue, maxYear, maxMonth, \
          mean, median, mode, stDev):
    '''
    This function is used to print a table with all of the calculated 
    information.

    Parameters
    ----------
    minValue : float
        Required info for the table.
    minYear : float
        Required info for the table. Printed as an int but it exists as a 
        float in the code.
    minMonth : float
        Required info for the table. Printed as an int but it exists as a 
        float in the code.
    maxValue : float
        Required info for the table.
    maxYear : float
        Required info for the table. Printed as an int but it exists as a 
        float in the code.
    maxMonth : float
        Required info for the table. Printed as an int but it exists as a 
        float in the code.
    mean : float
        Required info for the table.
    median : float
        Required info for the table.
    mode : float
        Required info for the table.
    stDev : float
        Required info for the table.

    Returns
    -------
    None.

    '''
    #define new lists to make a vertical table
    titles = ['Mean: ', 'Median: ', 'Mode: ', 'Standard Dev: ', \
             'Minimum Value: ', 'Minimum Year: ', 'Minimum Month: ', \
            'Maximum Value: ', 'Maximum Year: ', 'Maximum Month: ']
    values = [mean, median, mode, stDev, minValue, minYear, minMonth, \
              maxValue, maxYear, maxMonth]
    
    #change colors of the title for fun!
    for j in range(len(titles)):
        titles[j] = ColorText(titles[j], 'blue')
    
    #print the titles along with the corresponding value
    for i in range(len(titles)):
        print('{0:<30}'.format(titles[i]), '{0:>10.4g}'.format(values[i]))
    
#-----------------------Main Code Starts Here-------------------
#inform the user of what is happening
print('This program is designed to input data from a text file called \
EP305Formal2.txt and print out a statistical summary of a subset of the\
data.\n\nThat data is also plotted on a graph where the mean, \
median, mode and standard deviation are displayed as well. ')
print()

#read the text file in
months = file_read('EP305Formal2.txt')

#extract the subet
sub = subset_creator(months, 1949, 1956)

#calculate statistical information
mean = np.mean(sub)
median = np.median(sub)
mode = mode(sub)
stDev = np.std(sub)

#calculate the year and the month where the min and max occur
minYear, minMonth, minValue = minFinder(months, sub)
maxYear, maxMonth, maxValue = maxFinder(months, sub)

#plot the graph
graph(sub, mean, median, mode, stDev)
#print(minYear, minMonth, minValue)
#print(maxYear, maxMonth, maxValue)

#print the table
table(minValue, minYear, minMonth, maxValue, maxYear, maxMonth,\
      mean, median, mode, stDev)