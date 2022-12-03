#Name: Drew Zambelli
#Email: drew.zambelli04@myhunter.cuny.edu
#Date: September 30, 2021
#This program prints P-Logo

import matplotlib.pyplot as plt
import numpy as np

img = np.zeros( (30,30,3) )


img[0:,:6,0] = 1
img[0:21,25:31,0] = 1

img[0:,:6,2] = 1
img[0:21,25:31,2] = 1

img[0:6, :, 0] =1
img[0:6, :, 2] =1

img[15:21, :, 0] = 1
img[15:21, :, 2] = 1

plt.imshow(img)
plt.show()

plt.imsave("logo.png", img)

