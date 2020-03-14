import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('smarties.png',cv2.IMREAD_GRAYSCALE)

_,mask = cv2.threshold(img,220,255,cv2.THRESH_BINARY_INV)

titles = ['image','mask']
image = [img,mask]

for i in range(2):
    plt.subplot(1,2,i+1)
    plt.imshow(image[i],'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])