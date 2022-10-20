#Name: Drew Zambelli
#Email: drew.zambelli04@myhunter.cuny.edu
#Date: October 5, 2021
#This program prints Plaid Stripes

import matplotlib.pyplot as plt
import numpy as np

size = int(input("what is the size of the file?"))
saving = input("Enter output file:")
  
img = np.ones( ( size, size, 3) )

img[1::2, 0:, 0] = .94
img[1::2, 0:, 1] = .90
img[1::2, 0:, 2] = .55

img[0:, 1::2, 0] = .73
img[0:, 1::2, 1] = .56
img[0:, 1::2, 2] = .56

plt.imsave(saving, img)
