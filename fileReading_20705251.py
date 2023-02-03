# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 14:48:05 2022

@author: 20705251
"""

#file_name could be any name but it should be the same throughout
file_name = "pendulum.txt"

#open a file for reading
in_file = open(file_name, 'r')

#create 2 lists. Lists because I want to use the append function 
sp_length_v3 = []
sp_period_v3 = []

header = in_file.readline() #read in the header separately
print(header)

for line in in_file:
    values = line.split() #read data from each line in list
    sp_length_v3.append(float(values[1])) #column 2 convert to float
    sp_period_v3.append(float(values[2])) #column 3 convert to float
    
    
for i in range(len(sp_length_v3)):
    print('{0:>15}'.format(i), \
          '{0:>15.3f}'.format(sp_length_v3[i]), \
        '{0:>15.3f}'.format(sp_period_v3[i]))

in_file.close()