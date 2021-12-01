# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 19:01:44 2021

@author: tmccr
"""

import turtle as t

t.hideturtle()
t.speed(speed=0)
t.title("American Flag")

def draw_rectangle(length,height,color):
    t.color(color)
    if color == "white" or "#FFFFFF":
        t.color("black")
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    for i in range(2):
        t.forward(length)
        t.right(90)
        t.forward(height)
        t.right(90)
    t.end_fill()
    t.penup()
        
def draw_star(size,color):
    t.forward(0.5*size)
    t.right(162)
    t.color(color)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    for i in range(5):
        t.forward(size)
        t.right(144)
    t.end_fill()
    t.penup()
    t.left(162)
    t.backward(0.5*size)
    
def draw_star_array(rows,columns,E,G,size,color):
    for i in range(rows//2):
        t.backward(E)
        t.right(90)
        t.forward(G)
        for i in range(columns//2):
            t.left(90)
            draw_star(size,color)
            t.right(90)
            t.forward(G*2)
        t.left(90)
        draw_star(size,color)
        t.right(90)
        t.backward(G*columns)
        t.left(90)
        t.backward(E)
        t.right(90)
        for i in range(columns//2):
            t.forward(G*2)
            t.left(90)
            draw_star(size,color)
            t.right(90)
        t.backward(G*(columns-1))
        t.left(90)
    if (rows%2) == 1:
        t.backward(E)
        t.right(90)
        t.forward(G)
        for i in range(columns//2):
            t.left(90)
            draw_star(size,color)
            t.right(90)
            t.forward(G*2)
        t.left(90)
        draw_star(size,color)
        t.right(90)
        t.backward(G*columns)
        t.left(90)
        t.backward(E)

def get_color(color):
    if color == "white":
        return "#FFFFFF"
    if color == "red":
        return "#B22234"
    if color == "blue":
        return "#3C3B6E"

def draw_flag(height):

    A = (height)*1.0    # Hoist (height of the flag)
    B = (height)*1.9    # Fly (width) of the flag
    C = A*(7/13)        # Hoist (height) of the canton ("union)
    D = B*(2/5)         # Fly (width) of the canton
    E = F = (C/10)      # One-tenth of the height of the Canton
    G = H = (D/12)      # One twelfth of the width of the canton
    K = (A/13)*(4/5)    # Diameter of star
    L = (A/13)          # Width of stripe
    
    t.backward(B/2)

    draw_rectangle(B,A,get_color("white"))           #"white"
    for i in range(6):
        draw_rectangle(B,L,get_color("red"))       #"red"
        t.left(90)
        t.backward(L*2)
        t.right(90)
    draw_rectangle(B,L,get_color("red"))           #"red"
    t.left(90)
    t.forward(A-L)
    t.right(90)
    
    draw_rectangle(D,C,get_color("blue"))           #"blue"
    t.left(90)
    draw_star_array(9,11,E,G,K,get_color("white"))   #"white"

def main():    
    draw_flag(200)

    t.exitonclick()
    t.done()

if __name__ == "__main__":
    main()