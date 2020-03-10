import cv2
import numpy as np

img = cv2.imread('lena.jpg',1)
print(img.shape)
eyes = img[230:300,209:350]

cv2.imshow('Lenna Darling',img)

img[20:90,20:161] = eyes

cv2.imshow('More eyes',img)

cv2.waitKey(0)
cv2.destroyAllWindows()