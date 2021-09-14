# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 14:49:56 2021

@author: tmccr
STAT 1129 HW1
"""


#Create a list of your favorite colors. [0.5 point]
fav_colors = ["blue","black","white","green","orange"]

#Generate a list of numbers from 30 to 60 with interval 3, for example, 30, 33, 36, …… 60. [1 point]
num_list = list(range(30,61,3))
#print(num_list)

#Transfer this list into tuple [0.5 point]
tup_num_list = tuple(num_list)
#print(tup_num_list)

#Write code based on the following steps. Total 2 points.
#✓ Create an empty list.
prob3_list = []
#✓ append integers from 0 to 5 to this list; [0.5 point]
for i in range(6):
    prob3_list.append(i)
#✓ delete item 2; [0.5 point]
del prob3_list[2]
#✓ insert 2.0 to the original position where 2 was; [0.5 point]
prob3_list.insert(2,2.0)
#✓ return the length, maximal and minimal values of the newest list; [0.5 point]
print(len(prob3_list))
print(max(prob3_list))
print(min(prob3_list))

#Generate a list from 1 to 10, then sum up all the items. Eg: 1+2+3+…+ 10. [1 point]
prob4_list = list(range(1,11))

tot = 0
for i in prob4_list:
    tot += i
print(tot)
#print(sum(prob4_list))   Alternative/quicker method
