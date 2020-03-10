import cv2
import numpy as np

# Object Detection from a photo
'''
def faltuFunc(x):
    pass

cv2.namedWindow("Testing Image")
cv2.createTrackbar("LH","Testing Image",0,255,faltuFunc)
cv2.createTrackbar("LS","Testing Image",0,255,faltuFunc)
cv2.createTrackbar("LV","Testing Image",0,255,faltuFunc)
cv2.createTrackbar("UH","Testing Image",255,255,faltuFunc)
cv2.createTrackbar("US","Testing Image",255,255,faltuFunc)
cv2.createTrackbar("UV","Testing Image",255,255,faltuFunc)


while(True):
    frame = cv2.imread('smarties.png'   )
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lH = cv2.getTrackbarPos("LH","Testing Image")
    lS = cv2.getTrackbarPos("LS", "Testing Image")
    lV = cv2.getTrackbarPos("LV", "Testing Image")
    uH = cv2.getTrackbarPos("UH", "Testing Image")
    uS = cv2.getTrackbarPos("US", "Testing Image")
    uV = cv2.getTrackbarPos("UV", "Testing Image")

    lValue = np.array([lH,lS,lV])
    uValue = np.array([uH,uS,uV])


    Mask = cv2.inRange(hsv,lValue,uValue)
    res = cv2.bitwise_and(frame,frame,mask=Mask)

    cv2.imshow("TestingImage",frame)
    cv2.imshow("Result",res)
    cv2.imshow("Mask",Mask)


    key = cv2.waitKey(1)
    if (key==27):
        print(lValue)
        print(uValue)
        break

cv2.destroyAllWindows()
'''

# Object Detection using a live video add the code cv2.vidioCapture(0)

cap = cv2.VideoCapture(0)


def faltuFunc(x):
    pass

cv2.namedWindow("Testing Image")
cv2.createTrackbar("LH","Testing Image",0,255,faltuFunc)
cv2.createTrackbar("LS","Testing Image",0,255,faltuFunc)
cv2.createTrackbar("LV","Testing Image",0,255,faltuFunc)
cv2.createTrackbar("UH","Testing Image",255,255,faltuFunc)
cv2.createTrackbar("US","Testing Image",255,255,faltuFunc)
cv2.createTrackbar("UV","Testing Image",255,255,faltuFunc)


while(True):
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lH = cv2.getTrackbarPos("LH","Testing Image")
    lS = cv2.getTrackbarPos("LS", "Testing Image")
    lV = cv2.getTrackbarPos("LV", "Testing Image")
    uH = cv2.getTrackbarPos("UH", "Testing Image")
    uS = cv2.getTrackbarPos("US", "Testing Image")
    uV = cv2.getTrackbarPos("UV", "Testing Image")

    # lValue = np.array([lH,lS,lV])             # Found its value using the above code on image 
    # uValue = np.array([uH,uS,uV])
    
    lValue = np.array([90,128,181])
    uValue = np.array([164,255,255])

    Mask = cv2.inRange(hsv,lValue,uValue)
    res = cv2.bitwise_and(frame,frame,mask=Mask)

    cv2.imshow("TestingImage",frame)
    cv2.imshow("Result",res)
    cv2.imshow("Mask",Mask)


    key = cv2.waitKey(1)
    if (key==27):
        print(lValue)
        print(uValue)
        break

cap.release()
cv2.destroyAllWindows()
