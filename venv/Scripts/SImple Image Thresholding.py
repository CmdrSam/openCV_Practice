import cv2
import numpy as np

img = cv2.imread('Images/gradient.png',1)
_,th1 = cv2.threshold(img, 127,255,cv2.THRESH_BINARY)
_,th2 = cv2.threshold(img, 50,255,cv2.THRESH_BINARY)
_,th3 = cv2.threshold(img,150,255,cv2.THRESH_TRUNC)


cv2.imshow("Gradient",img)
cv2.imshow("Thresholded Image 1",th1)
cv2.imshow("Thresholded Image 2",th2)\
cv2.imshow("Thresholded Image 3",th3)

cv2.waitKey(0)
cv2.destroyAllWindows()