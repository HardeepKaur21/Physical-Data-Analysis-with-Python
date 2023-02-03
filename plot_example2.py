# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 13:23:08 2022

@author: 20705251
"""

import numpy as np #needed for many standard functions 
import matplotlib.pyplot as plt #needed for plotting

x = [0,1,2,3,4,5,5.5] #enter data to plot 
y = [7,1,2,6,4,3,3]

xx = np.array([0,1,2,3,4,5,5.5]) #using arrays instead of lists here
yy = np.array([7,1,2,6,4,3,3])
zz = yy**2 #if these were lists, I would have to square each element in a loop


plt.subplot(221) #this is the first plot in a in a 2x2 grid
plt.plot(x,y)

plt.subplot(222)
plt.plot(xx, yy, label = 'data') #add label to use in legend 
plt.legend()

plt.subplot(223) #this is the third plot ina 2x2 grid
plt.plot(xx ,zz, 'm*--') #use black (k) circle 

plt.subplot(224) #plt.pyplot(x, y, 'bo', x, y, 'r--')
plt.plot(x, y, 'kD', label = 'points') #plot y vs x. first using blue circles
plt.plot(x, y, 'y-', label = 'line') #and then using a red dashed line
plt.title('My second plot', color = 'b') #add title and change colour to blue
plt.xlabel('x-data', fontsize = 14, color = 'c') #add x-label, change font size
plt.ylabel('measurements')
plt.axis([-1,7,0,8]) #set axes to give some space around data points 
plt.text(2, 0.75, 'this is some text') #can put txt in plot
plt.grid(True) #put grid on 
plt.legend(loc = 'best', fontsize = 10) #find best place for legend, small font
plt.show()