import pandas as pd
import cv2
img = cv2.imread('lena.jpg',1)


cv2.imshow('Lenna\'s Image',img)

k = cv2.waitKey()
if (k==27):
    cv2.destroyAllWindows()

# Checking if git hub desktop works