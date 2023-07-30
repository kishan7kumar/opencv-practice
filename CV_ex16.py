# PROGRAM TO PLAY VIDEO FEED

import cv2
#windowname = "live video feed"
#cv2.namedWindow(windowname)


filename = 'C:\\Users\\kishan\\Videos\\opencvvideo\\testvideo.avi'
cam = cv2.VideoCapture(filename)           # capturing video file from destination specified from webcam


ret = True                                # taking a variable and making it true
                               
while ret:
    if cam.isOpened():             #checks if camera is opened
        ret, frame = cam.read()    #returns status of object    
    print(ret)
    if ret:                        # if ret is true play the video
        cv2.imshow('Open cv player',frame)
       
        if cv2.waitKey(33)==27:   #here to play at normal rate 1000/30=33 so waitkey is 33   #ESC key pressed will close the window
           break
    else:                          #if ret is false then break
        break            
cv2.destroyAllWindows()

cam.release()
