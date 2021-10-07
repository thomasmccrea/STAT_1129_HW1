# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 18:10:44 2021

@author: tmccr
"""
import numpy as np
from matplotlib import pyplot as plt

#Question 1: Creating this array (as shown in figure) with the array function of numpy.
#Using the array, multiply with 2 (Element-wise multiplication). Return the dimension and
#shape of this array.

#x = np.arange(1,13).reshape(3,4)
#print(x)

mat1 = np.array(range(1,13)).reshape(3,4)
print(mat1)

print(mat1*2)
print(mat1.ndim)
print(mat1.shape)

#Question 2: Iterating through a Multidimensional array’s Elements. Using nested for loop, to
#print out array in question 1. So that your printout result will look like:
#1 2 3 4
#5 6 7 8
#9 10 11 12
#Then iterating through a Multidimensional array’s Elements. Using flat method, to print out array in
#question 1. So that your printout result will look like:
#1 2 3 4 5 6 7 8 9 10 11 12 

# Before I really understood what end= was doing
#for r in mat1:
#    lin = ""
#    for c in r:
#        lin += str(c)+" "
#    print(lin)

for r in mat1:
    for c in r:
        print(c,end=" ")
    print()

# I was a little puzzled why the end= was changing my print statement from vertical to horizontal, but then it dawned on me that
# the default was set to \n or to add a new line, by specifying the end, we are ommiting that new line statement and as such
# it doesn't skip to the next line. That's why the empty print() in the code above is equal to print(end="\n")
for i in mat1.flat:
    print(i,end=" ")


#Question 3: create x integer array from 1 to 6, create y integer array from 5 to 10. using x
#integer array as X-axis, using y integer array as Y-axis, plot a line.

xpoints1 = range(1,7)
ypoints1 = range(5,11)
plt.plot(xpoints1,ypoints1)
plt.show()

#Question 4: Draw a line in a diagram from position (3, 2) to (6, 8) then to (9, 1) and finally to
#position (12, 10). Add markers to all the four points.

xpoints2 = np.array([3,6,9,12])
ypoints2 = np.array([2,8,1,10])
plt.plot(xpoints2,ypoints2,marker="D")
plt.show()

#Question 5: plot 6 points: (0,2), (1,4), (2, 6), (3, 14), (4, 10), (5, 12), using dashed line, using
#red color to draw the line, but marker size is 10, marker color is green. 

ypoints3 = np.array([2,4,6,14,10,12])
plt.plot(ypoints3,"D--r",ms=10,mec="g",mfc="g")
plt.show()