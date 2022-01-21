

import numpy as np
import cv2 

img = cv2.imread('AB1.jpg')
cv2.imshow('image',img)
print(img.shape)
grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale', grayscale)
filename = 'GREY_AB.jpg'
  
# Using cv2.imwrite() method
# Saving the image
cv2.imwrite(filename, grayscale)
  