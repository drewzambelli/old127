#Name: Drew Zambelli
#Email: drew.zambelli04@myhunter.cuny.edu
#Date: September 1, 2021
#This program draws a Pin-Wheel

import turtle
wn = turtle.Screen()

drew = turtle.Turtle()

drew.shape("arrow")
drew.color("purple")
drew.pensize(3)

drew.forward(30)

for i in range(3):
    drew.forward(50)
    drew.right(120)

drew.backward(30)
drew.right(90)
drew.forward(30)

for i in range(3):
    drew.forward(50)
    drew.right(120)

drew.backward(30)
drew.right(90)
drew.forward(30)

for i in range(3):
    drew.forward(50)
    drew.right(120)

drew.backward(30)
drew.right(90)
drew.forward(30)

for i in range(3):
    drew.forward(50)
    drew.right(120)

drew.backward(30)

wn.exitonclick()
