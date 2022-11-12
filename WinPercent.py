#Name: Drew Zambelli
#Email: drew.zambelli04@myhunter.cuny.edu
#Date: October 13, 2021
#This program prints Super Bowl stuff

import pandas as pd
import matplotlib.pyplot as plt

mess = input("Enter name of input file:")
saving = input("Enter name of output file:")

df = pd.read_csv(mess)

df["Date"] = pd.to_datetime(df["Date"].apply(str))

df["% Points"] = df["Winner Pts"]/(df["Winner Pts"]+df["Loser Pts"]) *100

df.plot(x= "Date", y="% Points")

fig = plt.gcf()
fig.savefig(saving)

