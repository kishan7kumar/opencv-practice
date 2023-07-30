# PROGRAM TO RECORD A LIVE VIDEO FEED AND SAVE IT

import cv2
#windowname = "live video feed"
#cv2.namedWindow(windowname)

cam = cv2.VideoCapture(0)           # capturing image from webcam


filename = 'C:\\Users\\kishan\\Videos\\opencvvideo\\testvideo.avi'   #saving location and filename
codec = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
framerate = 30
resolution = (640,480)

VideoFileOutput = cv2.VideoWriter(filename, codec, framerate, resolution)

if cam.isOpened():             #checks if camera is opened
    ret, frame = cam.read()    #returns status of object                                    # stores the variable
else:
     ret = False
while ret:
    ret, frame = cam.read()
    VideoFileOutput.write(frame)
    GrayOutput = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # for changing color spaces
    cv2.imshow('normal video feed',GrayOutput)
    #cv2.imshow('graysacle video feed',GrayOutput)
    if cv2.waitKey(1)==27:   #ESC key pressed will close the window
        break
cv2.destroyAllWindows()
VideoFileOutput.release()
cam.release()
