# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 10:49:41 2021

@author: tmccr
"""

#Question 0:
#Define a dictionary, composed with students name and their grade.
#marks = {‘Andy’:88, ‘Amy’:66, 'James': 90, 'Jules': 55, 'Arthur': 77}
marks = {"Andy":88, "Amy":66, "James": 90, "Jules": 55, "Arthur": 77}

#Question 1: [0.5 point]
#Using for loop, print out all the students name and their grade.
for i in marks:
    print(i,marks[i])

#Question 2: [0.5 point]
#Of this dictionary, calculate all the student’s mean grade, maximal grade, and minimal grade.
print(sum(marks.values()) / len(marks.values()))
print(max(marks.values()))
print(min(marks.values()))

#Question 3: [0.5 point]
#Using for loop or while loop, for all the keys in the dictionary, print out key. However, if ‘J’ appears,
#stop the loop.
for i in marks:
    if "J" in i:
        break
    print(i)

#Question 4: [0.5 point]
#Using for loop or while loop, for all the keys in the dictionary, print out key. However, if ‘J’ appears,
#skip this key, and continue the loop.
for i in marks:
    if "J" in i:
        continue
    print(i)

#Question 5: [1 point]
#Define a function, when call the function, only need to pass student’s name, your function will return
#this student’s grade. If the student name does not exit, print you cannot find this student’s name. 
def studentGrade(student_name):
    if student_name in marks:
        return marks[student_name]
    else:
        print("You cannot find this student's name.")

print(studentGrade("Amy"))

#Question 6: [0.5 point]
#Define a function. Using While Loop. As long as n is less than num, print out n and power of n.
#Otherwise, print out “greater than” the num value. When you call your function, specify the num values
#as 8.
def q6(n,num=8):
    while n <= num:
        print(n,n**2)
        n += 1
    print("greater than",num)

q6(6)

#Question 7: [0.5 point]
#Define a function. add all the integers from 1 to num, print out the sum. Using while loop.
def q7(num):
    n = 1
    tot = 0
    while n <= num:
        tot += n
        n += 1
    print(tot)

q7(5)

#Question 9: [0.5 point]
#Define a function. add all the integers from 1 to num, print out the sum at each step/iteration. Using for loop.
def q9(num):
    tot = 0
    for i in range(1,num+1):
        tot += i
        print(tot)

q9(3)

#Question 10: [0.5 point]
#Define a min function yourself, with 4 arguments. Your function will return the minimal value of the 4
#arguments. Do not use the python built-in functions.
def minimal (v1, v2, v3, v4):
    small = v1
    if v2<small:
        small = v2
    if v3<small:
        small = v3
    if v4<small:
        small = v4
    return small
print(minimal(1,5,-3,8))
    

