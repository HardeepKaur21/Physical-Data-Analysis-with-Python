# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 21:29:44 2022

@author: 20705251 - Hardeep Kaur Gill (Python 3.9)

Description:
    This code is about figuring out the parameters in the model 
    y = ax + y0 using linear model fitting. The result is a file in the same 
    directory as this python file that has 12000 estimates of the parameters 
    in the model.This is done using the Monte Carlo approach as errors on
    x and y are accounted for.
    
"""
#--------Imported Libraries--------
import numpy as np #for various functions including random(), sqrt() and empty

#----------------User Defined Functions---------------------
def file_write(all_params, file_name): #function three:
    """
    This function creates a file with the name "file_name" and inputs data 
    from the list all_params

    Parameters
    ----------
    all_params : list
        used to input data from it.
    file_name : string
        The file to be created

    Returns
    -------
    None.

    """
    
    #open a file for writing
    out_file = open(file_name, 'w')
    
        
    #write the values to the file
    for i in range(len(all_params)):
        print('{0:<7.7g}'.format(all_params[i][0]), "\t",\
              '{0:>7.7g}'.format(all_params[i][1]), file = out_file)
    #close the file
    out_file.close()


#------------------------Main Code Starts Here------------------
#inform the user of what is happening
print('This code is about figuring out the parameters in the model \
y = ax + y0 using linear model fitting. The result is a file in the same \
directory as this python file that has 12000 estimates of the parameters in \
the model.\n\nThis is done using the Monte Carlo approach as errors on\
 x and y are accounted for.')

M1, M2 = 0, 100 #assumed model parameters
sigmaX = 0.001 #the normal uncertainty of each set measurement point
sigmaY = 0.1 #additional uncertainty of the measured quantity
N = 12_000 #number of repeats


#independent variable 
x0 = np.linspace(2, 5, 50)
x = x0 + np.random.normal(100.0, sigmaX, size = x0.size)

y0 = M1*(x**2) + M2 #model

#it is a general rule of thumb to take the sqrt of N for the bins of a hist
BINS = min(int(np.sqrt(N)), 100) #to make it look nice 

all_params = np.empty((N, 2)) #create an empty array to store all fitting
# results it has N rows and 2 column

M = np.column_stack((x**2, np.ones_like(x**2)))


for i in range(N):
    #y is y0 with the added random factor
    y = y0 + np.random.normal(0.0, sigmaY, size = y0.size)
    
    #perform the fit 
    params, res, rank, s = np.linalg.lstsq(M, y, rcond = None)
   
    a, f = params

    all_params[i, :] = a, f #store the model params in an array


file_write(all_params, 'EP305simdata251.txt')