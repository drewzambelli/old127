import numpy as np
import matplotlib.pyplot as plt

print ("------------------------------------------\nWelcome to the Color Maker!\n------------------------------------------")
print("Please enter for each rbg color the value in which to increase/decrease them.")
print("If all 3 values given are 0, the program will end and save the resulting image.")

outFile = input("Enter outfile name:")

img = np.zeros ( (10, 10, 3) )

buildRed = 0
buildGreen = 0
buildBlue = 0

red = 1
green = 1
blue = 1

while red != 0 or green != 0 or blue != 0:
    red = int(input("How much do you want to change the red value by?"))
    green = int(input("How much do you want to change the green value by?"))
    blue = int(input("How much do you want to change the blue value by?"))

    buildRed = buildRed + (red/255)
    buildGreen = buildGreen + (green/255)
    buildBlue = buildBlue + (blue/255)
    if buildRed > 1.0:
        buildRed = 1.0
    if buildGreen > 1.0:
        buildGreen = 1.0
    if buildBlue > 1.0:
        buildBlue = 1.0
    if buildRed < 0:
        buildRed = 0
    if buildGreen < 0:
        buildGreen = 0
    if buildBlue < 0:
        buildBlue = 0
    
    print("The current rgb values are: {}, {}, {}".format(buildRed, buildGreen, buildBlue))

img[:,:,0] = buildRed
img[:,:,1] = buildGreen
img[:,:,2] = buildBlue

plt.imshow(img)

plt.imsave(outFile, img)
