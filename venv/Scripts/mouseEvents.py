import cv2
import numpy as np
# Find available events
# events = [i for i in dir(cv2) if ('EVENT' in i)]
# print(events)

# Listening mouse event creating callback function

 # Displaying colour and coordinates by clicking

def click_event(event,x,y,flags,param):
    if (event==cv2.EVENT_LBUTTONDOWN):
        print(x,' , ',y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = str(x) + ', ' + str(y)
        cv2.putText(img,text,(x,y),font,0.5,(255,255,0),1)
        cv2.imshow('Image',img)

    if (event == cv2.EVENT_RBUTTONDOWN):
        blue = img[y, x, 0]       # as the coordinates are R G B and blue is at 3rd positon
        green = img[y, x, 1]
        red = img[y, x, 2]

        font = cv2.FONT_HERSHEY_SIMPLEX
        rgbText = str(blue) + ', ' + str(green) + ', ' + str(red)
        cv2.putText(img, rgbText, (x, y), font, 0.5, (0, 0, 250), 2)
        cv2.imshow('Image', img)


''' Making lines by clicking

def click_event(event,x,y,flags,param):
    if (event == cv2.EVENT_LBUTTONDOWN):

        cv2.circle(img,(x,y),3,(0,0,255),-1)   # To create a circle and fill it with red colour
        points.append((x,y))

        if (len(points)>=2):
            cv2.line(img,points[-1],points[-2],(255,0,0),5)
        cv2.imshow('Image',img)
'''

'''
# To find the colour of the selected place in new Window
def click_event(event,x,y,flags,param):
    if (event == cv2.EVENT_LBUTTONDOWN):
        blue = img[y, x, 0]       # as the coordinates are R G B and blue is at 3rd positon
        green = img[y, x, 1]
        red = img[y, x, 2]

        cv2.circle(img,(x,y),3,(0,0,255),-1)
        colorImage = np.zeros((100,400,3),np.uint8)         # Here 3 means we are using 3 channels RGB
        colorImage[:] = [blue,green,red]

        cv2.imshow('Colour',colorImage)
        
'''

# img = np.zeros((512,512,3),np.uint8)
img = cv2.imread('lena.jpg',1)
cv2.imshow('Image',img)
points =[]
cv2.setMouseCallback('Image',click_event)    # The window name (ie 'Image') should be same everywhere

cv2.waitKey(0)
cv2.destroyAllWindows()