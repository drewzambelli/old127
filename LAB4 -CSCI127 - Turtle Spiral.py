#Name: Drew Zambelli
#Email: drew.zambelli04@myhunter.cuny.edu
#Date: September 30, 2021
#This program prints: Spiral Turtle

import turtle

wn = turtle.Screen()

drew = turtle.Turtle()

stampNum = int(input("Enter number of stamps the turtle will print:"))

turtle.colormode(255)
drew.shape("circle")

drew.penup()

steps = 10
r = 186
g = 164
b = 145

drew.color(r,g,b)


for i in range(stampNum):
    drew.stamp()
    steps = steps + 2
    if r + 3 <= 255 and g + 3 <= 255 and b + 3 <= 255:
        r = r + 3
        g = g + 3
        b = b + 3
    drew.color(r,g,b)
    drew.forward(steps)
    drew.right(24)

wn.exitonclick()
