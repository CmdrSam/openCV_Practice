import cv2

# Capture Livestream
capture = cv2.VideoCapture(0)

# Chaning Resolution
# capture.set(cv2.CAP_PROP_FRAME_WIDTH,700)  # We can use 3 in place of cv2.CAP_PROP_FRAME_WIDTH
# capture.set(cv2.CAP_PROP_FRAME_HEIGHT,700)  # We can use 4 in place of cv2.CAP_PROP_FRAME_HEIGHT


# Save recorded file
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('Output.avi',fourcc,20.0,(640,480))
while(True):
    ret, frame = capture.read()
    if (ret):
        #grey = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)           # Adding Greyscale
        text = 'Width: ' + str(capture.get(3)) + ' Height: '+ str(capture.get(4))
        font = cv2.FONT_HERSHEY_SIMPLEX
        frame = cv2.putText(frame,text,(10,50),font,1,(255,255,255),cv2.LINE_AA,5)

        #cv2.imshow('video frame',grey)     # Displaying grey image
        cv2.imshow('video frame', frame)

        if (cv2.waitKey(1)==ord('q')):
            break
    else:
        break

capture.release()       # SUPER IMPORTANT
cv2.destroyAllWindows()