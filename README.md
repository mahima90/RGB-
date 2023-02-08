# RGB-
RGB in python
import skimage.io as io
import matplotlib.pyplot as plt
import numpy as np
img=io.imread('1.jpg')
plt.imshow(img)
img.shape
# split
red=img[:,:,0]
green=img[:,:,1]
blue=img[:,:,2]
plt.imshow(red,cmap="Reds")
plt.imshow(blue,cmap="Blues")
plt.imshow(green,cmap="Greens")
