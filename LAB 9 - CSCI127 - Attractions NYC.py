#Name: Drew Zambelli
#Email: drew.zambelli04@myhunter.cuny.edu
#Date: October 30, 2021
#This program prints NYC attractions

import folium
import pandas as pd

userInput = input("Enter CSV file name:")
userOutput = input("Enter output file:")

attractions = pd.read_csv(userInput)
mapNYC = folium.Map(location=[40.768731, -73.964915], tiles="Cartodb Positron")

for index, row in attractions.iterrows():
    name = row["NAME"]
    lon = row["LATITUDE"]
    lat = row["LONGITUDE"]
    newMarker = folium.Marker([lat, lon], popup = name).add_to(mapNYC)

mapNYC.save(outfile=userOutput)
    
