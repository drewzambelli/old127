#Name: Drew Zambelli
#Email: drew.zambelli04@myhunter.cuny.edu
#Date: October 14, 2021
#This program prints Video Games

import pandas as pd

csvFile = input("Enter file name:")

videoGames = pd.read_csv(csvFile)

print("There are", videoGames["Name"].count(), "total games")
print("The number of games in each genre are")
print(videoGames["Genre"].value_counts())
print("The top 3 game publishers are")
print(videoGames["Publisher"].value_counts()[0:3])
