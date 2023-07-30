# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 22:30:58 2018

@author: kishan
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np

#importing fire images
imgpath = 'C:\\Users\\kishan\\Pictures\\Imagedataset\\firetest1.jpg'
img2 = cv2.imread(imgpath,0)
img1 = cv2.imread(imgpath,1)
img = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
th = 250
max_val = 255

ret,binary = cv2.threshold(img2, th, max_val, cv2.THRESH_BINARY)

kernel = np.ones((5,5),np.uint8)

#rectangular kernel
#kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
#Elliptical kernel
#kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
#Cross  kernel
#kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))

#erosion operation
erosion = cv2.erode(img,kernel ,iterations = 5)

#dilation operation
dilation = cv2.dilate(img, kernel ,iterations =5)

#opening operation
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

#closing operation
closing = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

#gradient operation   very useful for edge detection of fire
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

output = [img, binary, erosion, dilation, opening, closing, gradient]
titles = ['Original image with fire', 'Binary image', 'Eroded image', 'Dilated Image', 'Opening Image', 'Closing Image', 'Gradient Image']

for i in range(7):
    plt.subplot(4, 2, i+1)
    plt.imshow(output[i], cmap ='gray')
    plt.title(titles[i])
plt.show()