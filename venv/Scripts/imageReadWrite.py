import numpy as np
import cv2

img = cv2.imread('lena.jpg',1)
#print(img)  # Printing the Image Matrix

# Printing Lines
img = cv2.line(img,(0,0),(255,255),(255,0,255),2)   # COLORS ARE LOADED IN REVERSE ie BGR
img = cv2.arrowedLine(img,(100,0),(100,255),(0,0,0),2)

# Printing Shapes
img = cv2.rectangle(img,(384,0),(510,100),(100,100,100),-1)    # if Thickness = -1, then it will fill it with the given colour
img = cv2.circle(img,(300,100),30,(0,0,0),2)

# Printing Texts
font = cv2.FONT_HERSHEY_COMPLEX
size = 4
color = (0,0,0)
img = cv2.putText(img,'Lena',(10,450),font,size,color,thickness=2,lineType=cv2.LINE_AA)   # Text starting point = (10,500)


'''
# Create a image using numpy 0's method
img = np.zeros([512,512,3],np.uint8)

font = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
img = cv2.putText(img,'Test',(100,100),font,2,color=(100,100,100),thickness=2,lineType=cv2.LINE_AA)
'''

# Displaying Image
cv2.imshow('Darling',img)

# Closing Windown
k = cv2.waitKey(0)
if (k==27):             # k = 25 => ESC key
    cv2.destroyAllWindows()
elif(k==ord('s')):
    cv2.imwrite('Lenna_copy.png',img)
    cv2.destroyAllWindows()
