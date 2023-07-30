# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 17:50:50 2018

@author: kishan kumar
"""

import cv2

def nothing(x):
    pass

#importing image from folder
imgpath1 = 'C:\\Users\\kishan\\Pictures\\Imagedataset\\firetest1.jpg'


#reading images in  grayscale
img1 = cv2.imread(imgpath1,0)

windowname = 'Canny Edge Detection Trackbar'
cv2.namedWindow(windowname,cv2.WINDOW_NORMAL)


cv2.createTrackbar('min',windowname,10,250,nothing)
cv2.createTrackbar('max',windowname,10,250,nothing)

while(1):
    a = cv2.getTrackbarPos('min',windowname)
    b = cv2.getTrackbarPos('max',windowname)
    L1 = cv2.Canny(img1, a ,b, L2gradient = False)
    cv2.imshow(windowname,L1)

    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
