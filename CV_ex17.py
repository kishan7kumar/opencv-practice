# ********   PROGRAM TO PERFORM OBJECT TRACKING USING COLOR ***********
import cv2
import numpy as np

cam = cv2.VideoCapture(0)           #capturing image from webcam
if cam.isOpened():                  #checks if camera is opened
    ret, frame = cam.read()         #returns status of object                                    # stores the variable
else:
     ret = False

# TAKING CONTINOUS LOOP VIDEO FEED
while ret:
    ret, frame = cam.read()
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV) #converting the rgb video feed into hsv color space 

    # tracking blue color
    lowb = np.array([100, 80, 80])     # for lower value of blue
    highb = np.array([140, 255, 255])  # for higher value of blue

    # tracking green color
    lowg = np.array([60, 90, 90])      # for lower value of green
    highg = np.array([100, 255, 255])  # for higher value of green

    # tracking red color
    lowr = np.array([140, 150, 0])     # for lower value of red
    highr = np.array([180, 255, 255])  # for higher value of red

    # masking blue color object
    image_maskb = cv2.inRange(hsv, lowb, highb)
    outputb = cv2.bitwise_and(frame,frame, mask = image_maskb)  # performing and operation between captured image and binary image
    cv2.imshow('blue color tracking window',outputb) 

    # masking green color object
    image_maskg = cv2.inRange(hsv, lowg, highg)
    outputg = cv2.bitwise_and(frame,frame, mask = image_maskg)  # performing and operation between captured image and binary image
    cv2.imshow('green color tracking window',outputg)

    # masking red color object
    image_maskr = cv2.inRange(hsv, lowr, highr)
    outputr = cv2.bitwise_and(frame,frame, mask = image_maskr)  # performing and operation between captured image and binary image
    cv2.imshow('red color tracking window',outputr)   
    # print(image_mask)   
    if cv2.waitKey(1)==27:           #ESC key pressed will close the window
        break
cv2.destroyAllWindows()

cam.release()
