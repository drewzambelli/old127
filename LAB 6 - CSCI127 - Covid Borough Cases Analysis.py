#Name: Drew Zambelli
#Email: drew.zambelli04@myhunter.cuny.edu
#Date: October 6, 2021
#This program prints Covid Borough Cases Analysis

import matplotlib.pyplot as plt
import pandas as pd

covid = pd.read_csv("covidCases.csv")

borough = input("Enter borough name:")
saving = input("Enter output name:")


print("Min:", covid[borough].min())
print("Max:", covid[borough].max())
print("Mean:", covid[borough].mean())
print("Median:", covid[borough].median())
print("Standard Deviation:", covid[borough].std())

covid["Fraction"] = covid[borough]/covid["Case Count"]

covid.plot( x = "Date of Interest", y = "Fraction")

fig = plt.gcf()
fig.savefig(saving)




