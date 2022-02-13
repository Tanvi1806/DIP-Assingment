#program to perform all logical operations on two images
import cv2

img1 = cv2.imread("circle.jpg")
img2 = cv2.imread("rectangle.jpg")

img1 = cv2.resize(img1,(512,512))
img2 = cv2.resize(img2,(512,512))

#bitwise_and 
bitwise_and = cv2.bitwise_and(img2, img1)

cv2.imshow("bitwise_and", bitwise_and)

#bitwise_or
bitwise_or = cv2.bitwise_or(img2, img1)

cv2.imshow("bitwise_or", bitwise_or)

#bitwise_xor
bitwise_xor = cv2.bitwise_xor(img2, img1)

cv2.imshow("bitwise_xor", bitwise_xor)

#bitwise_not
bitwise_not = cv2.bitwise_not(img2)

cv2.imshow("bitwise_not", bitwise_not)


cv2.waitKey(0)
cv2.destroyAllWindows()