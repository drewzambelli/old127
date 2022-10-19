#Name: Drew Zambelli
#Email: drew.zambelli04@myhunter.cuny.edu
#Date: September 21, 2021
#This program prints a colored square

mess = input("Please enter a 6-digit hexadecimal number:")

import turtle

tess = turtle.Turtle()
tess.shape("turtle")

userColor = "#" + mess

tess.color(userColor)


for i in range (4):
    tess.left(90)
    tess.forward(100)
    tess.stamp()
