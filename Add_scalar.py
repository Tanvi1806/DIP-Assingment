import cv2
img1 = cv2.imread('AB1.jpg', 1)
img2 = 20

img = cv2.add(img1, img2)

cv2.imshow('image', img)
add_scalar = 'added_scalar.jpg'

cv2.imwrite(add_scalar, img)

cv2.waitKey(0)