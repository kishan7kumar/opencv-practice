# PROGRAM TO CAPTURE LIVE VIDEO FEED FROM WEBCAM

import cv2
#import matplotlib.pyplot as plt

#windowname = "live video feed"
#cv2.namedWindow(windowname)
cam = cv2.VideoCapture(0)           # capturing image from webcam

#print('width : '+str(cam.get(3)))   # prints default width of camera
#print('height: '+str(cam.get(4)))

cam.set(3,1280)
cam.set(4,720)
print('width : '+str(cam.get(3)))   # prints changed width of camera
print('height: '+str(cam.get(4)))

if cam.isOpened():                  #checks if camera is opened
    ret, frame = cam.read()         #returns status of object                                    # stores the variable
else:
     ret = False
while ret:
    ret, frame = cam.read()
    GrayOutput = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)   # for changing color spaces
    cv2.imshow('normal video feed',frame)
    cv2.imshow('graysacle video feed',GrayOutput)
    if cv2.waitKey(1)==27:           #ESC key pressed will close the window
        break
cv2.destroyAllWindows()

cam.release()
#plt.imshow(img1)
#plt.title('color image captured')
#plt.show()


