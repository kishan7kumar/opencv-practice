# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 16:01:35 2018

@author: kishan kumar
"""

import cv2



windowname1 = 'BLUR TOOLBOX'   # assigning the window name
#img = np.zeros((512,512,3),np.uint8) # making the windowed black
cv2.namedWindow(windowname1, cv2.WINDOW_NORMAL)  #assigning the window

imgpath = 'C:\\Users\\kishan\\Pictures\\at Palm beach road\\'
imgpath1 = imgpath + 'IMG_1338.jpg'
img1 = cv2.imread(imgpath1,1)


#mouse callback function
def Blur_tool(event,x,y,flags,param):  
    if event == cv2.EVENT_LBUTTONDBLCLK:
        img2 = cv2.blur(img1,(25,25))
        img1 = img2
        #  cv2.circle(img1, (x, y), 40, (0, 255, 0), -1)   #green circle
#    if event == cv2.EVENT_LBUTTONDOWN:
#        cv2.circle(img1, (x, y),  20, (0, 0, 255), -1) #red circle
#bind the callback function to window
#cv2.setMouseCallback(windowname1,Blur_tool)
cv2.setMouseCallback(windowname1,Blur_tool)

# loop to display the window
while(True):
    cv2.imshow(windowname1,img1)
    
    
    
    
    if cv2.waitKey(20) == 27:
        break
cv2.destroyAllWindows()    #destroy all window ehn user press 'Esc' key