#importing all modules
import cv2


windowname_1 = 'LIVE FIRE DETECTION CV' 
cv2.namedWindow(windowname_1,cv2.WINDOW_NORMAL)
windowname_2 = 'LIVE FIRE DETECTION' 
cv2.namedWindow(windowname_2,cv2.WINDOW_NORMAL)
#cv2.imshow(windowname,o)

cam= cv2.VideoCapture(0)

if cam.isOpened():
        ret, frame = cam.read()
else:
    ret = False

while ret:
    ret, frame = cam.read()
    th = 240
    max_val = 255
    ret, o = cv2.threshold(frame, th, max_val, cv2.THRESH_BINARY)
#THRESH_BINARY_INV
#THRESH_TOZERO
#THRESH_TOZERO_INV
#THRESH_TRUNC

    cv2.imshow(windowname_1,o)
    cv2.imshow(windowname_2,frame)
    if cv2.waitKey(1)==27:
        break

cv2.destroyAllWindows()
cam.release()

#creating a normal sized window



