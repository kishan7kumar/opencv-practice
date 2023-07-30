import cv2
import numpy as np

windowName = 'Drawing'   # assigning the window name
img = np.zeros((512,512,3),np.uint8) # making the windowed black
cv2.namedWindow(windowName)  #assigning the window

#mouse callback function
def draw_circle(event,x,y,flags,param):  
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img, (x, y), 40, (0, 255, 0), -1)
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y),  20, (0, 0, 255), -1)

#bind the callback function to window
cv2.setMouseCallback(windowName,draw_circle)

# loop to display the window
while(True):
    cv2.imshow(windowName,img)
    if cv2.waitKey(20) == 27:
        break
cv2.destroyAllWindows()    #destroy all windows when user press 'Esc' key
        
