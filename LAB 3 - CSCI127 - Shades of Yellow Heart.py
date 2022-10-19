#Name: Drew Zambelli
#Email: drew.zambelli04@myhunter.cuny.edu
#Date: September 20, 2021
#This program prints a yellow turtle twice that grows

import turtle



tess = turtle.Turtle()
turtle.colormode(255)

tess.shape("turtle")

tess.left(60)
for i in range (0,255,10):
    tess.forward(10)
    tess.pensize(i)
    tess.color(i,i,0)

tess.penup()
tess.backward(260)
tess.pendown()
tess.pensize(0)
tess.color("black")

tess.left(60)
for i in range (0,255,10):
    tess.forward(10)
    tess.pensize(i)
    tess.color(i,i,0)
