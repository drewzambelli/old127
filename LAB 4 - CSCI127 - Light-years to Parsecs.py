#Name: Drew Zambelli
#Email: drew.zambelli04@myhunter.cuny.edu
#Date: September 27, 2021
#This program prints Parsecs to Light-Years and vice-versa

decision = input("Please enter the conversion you want to do: 'a' for Light-Year to Parsec conversion 'b' for Parsec to Light-Year. ")

print("your seletion: " + decision)

if decision == "a":
    lightYears = float(input("Please enter a number of Light-Years:"))
    print("{} Light-years is equal to {} Parsecs.".format(lightYears, lightYears/3.26156))

if decision == "b":
    parsecs = float(input("Please enter a number of Parsecs:"))
    print("{} Parsecs is equal to {} Light-Years.".format(parsecs, parsecs*3.26156))
