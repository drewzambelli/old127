#Name: Drew Zambelli
#Email: drew.zambelli04@myhunter.cuny.edu
#Date: September 20, 2021
#This program prints shades of yellow to red

import turtle

turtle.colormode(255)

tess = turtle.Turtle()
tess.shape("turtle")

tess.right(90)
tess.penup()
tess.backward(100)
tess.pendown()


for i in range(0,255,10):
    tess.forward(10)
    tess.pensize(i)
    tess.color(255, 255-i, 0)

tess.penup()
tess.backward(260)
tess.left(90)
tess.pensize(0)
tess.color(0, 0, 0)
tess.pendown()

for i in range(0,255,10):
    tess.forward(10)
    tess.pensize(i)
    tess.color(255, 255-i, 0)
  
