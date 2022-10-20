#Name: Drew Zambelli
#Email: drew.zambelli04@myhunter.cuny.edu
#Date: October 6, 2021
#This program prints Square Eye

import turtle
wn = turtle.Screen()

drew = turtle.Turtle()
turtle.colormode(255)
turtle.bgcolor("khaki")

drew.pensize(5)

drew.speed(0)

for i in range (36):
    drew.pencolor(0,i*7,0)
    drew.forward(10)
    drew.left(10)
    for c in range(4):
        drew.left(90)
        drew.forward(300)
        drew.backward(50)
