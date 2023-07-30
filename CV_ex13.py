# PROGRAM TO CAPTURE IMAGE FROM WEBCAM

import cv2
import matplotlib.pyplot as plt

cam = cv2.VideoCapture(0)   # capturing image from webcam

if cam.isOpened():    #checks if camera is opened
    ret, frame = cam.read()     #returns status of object
    print(ret)
    print(frame)  # stores the variable
else:
     ret = False

img1 = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

plt.imshow(img1)
plt.title('color image captured')
plt.show()

cam.release()
    
