#Name: Drew Zambelli
#Email: drew.zambelli04@myhunter.cuny.edu
#Date: October 13, 2021
#This program prints Shelter Census


import pandas as pd
import matplotlib.pyplot as plt

inquiry = input("Enter name of input file:")
outName = input("Enter name of output file:")

homeless = pd.read_csv(inquiry)

homeless["Fraction Single Adults"] = homeless["Total Single Adults in Shelter"]/homeless["Total Individuals in Shelter"]

homeless.plot(x = "Date of Census", y = "Fraction Single Adults" )

fig = plt.gcf()
fig.savefig(outName)
