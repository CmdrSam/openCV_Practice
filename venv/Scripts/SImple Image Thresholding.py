import cv2
import numpy as np

img = cv2.imread('Images/gradient.png',1)
_,th1 = cv2.threshold(img, 127,255,cv2.THRESH_BINARY)   # Any pixel before 127 is turned black and vice versa
_,th2 = cv2.threshold(img, 50,255,cv2.THRESH_BINARY_INV)    # Opposite of THRESH_BINARY, here any pixel before 50 is turned white
_,th3 = cv2.threshold(img,150,255,cv2.THRESH_TRUNC)     #The  gradient stops changing after 150px
_,th4 = cv2.threshold(img,100,255,cv2.THRESH_TOZERO)    # When Pixel value is less than threshold(150) it is turned to 0

cv2.imshow("Gradient",img)
cv2.imshow("Thresholded Image 1",th1)
cv2.imshow("Thresholded Image 2",th2)
cv2.imshow("Thresholded Image 3",th3)
cv2.imshow("Thresholded Image 4",th4)

cv2.waitKey(0)
cv2.destroyAllWindows()