#Name: Drew Zambelli
#Email: drew.zambelli04@myhunter.cuny.edu
#Date: October 7, 2021
#This program prints Ramen!

import pandas as pd
import matplotlib.pyplot as plt

file = input("Enter file name:")

df = pd.read_csv("ramenRatings.csv")
df["Stars"] = pd.to_numeric(df["Stars"], downcast="float")


groupedStyle = df.groupby("Style")["Stars"].mean()

print("The average stars per serving style:")
print(groupedStyle)


groupedLocation = df.groupby("Country")

pleaseWork = groupedLocation.get_group("Singapore")["Stars"].idxmin()

print(df["Brand"][pleaseWork],"has the lowest rating in Singapore with", groupedLocation.get_group("Singapore")["Stars"].min(), "stars.")

