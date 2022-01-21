import cv2
img1 = cv2.imread('AB1.jpg', 1)
img2 = cv2.imread('A2.jpg', 1)

img1 = cv2.resize(img1,(512,512))
img2 = cv2.resize(img2,(512,512))

img = cv2.add(img1, img2)

cv2.imshow('image', img)
added = 'added.jpg'

cv2.imwrite(added, img)