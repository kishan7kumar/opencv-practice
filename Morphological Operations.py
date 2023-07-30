# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 20:24:14 2018

@author: kishan kumar
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np

#importing fire images
imgpath = 'C:\\Users\\kishan\\Pictures\\at Palm beach road\\firetest.jpg'
img = cv2.imread(imgpath,0)
th = 245
max_val = 255

ret,binary = cv2.threshold(img, th, max_val, cv2.THRESH_BINARY)

kernel = np.ones((5,5),np.uint8)

#rectangular kernel
#kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
#Elliptical kernel
#kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
#Cross  kernel
#kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))

#erosion operation
erosion = cv2.erode(binary,kernel ,iterations = 10)

#dilation operation
dilation = cv2.dilate(binary, kernel ,iterations = 3)

#opening operation
opening = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)

#closing operation
closing = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)

#gradient operation   very useful for edge detection of fire
gradient = cv2.morphologyEx(binary, cv2.MORPH_GRADIENT, kernel)

output = [img, binary, erosion, dilation, opening, closing, gradient]
titles = ['Original image with fire', 'Binary image', 'Eroded image', 'Dilated Image', 'Opening Image', 'Closing Image', 'Gradient Image']

for i in range(7):
    plt.subplot(4, 2, i+1)
    plt.imshow(output[i], cmap ='gray')
    plt.title(titles[i])
    plt.show()
     
    
    
    
