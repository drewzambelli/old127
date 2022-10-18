#Name: Drew Zambelli
#Email: drew.zambelli04@myhunter.cuny.edu
#Date: September 1, 2021
#This program prints a Rhombus-flower

import turtle
wn = turtle.Screen()
wn.bgcolor("khaki")

drew = turtle.Turtle()
drew.shape("turtle")
drew.fillcolor("green")
drew.pensize(3)

for i in range(6):
    drew.forward(100)
    drew.left(45)
    drew.forward(100)
    drew.left(135)
    drew.stamp()
    drew.forward(100)
    drew.left(45)
    drew.forward(100)
    drew.right(180 - (90/6))
    
wn.exitonclick()
