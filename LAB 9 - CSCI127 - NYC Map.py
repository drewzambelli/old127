#Name: Drew Zambelli
#Email: drew.zambelli04@myhunter.cuny.edu
#Date: October 30, 2021
#This program prints NYC Map Little Island

import folium
nycLittle = folium.Map(location=[40.75, -74.125],zoom_start=10)
folium.Marker(location = [40.7420577, -74.0101494], popup = "Little Island").add_to(nycLittle)

nycLittle.save(outfile='nycMap.html')
