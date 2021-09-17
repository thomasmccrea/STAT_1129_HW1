# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 20:47:28 2021

@author: tmccr
"""
#1. Using While Loop. As long as n is less than 10, print out n. However, when n equals to 5, stop the loop. (Initialize n=0). [0.5 point]
n=0
while n < 10:
    print(n)
    n += 1
    if n == 5:
        break
#2. Using while loop. Initialize n=0. While n is < 5, print out n. Otherwise, print out $n “is not less than 5”.[0.5 point]
n = 0
while n < 5:
    print (n)
    n += 1
print(n,"is not less than 5")
#3. Create your favorite fruit list, using For Loop, print out all the fruits in your list. However, when one fruit name equals to “apple”, stop the loop. [0.5 point]
fav_fruit_list = ["pineapples","apples","oranges","blueberries"]
for i in fav_fruit_list:
    if i != "apples":
        print("I like",i)
    else:
        print("Are",i,"really fruits?")
        break
#4. Add all the integers from 1 to 30, print out the sum. Using while loop. [0.5 point]
n = 0
i = 0
while n < 30:
    n += 1
    i += n
print(i)
#5. Create a weather dictionary. Using for loop, print out all the keys and values in the same line. The output should look like this [1 point]
weather = {"Sunny":"Play",
           "Rainy":"Watch TV",
           "Cloudy":"Walk"}
print(weather)
#or
keys = ""
values = ""
for i in weather:
    keys += i+", "
    values += weather[i]+", "
print("Keys:",keys[0:-2],";","Values:",values[0:-2])
#or
for i in weather:
    print("When it's",i,"let us",weather[i])
#Then add a new pair (“snowy”, “ski”) to your dictionary. [0.5 point]
weather.update({"Snowy":"Ski"})
print(weather)
#or
weather["Snowy"] = "Ski"
print(weather)
#6. Using if … else statement, write the above weather dictionary statement. For example, if weather is sunny, print out play, if weather is rainy, pint out watch TV…. [0.5 point] 
forcast = input("please type out one of the weather options: 'Sunny', 'Rainy', or 'Cloudy'\nType here: ")
if forcast == "Sunny":
    print(weather[forcast])
elif forcast == "Rainy":
    print(weather[forcast])
elif forcast == "Cloudy":
    print(weather[forcast])
else:
    print("Uh Oh! Looks like you mispelled something in the input. Please run the code again to try again")
#7. Using if…elif…else statement, to help grade students’ score. You can define grade yourself, for example, grade = 55 [1 point]
student_score = int(input("Please input the student's score\nType here: "))
if student_score >= 90:
    print("A")
elif student_score >= 80 and student_score < 90:
    print("B")
elif student_score >= 70 and student_score < 80:
    print("C")
elif student_score >= 60 and student_score < 70:
    print("D")
elif student_score < 60:
    print("F")
    

