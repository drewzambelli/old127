#Name: Drew Zambelli
#Email: drew.zambelli04@myhunter.cuny.edu
#Date: September 21, 2021
#This program prints Image Yellow-ish

import matplotlib.pyplot as plt
import numpy as np

request = input("Enter name of the input file:")
requestSecond = input("Enter name of the output file:")

img = plt.imread(request)

img2 = img.copy()
img2[:,:,2] = 0

plt.imsave(requestSecond, img2)
