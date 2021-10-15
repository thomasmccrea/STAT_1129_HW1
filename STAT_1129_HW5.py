# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 05:35:43 2021

@author: tmccr
"""
import numpy as np
from matplotlib import pyplot as plt

#Question 1: Plot a figure with multiple lines, as shown in figure, set the line width (1 point)

x1 = np.array(range(5))
y1 = np.array(range(5))

plt.plot(x1,y1,x1,y1+4,x1,y1+8, lw = "2")
plt.show()

#Question 2, Plot a histogram based on 800 randomly generated data samples, specify mean value to
#be 0, standard deviation to be 0.2, following normal distribution. (1 point)

mu, sigma = 0, 0.2
s = np.random.normal(mu, sigma, 800)
plt.hist(s)
plt.show()

#Question 3: You have a dictionary:
mydic = {"Apples": 45, "Bananas":25, "Cherries":15, "Dates":20}
#Create a Pie chat and a bar chat, to represent each fruit and their portion.
#You can define an fruit list and a count list, append all the fruit names into fruit list, append all the
#numbers into count list, then print out. Your output should look like this: (2 points)
fruitlist = []
countlist = []

for i in mydic:
    fruitlist.append(i) 
    countlist.append(mydic[i])

#print(fruitlist,"\n"+str(countlist))

print(fruitlist)
print(countlist)

plt.pie(np.array(countlist), labels = fruitlist, explode = [0.1,0.1,0.1,0.1])
plt.legend(bbox_to_anchor = (1.5,1), loc = "upper right")
plt.show()
plt.bar(np.array(fruitlist),np.array(countlist))
plt.show()

#Question 4, Create a scatter plot where we are going to compare two groups of marks: art and
#science. Specify a color for each scatter plot. Create x-label and y-label and title of this figure.
#Create a legend. You can Google to search how to do that. (2 points)

marks_range = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100] # this is x-axis values
math_marks = [88, 92, 80, 89, 90, 80, 60, 88, 80, 84] # this is the math marks
science_marks = [75, 59, 69, 48, 65, 56, 32, 45, 20, 30] # this is the science marks

plt.scatter(marks_range, math_marks, color = "r")
plt.scatter(marks_range, science_marks,color = "g")
plt.xlabel("Marks Range") 
plt.ylabel("Marks Scored")
plt.legend(["Math marks", "Science marks"],loc="lower left")
plt.show()

#Question 5: Design a figure with layout 1 by 4, using subplots() function. In this figure, you are
#required to integrate four plots among: scatter plot, multiple line plot, bar chat, pie chat, dots,
#histogram. I put one example here. Add title for each subplot. (2 points)

plt.subplot(1,4,1)
A = np.random.rand(10)
B = np.random.rand(10)
plt.scatter(A, B)
plt.title("Scatter Plot")

plt.subplot(1,4,2)
x = np.array(range(6))
y_1 = np.array([4,2,6,1,7,9])
y_2 = np.array([2,8,7,4,3,5])
plt.plot(x,y_1,x,y_2)
plt.title("Multiple Line Plot")

plt.subplot(1,4,3)
factors = np.array(["A","B","C","D"])
yi = np.array([20,30,50,80])
plt.bar(factors,yi)
plt.title("Bar Chart")

plt.subplot(1,4,4)
mu, sigma = 18, 23
s = np.random.normal(mu,sigma,2018)
plt.hist(s)
plt.title("Histogram")

plt.show()
