import cv2

img = cv2.imread('AB1.jpg')

ret, bw_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

bw = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

cv2.imshow("Binary", bw_img)

binary = 'binary.jpg'

cv2.imwrite(binary, bw_img)
  
cv2.waitKey(0)