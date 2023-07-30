# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 17:32:49 2018

@author: kishan
"""

import cv2
import numpy as np

windowname = 'Hough line'
cv2.namedWindow(windowname, cv2.WINDOW_NORMAL)
cam = cv2.VideoCapture(0)

if cam.isOpened():
    ret, frame = cam.read()
else:
    ret = False
    
while ret:
    ret, frame = cam.read()
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(grey, 50, 250, apertureSize = 5, L2gradient = True)
    lines = cv2.HoughLines(edges, 1 , np.pi/180, 200)  # to draw lines on detected edges
    if lines is not None:
        for rho, theta in lines[0]:
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a*rho
            y0 = b*rho
            pts1  = (int(x0 + 1000*(-b)), int(y0 + 1000*(a)))
            pts2  = (int(x0 - 1000*(-b)), int(y0 - 1000*(a)))
            cv2.line(frame, pts1, pts2, (0,255,0), 5)
     
    cv2.imshow(windowname, frame)
    if cv2.waitKey(1)==27:
         break
cam.release()
cv2.destroyAllWindows()

      