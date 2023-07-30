# ROTATING IMAGES IN VIDEO LIVE FEED

#importing all modules
import cv2
import time

windowname = 'Live video feed' 
cv2.namedWindow(windowname,cv2.WINDOW_NORMAL)
cam = cv2.VideoCapture(0)

if cam.isOpened():
    ret, frame = cam.read()  # here return is camera status and frame is camera variable
else:
        ret = False
        
rows, columns, channels = frame.shape
angle = 0
scale = 1

while True:
    
    ret, frame = cam.read()

    if scale <=2:
        scale = scale+0.1
    if scale >=2:
        scale = 0.1
  

    if angle==360:  #for continous motion 
        angle = 0;
    R = cv2.getRotationMatrix2D((columns/2, rows/2),angle,scale)  #changing angle to -angle will anticlocwise
    output = cv2.warpAffine(frame, R, (columns, rows))

    #creating a normal sized window
    cv2.imshow(windowname,output)

    #rotating by angle
    angle = angle + 1 
    time.sleep(0.01)
    if cv2.waitKey(1)==27:
        break
cv2.destroyAllWindows()
    
