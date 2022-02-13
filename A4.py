import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('AB1.jpg')
b, g, r = cv2.split(img)
zeros_ch = np.zeros(img.shape[0:2], dtype="uint8")

blue_img = cv2.merge([b, zeros_ch, zeros_ch])
cv2.imshow("Blue Image", blue_img)

green_img = cv2.merge([zeros_ch, g, zeros_ch])
cv2.imshow("Green Image", green_img)
 
red_img = cv2.merge([zeros_ch, zeros_ch, r])
cv2.imshow("Red Image", red_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
 
 