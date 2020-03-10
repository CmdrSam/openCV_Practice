import pandas as pd
import cv2
img = cv2.imread('lena.jpg',1)
print(img)

cv2.imshow('Darling',img)
k = cv2.waitKey(0)
if (k==27):
    cv2.destroyAllWindows()
elif(k==ord('s')):
    cv2.imwrite('Lenna_copy.png',img)
    cv2.destroyAllWindows()
