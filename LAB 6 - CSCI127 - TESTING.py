#Name: Drew Zambelli
#Email: drew.zambelli04@myhunter.cuny.edu
#Date: October 7, 2021
#This program prints Ramen!

import pandas as pd
import matplotlib.pyplot as plt

file = input("Enter file name:")

df = pd.read_csv("ramenRatings.csv")
df["Stars"] = pd.to_numeric(df["Stars"], downcast="float")


groupedStyle = df.groupby("Style")

print("The average stars per serving style:")

s = df.Series(["Bar: ",groupedStyle.get_group("Bar")["Stars"].mean(),"Bowl: ",groupedStyle.get_group("Bowl")["Stars"].mean(),"Box: ",groupedStyle.get_group("Box")["Stars"].mean()])
print("Can: ",groupedStyle.get_group("Can")["Stars"].mean())
print("Cup: ",groupedStyle.get_group("Cup")["Stars"].mean())
print("Pack: ",groupedStyle.get_group("Pack")["Stars"].mean())
print("Tray: ",groupedStyle.get_group("Tray")["Stars"].mean())
print (s)
groupedLocation = df.groupby("Country")

print("KAKO has the lowest rating in Singapore with",groupedLocation.get_group("Singapore")["Stars"].min(), "stars.")

