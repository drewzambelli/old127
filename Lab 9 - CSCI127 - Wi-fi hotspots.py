#Name: Drew Zambelli
#Email: drew.zambelli04@myhunter.cuny.edu
#Date: October 30, 2021
#This program prints NYC wi-fi spots

import folium
import pandas as pd

userInput = input("Please enter the name of the input file:")
userOutput = input("Please enter the name of the output file:")
userBorough = input("Please enter the name of the borough:")


hotSpots = pd.read_csv(userInput)
mapSpots = folium.Map(location=[40.768731, -73.964915], tiles="Stamen Watercolor")

groupedLocation = hotSpots.groupby("City")

manh = groupedLocation.get_group(userBorough)

for index, row in manh.iterrows():
    address = row["Location"]
    lon = row["Longitude"]
    lat = row["Latitude"]
    newMarker = folium.Marker([lat, lon], popup = address).add_to(mapSpots)

mapSpots.save(outfile = userOutput)
