#Name: Drew Zambelli
#Email: drew.zambelli04@myhunter.cuny.edu
#Date: October 1, 2021
#This program does Elevation stuff

#Import the libraries for arrays and displaying images:
import numpy as np
import matplotlib.pyplot as plt


#Read in the data to an array, called elevations:
elevations = np.loadtxt('elevationsNYC.txt')

#Take the shape (dimensions) of the elevations
#  and add another dimension to hold the 3 color channels:
mapShape = elevations.shape + (3,)

#Create a blank image that's all zeros:
floodMap = np.zeros(mapShape)

for row in range(mapShape[0]):
    for col in range(mapShape[1]):
        if elevations[row,col] <= 0:
            #Below sea level
           floodMap[row,col,2] = 0     #Set the blue channel to 100%
           floodMap[row, col, 0:2] = 1
        elif elevations[row,col] > 5 and elevations[row, col] <= 20:
            #Below the storm surge of Hurricane Sandy (flooding likely)
           floodMap[row,col,0:3] = 0.5     #Set the red channel to 100%
        elif elevations[row, col] >20:
            floodMap[row, col, 1] = 1
        else:
            #Above the 6 foot storm surge and didn't flood
            floodMap[row,col,0] = 1.0   #Set the green channel to 100%

#Save the image:
plt.imsave('floodMap.png', floodMap)
